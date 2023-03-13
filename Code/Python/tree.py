import xlrd
import numpy as np

data = xlrd.open_workbook("tree.xls")

table = data.sheets()[0] 

nrows=table.nrows

t=[]

with open('C:/Users/linru/Desktop/IMMC/Code/Python/tree', 'a+') as ff:

    for i in range(nrows):
        row=table.row(i)
        t.append([])
        for j in range(row.__len__()):
            t[i].append(table.cell_value(i,j))
            if(t[i][j]==''):
                t[i][j]=-1
            print(t[i][j],end=' ',file=ff)
        print('',file=ff)
        


