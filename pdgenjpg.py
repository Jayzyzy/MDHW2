from cProfile import label
from turtle import color
from skimage import io,data
from colorgen import randomcolor
import numpy as np 
import pandas as pd 
import os
import  matplotlib.pyplot as plt


png='png'
#label标号
l0='time'
l1='temp'
l2='Press'
l3='Volume'
l4='PoyEng'
l5='KinEng'
l6='TotEng'
l7='Enthalpy'
#对x,y轴标
def xy(ax,xlabel,ylabel):
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
#输入板块 
# print('请输入待查找的初始目录:', end='')
# id1=input()
id1='csvcls/'+input('pd所在文件夹')
print('key ylebal', end='')
ylabel=input()
putjpg='jpg/'+input('jpg所在文件夹')


for root, dirs, files in os.walk(id1):
    for file in files:
        print(os.path.join(root, file))
        csv=id1+'/'+file
        pd1=pd.read_csv(csv)
        ylst=list(pd1)
        print(ylst)
        # 定义生成图函数
        def drawpic(y1,ln,xlabel='time/fs',ylabel='Eng/eV',x='0',lx=l0,color=['#A9DFE6']):
            j=0
            li=''
            for i in y1:
                # ax=pd1.plot.scatter(x=x,y=i,color=color[j],label=ln[j])
                if j==0:
                    ax=pd1.plot.scatter(x=x,y=i,s=1,color=randomcolor(),label=ln[j][1:])
                else:
                    ax=pd1.plot.scatter(x=x,y=i,s=1,color=randomcolor(),label=ln[j][1:],ax=ax)
                xy(ax=ax,xlabel=xlabel,ylabel=ylabel)
                li=li+ln[j]
                j=j+1
            plt.savefig(putjpg+'/'+file[:-4]+lx+'to'+li+'.jpg')
            plt.close()
            # ax=0
        drawpic(y1=ylst[1:],ln=ylst[1:],x=ylst[0],ylabel=ylabel)
    