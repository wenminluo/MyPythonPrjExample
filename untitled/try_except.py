# Filename eg:try_except.py

import sys

try:
    s = input("Enter something-->");
except E0FError:
    print("\nWhy did you do an EOF on me?");
    sys.exit();  # exit the program
except:
    # here,we are not exiting the program
    print("\nSome error exception occurred.");
print("Done");
