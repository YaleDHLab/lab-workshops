# Word Vectors

To run this notebook locally on your machine, we recommend that you follow these steps.

### Installing Anaconda (Optional)

To follow along, the first step will be to [install Anaconda](https://www.anaconda.com/download/), a distribution of the Python programming language that helps make managing Python easier.

Once Anaconda is installed, open a new terminal window. (If you are on Windows, you should open an Anaconda terminal by going to Programs -> Anaconda3 (64-bit) -> Anaconda Prompt). Then you can create and activate a virtual environment:

```
# create a virtual environment with Python 3.6 named "3.6"
conda create python=3.6 --name=3.6

# activate the virtual environment
source activate 3.6
```

### Running the Workshop Notebook

You should now see `(3.6)` prepended on your path. Once you see that prefix, you can start the notebook with the following commands:

```
git clone https://github.com/YaleDHLab/lab-workshops
cd lab-workshops/word-vectors
pip install -r requirements.txt
jupyter notebook word-vectors.ipynb
```

Once the notebook is open, you can evaluate a code cell by clicking on that cell, then clicking `Cell -> Run Cells`. Alternatively, after clicking on a cell you can hold Control and press Enter to execute the code in the cell. To run all the cells in a notebook (which I recommend you do for this notebook), you can click `Cell -> Run All`.