def fakt(n):
    return 1 if n<=1 else n*fakt(n-1)
n =int(input("Szam: "))
print (n," ! = ",fakt(n),"\n","-"*20) 