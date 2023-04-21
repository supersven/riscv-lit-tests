import lit.formats

config.name = "RISC-V 64"
config.test_format = lit.formats.ShTest(True)

config.suffixes = ['.cmm']

config.substitutions.append(('%test-ghc',
    '/home/sven/src/ghc-riscv/_build/stage1/bin/riscv64-unknown-linux-gnu-ghc'))
