import os

# Creates text file of the result of calling pip list
os.system(f'pip list > piplist.txt')

# Read the file
with open('piplist.txt', 'r+') as f:
    pipl = f.read()

pipl = pipl.split()  # convert to list in preparating to isolate packages from original string
# To find starting index
for i in pipl:
    if i == 'alabaster':
        start = pipl.index(i)

# Strips everything from list until first package
pipl = pipl[start:]

# Strips away version numbers, And leaves us with desired list of packages
piplist = [pipl[x] for x in range(len(pipl)-1) if x % 2 == 0]


def upgrade():
    # THE MAGIC: upgrades all packages
    for i in pipl:
        os.system(f'pip install --upgrade {i}')


upgrade()
