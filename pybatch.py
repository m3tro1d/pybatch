#!/usr/bin/env python3

from glob import glob
from random import randint
import argparse
import os
import shutil
import sys

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Functions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


def get_new_name(fname, name_length, numeric, use_numbers, use_upper):
    """Returns a name according to the specified settings"""
    if not numeric:
        name = gen_name(name_length, use_numbers, use_upper)
    else:
        name = gen_numeric_name(name_length)
    ext = fname.split(".")[-1]
    new_name = "{}.{}".format(name, ext)
    return new_name


def parse_arguments():
    """Processes the input arguments"""
    parser = argparse.ArgumentParser(
        description="""Renames all files in the directory that match the pattern
        with [pseudo] randomly generated names.""")
    parser.add_argument("--mask", "-m",
                        default="*",
                        help="file mask (default: * e.g. all files)")
    parser.add_argument("--length", "-l",
                        metavar="LEN",
                        type=int, default=6,
                        help="length of generated names (default: 6)")
    parser.add_argument("--numbers", "-n",
                        action="store_true",
                        help="use numbers in generated names")
    parser.add_argument("--upper", "-u",
                        action="store_true",
                        help="use upper-case letters in generated names")
    parser.add_argument("--numeric", "-N",
                        action="store_true",
                        help="use only numbers in generated names")
    parser.add_argument("DIRECTORY",
                        help="files directory")
    return parser.parse_args()


def process_files(filenames, name_length, numeric,
                  use_numbers, use_upper, longest_len):
    """Processes the files in filenames according to the specified settings"""
    # Loop through the files
    for fname in filenames:
        # Process only files, not folders
        if os.path.isfile(fname):
            # Emulate a do-while loop
            while True:
                # Generate a new name...
                new_name = get_new_name(fname, name_length, numeric,
                                        use_numbers, use_upper)
                # ... until it is original
                if not os.path.isfile(new_name):
                    break
            # Rename the file
            shutil.move(fname, new_name)
            # Log the action
            print("{:>{}} -> {}".format(fname, longest_len, new_name))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main script
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    """Entry point of the script"""
    # Parse the input parameters
    args = parse_arguments()
    directory = os.path.abspath(args.DIRECTORY)

    # Check the directory
    if not os.path.isdir(directory):
        print("The specified directory does not exist.")
        sys.exit(1)

    # Change the directory
    os.chdir(directory)
    # Check the files
    filenames = glob(args.mask)
    if not filenames:
        print("No files found for the specified mask.")
        sys.exit(1)

    # Ask user
    print("This will rename the files in the '{}' directory.".format(directory))
    choice = input("Proceed (Y/n)? ")
    if choice not in ("y", "Y", ""):
        print("As you wish.")
        sys.exit(0)

    # Find longest filename's length for proper formatting later
    longest_len = len(max(filenames, key=len))

    # Process the files
    process_files(filenames, args.length, args.numeric,
                  args.numbers, args.upper, longest_len)


# Entry point
if __name__ == "__main__":
    main()
