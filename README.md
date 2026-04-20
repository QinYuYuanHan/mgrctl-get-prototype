# mgrctl get prototype

A simple prototype of a `kubectl-like get` command for mgrctl.

## Features

* Supports resources:

  * system
  * group

* Filtering:

  ```bash
  python main.py get system -f cpu=x86_64
  ```

* Output formats:

  ```bash
  python main.py get system -o json
  python main.py get system -o yaml
  ```

## Purpose

This is a prototype to explore CLI design and filtering behavior for a future mgrctl `get` command.
