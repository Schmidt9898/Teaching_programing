
import random
import Lenyomat
print("Generating random database")

numberofentry=100000
passpoolid=0
passpool=["10-million-password-list-top-100.txt","10-million-password-list-top-100000.txt"]

noinevek=[]
ferfinevek=[]
passwords=[]

try:
	with open(passpool[passpoolid],encoding="utf8") as file:
		passwords = file.readlines()
		passwords = [line.rstrip() for line in passwords]
	with open("osszesffi.txt",encoding="utf8") as file:
		ferfinevek = file.readlines()
		ferfinevek = [line.rstrip() for line in ferfinevek]
	with open("osszesnoi.txt",encoding="utf8") as file:
		noinevek = file.readlines()
		noinevek = [line.rstrip() for line in noinevek]
except Exception as e:
    print("There was an error : ",e)
    quit()

noinevek.pop(0)#remove title
ferfinevek.pop(0)

#print(ferfinevek[0])

id = 0

class Account:
	def __init__(self):
		global id
		self.id=id
		id+=1
		self.nem=random.choice(["ferfi","no"])
		self.firstname=random.choice(ferfinevek) if self.nem=="ferfi" else random.choice(noinevek)
		self.lastname=random.choice(ferfinevek) if self.nem=="ferfi" else random.choice(noinevek)
		self.friends=[]
		self.money=random.randint(100,1000000)
		self.password=Lenyomat.lenyomat(random.choice(passwords))
	


	def __str__(self):
		return self.id.__str__()+" "+self.firstname+" "+self.lastname+" "+self.nem+" "+self.money.__str__()+" "+self.friends.__str__()
	def todata(self):
		return self.id.__str__()+","+self.firstname+" "+self.lastname+","+self.nem+","+self.money.__str__()+","+self.password+","+self.friends.__str__()+"\n"

	def make_friends(A,B):
		if A.id==B.id:
			return 
		A.friends.append(B.id)
		B.friends.append(A.id)


people = [Account() for i in range(numberofentry)]
#print([p.__str__() for p in people])

for i in range(int(numberofentry*0.75)):
	Account.make_friends(random.choice(people),random.choice(people))




f = open("database.txt", "w")
f.writelines([p.todata() for p in people])
f.close()
