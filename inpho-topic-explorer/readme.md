### Default Install
1.  Install the [Anaconda Python 2.7 Distribution](http://continuum.io/downloads) - click on "Graphical Installer" under Python 2.7 
2.  Open a Terminal (Mac and Linux) or PowerShell (Windows).
3.  Run `pip install --pre topicexplorer -i https://inpho.cogs.indiana.edu/pypi/`.
    
    **Note:** `--pre` has *two* `-` characters. When the `1.0` release happens, `--pre` will no longer be necessary.
4.  Test installation by typing `topicexplorer -h` to print usage instructions.


## Usage

1.  Initialize the Topic Explorer on a file, folder of text files, or folder of folders:

    ```
    topicexplorer init insertPathToFiles 
    #for example: topicexplorer init Desktop/wikimedia_russian_texts/txt
    ```
    When prompted, name your corpus (ex: wikimedia_russian_texts).
    The init command will generate a configuration file called *CONFIG*.

2.  Train LDA models using the on-screen instructions:

    ```
    topicexplorer train CONFIG
    #for example: topicexplorer train Desktop/wikimedia_russian_texts/txt.ini
    ```
    When prompted, specify the number of topics you would like (defaults: 20, 40, 60, 80).
    When prompted, specify the number of training iterations (default: 200).
    
3.  Launch the topic explorer:

    ```
    topicexplorer launch CONFIG
    #for example: topicexplorer launch Desktop/wikimedia_russian_texts/txt
    ```

4.  Press Ctrl+C to quit all servers.
