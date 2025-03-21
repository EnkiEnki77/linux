# unix based systems support multiple users, each with their own home directory, files, and permissions

# sudo lets you run a command as a superuser. You need a password with superuser privileges.


# Permissions determine who can do what to files and directories. Theyre generally presented as a 10-
# character string.

# Anyone accessing a file or directory may or may not have permissions to read, write, or execute it.

# The first character of permissions will be a d or -, indicating directory or file respectively.

# Next three characters are rwx, read, write, execute permissions for the owner of the file. Generally
# the one who created the file, but this can be changed manually.

# If the permission is granted the letter is present, if its not granted itll be a -.

# The next 3 characters apply to permissions for the group

# The last 3 are permissions for everyone else.



# chmod command lets you change permissions.

# ls has an -l flag that prints out the permissions for each item

# chmod -R u=,g=,o= directory, lets you recursively change all the permissions in a directory.



# Executable files are files where the data is a program you can run on your computer.

# Files that end in .sh are shell scripts. They contain shell commands you can execute.

# you can execute a file by typing its filepath into the terminal.

# The -x flag on chmod strips a files execution permission.

# To add it back do u+x

