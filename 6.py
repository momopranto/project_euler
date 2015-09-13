sqsums = 0
sumsq = 0

for i in range(1,101):
	sqsums = sqsums + i**2
	sumsq = sumsq + i

sumsq = sumsq**2
print abs(sumsq-sqsums)