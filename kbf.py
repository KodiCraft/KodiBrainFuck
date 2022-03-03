#!/bin/python3

import argparse
import brainfuck
from kodibrainfuck import compile
import time
from bcolors import *
import sys
import re

parser = argparse.ArgumentParser(description="Interpret or compile some KodiBrainFuck")
parser.add_argument("input", help="File name for kbf program", type=str)
parser.add_argument("-o", "--out"   , help="File name for output location, if not specified, will run the program", default=None, type=str)
parser.add_argument("-m", "--min"   , help="Minimise output brainfuck by removing white space, newlines and comments", default=False, const=True, action="store_const")
parser.add_argument("-e", "--eval"  , help="Evaluate kbf from the command line rather than reading from a file", default=False, const=True, action="store_const")
parser.add_argument("-s", "--stdout", help="Outputs the compiled program to stdout instead of running it. Ignored if an output file is given", default=False, const=True, action="store_const")

args = parser.parse_args()

code = args.input if args.eval else open(args.input, "r").read()

out = compile(code)

if args.out:
    start_time = time.time()
    with open(args.out, "w") as f:
        if args.min:
            f.write(re.sub(r'[^+-<>,.\[\]]', "", out))
        else:
            f.write(compile(code))
    print(bcolors.OKGREEN + "Compilation successful! " + bcolors.ENDC + f"Compiled in {(time.time() - start_time)} seconds")
    print(bcolors.OKCYAN + "Wrote output brainfuck file to: " + bcolors.ENDC + args.out)
    print(bcolors.HEADER + "To run the compiled brainfuck code, run " + bcolors.ENDC + f"{sys.argv[0]} {args.out}")
else:
    if args.stdout:
        print(out)
    else:    
        brainfuck.interpret(out)
