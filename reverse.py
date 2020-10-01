Number=int(input("Enter a Number-"))
reverse=0
while Number>0:
	remainder=Number%10
	reverse=(reverse*10)+remainder
	Number=Number//10
print("Reverse=",reverse)