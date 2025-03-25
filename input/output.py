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



# stdin is a stream of data programs read from as they run. Just like all programs provide a way to read
# from stdout/stderr, they also provide a way to read from stdin. All of these streams are handled by your
# operating system.

# Python's API for reading stdin is the input function

# Bash's API for reading stdin is the read command



# You can pipe the output of one program into the input of another using |. This allows some very powerful
# automation.

# The | takes the stdout of the program on the left and pipes it into the stdin of the program on the right

# echo "Have you heard the tragedy of Darth Plagueis the Wise?" | wc -w
# cat /file/file.txt | grep Marshal

# The above work, because most shell commands can optionally read from stdin instead of filepath which is
# what the pipe sets them to do.


# grep -R "Bob" PATH_TO_TRANSACTIONS_DIR --exclude-dir="backups"
# Recursively searches through the defined directory for lines that contain the word Bob. Excludes the
# backups directory. Prints output to stdout. By default, stdout directs to the terminal, but we can
# use piping to direct stdout of one program to the stdin of another program. This also sets the second
# program to read from stdin instead of filepath.




# You can manually kill a program using: kill PID. where PID stand for process ID

# Every process on your machine has a unique ID. you can peep the processes and their ID's using ps command
# process status. the aux option just means show all processes including those owned by other users, and
# show extra info about them.

# If there's a malicious program running that you cant ctrl+c out of because its blocking you can manually
# kill it in another terminal, but youll need it's process ID. to find it's process ID you can run ps aux
# and pipe the stdout into grep name_of_malicious_file.txt. Youll then be able to see the PID and use it to
# kill the program.



# top is a command that allows you to see which processes are using the most resources on your computer,
# useful for diagnosing performance issues.

# By default top sorts by CPU usage, but you can enter M to sort by RAM usage.