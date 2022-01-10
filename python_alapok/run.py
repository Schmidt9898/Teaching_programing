
print("trying passwords")

from Lenyomat import *

#password = "1234"
passhash=lenyomat("99999")


charlist="qwertzuiopasdfghjklxcvbnmy0123456789"

n=5
print(pow(len(charlist),n))
print("Ez legfeljebb ",pow(len(charlist),n)/711366," masodpercig fog tartani.")
password=""
isfound=False
#codemaxlenght=4




def gen(str_,n):
	global isfound
	if isfound:
		return
	if n == 0:
		newphash=lenyomat(str_)
		#print(str_)
		if newphash == passhash:
			print("Megvan a jelszo a : ",str_)
			isfound=True
		return
	for i in range(len(charlist)):
		gen(str_+charlist[i],n-1)

gen("",n)





#for i in range(len(charlist)):
#	for j in range(len(charlist)):
#		for k in range(len(charlist)):
#			for l in range(len(charlist)):
#				newp=charlist[i]+charlist[j]+charlist[k]+charlist[l]
#				newphash=lenyomat(newp)
#				#print(newp)
#				if newphash == passhash:
#					print("Megvan a jelszo a : ",newp)
#					found=True
#					break
#			if isfound:
#				break
#		if isfound:
#			break
#	if isfound:
#		break




	




