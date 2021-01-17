#!/usr/bin/env python3

from glob import glob
from random import randint
from textwrap import dedent
import argparse
import os
import shutil
import sys

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Classes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class CustomArgumentParser(argparse.ArgumentParser):
    """Override ArgumentParser's help message"""
    def format_help(self):
        help_text = dedent(f"""\
        Pybatch is a script for renaming all the files that match the pattern
        with [pseudo] randomly generated names.

        Usage: {self.prog} [OPTIONS] DIR

        DIR:
          Directory of the files to be renamed

        Options:
          -h,  --help      show help
          -m,  --mask      file mask (def: {self.get_default("mask")})
          -l,  --length    length of generated names (def: {self.get_default("length")})
          -n,  --numbers   use numbers (def: {self.get_default("numbers")})
          -u,  --upper     use upper-case letters (def: {self.get_default("upper")})
          -N,  --numeric   use only numbers (def: {self.get_default("numeric")})

        For more information visit:
        https://github.com/m3tro1d/pybatch
        """)
        return help_text

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Functions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def valid_dir(string):
    """Checks if the string is a valid directory"""
    path = os.path.abspath(string)
    if not os.path.exists(path):
        error = f"Directory does not exists: {path}"
        raise argparse.ArgumentTypeError(error)
    if not os.path.isdir(path):
        error = f"Not a directory: {path}"
        raise argparse.ArgumentTypeError(error)
    return path


def positive_int(string):
    """Cheks if the string is a valid and positive integer"""
    try:
        value = int(string)
        if value <= 0:
            raise ValueError
    except ValueError:
        error = f"Invalid value: {string}"
        raise argparse.ArgumentTypeError(error)
    return value


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
    new_name = f"{name}.{ext}"
    return new_name


def parse_arguments():
    """Processes the input arguments"""
    parser = CustomArgumentParser(usage="%(prog)s [OPTIONS] DIR")

    parser.add_argument("-m", "--mask", default="*")

    parser.add_argument("-l", "--length", default=6, type=positive_int)

    parser.add_argument("-n", "--numbers", action="store_true")

    parser.add_argument("-u", "--upper", action="store_true")

    parser.add_argument("-N", "--numeric", action="store_true")

    parser.add_argument("directory", type=valid_dir)

    args = parser.parse_args()
    return args


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
            print(f"{fname : >{longest_len}} -> {new_name}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main script
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    """Entry point of the script"""
    # Parse the input parameters
    args = parse_arguments()
    directory = args.directory

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
    print(f"This will rename the files in the '{directory}' directory.")
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
    try:
        main()
    except KeyboardInterrupt:
        print("User interrupt", file=sys.stderr)
        sys.exit(1)
