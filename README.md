# FDI, Assets & Liabilities

Please note. We use github for versioning purposes only. If anyone wants the actual data involved it will always be easily accessible via the ONS website (www.ons.gov.uk) and API service.

## Setup & Prep
1.) Download this repository with the "download ZIP" button.

2.) Unzip everything into its own folder.

3.) You will need to copy all 4 source files required into this folder. The filenames might vary but are essentially: FDI inwards, FDI outwards, Assets, Liabilities.

## Explanation

The various tabs from these 4 spreadsheets combine to give us 10 distinct explorable datasets as outline in the table below.

![alt tag](/images/summary.png)

## Usage

These scripts are run from a batch file (there's too much going on to really build an convenient mouse click launcher).

To use it:

1.) Right click and edit the "click to run" file.

2.) Update both the file names and extensions (either .xls or .xlsx) by changing the information shown in green below (you need to include the quotes).

![alt tag](/images/batch_commands.png)

Note: DO NOT use a filename with a space in it. If you get one just take the space out before running these scripts.

3.) Save, exit and double click the batch file to extract and transform the data.


## Optional Processing

Each dataset is created by runnng three seperate commands. These are clearly marked in the batch file so you can tailor what datasets the script is creating by removing the unwanted code (see example below for what you'd need to remove to not process 5).

![alt tag](/images/single_dataset.png)


## Note

This was one of the first recipe suites we did and databaker has come a long way since this was written so - DONT - use this one as an example, it's rather clunky :)




