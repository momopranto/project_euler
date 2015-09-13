def generate_triangle(n):
	n = n + 1
	num = 0
	for i in range(n):
		num = num + i
	return num

def factors(n):
    return filter(lambda i: n % i == 0, range(1, n + 1))
	
z = 1
while True:
	print str(generate_triangle(z)) + " -> " + str(len(factors(generate_triangle(z))))
	if len(factors(generate_triangle(z))) >= 500:
		break
	z = z + 1