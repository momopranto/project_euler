one = "one"
two = "two"
three = "three"
four = "four"
five = "five"
six = "six"
seven = "seven"
eight = "eight"
nine = "nine"
ten = "ten"
eleven = "eleven"
twelve = "twelve"
thirteen = "thirteen"
fourteen = "fourteen"
fifteen = "fifteen"
sixteen = "sixteen"
seventeen = "seventeen"
eighteen = "eighteen"
nineteen = "nineteen"
twenty = "twenty"
thirty = "thirty"
forty = "forty"
fifty = "fifty"
sixty = "sixty"
seventy = "seventy"
eighty = "eighty"
ninety = "ninety"
hundred = "hundred"
thousand = "thousand"

sum = 0

for n in range(1,1001):
	x = ""
	if n==1000:
		x = x + one + thousand
	if n < 1000:
		if (n/100)%10==1:
			x = x + one + hundred
		if (n/100)%10==2:
			x = x + two + hundred
		if (n/100)%10==3:
			x = x + three + hundred
		if (n/100)%10==4:
			x = x + four + hundred
		if (n/100)%10==5:
			x = x + five + hundred
		if (n/100)%10==6:
			x = x + six + hundred
		if (n/100)%10==7:
			x = x + seven + hundred
		if (n/100)%10==8:
			x = x + eight + hundred
		if (n/100)%10==9:
			x = x + nine + hundred
		if ((n/10)%10!=0 or n%100!=0) and n>100:
			x = x + "and"
		if (n/10)%10==1:
			if n%100==10:
				x = x + ten
			if n%100==11:
				x = x + eleven
			if n%100==12:
				x = x + twelve
			if n%100==13:
				x = x + thirteen
			if n%100==14:
				x = x + fourteen
			if n%100==15:
				x = x + fifteen
			if n%100==16:
				x = x + sixteen
			if n%100==17:
				x = x + seventeen
			if n%100==18:
				x = x + eighteen
			if n%100==19:
				x = x + nineteen
		else:
			if (n/10)%10==2:
				x = x + twenty
			if (n/10)%10==3:
				x = x + thirty
			if (n/10)%10==4:
				x = x + forty
			if (n/10)%10==5:
				x = x + fifty
			if (n/10)%10==6:
				x = x + sixty
			if (n/10)%10==7:
				x = x + seventy
			if (n/10)%10==8:
				x = x + eighty
			if (n/10)%10==9:
				x = x + ninety
			if n%10==1:
				x = x + one
			if n%10==2:
				x = x + two
			if n%10==3:
				x = x + three
			if n%10==4:
				x = x + four
			if n%10==5:
				x = x + five
			if n%10==6:
				x = x + six
			if n%10==7:
				x = x + seven
			if n%10==8:
				x = x + eight
			if n%10==9:
				x = x + nine
	print str(n) + ": " + x + " -> " + str(len(x))
	sum = sum + len(x)

print sum