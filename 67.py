l = []	
with open("triangle.txt","r") as f:
	l = [map(int, x.split()) for x in f.readlines()]
	
while len(l)>1:
	a0 = l.pop()
	a1 = l.pop()
	tmp = []
	for i,t in enumerate(a1):
		tmp.append(max(a0[i],a0[i+1]) + t)
	l.append(tmp)
	
print l[0][0]