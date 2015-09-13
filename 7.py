from gmpy2 import *

n = 1

for i in range(10001):
	n = next_prime(n)
	if i==10001:
		print n