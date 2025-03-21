# All the data stored on your computer is organized into files and directories, which are organized
# into a tree-like structure called the filesystem.

# Directories are containers that hold files and other directories
# Files are dumps of raw binary data, they can represent anything, images, text, videos, etc.

# At the top of the file system is a single directory, called the root directory.

# When you open the terminal your working directory (the one youre currently in) will likely be your home
# directory.

# The pwd command prints the filepath to your working directory.

# A file path is a string that describes the location of a file or directory.

# /home/remdu
# / is the root directory, home is the name of a directory inside the root, /remdu is a directory inside
# /home, and is the working directory since its the last directory in the file path.


# The ls command lets you see the contents of your current working directory


# The cd command lets you go to a directory further down in the filesystem tree.
# cd .. lets you move back up a directory.


# You can pass an argument to ls to read the contents of child directories of your working directory:
# ls worldbanc



# relative filepaths take your working directory into account, so they only show the file path to a
# resource starting from your working directory.

# absolute filepaths start from the root directory.


# Relative paths are useful when you know what directory youre in, absolute when you dont.




# The cat command allows you to view the contents of a file or multiple and concatenate their contents

# If you only want to print a certain portion of a file use head -n int, starts from the first line

# tail works similar but starting from the end of the file.


# To go back multiple directories in the file system use cd ../..



# The less and more commands allow you to view the contents of a file one page or line at a time.
# less is the same as more just with more features.
# Press enter to go down a line, q to exit back to your shell,
# pass in -N to show line numbers
# Use spacebar to scroll a page down, and b to go back up.



# Touch updates the access and modification timestamps of a file. If a file doesnt exist it will create
# an empty file with that name. You can also create multiple files at once
# It can be used to check if files exist without altering them.


# mkdir command creates in a new directory in the working directory.



# mv command renames or moves a file.
# To rename: mv some_file.txt new_name.txt
# To move a file from current directory to a nested one: mv some_file.txt some_directory/some_file.txt
# To move a file to parent directory: mv some_file.txt ../some_file.txt
# You can also rename a file when you move it, if you just want to move it, you can omit the file name:
# mv some_file.txt some_directory/


# The rm command deletes a file or empty directory.
# you can add the -r flag to delete all of a directories contents recursively.



# The cp command copies a file from one directory to another: cp some_file.txt destination/
# Or you can recursively copy a directory and its contents to another: cp -R my_dir new_dir


# A users home directory is where their personal files are stored. Its also the directory a user starts
# in when logging into a system.
# A good convention is to do all programming work in a workspace directory in your home directory.

# To cd home use the ~.



# grep has capabilities such as letting you search for a word in a file.
# It will print every line in the file that contains that word

# You can also search multiple files: grep "hello" file.txt file_2.txt

# Or recursively search a whole directory: grep -r "hello"

# . is an alias for the working directory.



# Use find command to find a file or directory by name in a given directory: find directory/ -name file.txt

# Can also find files that match a pattern: find -name "*.txt"

# * is a wildcard that matches anything. If you want to find files that contain a specific word you can
# use * to match everything else.
# Use the wildcard on both ends of a query if you dont know where it might be in the word or if its in the
# middle.










