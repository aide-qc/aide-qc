FROM qcor/code-base:latest
ENV PYTHONPATH "${PYTHONPATH}:/usr/local/aideqc/qcor"
RUN sudo apt-get update && sudo apt-get install -y qcor \
  && git clone https://github.com/ornl-qci/qcor && cp -r qcor/examples cpp-examples \
  && cp -r qcor/python/examples py-examples && cp -r qcor/mlir/parsers/qasm3/examples mlir-qasm3-examples && rm -rf qcor
