import numpy as np
import matplotlib.pyplot as plt
import math
import numba
from numba import jit
import xlwt
import xlrd
#xlwt,xlrd是python将数据导入excel表格使用的库
@jit(nopython=True)
def norm(u,sig,x):
    return math.exp((-(x-u)**2)/(2*(sig**2)))/(math.sqrt(2*math.pi)*sig)

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

dt=1

M=8
Q=7
maxx=54
maxy=37

pos=[]#[Pos(50,10),Pos(10,30),Pos(20,10),Pos(50,20),Pos(10,10)]

typ=[]#[2,3,1,0,4]


typName=[["越野滑雪设施"],["农作物农场"],["牧场"],["再生农场"],["农业旅游中心"]]

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
        [],
        [],
        [],
        [],
        []]],
    ["污染",[
        [-0.2],
        [-0.5],
        [-0.2],
        [-0.15],
        [-2.5]]]
        ]

cx=61.00
cy=34.60
def dis(pos1,pos2):
    d=pos1+(-pos2)
    return math.sqrt((d.x*cx)**2+(d.y*cy)**2)

def U(j,i,posk,pos):
    '''
    位于posk的第j种建筑对位于pos的第i个指标的影响程度
    '''
    if(i==0 or i==2 or i==3 or i==4 or i==5):
        return 0
    if(i==6):
        if(j==0):
            return 0.004*365
        if(j==4):
            return 0.0023*365
        return 0
    if(i==7):
        d=dis(posk,pos)
        if(((j==0 or (j==4)) and d<=1000)or((j==1 or j==2) and d<=750)):
            return 1
        return 0
    return 0

def V(i,j,a):
    '''
    第i个指标为a时对所在地块的第j种建筑的影响程度
    '''
    temp=aInfo[i][1][j]
    if(i<=6):
        if(temp.__len__()==0):
            return 1
        if(temp.__len__()==2):
            return norm(temp[0],temp[1],a)
        if(temp.__len__()==3):
            return norm(temp[0],temp[1],a)*temp[2]
    elif(i<=7):
        return temp[0]*(a!=0)

def dif(T,a0,W):

    a=np.zeros([maxx,maxy,M,int(T/dt)])

    a[:,:,:,0]=a0

    A=np.zeros([N,int(T/dt)])
    '''
    T*N*maxx*maxy*M=20*400*60*40*8
    '''
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
            # for x in range(maxx):
            #     for y in range(maxy):
            for kk in range(N):
                x=pos[kk].x
                y=pos[kk].y
                for i in range(M):
                    if(i==7 and U(typ[k],i,pos[k],Pos(x,y))):
                        da[x,y,i]=1
                    elif(i==1):
                        if(a[x,y,i,t-1]):
                            da[x,y,i]=-0.125
                    else:
                        da[x,y,i]+=A[k,t]*U(typ[k],i,pos[k],Pos(x,y))
        # print(da*dt)
        a[:,:,:,t]=a[:,:,:,t-1]+da*dt
        # print(a[:maxx,:maxy,0,t])
        # print(da[:maxx,:maxy,0])
        # print(A[:N,t])
    return A

s=[13.59-3.22,2.59-0.11,0.675-0.41,1.97-0.06,64.26,3.71]

c=[32.16,0.18,0.075,3.71,185.35]

def S(j,t):
    if t==0:
        return -c[j]
    return s[j]

@jit(nopython=True)
def h(flag,t,T):
    if(flag==1):
        return 1/(math.exp(t-1)+1)
    else:
        return 1-1/(math.exp(t-1)+1)

@jit(nopython=True)
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

with open("C:/Users/linru/Desktop/IMMC/Code/Python/out","rb") as f:
    s = f.read()
    l=s.splitlines()
    for i in range(l.__len__()):
        ii=l[i].split()
        for j in range(ii.__len__()):
            a0[j,i,0]=float(ii[j])

with open("C:/Users/linru/Desktop/IMMC/Code/Python/tree","rb") as f:
    s = f.read()
    l=s.splitlines()
    for i in range(l.__len__()):
        ii=l[i].split()
        for j in range(ii.__len__()):
            a0[i,j,1]=float(ii[j])
            if(float(ii[j])!=-1):
                pos.append(Pos(i,j))
                typ.append(0)

with open("C:/Users/linru/Desktop/IMMC/Code/Python/合理的坐标.txt","rb") as f:
    s = f.read()
    l=s.splitlines()
    flag=1
    for i in range(l.__len__()):
        ii=l[i].split()
        if(ii.__len__()==0):
            flag=not flag
            continue
        pos.append(Pos(int(ii[0]),int(ii[1])))
        typ.append(flag+3)

N=373

a0[:,:,2]=0.719
a0[:,:,3]=104.1
a0[:,:,4]=5.5
a0[:,:,5]=9.3
a0[:,:,6]=0.01
a0[:,:,7]=0

ans=[]

print(P(0.2,10,a0,W))

# def rule(t):
#     return t.get('num')
# out=[]

# wb = xlwt.Workbook()
# # 添加一个表
# ws = wb.add_sheet('test')

# #添加数据使用.write函数（横坐标，纵坐标，内容）注意横纵坐标从0开始，横纵坐标即对于excel而言

# for x in range(maxx):
#     out.append([])
#     for y in range(maxy):
#         ans=[]
#         for ty in range(5):
#             pos=[Pos(x,y)]
#             typ=[ty]
#             N=1
#             ans.append({'type':ty,'num':P(0.2,5,a0,W)})
#         ans.sort(reverse=True,key=rule)
#         out[x].append(ans[0])
#         print(out[x][y].get('type'),end=' ')
#         ws.write(x, y, out[x][y].get('type'))
#     print("")

# wb.save('test.xls')