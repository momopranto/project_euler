from gmpy2 import *

sum = 0
n = 1
while True:
	n = next_prime(n)
	if n < 2000000:
		sum = sum + n
	else:
		break

print sum