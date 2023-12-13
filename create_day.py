# takes in day number as command line argument
# makes a new folder called dayx if dayx doesn't exist else prints an error
# in the folder creates empty solution1.py, solution2.py, input.txt, and test_case.txt files
# all empty

import os
import sys

if len(sys.argv) != 2:
    print("Usage: python3 create_day.py <day_number>")
    exit()

day = sys.argv[1]
path = "day" + day

if os.path.exists(path):
    print("Error: Folder already exists")
    exit()

os.mkdir(path)

# make files
open(path + "/solution1.py", "w")
open(path + "/solution2.py", "w")
open(path + "/input.txt", "w")
open(path + "/test_case.txt", "w")

print("Created folder day" + day)