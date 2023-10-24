"""
argparse_utils.py

Util functions to be used by argparse for various scripts
"""
import os

"""
Function for validating that input file exists
"""
def input_str(path):
    if not os.path.exists(path):
        parser.error(f"Please enter a valid path to a file. Got: {path}")
    return path

"""
Function for validating that output folder exists
"""
def output_str(path):
    if not os.path.exists(path):
        parser.error(f"Please enter a valid path. Got: {path}")
    return path

"""
Function for validating the spaCy model type
"""
def model_str(model):
    if model not in ['sm', 'md', 'lg', 'trf']:
        parser.error(f"Please enter a valid model (sm, md, lg, trf). Got: {model}")
    return model
