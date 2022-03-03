# KodiBrainFuck
A simple superscript of brainfuck that adds support for a few useful tools to make writing brainfuck more bearable

# Usage

## Installation
Using KodiBrainFuck is as simple as installing the python files in an accessible location and running the script `kbf.py`
kbf's help page can be displayed by using `kbf.py -h`

## Running a kbf program
By default, kbf is in **run mode**. Meaning that it will simply compile and interpret the input KodiBrainFuck (or regular brainfuck)
Example:
helloworld.kbf
```
"Hello World!"[.>]
```
```sh
$ kbf.py helloworld.kbf
Hello World!
```
The flag `-e` tells kbf to read the input argument as code instead of a file
```sh
$ kbf.py -e '"Hello World!"[.>]'
Hello World!
```

## Compiling a kbf program
KodiBrainFuck can be **compiled** to standard brainfuck that can then be interpreted by any brainfuck interpreter.
The flag `-o OUT` allows you to specify an output file. This will not run the program.
The flag `-s` will output the compiled brainfuck to stdout.
```sh
$ kbf.py -e '"Hello World!"[.>]' -s
[-]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++>[-]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[
-]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++>[-]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-
]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++++++++++++++++><<<<<<<<<<<<[.>]
```
*(kbf itself can interpret regular brainfuck, so you can test your code with *`kbf.py helloworld.bf`*)*

# Features
## Literal string allocation
KodiBrainFuck supports allocating literal strings into memory. It will assign in memory the exact values of each character one by one, then navigate back to the beginning of the string. This means that the entire string is loaded into memory at once without moving the memory pointer.

The syntax for allocating a literal string is `"string"`
```sh
$ kbf.py -e '"h"'' -s
[-]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++><
```
Notice the `[-]` at the start which will clear the memory at that location and the `<` at the end which ensures that the pointer returns to its initial location
If you would like to navigate back to the end of the string, **loops** can be used
```
$ kbf.py -e '"A rather long string of text"{25:>}.' -s
[-]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++>[-]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++>[-]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++>[-]++++++++++++++++++++++++++++++++>[-]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++>[-]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++>[-]++++++++++++++++++++++++++++++++>[-]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>[-]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>[-]+++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++><<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>
>>>>.
```
More information on loops is available below
Since the string allocation loads the entire string into memory, it can be impractical for simply printing out some text for the user to read. There is not yet a solution for this, however it is in the works as of writing.

## Loops
KodiBrainFuck supports simple loops. As brainfuck is a language where you will often require using the same instruction or couple of instructions multiple times, it can often get hard to read.
A loop can be described with the syntax `{n:instructions}` where `n` is an integer representing the amount of times the instructions should be repeated. For instance:
```sh
$ kbf.py -e "{3:+}" -s
+++
```
Loops may include **macros** or **literals** inside of them

## Macros
KodiBrainFuck supports **macros** as a way to minimise code repetition and to help readability. A macro's name can only be one non-syntax character long, to keep the spirit of the single-character instructions in brainfuck. A macro can be defined with the syntax `=n:instructions=` where `n` is the name of the macro. Macros may include **loops** and **string literals**. Macros may not define other macros but can include other macros, including themselves, with up to 3 levels of depth. After the 3rd level, macros will be left in the compiled code (unless the `--min` flag is used, in which case it will be ignored). Using macros inside macros is **not recommended**
```sh
$ kbf.py -e '=h:"Hello World! "==p:[.>]=hphp'
Hello World! Hello World!
```

## References
KodiBrainFuck can link files together in order to keep your code organized by, for instance including macros or large functions inside of a separate file. Linking a file can be done with the syntax `(path/to/file)`, the contents of the file will be compiled when it is linked, which means that **files referencing each other may cause an infinite loop! You have been warned!**

## Comments
As macros will end up taking up characters you would traditionally use as comments in brainfuck, KodiBrainFuck supports its own comment syntax. To create a comment, simply surround some text in `/`, for instance, `/This comment will not appear in the compiled output/`.

# TODO
[] Memory efficient print function
[] Optimisations for string literals
[] General compiler optimisations
[] More example scripts

# Third party code
[Brainfuck interpreter in python by pocmo](https://github.com/pocmo/Python-Brainfuck)
