import numpy as np
import matplotlib.pyplot as plt

dt=0.0001#

M=1
N=2
Q=1
T=1
maxx=54
maxy=35

pos=[[1,1],[2,2]]#

typ=[1,1] #

def e(xx,yy,typ,A,x,y):
    
    if(xx==x and yy==y):
        return -A
    return -A/((x-xx)**2+(y-yy)**2)

def get(typ,i,aa):
    return aa
    # return i*typ/aa

def dif(a0):

    a=np.zeros([maxx,maxy,M,int(T/dt)])

    a[:maxx,:maxy,:M,0]=a0

    A=np.zeros([N,int(T/dt)])

    '''
    (T/dt)*numx*numy*N*M=20*1000*1000*5*10=10^9
    '''
    for t in range(1,int(T/dt)):
        # print("t:",t)
        for k in range(0,N):
            # print(a[1:maxx+1,1:maxy+1,1,t])
            sum=0.0
            for ii in range(0,M):
                sum=sum+get(typ[k],ii,a[pos[k][0],pos[k][1],ii,t-1])
            sum/=M
            A[k,t]=sum
        da=np.zeros([maxx,maxy,M])
        for k in range(0,N):
            for x in range(0,maxx):
                for y in range(0,maxy):
                    for i in range(0,M):
                        da[x,y,i]+=A[k,t]*e(pos[k][0],pos[k][1],typ[k],A[k,t],x,y)
        a[:,:,:,t]=a[:,:,:,t-1]+da*dt
        # print(a[:maxx,:maxy,0,t])
        # print(da[:maxx,:maxy,0])
        # print(A[:N,t])
    
    return A

def S(typ,t):
    return 1

def h(flag,t):
    if(flag==1):
        return t
    else:
        return T-t

def rate(r,t):
    return r*h(1,t)+(1-r)*h(2,t)

def P(r,a0):
    A=dif(a0)
    p=0
    for t in range(1,int(T/dt)):
        dp=0
        for k in range(N):
            dp+=A[k,t]*S(typ[k],t)*rate(r,t)
        p+=dp*dt

a0=np.zeros([maxx,maxy,M])

a0[1,1,0]=10

a0[2,2,0]=5

print(dif(a0)[0:2])