from matplotlib import pyplot as plt
import math

print("asd")

def norm(x,y):
	return max(abs(x*2-y),abs(1*x))



for x in range(-10,10):
	for y in range(-10,10):
		if norm(x/2,y/2)<=1:
			plt.scatter(x/2,y/2,100)
			print(x/5,y/5)





plt.show()