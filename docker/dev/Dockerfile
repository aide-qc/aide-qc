FROM qcor/code-base:latest
ENV PYTHONPATH "${PYTHONPATH}:$HOME/.xacc"
RUN sudo apt-get update && sudo apt-get install -y aideqc-llvm \
  && git clone --recursive https://github.com/eclipse/xacc && cd xacc && mkdir build && cd build \
  && $HOME/.local/bin/cmake -G Ninja .. -DXACC_BUILD_TESTS=TRUE -DPython_EXECUTABLE=$(which python3) -DPython_INCLUDE_DIR=/usr/include/python3.8 -DPython_LIBRARY=/usr/lib/libpython3.8.so \
  && $HOME/.local/bin/cmake --build . --target install \
  && cd ../../ && git clone https://github.com/ornl-qci/qcor && cd qcor && mkdir build && cd build \
  && $HOME/.local/bin/cmake .. -G Ninja -DLLVM_ROOT=/usr/local/aideqc/llvm -DMLIR_DIR=/usr/local/aideqc/llvm/lib/cmake/mlir \
         -DQCOR_BUILD_TESTS=TRUE -DPython_EXECUTABLE=$(which python3) -DPython_INCLUDE_DIR=/usr/include/python3.8 \
        -DPython_LIBRARY=/usr/lib/libpython3.8.so \
  && $HOME/.local/bin/cmake --build . --target install 
