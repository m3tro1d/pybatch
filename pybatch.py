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

parser.add_argument('-m', '--mask', default='*',
	help='File mask. The default is * (all files).')

args = parser.parse_args()
directory = args.dir
file_mask = args.mask


# Ask user
print('This will rename the files in the \'{}\' directory.'.format(directory))
choice = input('Proceed (Y/n)? ')
if not (choice == 'y' or choice == 'Y' or choice == ''):
	print('As you wish.')
	sys.exit(0)


# Rename the files (only random names for now)
