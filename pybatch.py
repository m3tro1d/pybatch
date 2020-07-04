import argparse
import os
import shutil
import sys
from glob import glob
from random import randint


def gen_name(length, numbers=False, uppercase=False):
	"""Returns a [pseudo] randomly generated name"""
	name = ""
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
	description="""Renames all files in the directory that match the pattern with
[pseudo] randomly generated names.""")

parser.add_argument("--mask", "-m", default="*",
	help="file mask (default: * e.g. all files)")

parser.add_argument("--length", "-l", type=int, default=6,
	help="length of generated names (default: 6)")

parser.add_argument("DIRECTORY",
	help="files directory")

args = parser.parse_args()
directory = os.path.abspath(args.DIRECTORY)
file_mask = args.mask
name_length = args.length


# Check the directory
if not os.path.isdir(directory):
	print("The specified directory does not exist.")
	sys.exit(1)

# Change the directory
os.chdir(directory)
# Check the files
if not glob(file_mask):
	print("No files found for the specified mask.")
	sys.exit(1)


# Ask user
print("This will rename the files in the '{}' directory.".format(directory))
choice = input("Proceed (Y/n)? ")
if not (choice == "y" or choice == "Y" or choice == ""):
	print("As you wish.")
	sys.exit(0)


# Loop through the files
for fname in glob(file_mask):
	# Process only files, not folders
	if os.path.isfile(fname):
		# Generate a new name
		ext = fname.split(".")[-1]
		new_name = "{}.{}".format(gen_name(name_length), ext)

		# Rename the file
		shutil.move(fname, new_name)

		# Log the action
		print("{} -> {}".format(fname, new_name))
