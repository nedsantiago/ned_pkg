# Process Name: 
# Read CSV files
# 
# Description:  
# A standard way to read csv files to avoid re-learning the usual mistakes.
# Use this with a "with" statement
# 
# Inputs:       
# Given a string that represents the path to a csv
# 
# Outputs:      
# Produces an open object

from csv import DictReader


def dict_read_csv(file_path):
    assert type(file_path) is str, TypeError("file path needs to be a string")

    return open(file_path, "r", encoding="utf-8-sig")