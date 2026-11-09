import sys

name = sys.argv[1]
mobile = sys.argv[2]

if len(name) <= 15 and len(mobile) <= 10:
    print("PASS")
else:
    print("FAIL")
