f1 = 1
f2 = 1
index = 2
while True:
	tmp = f1 + f2
	f1 = f2
	f2 = tmp
	index = index + 1
	if len(str(f2))==1000:
		print index
		break