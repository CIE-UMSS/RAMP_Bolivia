# Using RAMP for generating load courves for remote communities in Bolivia

## Description
This repository contains the source code, documentation, and resources for implementing a high-resolution multi-energy load profile generation model tailored for the unique energy consumption patterns observed in Bolivia.

## Overview
RAMP is an open-source software suite for the stochastic simulation of any user-driven energy demand time series based on few simple inputs.
This stochastic model aims to generate high-resolution multi-energy load profiles for remote areas in Bolivia. It utilizes advanced algorithms to simulate energy consumption behaviors, considering various factors such as user classes, appliance usage patterns, and environmental conditions specific to the region.


## Recommended installation method
RAMP has been successfully installed and used on macOS, Windows and Linux.

The easiest way to make RAMP software working is to use the free conda package manager which can install the current and future RAMP dependencies in an easy and user friendly way.

To get conda, download and install "Anaconda Distribution", or "miniconda" which is lighter. You can install RAMP using pip, conda or from source code.
### Installing through pip

1. To install the RAMP software, we recommend creating a new environment. Navigate to the directory where RAMP_Bolivia is located using the Anaconda prompt, then execute the following command:

    ``````
    conda env create -f environment.yml
    ``````
2. If you create a new environment for RAMP, you'll need to activate it each time before using it, by writing the following line in the Anaconda Prompt:
    ```
    conda activate ramp
    ```
3. Now you can use pip to install rampdemand on your environment as follow:

    ```
    pip install rampdemand
    ```
### Installing through the source code

You can also install RAMP from the source code! To do so, you first need to download the source code, which can be done in two ways:

You can use git to clone the repository via:

```
git clone https://github.com/RAMP-project/RAMP.git
```
    
Or, you may download the source code directly from:

RAMP GitHub Repository: https://github.com/RAMP-project/RAMP

In this second case, the source code will be downloaded as a zip file, so you'll need to extract the files.

After downloading the source code using any of abovementioned methods, you'll need to use your anaconda prompt to install it. There are two options again:

You may follow the first two steps mentioned in Installing through pip. Then, change the directory in the prompt to the folder where the source code is saved (where you can find the setup.py file). To install the RAMP software, you may then use:
```
python setup.py install
```

Alternatively, without taking any prior action, simply change the directory in the prompt to the folder where the source code is saved and then use:
```
conda env create -f environment.yml
```
## Quick start

In the repository, you'll find the ```/inputs``` directory, where you can access the essential input files necessary to execute RAMP. These files are organized into different folders, each corresponding to specific use cases in the Bolivian context. Each folder contains a description to guide you through its contents.

Two formats are available for input files: Python files and Excel files. Python files can be executed either within an Integrated Development Environment (IDE), such as Spyder, or directly from the terminal using command-line options.

You can run input files with the extensions .py or .xlsx from the command line. To execute these files, navigate to the inputs folder corresponding to the UseCase you wish to model. If you already know the number of daily profiles you intend to simulate, you can specify it using the -n option.
```
ramp -i <path to .xlsx or .py input file> -n 10
```
This will simulate 10 daily profiles. Note that if you do not provide this option you will being prompted for the number of daily profiles within the console.

If you want to save ramp results to a custom file, you can provide it with the option -o:

```
ramp -i <path to .xlsx input file> -o <path where to save RAMP outputs>
```
Note

You can provide a number of output files, separated from each others by a single blank space, matching the number of input files.

For other examples of command lines options, such as setting date ranges, please visit [the dedicated section](https://rampdemand.readthedocs.io/en/latest/examples/year_simulation/year_simulation.html#setting-date-range) of the documentation.


Other options are documented in the help command:
```
ramp -h
```
It is possible to convert python files into spreadsheet. To do so, go to the ```/spreadshet_inputs``` folder and run:

```
python ramp_convert_old_input_files.py -i <path to the input file you wish to convert>
```
You can create the input files in either Python format or spreadsheet format, using the provided examples as a guide.

## Documentation
Detailed documentation, including usage instructions, API reference, and model insights, can be found [here](https://rampdemand.readthedocs.io/en/latest/?badge=latest). Refer to the documentation for comprehensive guidance on utilizing the stochastic model effectively.

## License
Licensed under the MIT License, allowing for free and open use, modification, and distribution.

## Acknowledgments
We acknowledge the support of ARES for funding and resources that contributed to the development of this stochastic model for the Bolivian case. Additionally, we extend our gratitude to the open-source community for valuable feedback and contributions.

## Contact
For questions, feedback, or collaboration inquiries, please contact clsanchez@uliege.be.

## More information
Want to know more about the possible applications of RAMP, the studies that relied on it and much more? Then take a look at the [RAMP Website](https://rampdemand.org/)!

