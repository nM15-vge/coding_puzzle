import sys

filename = sys.argv[1]

with open(filename) as f:
    content = f.readlines()

print(content)

