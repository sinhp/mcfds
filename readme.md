If you have not done already you need to install [Anaconda](https://docs.anaconda.com/anaconda/install/index.html)


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
