import os
import sys
import argparse
import shutil
from glob import glob

# Parse the input parameters
parser = argparse.ArgumentParser(
	description='''Renames all files in the directory that match the pattern with
[pseudo] randomly generated names.''')

parser.add_argument('-d', '--dir', default='.',
	help='Files directory. The default is current directory.')

args = parser.parse_args()
print(args)

# Rename the files (only random names for now)
