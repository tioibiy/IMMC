import numpy as np
import matplotlib.pyplot as plt

dt=1

M=3
N=1
Q=1
T=10
maxx=100
maxy=100

pos=[[0,0],[2,1]]

typ=[0,1]

def e(xx,yy,typ,A,x,y):
    if(xx==x or yy==y):
        return A*typ
    return A*typ/((x-xx)**2+(y-yy)**2)

def get(typ,i,aa):
    return i*typ/aa

a=np.ones([maxx,maxy,15,25])

A=np.zeros([105,25])

'''
(T/dt)*numx*numy*N*M=20*1000*1000*5*10=10^9
'''
for t in range(0,int(T/dt)):
    for k in range(1,N+1):
        sum=0.0
        for ii in range(1,M+1):
            sum=sum+get(typ[k],ii,a[pos[k][0],pos[k][1],ii,t])
        sum/=M
        A[k,t]=sum
    da=np.zeros([maxx,maxy,15,25])
    for k in range(1,N+1):
        for x in range(0,maxx):
            for y in range(0,maxy):
                for i in range(1,M+1):
                    da[x,y,i,t]=A[k,t]*e(pos[k][0],pos[k][1],typ[k],A[k,t],x,y)
    a=a+da