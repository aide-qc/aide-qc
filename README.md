# Advanced Integrated Development Environment for Quantum Computing
AIDE-QC is a next-generation software stack enabling heterogeneous quantum-classical programming, compilation, and execution on both near-term and future fault-tolerant quantum computers. Our approach treats quantum computers as novel co-processors and puts forward C++ and Pythonic programming models for quantum code expression and compilation to native backend gate sets.

The AIDE-QC project decomposes the stack research and development into Programming, Compiler, Verification and Validation, Error Mitigation, Optimization, and Software Integration thrusts. The union of these efforts represents the development of a holistic software ecosystem that enables an extensible and modular approach to the quantum-classical programming workflow.

AIDE-QC builds upon the service-oriented XACC quantum programming framework and puts forward service interfaces or plugins for quantum language parsing, intermediate representations, transformations on compiled circuits, error mitigation strategies, and backend execution and emulation, to name a few. These plugin interfaces enable the AIDE-QC to remain flexible as the quantum computing research landscape grows and advances. On top of that, AIDE-QC puts forward a novel C++ compiler for heterogeneous quantum-classical computing, QCOR.

This repository holds nightly binary builds for the platform as well as a command line executable for creating browser-based IDEs for quantum-classical computing.

## Install aide-qc IDE

```bash
$ python3 -m pip install --user .
# -i installs the AIDE-QC IDE, start one with name myide
$ aide-qc -i --start myide 
# web browser tab should open with new IDE ready for your work
```