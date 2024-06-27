# Reading-from-Delphes
Simple pyroot scripts to read from Delphes output and produce simple histograms.

## Installation

[Pipenv](https://pipenv.pypa.io/en/latest/) is recommended for managing the package dependencies for this project. Plenty of tutorials ([example](https://realpython.com/pipenv-guide/)) are available for more details on how to use it.

You can install pipenv locally using the following command. It will place the files inside your home directory.

```shell
pip install --user pipenv
```

If the above command succeeds and you still cannot find the `pipenv` command, then add the following lines to your `.bashrc`. You will need open a new shell for the changes to take effect. Alternatively you can run the commands in your existing session.

```shell
export PATH=${HOME}/bin:${HOME}/.local/bin:${PATH}
export LD_LIBRARY_PATH=${HOME}/lib:${HOME}/.local/lib64:${LD_LIBRARY_PATH}
```

The following commands will download and install this package on the B'ham PP cluster. The `--site-packages` argument is important as it will reuse the system PyROOT.

```shell
git clone https://github.com/BILPAware/FutureWMassAnalysis.git
cd FutureWMassAnalysis
pipenv install --site-packages .
```

Create a local configuration file and edit it to include the path to your aMC@NLO with Delphes installed.
```shell
cp analysis.yaml.example .analysis.yaml
vim .analysis.yaml
```

## How to use
Run the following inside the `FutureWMassAnalysis` directory.

```
pipenv run python PlotFromRoot.py example.yaml
```

It works with signal samples provided [here](https://bilpa.docs.cern.ch/projects/wmass/samples/).

