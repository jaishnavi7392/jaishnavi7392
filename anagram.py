#Find whether a string is anagram of given string?

str1=input("Enter the string:")
str2=input("Enter the string:")

k1=' '.join(sorted(str1))
k2=' '.join(sorted(str2))
if(k1==k2):
	print(str2,"is a anagram of given string",str1)
else:
	print(str2,"is not a anagram of given string",str1)
