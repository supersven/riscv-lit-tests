# LLVM lit tests for the GHC RISCV-64 NCG

## Debug tests

Run in one terminal:

``` sh
qemu-riscv64 -g 1111 a.out
```

In another:

``` sh
gdb a.out

# in GDB
target remote localhost:1111

c
```

Compile the test with `-optc=-g` to get debugging symbols for C code.
