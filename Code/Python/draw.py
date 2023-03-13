import numpy as np

import math

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


with open("C:/Users/linru/Desktop/IMMC/Code/3D/5.obj","rb") as f:
    s = f.read()

xyz = s.splitlines()

start=[]

asp=[]


out=[]

index=[]

for inf in range(3188): 
    # print(xyz[inf].split()[0])
    if(xyz[inf].split()[0]==b'v'):
        index.append(inf)
        start.append([float(xyz[inf].split()[1]),float(xyz[inf].split()[2]),float(xyz[inf].split()[3])])
    elif(xyz[inf].split()[0]==b'vn'):
        i=inf-1596
        asp.append([float(xyz[inf].split()[1]),float(xyz[inf].split()[2]),float(xyz[inf].split()[3])])
        out.append(180*math.acos(asp[i][2]/math.sqrt(asp[i][0]**2+asp[i][1]**2+asp[i][2]**2))/math.pi)


fig = plt.figure(dpi=100)


ax = fig.add_axes(Axes3D(fig))


ax.set_zlim3d(0,12) 

# print(start[1],end[1])


for i in range(1596-4):

    ax.quiver(start[i][0],start[i][1],start[i][2],asp[i][0],asp[i][1],asp[i][2],arrow_length_ratio=0.1)

plt.show()

# fig = plt.figure(dpi=150)  

# # ax = plt.axes(projection='3d')

# # plt.axis('off')

# start=np.array(start)
# out=np.array(out)

# with open('C:/Users/linru/Desktop/IMMC/Code/Python/out', 'a+') as ff:

#     for i in range(37):
#         for j in range(54):
#             print(out[(37-i)*54+j],end=' ',file=ff)
#         print("",file=ff)

plt.scatter(-start[:,1],start[:,0],c=out,s=17)
plt.colorbar()
# ax.scatter3D(x, y, z,c=num)

plt.show()