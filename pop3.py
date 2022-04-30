import numpy as np 
import pandas as pd 
import os
#批量转换为pd
#输入板块 
print('请输入待查找的初始目录:', end='')
inpu=input()
id1='data/'+inpu
# print('请输入pd的初始目录:', end='')
putpd='pd/'+inpu
# print('请输入csv的初始目录:', end='')
putfilelocal='csv/'+inpu
for root, dirs, files in os.walk(id1):
    for file in files:
        print(os.path.join(root, file))
        putfilename=file
        f=open(id1+'/'+file,'r')
        f3=f.readlines
        f.seek(0,0)        
        ff=open(putpd+'/'+putfilename,'w+')
        new=[]
        i=0
        for line in f:
            i=i+1
            o=0
            for j in line:
                if j.isalpha() :
                    o=o+1
                    break
            if o==0 and line[0]!='-':
                new.append(line)
        for n in new:
            ff.write(n)
        ff.close()
        f.close()
        txt = np.loadtxt(putpd+'/'+putfilename) 
        txtDF = pd.DataFrame(txt) 
        txtDF.to_csv(putfilelocal+'/'+putfilename+'.csv',index=False)