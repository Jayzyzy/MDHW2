from cProfile import label
from turtle import color
from skimage import io,data
import numpy as np 
import pandas as pd 
import os
import  matplotlib.pyplot as plt
#合并相关列并输出
id1='csv/'+input('csv/')
idput='csvcls/'+input('输出到文件夹')
j=0
pdcls=[]
print('输入列:', end='')
clm=input()
fncls=''
for root, dirs, files in os.walk(id1):
    for file in files:
        fncls=fncls+file[:-4]
        print(os.path.join(root, file))
        putpd='pd'
        csv=id1+'/'+file
        pd1=pd.read_csv(csv)
        if j==0:
            pd2=pd1[['0']]
        pd1=pd1[[clm]]
        f=clm+file[:-4]
        pd1.columns = [f]
        pdcls.append(pd1)
        if j==0:
            d=pd2.merge(pd1, how='outer', left_index=True, right_index=True)
            
        if j==1:
            df_outer = d.merge(pd1, how='outer', left_index=True, right_index=True)
        elif j>1:
            df_outer =df_outer.merge(pd1, how='outer', left_index=True, right_index=True)
        j=j+1
outputpath=idput+'/'+clm+fncls
df_outer.to_csv(outputpath,sep=',',index=False,header=True)
print(list(df_outer))

pd1=pd.read_csv(outputpath)
print(list(pd1))