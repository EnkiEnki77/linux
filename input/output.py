# man command shows the manual for other programs.

# Often times youre looking for specific information, such as what a certain flag does. So you can
# search using "/", go to the next result using "n", or go back a result using "N"


# Commands take flags to alter their functionality:
# ls -l for a long list
# ls -a to show all files, including hidden ones
# ls -al you can also combine flags.

# The convention is single character commands are prefixed with a single dash -h, multi-character two dashes
# --help.



# By convention most CLI tools have a help flag -h or --help to learn how the tool works.

# It's often easier to parse than a full man, acting as more of a quickstart guide than a full manual.


# curl is a CLI tool that lets you make network requests from the command line.



# exit codes are how programs communicate whether they executed properly or not, 0 is success, anything else
# was an error. To check the exit code for the last tool you ran print the $? variable.



# All programming languages have a way to print to stdout, which is a stream of data that prints to the
# terminal. In JS it's console.log, in Python print, in Bash it's echo.



# stderr is a data stream just like stdout, but it's intended for error messages.

# It's a separate stream so you can print it to a different place, but by default both stdout and stderr
# print to your terminal. Though you can direct stdout and stderr to print somewhere else using the >
# and 2> operators respectively.

# So in bash the echo command is how you access the stdout stream, > is the operator to choose where it's
# directed.


# When you execute a command or script you can redirect the stdout or the stderr to another file.
# /tmp/ is a great place to temporarily log things, because files there are deleted by your system routinely

