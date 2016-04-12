import sys

term = -1
number = 100000000
count = 0 #doesn't really matter, right? i can always expect at least number and term
lister = []

for idx, arg in enumerate(sys.argv):
    if idx == 0:
	nothing = 1
    elif idx == 1:
	term = arg
    elif idx == 2:
	number = arg
    else:
	count = open(arg).read().count(term)	
	if int(count) >= int(number):
            lister.append(arg) 
                 
for item in lister:
    print item
