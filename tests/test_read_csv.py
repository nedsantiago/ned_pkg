# Process Name: 
# Test Read CSV
# 
# Description:  
# Tests read_csv.py
# 
# Inputs:       
# No inputs required, simply run the test
# 
# Outputs:      
# Shows the test results in the terminal

import pytest
import io
# import module to test
from ..read_csv import *


def test_dict_read_csv():
    file = dict_read_csv(file_path="./tests/sample_csv.csv")
    assert isinstance(file, io.TextIOWrapper), TypeError("Value must be an TextIOWrapper object")