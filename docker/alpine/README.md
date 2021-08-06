<img src="https://github.com/aide-qc/deploy/blob/master/aide_qc_logo_v3.png?raw=true" alt="drawing" width="600"/>

# Welcome to AIDE-QC!

You are now using the Advanced Integrated Development Environment (IDE) for Quantum Computing (AIDE-QC). <br>
This project provides a pre-built image containing the entire AIDE-QC software stack, including the [`qcor`](https://github.com/ornl-qci/qcor) <br>
C++ compiler and Python quantum JIT environment, the [XACC](https://github.com/eclipse/xacc) framework and high-level Python API, <br>
and the OpenQASM 3 MLIR compiler. Moreover, you have access to novel circuit synthesis tools from the [BQSKit](https://github.com/BQSKit) library. 

For much more on the AIDE-QC platform, check out [docs.aide-qc.org](http://docs.aide-qc.org).

## Getting Started

In the file browser to the left you'll notice a number of example directories. We have provided illustrative examples in C++, <br>
Python, and OpenQASM 3 (via the MLIR compiler). Feel free to try them out! To start, open a Terminal with `CTRL`+<code>\`</code> (single-quote). <br>
From the terminal, you have the `qcor` compiler available in your path as well as the Python bindings for `qcor` and XACC in your `PYTHONPATH`. <br>
Open up the simple `bell.py`, look at it, and run it with 
```bash
$ code-server py-examples/bell.py (or just double-click in file browser)
$ python3 py-examples/bell.py -shots 100
{
    "AcceleratorBuffer": {
        "name": "qrg_ASjHA",
        "size": 2,
        "Information": {},
        "Measurements": {
            "00": 44,
            "11": 56
        }
    }
}
```
To run on IBM or any other physical backend, check out how to provide your [API credentials](https://aide-qc.github.io/deploy/users/remote_qpu_creds/). 

To run a C++ example like [Phase Estimation](https://github.com/ORNL-QCI/qcor/blob/master/examples/qpe/qpe_callable_oracle.cpp), run the following
```bash
$ qcor -shots 100 cpp-examples/qpe/qpe_callable_oracle.cpp
$ ./a.out
X qrg_ASjHA3
H qrg_ASjHA0
H qrg_ASjHA1
H qrg_ASjHA2
CPhase(0.785398) qrg_ASjHA0,qrg_ASjHA3
CPhase(0.785398) qrg_ASjHA1,qrg_ASjHA3
CPhase(0.785398) qrg_ASjHA1,qrg_ASjHA3
CPhase(0.785398) qrg_ASjHA2,qrg_ASjHA3
CPhase(0.785398) qrg_ASjHA2,qrg_ASjHA3
CPhase(0.785398) qrg_ASjHA2,qrg_ASjHA3
CPhase(0.785398) qrg_ASjHA2,qrg_ASjHA3
Swap qrg_ASjHA0,qrg_ASjHA2
H qrg_ASjHA0
CPhase(-1.5708) qrg_ASjHA1,qrg_ASjHA0
H qrg_ASjHA1
CPhase(-1.5708) qrg_ASjHA2,qrg_ASjHA1
CPhase(-0.785398) qrg_ASjHA2,qrg_ASjHA0
H qrg_ASjHA2
Measure qrg_ASjHA0
Measure qrg_ASjHA1
Measure qrg_ASjHA2

{
    "AcceleratorBuffer": {
        "name": "qrg_ASjHA",
        "size": 4,
        "Information": {},
        "Measurements": {
            "100": 100
        }
    }
}
```