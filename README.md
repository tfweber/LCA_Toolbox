#### This is a documentation for setting up Brightway 2.5 in combination with ecoinvent and later with other databases. In order for this script to work, you need to have Brightway installed on your computer and an active environment in which you have defined your project. To do this, navigate to your local project folder/GitHub repository by using

    ```
    cd C:\Users\TimWeber\repos_20LCA\explore_v2
    ```

#### Adjust this with what your local folder structure is. Then, create your environment (here called explore_v2, this can be adjusted to your desired names) which is installed and forged with cmutel brightway25 channel.

    ```
    conda create -n explore_v2 -c conda-forge -c cmutel brightway25
    ```

#### You will be asked to activate this environment. You should agree to this.

    ```
    conda activate explore_v2
    ```

#### Once activated, I also installed these helper functions:

    ```
    conda install -c conda-forge jupyterlab
    ```

#### You now have an active environment and installed Brightway 2.5 on your local computer. You can now make sure to get access to the ecoinvent version you want to import to your Brightway project using the provided script. Congrats on this step in your Brightway journey!

#### After having completed these steps in your Anaconda Prompt it's time to work in the script provided in this repository.

#### When we open the script ecoinvent_importing.ipynb we follow the instructions to get ecoinvent ready and matched with the corresponding ecoinvent biosphere flows contained in brightway. 

    ```# basic imports from brightway
    import bw2analyzer as ba
    import bw2calc as bc
    import bw2data as bd
    import bw2io as bi
    from bw2io.importers import SingleOutputEcospold2Importer
    import bw2analyzer as bwa
    from bw2data import methods

    # other relevant packages
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path
    ```
 
#### Firstly, we install all the packages required for our installation and later analysis.

    ```
    bd.projects.set_current('explore_v2')
    ```

#### In this project setting, we define the name of the project we want to work in, e.g. explore_v2. After this, we setup the ecoinvent-3.10-biosphere as can be downloaded from Brightway.

    ```
    ei_path = 'C:/Users/TimWeber/repos_20LCA/explore_v2/data/ecoinvent 3.10_consequential_ecoSpold02/datasets'
    ei_conseq = "ecoinvent-3.10-consequential"
    ```

#### After we have the biosphere flows imported, we can import the technosphere flows, for which we define the path and the name of the database following the 2 lines of code above.

    ```
    ei_importer = SingleOutputEcospold2Importer(ei_path, ei_conseq)
    ei_importer.apply_strategies()
    ei_importer.write_database()
    ```

#### This part now imports the Ecospold2 files, in which ecoinvent is stored and matches these with the biosphere flows and also writes the database stored in ei_path and named ei_conseq. These 2 objects store the path to ecoinvent on your local computer and also the name for your database, which is written in the code above.

#### Congrats for the 2nd time! You have now successful written an ecoinvent database in your Brightway project. Impact Assessment methods are in this case added through the import of ecoinvent-3.10-biosphere, you can access them via

    ```
    bd.methods
    ```

#### And from this point you can store your desired methods in objects to be able to access them quicker and easier. E.g. by

    ```
    lcia_gwp100 = ('EF v3.1', 'climate change', 'global warming potential (GWP100)')
    lcia_water = ('EF v3.1','water use','user deprivation potential (deprivation-weighted water consumption)')
    lcia_land = ('EF v3.1', 'land use', 'soil quality index')
    ```

#### Thanks for now, much more to add and learn. Please make tfweber aware of any issues or feedback.