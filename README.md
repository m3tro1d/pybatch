# Pybatch
This is just a simple script to rename all files with the randomly generated names. *Also first time I practiced the `argparse` module*.

## Usage
```
usage: pybatch.py [-h] [--mask MASK] [--length LEN] [--numbers] [--upper] DIRECTORY

positional arguments:
  DIRECTORY             files directory

optional arguments:
  -h, --help            show this help message and exit
  --mask MASK, -m MASK  file mask (default: * e.g. all files)
  --length LEN, -l LEN  length of generated names (default: 6)
  --numbers, -n         use numbers in generated names (default: False)
  --upper, -u           use upper-case letters in generated names (default: False)
```
**Note**: always double-check the directory that you are working with. Renaming cannot be undone.
