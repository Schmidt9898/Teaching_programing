print("3n+1 problem")


n=int(input("Adj egy számot."))
count=0
while(True):
	count+=1
	if n%2==0 : #even
		n/=2
	else:
		n=n*3+1
	print(n)
	if n == 1 or count>10000000:
		break

print("done count ",count)

