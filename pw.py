#! python3
# pw.py - A password locker program created
# by guidlines of Automate the Boring Stuff with Python

import sys


PASSWORDS = {'email': '13dEnricocj*'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line argument is the account name
