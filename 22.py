import string

list = None
with open('names.txt','r') as f:
	list = sorted(f.readlines()[0].split(','))
	
totalscore = 0
alpha = string.ascii_uppercase

for x,y in enumerate(list):
	sum = 0
	for i in y:
		sum = sum + alpha.find(i) + 1
	totalscore = totalscore + sum*(x+1)
	
print totalscore