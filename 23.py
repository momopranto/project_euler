def factors(n):
    return filter(lambda i: n % i == 0, range(1, n + 1))

def isAbundant(n):
	sum = 0
	f = factors(n)
	f.pop()
	for x in f:
		sum = sum + x
	return sum>n
		
def abundantSum(n):
	for x in range(len(abundantNums)):
		for y in range(x,len(abundantNums)):
			if abundantNums[x]+abundantNums[y]==n:
				return True
	return False
	
abundantNums = []	
sum = 0
for i in range(1,28124):
	if isAbundant(i):
		abundantNums.append(i)
print "Abundant numbers generated"
		
for i in range(1,28124):
	if abundantSum(i)==False:
		sum = sum + i
	print str(i/28124) + "%"
		
print sum

