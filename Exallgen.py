from cProfile import label
from turtle import color
from skimage import io,data
import numpy as np 
import pandas as pd 
import os
import  matplotlib.pyplot as plt

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
print('请输入待查找的初始目录:', end='')
q=input()
id1='csv/'+q
png='jpg/'+q
for root, dirs, files in os.walk(id1):
    for file in files:
        print(os.path.join(root, file))
        csv=id1+'/'+file
        pd1=pd.read_csv(csv)
        # 定义生成图函数
        def drawpic(y1,ln,xlabel='time/fs',ylabel='Eng/eV',x='0',lx=l0,color=['g']):
            j=0
            li=''
            for i in y1:
                # ax=pd1.plot.scatter(x=x,y=i,color=color[j],label=ln[j])
                if j==0:
                    ax=pd1.plot.scatter(x=x,y=i,color=color[j],label=ln[j])
                else:
                    ax=pd1.plot.scatter(x=x,y=i,color=color[j],label=ln[j],ax=ax)
                xy(ax=ax,xlabel=xlabel,ylabel=ylabel)
                li=li+ln[j]
                j=j+1
            plt.savefig(png+'/'+file[:-4]+lx+'to'+li+'.jpg')
            plt.close()
            # ax=0
        # 温度随步数变化
        drawpic(y1=['2'],ln=[l2],ylabel='pressure/bar',x='1',xlabel='Temp/K')
        # drawpic(y1=['3'],ln=[l3])
        # drawpic(y1=['4','5','6'],ln=[l4,l5,l6],color=['g','r','b'])
        # drawpic()
        # drawpic(y1=['1'],ln=[l1],ylabel='temp/K')

        
    