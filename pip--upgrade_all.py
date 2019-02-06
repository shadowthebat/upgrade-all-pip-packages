import os


def upgrade():
    # Creates text file of the result of calling pip list
    os.system(f'pip list > piplist.txt')

    # Read the file
    with open('piplist.txt', 'r+') as f:
        pipl = f.read()

    # convert to list in preparating to isolate packages from original string
    pipl = pipl.split()

    # Strips everything from list until first package
    pipl = pipl[4:]

    # Strips away version numbers, And leaves us with desired list of packages
    pipl = [pipl[x] for x in range(len(pipl)-1) if x % 2 == 0]

    # THE MAGIC: upgrades all packages
    for i in pipl:
        os.system(f'pip install --upgrade {i}')


upgrade()
