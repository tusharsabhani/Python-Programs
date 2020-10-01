number=int(input("Enter a Number-"))
sum=0
temporary=number
while number>0:
	remainder=number%10
	sum=sum+(remainder**3)
	number=number//10
if temporary==sum:
	print(temporary,'is an armstrong.')
else:
	print(temporary,'is not an armstrong.')