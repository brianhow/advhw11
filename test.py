import os
tests = []
os.system("ls test*.cpp > output.txt")
with open('output.txt') as f:
	for line in f:
		tests.append(line)	
