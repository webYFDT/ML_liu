# -*- coding: utf-8 -*-
import numpy as np
import re
f=open('title15.txt')

lines=f.readlines()
data_list=[]
for line in lines:
    data_one=re.findall(r'[\d.-]+',line)
    data_list.append(data_one)

data=np.float32(np.array(data_list))

Wg=np.matrix([0,0,0,0,0])
DAxunhuan=0#大循环
xiugai=0#h(X)函数的Wg修改的次数
hX=0

while True:
    mis=0
    DAxunhuan+=1
    for i in xrange(len(data)):
        dataone=list(data[i][:4])
        #print len(dataone)
        y=data[i][4]
        dataone.append(1.0)
        data_x=np.matrix(dataone)
        WgX=Wg*(data_x.T)
        #print WgX,data[i][4]
        if WgX<=0:
            #print WgX
            hX=-1
        else:
            hX=1
        if hX!=y:
            #print mis
            xiugai+=1
            Wg=Wg+y*data_x
            mis+=1
    if mis==0:
        break

print DAxunhuan
print xiugai
        
      
        