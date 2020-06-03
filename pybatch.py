import os
import sys
import argparse
import shutil
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
	help='Files directory. The default is current directory.')

parser.add_argument('-m', '--mask', default='*',
	help='File mask. The default is * (all files).')

args = parser.parse_args()
directory = os.path.abspath(args.dir)
file_mask = args.mask


# Ask user
print('This will rename the files in the \'{}\' directory.'.format(directory))
choice = input('Proceed (Y/n)? ')
if not (choice == 'y' or choice == 'Y' or choice == ''):
	print('As you wish.')
	sys.exit(0)


# Change the directory
os.chdir(directory)
# Loop through the files
for f in glob(file_mask):
	print(f)
