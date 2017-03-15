fossasia-badge-generator
========================

This script generates the badges for the FOSSASIA conference.

Specification
-------------

### Input

- The input is a set of csv files in the same folder, UTF-8.
- The csv file is named after the badge type to take. 
  Example: `vip.png.csv` uses the picture `vip.png`.
- The csv has the following three columns
  1. First Nmae
  2. Second Name
    - If there is no last name, the first name is split at the last space
      if the name has more than 12 letters
  3. Twitterhandle

### Output

The output file is svg / pdf / multipage pdf of size A3.
Each badge has the size A6.
The outputs are in a folder derived form the input csv.

### Usage

Run the Python file with Python 3.
It turns all input files to the output files.

