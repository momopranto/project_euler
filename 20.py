f = 1
sum = 0
for i in range(100,0,-1):
	f = f * i
	
for x in str(f):
	sum = sum + int(x)
	
print sum