# Multiples of 3 & 5

# First Way:
start = 0
total = 0
while start < 1000:
	if start % 15 == 0:
		total += start
		#print(start,15)
	elif start % 3 == 0:
		total += start
		#print(start,3)
	elif start % 5 == 0:
		total += start
		#print(start,5)
	else:
		pass
	start += 1
print(total)