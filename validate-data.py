import sys

name = sys.argv[1]
mobile = sys.argv[2]

if len(name) <= 20 and len(mobile) <= 10:
    print("PASS")
else:
    print("FAIL")
