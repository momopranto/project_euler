terms = []

for a in range(2,101):
	for b in range(2,101):
		x = a**b
		if x not in terms:
			terms.append(x)
			
print len(terms)