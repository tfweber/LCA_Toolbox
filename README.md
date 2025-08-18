# README.md 

#### This repository is structured in a way to guide the user through the different steps and functionalities that brightway 2.5 offers, from importing and working with ecoinvent, to foreground analysis, to importing Brightway EXCEL models. There is a Jupyter notebook for every category identified. Contributions and suggestions for further categories are welcome to enable a collective learning experience.

#### Firstly, we need to install and setup the background for Brightway 2.5 on our machine so we can work in the repository. We need to have Brightway installed on your computer and an active environment in which you have defined your project. To do this, navigate to your local project folder/GitHub repository by using

    ```
    cd C:\Users\TimWeber\repos_20LCA\brightway25
    ```

#### Adjust this with what your local folder structure is. Then, create your environment (here called explore_v2, this can be adjusted to your desired names) which is installed and forged with cmutel Brightway25 channel.

    ```
    conda create -n brightway25 -c conda-forge -c cmutel brightway25
    ```

#### You will be asked to activate this environment. You should agree to this.

    ```
    conda activate brightway25
    ```

#### Once activated, this installs a few helper functions:

    ```
    conda install -c conda-forge jupyterlab
    ```

#### You now have an active environment and installed Brightway 2.5 on your local computer. You can now make sure to get access to the ecoinvent version you want to import to your Brightway project using the provided script. After having completed these steps in your Anaconda Prompt it's time to work in the script provided in this repository. Congrats on the first step in your Brightway journey!
