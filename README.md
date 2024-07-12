<div align="center" markdown>
<img src="https://github.com/user-attachments/assets/aeaa45e2-a0ea-4ac2-9cf4-54feb59eb4e9">

Simple logger to save logs in a file and print them in the console.

<p align="center">
    <a href="#Overview">Overview</a> •
    <a href="#Quick-Start">Quick Start</a> 
</p>

[![Build Status](https://github.com/fatracing/pylogger/actions/workflows/checks.yml/badge.svg)](https://github.com/fatracing/pylogger/actions)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

</div>

## Overview
This is a simple logger to save logs in a file and print them in the console. It also can dump tracebacks and archive logs in a zip file.

## Quick Start
Install with pip:
```bash
pip install git+https://github.com/fatracing/pylogger.git
```

Import and use:
```python
from pylogger import Logger

logger = Logger(__file__)

logger.info("Hello, world!")
logger.error("Something went wrong!")
```