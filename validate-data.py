import sys
name = input("What is your name: ")
number = input("What is your number: ")
if len(name) <= 15 and len(number) <= 10:
	print("Pass")
else:
	print("Fail")
