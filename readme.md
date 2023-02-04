If you have not done already you need to install [Anaconda](https://docs.anaconda.com/anaconda/install/index.html) first.


## Install the Dependencies
The notebooks are compatible with Python version 3.5 or later, all packages required are listed in `environment.yml` and `requirements.txt`. Pick any option below to install the dependencies:

#### Create a `conda` environment

Open your `Terminal` (or Command Prompt on Windows). 

Use `environment.yml` to create a `conda` environment by executing the following command line:

```
conda env create -f environment.yml
```

This creates a `conda` environment named "mcfds_LinAlg". For `conda` 4.6 and later versions, activate this environment with

```
conda activate mcfds_LinAlg
```

For `conda` version prior to 4.6, run `source activate mcfds_LinAlg` on Linux and MacOS, `activate mcfds_LinAlg` on Windows.

#### Install with `conda`

```
conda install matplotlib numpy scipy jupyter imageio ipywidgets
```

#### Install with `pip`

Install the packages using `requirements.txt` for `pip`:
```
pip install -r requirements.txt
```

## Check Installation
Run the script `check_install.py` to check whether the required packages are installed correctly:

```
python check_install.py
```


### Opening and running Jupyter Notebooks 

To launch a Jupyter notebook, open your terminal and navigate to the directory where you would like to save your notebook. Then type the command `jupyter notebook` in the your terminal (at the directory where you have saved your notebook) and the program will instantiate a local server at localhost:8888 (or another specified port). For more detailed tutorial see here: https://www.codecademy.com/article/how-to-use-jupyter-notebooks 

You can also run a Jupyter notebook via VSCode. Here is the full guide: https://code.visualstudio.com/docs/datascience/jupyter-notebooks


