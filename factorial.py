#Find the factorial of given function using recursive function?

def factorial(k):
	fact=1
	if(k==0):
		print(" 1 is the factorial of ",k)
	else:
		i=1
		while(i<=k):
			fact=fact*i
			i=i+1
	return fact
	
n=int(input("enter the number:"))
print(factorial(n))
