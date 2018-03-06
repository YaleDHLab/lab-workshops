# Introduction to Topic Modeling with Python

The materials for this workshop are all located in the linked IPython Notebook. To open the notebook, we recommend the following workflow.

### Getting Started with Anaconda

First, let's [install Anaconda](https://www.anaconda.com/download/).

Once Anaconda is installed, create and activate a virtual environment:

```
# create a virtual environment with Python 3.6 named "3.6"
conda create python=3.6 --name=3.6

# activate the virutal environment
source activate 3.6
```

### Running the Workshop Notebook

You should now see `(3.6)` prepended on your path. Once you see that prefix, you can start the notebook with the following commands:

```
git clone https://github.com/YaleDHLab/lab-workshops
cd lab-workshops/topic-modeling-python
pip install -r requirements.txt
jupyter notebook model-topics.ipynb
```