import os
import sys
import argparse
import shutil
from random import randint
from glob import glob


def gen_name(length, numbers=False, uppercase=False):
	'''Returns a randomly generated name'''
	name = ''
	# Generating
	for _ in range(length):
		# Numbers
		if numbers and randint(0, 1) == 1:
			name += str(randint(0, 9))
			continue
		# Uppercase letters
		if uppercase and randint(0, 1) == 1:
			name += chr(randint(65, 90))
			continue
		# Plain boring letters
		name += chr(randint(97, 122))
	return name


# Parse the input parameters
parser = argparse.ArgumentParser(
	description='''Renames all files in the directory that match the pattern with
[pseudo] randomly generated names.''')

parser.add_argument('-d', '--dir', default='.',
	help='files directory (default: current)')

parser.add_argument('-m', '--mask', default='*',
	help='file mask (default: * e.g. all files)')

args = parser.parse_args()
directory = os.path.abspath(args.dir)
file_mask = args.mask


# Check the directory
if not os.path.isdir(directory):
	print('The specified directory does not exist.')
	sys.exit(1)


# Ask user
print('This will rename the files in the \'{}\' directory.'.format(directory))
choice = input('Proceed (Y/n)? ')
if not (choice == 'y' or choice == 'Y' or choice == ''):
	print('As you wish.')
	sys.exit(0)


# Change the directory
os.chdir(directory)
# Loop through the files
for fname in glob(file_mask):
	if os.path.isfile(fname):
		# Generate the new name
		ext = fname.split('.')[-1]
		new_name = '{}.{}'.format(gen_name(6), ext)
		# Rename the file
		shutil.move(fname, new_name)
		# Log the action
		print('{} -> {}'.format(fname, new_name))
