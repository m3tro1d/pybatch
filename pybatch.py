import os
import sys
import argparse
import shutil
from glob import glob

# Parse the input parameters
parser = argparse.ArgumentParser(
	description='''Renames all files in the directory that match the pattern with
[pseudo] randomly generated names.''')

args = parser.parse_args()

# Rename the files (only random names for now)
