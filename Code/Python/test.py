import numpy as np
import matplotlib.pyplot as plt

dt=0.001#

M=1
N=2
Q=7
T=1
maxx=54
maxy=35

class Pos:
    x,y
    def __init__(self,xx,yy):
        self.x=xx
        self.y=yy
pos=[Pos(1,1),Pos(2,2)]#

typ=[1,1] #

typName=["滑雪","农作物农场","牧场","再生农场","太阳能电池阵列","农业光伏农场","农业旅游中心"]

aName=["坡度","植被覆盖率","湿度","降水","光照","温度","交通","污染","污染对产业的影响","人口","就业"]

def norm(sig,u,x):
    return math.exp((-(x-u)**2)/(2*(sig**2)))/(math.sqrt(2*math.pi)*sig)

def U(j,i,posk,pos):
    '''
    位于posk的第j种建筑对位于pos的第i个指标的影响程度
    '''
    if(xx==x and yy==y):
        return -A
    return -A/((x-xx)**2+(y-yy)**2)

def V(i,j,a):
    '''
    第i个指标为a时对所在地块的第j种建筑的影响程度
    '''
    return a

def dif(a0,w):

    a=np.zeros([maxx,maxy,M,int(T/dt)])

    a[:,:,:,0]=a0

    A=np.zeros([N,int(T/dt)])

    for t in range(1,int(T/dt)):
        # print("t:",t)
        for k in range(N):
            # print(a[1:maxx+1,1:maxy+1,1,t])
            sum=0
            for i in range(M):
                sum+=V(ii,typ[k],a[pos[k].x,pos[k].y,i,t-1])*w[i]
            sum/=M
            A[k,t]=sum
        da=np.zeros([maxx,maxy,M])
        for k in range(N):
            for x in range(maxx):
                for y in range(maxy):
                    for i in range(M):
                        da[x,y,i]+=A[k,t]*U(typ[k],i,pos[k],pos(x,y))
        a[:,:,:,t]=a[:,:,:,t-1]+da*dt
        # print(a[:maxx,:maxy,0,t])
        # print(da[:maxx,:maxy,0])
        # print(A[:N,t])
    return A

def S(typ,t):
    if t==0:
        return 
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
    for t in range(0,int(T/dt)):
        dp=0
        for k in range(N):
            if t==0:
                dp+=S(typ[k],t)*rate(r,t)
            dp+=A[k,t]*S(typ[k],t)*rate(r,t)
        p+=dp*dt

a0=np.zeros([maxx,maxy,M])

a0[1,1,0]=10

a0[2,2,0]=5

print(dif(a0)[0:2])

