#!/bin/python3
SYNTAX_CHARS = ["+", "-", ">", "<", ".", ",", "{", "}", ":", '"', "=", "(", ")"]

from termios import error
from bcolors import bcolors
import sys
from os import path

macros = {}


def compile(inp):
    global macros
    return _compile(_compile(_compile(inp)))


def _compile(inp):
 try:
    global macros
    codePt = 0
    output = ""    
    while codePt < len(inp):
        char = inp[codePt]
        if char == "{":
            read = _readUntil("}", "{", inp, codePt)
            fullLoop = read[0]
            splitLoop = fullLoop.split(":")
            if len(splitLoop) > 2:
                print(bcolors.FAIL + "Compilation error! " + bcolors.ENDC + f"Syntax error, unexpected ':'")
                print(bcolors.OKCYAN + "Hint: " + bcolors.ENDC + "':' is used to mark a separation in a loop function!")
                exit(1)

            output += splitLoop[1] * int(splitLoop[0])
            codePt += read[1]
        elif char == '"':
            read = _readUntil('"', 'ඞ', inp, codePt) 
            fullLiteral = read[0]
            memOffset = 0
            for i in fullLiteral:
                output += "[-]"
                output += ord(i) * "+"
                output += ">"
                memOffset += 1
            output += memOffset * "<"
            codePt += read[1]
        elif char == "=":
            read = _readUntil("=", "ඞ", inp, codePt)
            fullMacro = read[0]
            splitMacro = fullMacro.split(":")
            if len(splitMacro) > 2:
                print(bcolors.FAIL + "Compilation error! " + bcolors.ENDC + f"Syntax error, unexpected ':'")
                print(bcolors.OKCYAN + "Hint: " + bcolors.ENDC + "':' is used to mark a separation in a macro!")
                exit(1)
            if len(splitMacro[0]) != 1 or splitMacro[0] in SYNTAX_CHARS:
                print(bcolors.FAIL + "Compilation error! " + bcolors.ENDC + f"Invalid macro name: '{splitMacro[0]}'")
                print(bcolors.OKCYAN + "Hint: " + bcolors.ENDC + "A macro must be exactly one non-syntax character long")
                exit(1)
            macros[splitMacro[0]] = splitMacro[1]
            codePt += read[1]
        elif char == "(":
            read = _readUntil(")", "∆", inp, codePt)
            file = read[0]
            if path.isfile(file):
                with open(file, "r") as f:
                    output += compile(f.read())
                codePt += read[1]
            else:
                print(bcolors.FAIL + "Compilation error! " + bcolors.ENDC + f"File '{file}' does not exist!")
                exit(1)
        elif char in macros.keys():
            output += macros[char]
        else:    
            output += char
        codePt += 1
    return output
 except error as e:
    print(bcolors.FAIL + "Compilation error! " + bcolors.ENDC + str(e))
    exit(1)

def _readUntil(target, antitarget, source, start):
    output = ""
    pt = start + 1
    if pt >= len(source):
        print(bcolors.FAIL + "Compilation error! " + bcolors.ENDC + f"Syntax error, expected '{target}'")
        print("At: " + str(start))
        exit(1)
    else:
        while source[pt] != target:
            if source[pt] == antitarget:
                print(bcolors.FAIL + "Compilation error! " + bcolors.ENDC + f"Cannot nest loops!")
                print("At: " + str(pt))
            output += source[pt]
            pt += 1
            if pt >= len(source):
                print(bcolors.FAIL + "Compilation error! " + bcolors.ENDC + f"Syntax error, expected '{target}'")
                print("At: " + str(start))
                exit(1)
    return (output, pt - start)

if __name__ == "__main__":
    compile(sys.argv[1])
