## Installation
There are two types of install: Default and Developer.

### Default Install
1.  Install the [Anaconda Python 2.7 Distribution](http://continuum.io/downloads).
2.  Open a Terminal (Mac and Linux) or PowerShell (Windows).
3.  Run `pip install --pre topicexplorer -i https://inpho.cogs.indiana.edu/pypi/`.
    
    **Note:** `--pre` has *two* `-` characters. When the `1.0` release happens, `--pre` will no longer be necessary.
4.  Test installation by typing `topicexplorer -h` to print usage instructions.

### Developer Install
1.  [Set up Git](https://help.github.com/articles/set-up-git/)
2.  Install the [Anaconda Python 2.7 Distribution](http://continuum.io/downloads).
3.  Open a terminal and run `pip install --src . -e git+https://github.com/inpho/topic-explorer#egg=topicexplorer`
4.  Test installation by typing `topicexplorer -h` to print usage instructions.

## Usage
![Workflow](http://inphodata.cogs.indiana.edu/img/workflow.png)

1.  Initialize the Topic Explorer on a file, folder of text files, or folder of folders:

    ```
    topicexplorer init PATH [CONFIG]
    ```

    This will generate a configuration file called *CONFIG*.

2.  Train LDA models using the on-screen instructions:

    ```
    topicexplorer train CONFIG
    ```

3.  Launch the topic explorer:

    ```
    topicexplorer launch CONFIG
    ```

4.  Press Ctrl+C to quit all servers.
