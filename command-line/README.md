# Command Line Crash Course

Welcome to the DHLab's introduction to the command line. This guide provides an overview of helpful Unix terminal commands to help with common tasks. To access a Unix terminal on your personal computer, feel free to follow the guides below:

#### OSX

OSX has a built-in Unix terminal that you can access by following these steps:

1. Open Spotlight Search by pressing CMD+SPACEBAR, or by going to the magnifying glass in the top right-hand corner of your screen.

2. Type "terminal" and press RETURN.

3. Alternatively, you can navigate to Finder -> Applications -> Utilities -> Terminal.

#### Windows

Windows does not have a built-in Unix terminal. There are some attempts to provide Unix terminals for Windows machines, including [MinGW](https://git-scm.com/downloads) and [Cygwin](https://www.cygwin.com/), but the easiest thing to do is to gain access to a Linux server from your Windows machine.

One of the most popular ways to gain access to a Linux server from Windows is to use [PuTTY](http://www.putty.org/) to access a Linux server on Amazon Web Services. AWS has a nice guide on [ssh'ing to a Linux server](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html) (or instance) from Windows. 

# Getting Started with the Command Line

Each of the sections below is meant as an introduction to a commonly-used set of terminal commands. To get started, try running the commands below each section in a terminal.

## Move the Terminal

The following commands help identify some of the ways you can move a terminal through your computer's file system. The "file system" is a fancy name for the hierarchical series of folders (or "directories") that exist on a given computer. The commands below are valuable because they allow you to navigate through your computer to gain access to different files and resources:

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>pwd</b> | present the terminal's working directory |
| <b>ls</b> {directory} | list the contents within directory | 
| <b>cd</b> {destination} | change the terminal's working directory to {destination} |

<i>Examples</i>:  
```
pwd         # Identify the current working directory
cd ..       # Move the current working directory one level up
pwd         # Show the terminal's new location
cd ubuntu   # Change directories back to your original location
ls -lsh .   # Identify all files in the current working directory
```

### Create, Update, and Delete Files

While moving through one's computer is useful, it's more fun to work with actual files. The following commands identify some of the ways you can create, read, update, and delete files from the terminal:

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>mkdir</b> {directory-name} | make a new directory (or folder) named {directory-name} |
| <b>touch</b> {file-name} | create an empty file named {file-name} | 
| <b>nano</b> {file-name} | open {file-name} for editing with the nano text editor |
| <b>cat</b> {file-name} | display the contents of a file on the terminal |
| <b>mv</b> {file-name} {new-location} | move {file-name} to {new-location} |
| <b>rm</b> {file-name} | delete the file named {file-name} | 

<i>Examples</i>:

Make a directory in which to store files

```
cd /home/ubuntu              # Change to a particular directory
mkdir folder-with-data       # Create a new directory named folder-with-data  
ls                           # Show that the directory was created
```

Change into that directory and make some new files

```
cd folder-with-data          # Change directories into the new folder  
ls                           # Show all files in the current directory
touch 0 1 2 3 4 5            # Create empty files in folder-with-data
ls                           # Show all files in the directory again
```

Enter text content into one of the files in the directory

```
nano 0                  # Use the nano text editor to open the file named "0"
{{ type a message }}    # Enter a message in the file
{{ press CONTROL+X }}   # Exit the text editor
{{ press y to save }}   # Indicate the changes made to the file should be saved
{{ press ENTER }}       # Accept the default write mode
nano 0                  # Open the file again to ensure the text is still there
{{ press CONTROL+X }}   # Exit the text editor again
```

Rename one of the files in the directory
```
mv 0 special-file.txt    # Rename the file named "0" to "special-file.txt"
ls                       # Show the files in folder-with-data
```

Delete the directory we just made

```
cd ..                    # Move one directory up
ls                       # Show all files in the new directory
rm -r folder-with-data/  # Delete everything in folder-with-data
```

### Helpful Shortcuts

When fist learning about the terminal, it's good practice to type out one's commands. After mastering some of the basics, it's helpful to expedite terminal work with the following shortcuts:

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>UP-ARROW-KEY</b> | pull up the last command submitted in this terminal |
| <b>TAB</b> | attempt to auto-complete the current terminal command |

<i>Examples</i>: 

Make a new directory:
```
ls                                      # Show all files in the current directory
mkdir new-folder                        # Make a new directory
ls                                      # Show all files in the current directory
```

Delete the new directory using autocomplete:
```
rm -r new-fo {{press tab then enter}}   # Autocomplete the directory name
ls                                      # Show that the folder was deleted
```

Make the directory again, this time using shortcuts

```
{{press the up arrow key four times}}   # Cycle through previous commands
{{press enter}}                         # Submit the command to create the directory
ls                                      # Show that the folder was created
```

Delete the directory again, this time using shortcuts

```
{{press the up arrow key four times}}   # Delete the directory again
{{press enter}}                         # Submit the command to delete the directory
ls                                      # Show that the directory is gone
```

# Useful Commands

The commands above are meant as a brief introduction to helpful Unix commands. The commands below are a little more advanced, and get useful work done.

### Download Data from the Web

The web has lots of data, and the command line makes it easy to fetch that data. The following commands allow you to kick start some data collection:

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>curl</b> {url} | request the html content from {url} |
| <b>wget</b> {url} | download html data from {url} |

<i>Examples</i>:  


```
# Download data from plato.stanford.edu:
wget -r -l 4 http://plato.stanford.edu/

# Download an image:
curl -O https://pbs.twimg.com/profile_images/673907521313234944/WmuM7gbC.png
```

### Compress and Uncompress Files

It's sometimes necessary to compress or uncompress files. One can do so with the following commands:

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>unzip</b> {directory.zip} | Unzip the files in {directory.zip} |
| <b>tar</b> -zcf {directory.tar.gz} {directory} | Compress the files in {directory} into {directory.tar.gz} |
| <b>tar</b> -zxf {directory.tar.gz} | Uncompress the data in {directory.tar.gz} |

<i>Examples</i>:
```
mkdir my-files                      # make a new directory
cd my-files                         # change into the new directory
touch 0 1 2 3                       # make some files in the directory
cd ..                               # move up one directory
tar -zcf my-files.tar.gz my-files   # compress my-new-files
ls                                  # show the files in the current directory
rm -r my-files                      # delete the my-files directory
ls                                  # show that the directory is gone
tar -zxf my-files.tar.gz            # uncompress my-new-files.tar.gz
ls                                  # show the files in the current directory
```

### Chain Commands Together

Often the most powerful uses of the command line involve combining multiple commands into one larger command. The following commands show some ways of doing so:

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| {command} <b>></b> {file-name} | pipe the result of {terminal-command} into {file-name} |
| {command-a} <b>\|</b> {command-b} | pipe {command-a}'s output into {command-b} |
| {command-a} <b>&&</b> {command-b} | execute {command-a} then execute {command-b} |

<i>Examples</i>:  
```
pwd                                   # show where the terminal is located
mkdir secret-data && cd secret-data   # make and move into a new directory
pwd                                   # show the terminal's new location
echo "hello you" > hello              # write content into a new file
nano hello                            # open the hello file in a text editor
{{ CONTROL+X }}                       # exit the text editor
cd ..                                 # move one directory up
cat secret-data/hello                 # display the contents of the new file
```

### Search and Count

One useful series of commands focus on searching through data or counting items on the command line. You can get started with these tasks using the commands below:

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>grep</b> {string} {file} | search for all instances of {string} in {file} |
| {command} <b> \| wc</b> [-l, -w] | count the <b>l</b>ines or <b>w</b>ords in the output of {command} |

<i>Examples</i>:
```
# get some sample song lyric data
wget https://github.com/YaleDHLab/lab-workshops/blob/command-line/command-line/data/lyrics.tar.gz?raw=true

tar -zxf lyrics.tar.gz   # unzip the data
cd lyrics                # change into the lyrics folder
ls                       # list all of the files in the folder
grep title: *            # search for 'title' in the directory
ls | wc -l               # count the files in the current directory
```

### Analyze and Terminate Processes

It's often helpful to analyze how many system resources are being used by different processes on a machine, or to be able to kill particular applications or processes that are stuck. One can do so with the following commands:

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>top</b> | check memory and computer usage |
| <b>ps</b> | list the processes running on your machine |
| <b>kill</b> {pid} | kills the process with process id {pid} |

<i>Examples</i>:
```
top                    # check current system usage
q                      # exit the screen
ps -ef                 # find all processes currently running
ps -ef | grep Python   # find all running Python processes

# CAUTION! force kill all currently running Python processes
ps -ef | grep Python | awk '{print $2}' | xargs kill -9
```

### Useful Tips and Tricks

The following odds and ends don't fall clearly into any of the above categories, but they're very useful commands to know:

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>which</b> {program} | check whether and where {program} is installed |
| <b>clear</b> | clear the terminal |
| <b>screen</b> | create a screen for the current terminal session |

<i>Examples</i>:
```
ls          # show all files in the current directory
clear       # clear the terminal
which r     # check whether and where the R programming language is installed
```

### Learn More about Commands

The guide above is meant only as a brief introduction to a small subset of available Unix commands. To learn more about any of these commands, or about any other Unix terminal command, just remember the `man` command:

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>man</b> {command} | pull up the manual for {command} |

<i>Examples</i>:
```
man ls     # pull up the manual for the ls command
man grep   # pull up the manual for the grep command
```

### Command Line Tutorial

If you want to master the command line, feel free to consult CodeCademy's excellent tutorial:

Learn the Command Line, by CodeCademy: https://codecademy.com/learn/learn-the-command-line
