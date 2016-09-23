# Introduction to the Command Line

Welcome to the DHLab's introduction to the command line. This guide provides an overview of helpful Unix terminal commands to help with common tasks. To access a Unix terminal on your personal computer, feel free to follow the guides below:

#### OSX

OSX has a built-in Unix terminal that you can access by following these steps:

1. Open Spotlight Search by pressing CMD+SPACEBAR, or by going to the magnifying glass in the top right-hand corner of your screen.

2. Type "terminal" and press RETURN.

3. Alternatively, you can navigate to Finder -> Applications -> Utilities -> Terminal.

#### Windows

Windows does not have a built-in Unix terminal. There are some attempts to provide Unix terminals for Windows machines, including [MinGW](https://git-scm.com/downloads) and [Cygwin](https://www.cygwin.com/), but the easiest thing to do is to gain access to a Linux server from your Windows machine.

One of the most popular ways to gain access to a Linux server from Windows is to use [PuTTY](http://www.putty.org/) to access a Linux server on Amazon Web Services. AWS has a nice guide on [ssh'ing to a Linux server](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html) (or instance) from Windows. 

# The Command Line

## Move the Terminal

The following commands help identify some of the ways you can move a terminal through your computer's file system:

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>pwd</b> | present the terminal's working directory |
| <b>ls</b> {directory} | list the contents within directory | 
| <b>cd</b> {destination} | change the terminal's working directory to {destination} |

<i>Examples</i>:  
```
pwd         # Identify the current working directory
ls -lsh .   # Identify all files in the current working directory
cd ..       # Move the current working directory one level up
```

## Create, Update, and Delete Files

The following commands identify some of the ways you can create, read, update, and delete files from the terminal:

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>mkdir</b> {directory-name} | make a new directory (or folder) named {directory-name} |
| <b>touch</b> {file-name} | create an empty file named {file-name} | 
| <b>nano</b> {file-name} | open {file-name} for editing with the nano text editor |
| <b>cat</b> {file-name} | display the contents of a file on the terminal |
| <b>mv</b> {file-name} {new-location} | move {file-name} to {new-location} |
| <b>rm</b> {file-name} | delete the file named {file-name} | 

<i>Examples</i>:  
```
mkdir folder-with-data       # Create a new directory named folder-with-data  
cd folder-with-data          # Change directories into the new folder  
touch 0 1 2 3 4 5 6 7 8 9    # Create empty files in folder-with-data
mv 9 last-in-sequence.txt    # Rename file 9 to "last-in-sequence.txt"  
ls                           # Show the files in folder-with-data
cd ..                        # Move one directory up
ls                           # Show all files in the new directory 
rm -r /folder-with-data/     # Delete everything in folder-with-data
```

## Helpful Shortcuts

The following commands identify some helpful commands that can expedite your workflow:

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>UP-ARROW-KEY</b> | pull up the last command submitted in this terminal |
| <b>TAB</b> | attempt to auto-complete the current terminal command |

<i>Examples</i>:  
```
mkdir new-folder-with-data                    # Make a new directory
rm -r new-folder-w {{press tab}}              # Autocomplete the directory name
{{press up arrow key twice then hit enter}}   # Make the directory again
{{press up arrow key twice then hit enter}}   # Delete the directory again
```

## Download Data from the Web

The following commands allow you to collect data from websites.

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>curl</b> {url} | request the html content from {url} |
| <b>wget</b> {url} | download html data from {url} |

<i>Examples</i>:  
```
wget -r -l 4 http://plato.stanford.edu/   # Download html from plato.stanford.edu
curl -O https://pbs.twimg.com/profile_images/673907521313234944/WmuM7gbC.png
open WmuM7gbC.png                         # Download and open an image
```

## Chaining Commands Together

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| {command} <b>></b> {file-name} | pipe the result of {terminal-command} into {file-name} |
| {command-a} <b>\|</b> {command-b} | pipe {command-a}'s output into {command-b} |
| {command-a} <b>&&</b> {command-b} | execute {command-a} then execute {command-b} |

<i>Examples</i>:  
```
mkdir secret-data && cd secret-data   # make and move into a new directory
echo "hello you" > secret-data/hello  # write content into a new file
cat secret-data/hello                 # display the contents of the new file
```

## Searching and Counting

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>grep</b> {string} {file} | search for all instances of {string} in {file} |
| {command} <b> \| wc</b> [-l, -w] | count the <b>l</b>ines or <b>w</b>ords in the output of {command} |

## Analyzing and Killing Processes

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>top</b> | check memory and computer usage |
| <b>ps</b> | list the processes running on your machine |
| <b>kill</b> {pid} | kills the process with process id {pid} |

## Useful Tips and Tricks

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>which</b> {program} | check whether and where {program} is installed |
| <b>clear</b> | clear the terminal |
| <b>screen</b> | create a screen for the current terminal session |

## Learning More

| <i>command</i> | <i>result</i> |
|:------- |:-------- |
| <b>man</b> {command} | pull up the manual for {command} |