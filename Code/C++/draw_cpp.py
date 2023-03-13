import matplotlib.pyplot as plt

x=[]
y1=[]
y2=[]
y3=[]

with open("C:/Users/linru/Desktop/IMMC/Code/C++/out","rb") as f:
    s = f.read()
    l=s.splitlines()
    for i in range(l.__len__()):
        ii=l[i].split()
        x.append(float(ii[0]))
        y1.append(float(ii[1]))
        y2.append(float(ii[2]))
        y3.append(float(ii[3]))

plt.figure(dpi=150)
# plt.plot(x,y1,c='k',linestyle='--')#,lable='植被覆盖率')
plt.plot(x,y3,c='k')#,linestyle='-.')#,lable='污染')
# plt.plot(x,y3,c='k')

plt.show()