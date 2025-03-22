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



# You can add environment variables using the export command, and you can view all the environment variables
# using the env command.

# To give execution privilege for a file run chmod +x ./file.txt



# There are environment variables built in to your shell, meaning different programs and parts of your
# system know about them.
# For example PATH

# The PATH variable is a list of directories your shell will look into when you run a command.
# If you type ls for example, your shell will look in every directory listed in PATH until it finds an ls
# executable. If it finds one itll run it, otherwise itll give an error like command not found.

# Without PATH you could only run executables through their full path.



# If you install a new program and you get a command not found error when trying to execute it in the shell
# It's likely because the directory it's installed in isn't in the list of directories for PATH.

# You can add a script to your PATH to make it executable from anywhere by adding its absolute path to PATH
# export PATH="$PATH:new/path"

# Doing the above will only change PATH for the current shell session. To change it permanently you have
# to add the above command to the shell config.



