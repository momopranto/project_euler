z = 0

for n in range(100,999):
	for i in range(100,999):
		x = n*i
		if str(x)[::-1]==str(x):
			if (x > z):
				z = x

print z