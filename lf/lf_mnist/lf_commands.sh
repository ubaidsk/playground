#!/usr/bin/env bash

# gfortran -c examples/expr2.f90 examples/dgemv.f examples/lsame.f examples/xerbla.f -o tmp

lfortran -c examples/expr2.f90 -o main.o --implicit-interface --generate-object-code
lfortran -c examples/dgemv.f -o dgemv.o --implicit-interface --fixed-form --generate-object-code
lfortran -c examples/lsame.f -o lsame.o --implicit-interface --fixed-form --generate-object-code
lfortran -c examples/xerbla.f -o xerbla.o --implicit-interface --fixed-form --generate-object-code



lfortran -c src/expr2.f90 --target=wasm32-wasi --implicit-interface
lfortran -c src/lapack.f --fixed-form --target=wasm32-wasi
/Users/ubaid/ext/wasi-sdk-19.0/bin/clang --target=wasm32-wasi -nostartfiles -Wl,--entry=my_start -Wl,-lwasi-emulated-process-clocks -o my_app expr2.o lapack.o /Users/ubaid/Desktop/OpenSource/lfortran/src/bin/../runtime/lfortran_runtime_wasm_wasi.o -Wl,-zstack-size=52428800 -Wl,--initial-memory=268435456 -Wl,--max-memory=268435456



lfortran -c src/expr2.f90 --target=wasm32-unknown-emscripten --implicit-interface --skip-pass unused_functions
lfortran -c src/lapack.f --fixed-form --target=wasm32-unknown-emscripten

/Users/ubaid/ext/emsdk/upstream/emscripten/emcc --target=wasm32-unknown-emscripten -sSTACK_SIZE=50mb -sINITIAL_MEMORY=256mb -o mnist.js expr2.o lapack.o /Users/ubaid/Desktop/OpenSource/lfortran/src/bin/../runtime/lfortran_runtime_wasm_emcc.o --no-entry -sEXPORTED_FUNCTIONS=_classifier,_malloc,_free

lfortran -c src2/expr2.f90 --generate-object-code --rtlib --target=wasm32-unknown-emscripten


(lf) ubaid@ubaids-MacBook-Pro lf_mnist % lfortran -c src/expr2.f90 --implicit-interface --target=wasm32-wasi --skip-pass unused_functions
warning: Argument `access` isn't supported yet
  --> src/expr2.f90:26:5
   |
26 |     open(12, file="mnist.data", form="unformatted", access="stream", status="old")
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ignored for now


Note: Please report unclear, confusing or incorrect messages as bugs at
https://github.com/lfortran/lfortran/issues.
(lf) ubaid@ubaids-MacBook-Pro lf_mnist % lfortran -c src/lapack.f --target=wasm32-wasi --fixed-form --skip-pa
ss unused_functions
(lf) ubaid@ubaids-MacBook-Pro lf_mnist % /Users/ubaid/ext/wasi-sdk-19.0/bin/clang --target=wasm32-wasi -nostartfiles -Wl,--entry=_start -Wl,-lwasi-emulated-process-clocks -o my_wasm_app expr2.o lapack.o.tmp.o /Users/ubaid/Desktop/OpenSource/lfortran/src/bin/../runtime/lfortran_runtime_wasm_wasi.o
clang-15: error: no such file or directory: 'lapack.o.tmp.o'
(lf) ubaid@ubaids-MacBook-Pro lf_mnist % /Users/ubaid/ext/wasi-sdk-19.0/bin/clang --target=wasm32-wasi -nostartfiles -Wl,--entry=_start -Wl,-lwasi-emulated-process-clocks -o my_wasm_app expr2.o lapack.out.tmp.o /Users/ubaid/Desktop/OpenSource/lfortran/src/bin/../runtime/lfortran_runtime_wasm_wasi.o
