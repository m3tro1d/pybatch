# Pybatch
This is just a simple script to rename all files with the randomly generated names.

## Usage
```
Usage: pybatch.py [OPTIONS] DIR

DIR:
  Directory of the files to be renamed

Options:
  -h,  --help      show help
  -m,  --mask      file mask (def: *)
  -l,  --length    length of generated names (def: 6)
  -n,  --numbers   use numbers (def: False)
  -u,  --upper     use upper-case letters (def: False)
  -N,  --numeric   use only numbers (def: False)
```

**Note**: always double-check the directory that you are working with. Renaming cannot be undone.
