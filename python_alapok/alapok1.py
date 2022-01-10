print("Hello vilag")
#Python 0
#ez a sor a komment

#értékadás
a=10
print("Value of A is "+str(a))

a , b = 1,2
c=(3,4)
a,b=c
c_first=c[0]

print("A=={:} and B=={:} ".format(a,b))
print("C=={:} ".format(c_first))


a="string value"
print("A=="+str(a))

a=1
a=a+1
a+=2
print("A=="+str(a))

a=11
a=a/7
print("A=="+str(a))

a=int(a)
print("A=="+str(a))

#a=input("Add meg az a értékét!\n")
#print("A=="+str(a))


#+-*/%!


#elágazások 
condition=True
if condition :
	print("condition was true")
else:
	print("condition was false")

a=5
if a%2==0:
	print("páros")
else:
	print("páratlan")
    
a=0

if a>0:
    pass
elif a<0:
    pass
else:
    pass

#feltételes értékadás
a=5 if condition else 4


#tömbök

tomb = [1,2,3,4,5]

print("tomb első eleme == "+str(tomb[0]))
print("tomb utolsó eleme == "+str(tomb[-1]))
tomb.append(6)
print("tomb utolsó eleme == "+str(tomb[len(tomb)-1]))
tomb.pop()
print("tomb utolsó eleme == "+str(tomb[-1]))
tomb.pop(0)
print("tomb első eleme == "+str(tomb[0]))
print(tomb)
tomb.remove(3)
print("A tomb ",tomb," és mérete ",len(tomb))



# ciklusok
for i in range(10):
    print("Ez a ",i,". ciklus!")

for i in range(len(tomb)):
    print("Ez a tomb ",i,". eleme = ",tomb[i])


while True:
    break

#lopvakusz
for i in range(5):
    print("----Most látsz---")
    continue
    print("----Most nem látsz----")





    





    


