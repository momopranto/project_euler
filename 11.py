mat = None
with open("mat.txt","r") as f:
	mat = f.readlines()
for x in range(len(mat)):
	mat[x] = mat[x][:-1]	
mx = []
for x in range(len(mat)):
	mx.append(mat[x].split(" "))
for x in range(len(mx)):
	for y in range(len(mx[x])):
		mx[x][y] = int(mx[x][y])

maxprod = 0

#horizontal
for i in range(len(mx)):
	for x in range(len(mx[i])-3):
		#print str(mx[i][x]) + " " +  str(mx[i][x+1]) + " " + str(mx[i][x+2]) + " " + str(mx[i][x+3]) + "\n"
		prod = mx[i][x] * mx[i][x+1] * mx[i][x+2] * mx[i][x+3]
		if prod > maxprod:
			maxprod = prod

#vertical
for i in range(len(mx[0])):
	for x in range(len(mx)-3):
		#print str(mx[x][i]) + " " +  str(mx[x+1][i]) + " " + str(mx[x+2][i]) + " " + str(mx[x+3][i]) + "\n"
		prod = mx[x][i] * mx[x+1][i] * mx[x+2][i] * mx[x+3][i]
		if prod > maxprod:
			maxprod = prod
		
#diagonal sw to ne	
#top	
for k in range(3,len(mx)):
	for j in range(k-2):
		i = k - j
		#print str(mx[i][j]) + "->"
		prod = mx[i][j] * mx[i-1][j+1] * mx[i-2][j+2] * mx[i-3][j+3]
		if prod > maxprod:
			maxprod = prod
		#print str(mx[i][j]) + " " + str(mx[i-1][j+1]) + " " + str(mx[i-2][j+2]) + " " + str(mx[i-3][j+3]) + "\n"

#bottom
for k in range(len(mx)-2,0,-1):
	for j in range(k-2):
		i = k - j
		#print str(mx[len(mx)-j-1][len(mx)-i-1]) + "->"
		prod = mx[i][j] * mx[i-1][j+1] * mx[i-2][j+2] * mx[i-3][j+3]
		if prod > maxprod:
			maxprod = prod
		#print str(mx[i][j]) + " " + str(mx[i-1][j+1]) + " " + str(mx[i-2][j+2]) + " " + str(mx[i-3][j+3]) + "\n"
		
#diagonal nw to se
#bottom	
for k in range(len(mx)-3):
	for j in range(len(mx)-(k+3)):
		i = k + j
		#print str(mx[i][j]) + "->"
		prod = mx[i][j] * mx[i+1][j+1] * mx[i+2][j+2] * mx[i+3][j+3]
		if prod > maxprod:
			maxprod = prod
		#print str(mx[i][j]) + " " + str(mx[i+1][j+1]) + " " + str(mx[i+2][j+2]) + " " + str(mx[i+3][j+3]) + "\n"

#top
for k in range(len(mx)-3):
	for j in range(len(mx)-(k+3)):
		i = k + j
		#print str(mx[j][i]) + "->"
		prod = mx[j][i] * mx[j+1][i+1] * mx[j+2][i+2] * mx[j+3][i+3]
		if prod > maxprod:
			maxprod = prod
		#print str(mx[j][i]) + " " + str(mx[j+1][i+1]) + " " + str(mx[j+2][i+2]) + " " + str(mx[j+3][i+3]) + "\n"

print maxprod