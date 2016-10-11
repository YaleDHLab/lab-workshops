### Get Russian Poetry Data

To get a zip archive of Russian poetry, visit:

https://s3-us-west-2.amazonaws.com/lab-workshops/russian-poetry.zip

Then move this directory to your Desktop to make it easier to find.

### Default Install
1.  Install the [Anaconda Python 2.7 Distribution](http://continuum.io/downloads) - click on "Graphical Installer" under Python 2.7 
2.  Open a Terminal (Mac and Linux) or PowerShell (Windows).
3.  Run `pip install --pre topicexplorer -i https://inpho.cogs.indiana.edu/pypi/`.
    
    **Note:** `--pre` has *two* `-` characters. When the `1.0` release happens, `--pre` will no longer be necessary.
4.  Test installation by typing `topicexplorer -h` to print usage instructions.


## Generating Topics

1.  Initialize the Topic Explorer on a file, folder of text files, or folder of folders:

    ```
    topicexplorer init insertPathToCorpus
    #for example: topicexplorer init Desktop/wikimedia_russian_texts/txt
    ```
    When prompted, name your corpus (ex: wikimedia_russian_texts).
    
    The init command will generate a configuration file called *CONFIG*.


2.  Set a min and max frequency for word occurence:
    
    ```
    topicexplorer prep insertPathToCorpus
    #for example: topicexplorer prep Desktop/wikimedia_russian_texts/txt
    ```
    When prompted, enter max number (ex: 500).
   
    When prompted, enter min number (ex: 1).
    

3.  Train LDA models using the on-screen instructions:

    ```
    topicexplorer train CONFIG
    #for example: topicexplorer train Desktop/wikimedia_russian_texts/txt.ini
    ```
    When prompted, specify the number of topics you would like (defaults: 20, 40, 60, 80).
    
    When prompted, specify the number of training iterations (default: 200).
    

4.  Launch the topic explorer:

    ```
    topicexplorer launch CONFIG
    #for example: topicexplorer launch Desktop/wikimedia_russian_texts/txt
    ```


5.  Press Ctrl+C to quit all servers.
