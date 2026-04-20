# mgrctl get command prototype
GSOC Uyuni Project #245 | kubectl-like CLI query command implementation

## Overview
This project is a prototype implementation of a `kubectl`-like `get` command for `mgrctl` in Uyuni.

The goal is to improve usability by allowing users to query objects in a simple and consistent way.

## Features
- Support basic resource types:
  - `system`
  - `group`
- Filtering support:
  ```bash
  mgrctl get system --filter cpu=x86_64
  Output formats:
  mgrctl get system -o yaml
mgrctl get system -o json

Design

The command follows a standard structure identical to kubectl syntax:
mgrctl get <resource> [options]
Current Status
This is an early prototype demonstrating core foundations:
Complete CLI command structure
Basic resource filtering logic
Multiple structured output formatting
Next Steps
Extend support to more Uyuni resource types
Improve advanced filtering & searching capabilities
Full integration with official real Uyuni RESTful API
Complete command help documentation
Prepare upstream Pull Request to uyuni-tools official repository
Motivation
This project is part of my exploration of improving the usability of Uyuni CLI developer tools.
I would like to further develop this prototype into a complete, official contribution to the open-source Uyuni project for Google Summer of Code.
