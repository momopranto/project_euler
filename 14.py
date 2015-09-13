def collatz_sequence(x):
    seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1 
       seq.append(x)    # Added line
    return seq

highestX = -1
highestLen = -1
for i in range(1000000):
	print str(i/10000) + "%"
	if len(collatz_sequence(i)) > highestLen:
		highestLen = len(collatz_sequence(i))
		highestX = i

print highestX