import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

with open("C:/Users/linru/Desktop/IMMC/Code/3D/无标题.obj","rb") as f:
    s = f.read()

xyz = s.splitlines()

start=[]

end=[]

for inf in range(4,1596):
    start.append([float(xyz[inf].split()[1]),float(xyz[inf].split()[3]),float(xyz[inf].split()[2])])

for inf in range(1596,3188):
    end.append([float(xyz[inf].split()[1]),float(xyz[inf].split()[3]),float(xyz[inf].split()[2])])

# fig = plt.figure()

# ax = fig.add_axes(Axes3D(fig))

# # ax.set_zlim3d(0,12)

# # print(start[1],end[1])

# for i in range(1596-4):
#     ax.quiver(start[i][0],start[i][1],start[i][2],end[i][0],end[i][1],end[i][2],arrow_length_ratio=0.1)


# plt.show()
# fig = plt.figure()  
# ax = plt.axes(projection='3d')
# plt.axis('off')

# ax.scatter3D(x, y, z,c=num)
# plt.show()