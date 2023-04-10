import lit.formats

config.name = "My Example"
config.test_format = lit.formats.ShTest(True)

config.suffixes = ['.cmm']

config.substitutions.append(('%test-ghc',
    '../ghc-riscv/_build/stage1/bin/riscv64-unknown-linux-gnu-ghc'))
