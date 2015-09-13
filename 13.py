list = None
with open("list.txt","r") as f:
	list = f.readlines()

for i in range(len(list)):
	list[i] = int(list[i][:-1])

sum = 0
for x in list:
	sum = sum + x
	print sum
print sum