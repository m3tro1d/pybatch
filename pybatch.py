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


def gen_numeric_name(length):
    """Returns a [pseudo] randomly generated name of numbers"""
    name = ""
    for _ in range(length):
        name += str(randint(0, 9))
    return name


def get_new_name(name_length, numeric, use_numbers, use_upper):
    # Returns a name according to the specified settings
    if not numeric:
        name = gen_name(name_length, use_numbers, use_upper)
    else:
        name = gen_numeric_name(name_length)
    ext = fname.split(".")[-1]
    new_name = "{}.{}".format(name, ext)
    return new_name


# Parse the input parameters
parser = argparse.ArgumentParser(
    description="""Renames all files in the directory that match the pattern
    with [pseudo] randomly generated names.""")

parser.add_argument("--mask", "-m", default="*",
                    help="file mask (default: * e.g. all files)")

parser.add_argument("--length", "-l", type=int, default=6, metavar="LEN",
                    help="length of generated names (default: 6)")

parser.add_argument("--numbers", "-n", action="store_true",
                    help="use numbers in generated names")

parser.add_argument("--upper", "-u", action="store_true",
                    help="use upper-case letters in generated names")

parser.add_argument("--numeric", "-N", action="store_true",
                    help="use only numbers in generated names")

parser.add_argument("DIRECTORY",
    help="files directory")

args = parser.parse_args()
directory = os.path.abspath(args.DIRECTORY)
file_mask = args.mask
name_length = args.length
use_numbers = args.numbers
use_upper = args.upper
numeric = args.numeric


# Check the directory
if not os.path.isdir(directory):
    print("The specified directory does not exist.")
    sys.exit(1)

# Change the directory
os.chdir(directory)
# Check the files
filenames = glob(file_mask)
if not filenames:
    print("No files found for the specified mask.")
    sys.exit(1)


# Ask user
print("This will rename the files in the '{}' directory.".format(directory))
choice = input("Proceed (Y/n)? ")
if choice not in ("y", "Y", ""):
    print("As you wish.")
    sys.exit(0)


# Find longest filename's length for later formatting
longest_len = len(max(filenames, key=len))


# Loop through the files
for fname in filenames:
    # Process only files, not folders
    if os.path.isfile(fname):
        # Emulate a do-while loop
        while True:
            # Generate a new name...
            new_name = get_new_name(name_length, numeric, use_numbers, use_upper)
            # ... until it is original
            if not os.path.isfile(new_name):
                break
        # Rename the file
        shutil.move(fname, new_name)
        # Log the action
        print("{:>{}} -> {}".format(fname, longest_len, new_name))
