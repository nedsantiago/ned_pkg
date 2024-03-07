# Process Name: 
# Test File Dialog
# 
# Description:  
# Tests file_dialog.py
# 
# Inputs:       
# No inputs required, simply run the test
# 
# Outputs:      
# Shows the test results in the terminal

import pytest
# import module to test
from ..src.file_dialog import *


def test_request_open_folder_is_str():
    note_to_user = "Testing open folder is string, get anything"
    return_type = type(request_open_folder(note=note_to_user))
    assert return_type is str, TypeError("Return type must be a string")

def test_request_open_file_is_str():
    note_to_user = "Testing open file is string, get anything"
    return_type = type(request_open_file(note=note_to_user))
    assert return_type is str, TypeError("Return type must be a string")

def test_request_write_file_is_str():
    note_to_user = "Testing write file is string, get anything"
    return_type = type(request_write_file(note=note_to_user))
    assert return_type is str, TypeError("Return type must be a string")