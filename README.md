# Advanced Integrated Development Environment for Quantum Computing
AIDE-QC is a next-generation software stack enabling heterogeneous quantum-classical programming, compilation, and execution on both near-term and future fault-tolerant quantum computers. Our approach treats quantum computers as novel co-processors and puts forward C++ and Pythonic language extensions for quantum code expression and compilation to native backend gate sets.


This repository holds nightly binary builds for the platform as well as a command line executable for creating browser-based IDEs for quantum-classical computing.

## Manually install aide-qc

```bash
# Install the command line tool
$ git clone https://github.com/aide-qc/aide-qc
$ cd aide-qc
$ python3 -m pip install --user .

# Note: if you provide --user, you may have to 
$ export PATH=$PATH:$(python3 -m site --user-base)/bin

# Note: -i installs the AIDE-QC IDE, --start starts IDE with name myide
$ aide-qc -i --start myide 

# After download and start, 
# web browser tab should open with new IDE ready for your work

```
