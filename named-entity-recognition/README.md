# Named Entity Recognition

Named Entity Recognition (NER) is the process of identifying "entities" (people, locations, organizations...) in unstructured text. NER is frequently used in data analysis because it helps one quickly identify the key agents within a corpus of texts. The guide below is meant to help you run NER on texts for your own research projects.

## Software Requirements

There are lots of packages and software solutions for running NER on corpora. One of the most popular is Stanford's [CoreNLP](https://stanfordnlp.github.io/CoreNLP/) package, which performs a wide variety of analytic techniques on input text files. The guide below will help you get set up to use Stanford's CoreNLP on a machine you control.

Steps to install all required software:

1. [Download the CoreNLP software to your desktop](https://stanfordnlp.github.io/CoreNLP/index.html#download)
2. [Install the Java Development Kit (JDK)](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
3. [Install the Anaconda Python Distribution](https://www.anaconda.com/download/)

## Getting Started

<b>Download Stanford Corenlp Sourecode</b>

Visit the [Stanford CoreNLP homepage](https://stanfordnlp.github.io/CoreNLP/index.html#download) and click the big Download button. Once the download finishes, move the downloaded folder to your desktop and unzip it.

#### Open a Terminal

Once the three dependencies above are installed, you will want to open a terminal.

| Operating System | Command |
|---|---|
| OSX | type COMMAND+SPACE_BAR, type <i>terminal</i>, and hit ENTER [[screenshot](./images/osx_terminal.png)] |
| Windows | go to Programs/Apps -> Anaconda3 -> Anaconda Prompt [[screenshot](./images/windows_terminal.png)] |

#### Change Terminal Directories to the CoreNLP folder

Once you have a terminal, you will need to change the terminal's directory to your desktop. You can do so by running the following commands:

| Operating System | Command |
|---|---|
| OSX | `cd ~/Desktop`  |
| Windows | `cd C:\Users\YOUR_USERNAME\Desktop` |

After executing the command above, you can move the terminal into the Stanford CoreNLP folder by typing:

| Operating System | Command |
|---|---|
| OSX | `cd stanford-corenlp-full-2017-06-09`  |
| Windows | `cd stanford-corenlp-full-2017-06-09` |

If you now type `ls` on OSX or `dir` on Windows, then hit ENTER, you should see a long list of files, one of which is named input.txt. If you don't see that file, raise your hand or close your terminal and repeat the steps above to get your terminal set up.

#### View the Sample Input File

Open the Stanford CoreNLP directory on your desktop and double-click <i>input.txt</i>. You should see: "Stanford University is located in California. It is a great university, founded in 1891."

In the steps below, we'll run NER on this text to try and identify entities within the file.

#### Run NER on the Sample Input File

With your terminal in the corenlp folder, you can run NER on the sample input file by typing the following into your terminal and hitting enter:

```java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file input.txt```

This command does the following:

| Command Element | Function |
|---|---|
| java | Ask your machine to submit code to your Java interpreter |
| -cp '*' | Add all JAR files in your current directory to your classpath |
| -Xmx2g | Allocate 2 gigabytes of RAM for this process |
| edu.stanford...NLP | Specify the path to the main CoreNLP file [[source](https://github.com/stanfordnlp/CoreNLP/blob/master/src/edu/stanford/nlp/pipeline/StanfordCoreNLP.java)] |
| -annotators ... | Enumerate the markup options to include in output [[read more](https://stanfordnlp.github.io/CoreNLP/annotators.html)] |
| -file input.txt | Specify the input file to process |

#### View the Output

You should see some some output text on your terminal. Once this process finishes, open the input.txt.xml file in the Stanford CoreNLP folder. Opening this file should reveal a huge XML file with lots of markup. Congratulations--you've just performed Named Entity Recognition!

## Understanding CoreNLP Output

The output from the CoreNLP pipeline looks a bit like this:

```
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="CoreNLP-to-HTML.xsl" type="text/xsl"?>
<root>
  <document>
    <sentences>
      <sentence id="1">
        <tokens>
          <token id="1">
            <word>Stanford</word>
            <lemma>Stanford</lemma>
            <CharacterOffsetBegin>0</CharacterOffsetBegin>
            <CharacterOffsetEnd>8</CharacterOffsetEnd>
            <POS>NNP</POS>
            <NER>ORGANIZATION</NER>
            <Speaker>PER0</Speaker>
          </token>
          <token id="2">
            <word>University</word>
            <lemma>University</lemma>
            <CharacterOffsetBegin>9</CharacterOffsetBegin>
            <CharacterOffsetEnd>19</CharacterOffsetEnd>
            <POS>NNP</POS>
            <NER>ORGANIZATION</NER>
            <Speaker>PER0</Speaker>
          </token>
        [...]
      [...]
    [...]
  [...]
</root>
```

This XML document models an input `document` in the following way:

The `document` contains `sentences`.  
Each `sentence` contains `tokens`.  
Each `token` contains `word`, `lemma`, `POS`, `NER` and other attributes.  

Each token's `word` attribute refers to the raw input word (e.g. cats).  
Each token's `lemma` attribute refers to the linguistic lemma of the input word (e.g. cat).  
Each token's `POS` attribute identifies the word's Part Of Speech.    
Each token's `NER` attribute identifies whether the word contains an <i>entity</i>.  

Most words will have an `NER` attribute of `0`, which means the given word is not a named entity. If a word does contain an entity, however, its `NER` attribute will equal one of the following types of entities: `PERSON`, `LOCATION`, `ORGANIZATION`, `MISC`, `MONEY`, `NUMBER`, `ORDINAL`, `PERCENT`, `DATE`, `TIME`, `DURATION`, `SET`.

In the sample input.txt file, for example, both <i>Stanford</i> and <i>University</i> have NER values of `ORGANIZATION`, as the two words identify a particular organization.

Given the above structure in the Stanford output files, one can easily retrieve people, locations and organizations from an input set of texts.

## Annotating Multiple Files

To process multiple files, you can create a file called `input_files.txt` that has the path to each file to be processed on a new line:

```
files_to_process/file1.txt
files_to_process/file2.txt
files_to_process/file3.txt
```

If you have a folder with serveral files you with to process, you can list each file on a new line by running:

| Operating System | Command |
|---|---|
| OSX | `ls files_to_process/* > input_files.txt`  |
| Windows | `dir files_to_process\* /s/b > input_files.txt` |

You can then run the CoreNLP on this list of files by running:

```java -cp "../path/to/stanford-corenlp-full-2017-06-09/*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -filelist input_files.txt -outputDirectory corenlp_output```

<b>NB</b>: Windows users will need to replace the `/` folder delimeter with `\` in the command above.

## Sample Application

Let's suppose we wish to perform NER on all of the [Sherlock Holmes tales](https://sherlock-holm.es/ascii/). To do so, we would need to gain access to plain text copies of all the tales available here, and we'd want to place them all in a common directory. For now, let's download a sample of the Holmes tales from [here](https://s3-us-west-2.amazonaws.com/lab-workshops/sherlock_holmes_sample.zip) and drag them into the CoreNLP folder on your desktop.

Once those files are in your CoreNLP folder, let's generate an `input_files.txt` using the commands mentioned above:

| Operating System | Command |
|---|---|
| OSX | `ls sherlock_holmes_sample/* > input_files.txt`  |
| Windows | `dir sherlock_holmes_sample\* /s/b > input_files.txt` |

Now let's submit that list of files to the CoreNLP pipeline:

```java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -filelist input_files.txt -outputDirectory corenlp_output```

This will generate a folder called corenlp_output in your CoreNLP folder, and will store each processed file in that folder.

## Analyzing CoreNLP Output

Given these output files, we can perform various kinds of analysis. One of the simplest kinds of analysis is to count the number of times each entity occurs. To do so, download [this file](https://gist.githubusercontent.com/duhaime/08f8ac4962f53c185e705189a3f6e9b5/raw/d66e20aa2fabc086211f2f2cf09e3e0fde4a6cdf/count_corenlp_entities.py) to your CoreNLP folder and save it as count_corenlp_entities.py.

Once that's all set, you can run:

```
python count_corenlp_entities.py corenlp_output/
```

This will generate a file named `open ner_counts.txt` that identifies the number of times each entity occurs in your dataset. Et voila, you now have tabluar data you can visualize!
