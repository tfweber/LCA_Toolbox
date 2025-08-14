#### This is a documentation for setting up Brightway 2.5 in combination with ecoinvent and later with other databases. In order for this script to work, you need to have Brightway installed on your computer and an active environment in which you have defined your project. To do this, navigate to your local project folder/GitHub repository by using

    ```
    cd C:\Users\TimWeber\repos_20LCA\explore_v2
    ```

#### Adjust this with what your local folder structure is. Then, create your environment (here called explore_v2, this can be adjusted to your desired names) which is installed and forged with cmutel brightway25 channel.

    ```
    conda create -n brightway25 -c conda-forge -c cmutel brightway25
    ```

#### You will be asked to activate this environment. You should agree to this.

    ```
    conda activate brightway25
    ```

#### Once activated, I also installed these helper functions:

    ```
    conda install -c conda-forge jupyterlab
    ```

#### You now have an active environment and installed Brightway 2.5 on your local computer. You can now make sure to get access to the ecoinvent version you want to import to your Brightway project using the provided script. Congrats on this step in your Brightway journey!

#### After having completed these steps in your Anaconda Prompt it's time to work in the script provided in this repository.