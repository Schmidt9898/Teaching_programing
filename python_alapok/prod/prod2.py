import numpy as np

A=[[1,2,1,2],[1,0,1,1],[1,1,3,2],[-11,-15,-14,-18]]
A=np.asmatrix(A)
U=np.diag([1,1,1])
U=np.append(U,[[0,0,0]],axis=0)
B=["u1","u2","u3","z"]
xb=np.transpose(np.asmatrix([40,38,26,0]))

M=np.append(xb,A,axis=1)
M=np.append(M,U,axis=1)


def has_minus_z(M):
	ret=[]
	for i in range(8):
		if(M[3,i]<0):
			ret.append(i)
	return ret


def find_min_pivot(M,row):
	xb=M[:,0]
	a=M[:,row]

	min=a[0,0] 
	min_i=0
	for i in range(4):
		if min > xb[i,0]/a[i,0]

	print(xb)
	print(a)

def solve_for_pivot(M):
	
	
	return M


pivot=-1
minuses=has_minus_z(M)
while(len(minuses)>0):
	pivot=minuses[0]
	find_min_pivot(M,minuses[0])
	M=solve_for_pivot(M)
	print(pivot)
	minuses=has_minus_z(M)
	break
	

#print(M)
#print(U)
#print(xb)