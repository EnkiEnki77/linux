# A program is simply a set of instructions a computer can execute, and an executable is a file
# that contains a program.

# There are two kinds of programs, compiled and interpreted.

# Compiled programs dont rely on other programs to run. Theyre written in languages like C, Rust, or Go

# interpreted programs require an interpreter to be run. Theyre written in languages like Ruby, JS, Python
# The interpreter reads the code as it runs line by line.


# Compiled programs are converted from human readable source code to machine code.
# Machine code is a set of instructions a computer can execute directly.
# Your cpu is hardware designed to execute machine code.

# Interpreted programs are executed by another program called an interpreter.


# The which command tells you the filepath of an installed command line program: which sh

# Interpreters are programs written in a compiled language such as C or Go



# You can run any compiled executable by typing its file path into your terminal.
# bin/genids.sh

# For inerpreted files though the program needs to be told what interpreter to use for the file

# you can list this at the top of the file with a shebang.

# Shebang is a special line at the top of the file that tells the computer what program to use to interpret
# the file.

# ! interpreter [optional-args]

# For a python script for example:
#!/usr/bin/python3



# Bash has configuration files that run everytime you set up a shell environment. They can be used to set
# aliases, functions, and environment variables. Its a hidden file, but you can use the -a flag with ls
# to peak hidden files. Its located at the root ~
# .bashrc is the config file.


# Use the nano command to edit files

# You can edit the bash config to give a message or run a function whenever you start a new shell environment

