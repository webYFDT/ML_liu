# -*- coding: utf-8 -*-
import numpy as np
import re
import random
f=open('title15.txt')
#f=open('title19-20A.txt')
lines=f.readlines()
data_list=[]
for line in lines:
    data_one=re.findall(r'[\d.-]+',line)
    data_one_float=[float(i)  for i in data_one]
    data_list.append(data_one_float)

data=np.array(data_list)
#print data
sum_num=0
for j in xrange(2000):#测试两千次
    Wg=np.matrix([0,0,0,0,0])
    DAxunhuan=0#大循环
    xiugai=0#h(X)函数的Wg修改的次数
    hX=0    
    while True:
        mis=0
        DAxunhuan+=1
        order=range(len(data))#每次抽取数据的顺序
        random.shuffle(order)#打乱列表顺序
        for i in order:
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
    
    print '第%d次测试，循环样本  %d  次，修改Wg  %d  次'%(j,DAxunhuan,xiugai) 
    sum_num+=xiugai
mean_num=sum_num/2000.0
print '平均修改次数：%d'%mean_num     
      
        