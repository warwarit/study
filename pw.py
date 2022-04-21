#!/usr/bin/env python3
# Program for on safe password keep

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHfhTxFtjVB6',
             'blog': 'VmAlvQyKAxiVH6G8vOlifMLZF3sdt',
             'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Use: python pw.py [user name] - copy password username')
    sys.exit()

account = sys.argv[1] # firet arg comand line is username

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'Password for {account} copy in bufer.')
else:
    print(f'User name {account} epsent in PASSWORD.')