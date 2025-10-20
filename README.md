### LCA_Toolbox - An exploration of Python modelling tools for LCA practicioners

The goal of this respository is to make the use of Brigthway 2.5 and other python based LCA tools intuitive for first time Brightway users in Python. 

It is recommended to have Anaconda Navigator and Anaconda Prompt installed. Further recommended software is VSCode and the GitHub extension that you can install in VSCode. You also need to have Python installed and the extensions for Jupyter.

First, the repository has to be cloned and stored on your local machine. Then open the Anaconda Prompt terminal and navigate to the folder using the following command.

    cd C:\Users\yourname\cloned_repository_folder
    
Now, we can install the environment and the required dependencies. Among others, creating the environment from LCA_Toolbox.yml will install Brightway 2.5, premise and helper packages.

    conda env create -f LCA_Toolbox.yml
    
An environment called LCA_Toolbox is now created, which has to be activated in the next step. You will be asked to activate this environment. You should agree to this.

    conda activate LCA_Toolbox

Once activated, this installs a few helper functions:

    conda install -c conda-forge jupyterlab

We now have an activated environment with Brightway 2.5 and PREMISE as open source LCA software tools for Life Cycle Assessment and the development of prospective Life Cycle Inventories. The different scripts in this repository guide you through the installation of different background databases, analysis functions in brightway and application examples for conducting prospective LCA.

If you change something don't forget to push to GitHub