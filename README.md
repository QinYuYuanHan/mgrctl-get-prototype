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
## 🚀 How to Run

```bash
python main.py get system
python main.py get system -f cpu=x86_64
python main.py get system -o yaml
🧩 Architecture
cli.py: command parsing
get.py: core logic
api.py: data layer (mock)
output.py: formatting
