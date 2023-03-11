import numpy as np
import matplotlib.pyplot as plt
import math

dt=0.1

M=1
N=2
Q=7
maxx=54
maxy=35

class Pos:
    x=0
    y=0
    def __init__(self,xx,yy):
        self.x=xx
        self.y=yy
    def __neg__(self):
        return Pos(-self.x,-self.y)
    def __add__(self,other):
        return Pos(self.x+other.x,self.y+other.y)
    def __pow__(self,p):
        return self.x**p+self.y**p
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y

pos=[Pos(1,1),Pos(2,2)]

typ=[1,1]

typName=["越野滑雪设施","农作物农场","牧场","再生农场","农业旅游中心"]

aInfo=[
    ["坡度",[
        [7,     7.31925913496,      1.204006794416  ],
        [1.43,  11.82242338696,     1.812524150414  ],
        [0,     13.3434199704295,   2               ],
        [0,     14.82602218506,     2               ],
        [6,     5.164802761524,     1.139830742189  ]]],
    ["植被覆盖率",[
        [0.35,  0.0448725256473],
        [],
        [],
        [],
        [0.3,   0.0383879784927]]],
    ["湿度",[
        [15,    0.058],
        [70,    0.045],
        [60,    0.047],
        [55,    0.1],
        [55,    0.086]]],
    ["降水",[
        [],
        [70,8.22],
        [76.6,9.62],
        [70,9.2],
        [67,2.93]]],
    ["光照",[
        [6.7,0.989],
        [12,2.55],
        [7.3,0.76],
        [6.9,0.83],
        [8,0.295]]],
    ["温度",[
        [-4,2.56],
        [21,5.24],
        [20,3.14],
        [18,5.75],
        [16,4.29]]],
    ["人口",[
        [0.004,1000],
        [],
        [],
        [],
        [0.0023,1500]]]
]

def norm(u,sig,x):
    return math.exp((-(x-u)**2)/(2*(sig**2)))/(math.sqrt(2*math.pi)*sig)

def U(j,i,posk,pos):
    '''
    位于posk的第j种建筑对位于pos的第i个指标的影响程度
    '''
    if(posk==pos):
        return -1
    return -1/((pos+(-posk))**2)

def V(i,j,a):
    '''
    第i个指标为a时对所在地块的第j种建筑的影响程度
    '''
    temp=aInfo[i][1][j]
    if(temp.__len__()==0):
        return 1
    if(temp.__len__()==2):
        return norm(temp[0],temp[1],a)
    if(temp.__len__()==3):
        return norm(temp[0],temp[1],a)*temp[2]

def dif(T,a0,W):

    a=np.zeros([maxx,maxy,M,int(T/dt)])

    a[:,:,:,0]=a0

    A=np.zeros([N,int(T/dt)])

    for t in range(1,int(T/dt)):
        # print("t:",t)
        for k in range(N):
            # print(a[1:maxx+1,1:maxy+1,1,t])
            sum=0
            for i in range(M):
                sum+=V(i,typ[k],a[pos[k].x,pos[k].y,i,t-1])*W[i]
            sum/=M
            A[k,t]=sum
        da=np.zeros([maxx,maxy,M])
        for k in range(N):
            for x in range(maxx):
                for y in range(maxy):
                    for i in range(M):
                        da[x,y,i]+=A[k,t]*U(typ[k],i,pos[k],Pos(x,y))
        # print(da*dt)
        a[:,:,:,t]=a[:,:,:,t-1]+da*dt
        # print(a[:maxx,:maxy,0,t])
        # print(da[:maxx,:maxy,0])
        # print(A[:N,t])
    return A

def S(j,t):
    if t==0:
        return -1
    return 1

def h(flag,t,T):
    if(flag==1):
        return t
    else:
        return T-t

def rate(r,t,T):
    return r*h(1,t,T)+(1-r)*h(2,t,T)

def P(r,T,a0,W):
    A=dif(T,a0,W)
    p=0
    for t in range(0,int(T/dt)):
        dp=0
        for k in range(N):
            if t==0:
                dp+=S(typ[k],t)*rate(r,t,T)
            dp+=A[k,t]*S(typ[k],t)*rate(r,t,T)
        p+=dp*dt
    return p

a0=np.zeros([maxx,maxy,M])

W=np.ones([M])

a0[1,1,0]=1.3

a0[2,2,0]=90

print(P(0.5,10,a0,W))

