def cb(x):
	print (x*x*x)

for i in range(20):
	if(i % 2) == 0:
		print i
	else:
		cb(i)
