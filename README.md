# LCA_Toolbox - An exploration of Python modelling tools for LCA practicioners

The goal of this respository is to make the use of Brigthway 2.5 as intuitive and easy to a beginner in Python. The repository is structured to first install and import all necessary software to setup a functioning environment to analyse your Brightway 2.5 models in. An other aim is to enable the user to apply different background databases such as EcoInvent, EXIOBASE, BONSAI and others. 

First, we need to clone the repository and store it on your local machine. Then navigate to this folder in your Anaconda Prompt terminal. When you navigated to your repository, we now want to install and activate an environment for this work. The settings and dependencies are stored in brightway25_tw.yml, which we are referencing now to install all packages required for this repository.

    conda env create -f brightway25_tw.yml
    
You will be asked to activate this environment. You should agree to this.

    conda activate brightway25_tw

Once activated, this installs a few helper functions:

    conda install -c conda-forge jupyterlab

We now have an activated environment with Brightway 2.5 and PREMISE as softwares to conduct LCA and prospective LCA. The repository guides you through the installation of different databases, analysis tools for brightway and application examples for conducting prospective LCA.
