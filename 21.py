def d(n):
	divisors = []
	for i in range(1,n):
		if n%i==0:
			divisors.append(i)
	return sum(divisors)

amicables = []
for i in range(1,10000):
	b = d(i)
	if d(i)==b and d(b)==i and i!=b:
		if not(i in amicables) and not(b in amicables):
			amicables.append(i)
			amicables.append(b)

print sum(amicables)