#include <stdio.h>
#include <stdlib.h>

#include "Rts.h"

RTS_FUN_DECL(one);

StgRegTable * StgRun (StgFunPtr f, StgRegTable *basereg);

// Call cmm and print result regs
int main(int argc, char *argv[]) {
    StgRegTable * regTable = malloc(sizeof(StgRegTable));

    StgWord result = (StgWord) StgRun((StgFunPtr) one, regTable);

    printf("result: %lu\n", result);
    return 0;
}
