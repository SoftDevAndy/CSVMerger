# CSVMerger
Merges two CSV files based on a column header.

Simple project for a bud!

# Instructions

Install Python

https://www.python.org/downloads/

Once it's installed, open a command window and try the following command

```python -V```

You should see something like 

```Python 3.8.0```

To be safe install 

In the same command window run the following commands

json

```pip install json```

pandas

```pip install pandas```

Now both of the libraries needed to run the script are now installed.


# Running the Script

Move the script and the config into the same folder as both the csvs you need to merge

Update the config file

```
{
    "IN_FILE_A_LOCATION" : "FILEA.csv",
    "IN_FILE_B_LOCATION" : "FILEB.csv",
    "MERGE_COLUMN" : "companyname",
    "OUT_FOLDER_LOCATION" : "",
    "OUT_FILENAME" : "OUTPUT",
    "OUTFILE_TYPE" : ".csv"
}
```

Open a command line and navigate to where the script is and simply run this command

```
python CSVMerger.py
```

A file should appear in the location you've set (or where you've run the script from) named

```OUTPUT-20191122215550.csv```

or similar.
