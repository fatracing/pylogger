"""This module contains the Logger class for logging to the file and stdout."""

import logging
import os
import shutil
import sys
from datetime import datetime

log_level = os.getenv("LOG_LEVEL", "DEBUG")
# region constants
LOG_FORMATTER = "%(name)s | %(asctime)s | %(levelname)s | %(message)s"
LOG_DIR = os.path.join(os.getcwd(), "logs")
TB_DIR = os.path.join(LOG_DIR, "tracebacks")
ARCHIVES_DIR = os.path.join(os.getcwd(), "log_archives")
# endregion
for directory in [LOG_DIR, TB_DIR, ARCHIVES_DIR]:
    os.makedirs(directory, exist_ok=True)


class Logger(logging.Logger):
    """Handles logging to the file and stdout with timestamps.

    Args:
        name (str): Logger name.
        level (str): Log level.
        log_dir (str): Log directory.
    """

    def __init__(
        self,
        name: str,
    ):
        super().__init__(name)
        self.log_dir = LOG_DIR
        self.setLevel(log_level)
        self.stdout_handler = logging.StreamHandler(sys.stdout)
        self.file_handler = logging.FileHandler(
            filename=self.log_file, mode="a", encoding="utf-8"
        )
        self.fmt = LOG_FORMATTER
        self.stdout_handler.setFormatter(logging.Formatter(LOG_FORMATTER))
        self.file_handler.setFormatter(logging.Formatter(LOG_FORMATTER))
        self.addHandler(self.stdout_handler)
        self.addHandler(self.file_handler)

    @property
    def log_file(self) -> str:
        """Generates log file path based on current date.

        Returns:
            str: Log file path.
        """
        today = datetime.now().strftime("%Y-%m-%d")
        log_file = os.path.join(self.log_dir, f"{today}.txt")
        return log_file

    def dump_traceback(self, tb: str) -> None:
        """Saves traceback to the file.

        Args:
            tb (traceback): Traceback object.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        save_path = os.path.join(TB_DIR, f"{timestamp}.txt")
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(tb)

        self.info("Traceback saved to %s.", save_path)

    def archive_logs(self) -> str:
        """Archives log files for the current day and returns archive path.

        Returns:
            str: Archive path.
        """
        save_path = os.path.join(
            ARCHIVES_DIR, f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
        )
        self.debug("Starting to archive logs to %s from %s", save_path, self.log_dir)
        shutil.make_archive(save_path, "zip", self.log_dir)
        self.info("Logs archived to %s.", save_path)
        return save_path + ".zip"
