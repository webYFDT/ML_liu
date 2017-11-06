# -*- coding: utf-8 -*-
import numpy as np
import re
import random
def get_data(filename):
    f=open(filename)
    
    
    lines=f.readlines()
    data_list=[]
    
    for line in lines:
        data_one=re.findall(r'[\d.-]+',line)
        data_one_float=[float(i)  for i in data_one]
        data_list.append(data_one_float)
        #data_list.append(data_one)
    #print data_list
    #print np.array(data_list)
    data=np.array(data_list)
    #print np.float64(np.array(data_list))
    #data=np.float32(np.array(data_list))
    #print 3
    f.close()
    return data
def get_mis_num(data,Wg):
    Wg_mis_point=0    
    for k in xrange(len(data)):
        dataone=list(data[k][:4])
        
        y=data[k][4]
        dataone.append(1.0)
        data_x=np.matrix(dataone)
        WgX=Wg*(data_x.T)
        if WgX<=0:
            hX=-1
        else:
            hX=1  
        if hX!=y:
            Wg_mis_point+=1  
    #print Wg_mis_point
    return Wg_mis_point
data=get_data('title19-20A.txt')
data_test=get_data('title19-20B.txt')
#print data_test

#input()
sum_error=0
Wg_list=[]
Wg_mis_point_list=[]
for j in xrange(2000):#测试两千次
    Wg=np.matrix([0,0,0,0,0])
    mis=0    #记录更新次数
    break_mis=0
    while True:
        
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

                Wg=Wg+y*data_x
                mis+=1
                Wg_mis_point=get_mis_num(data,Wg)
                #print mis,Wg_mis_point
                Wg_list.append(Wg)
                Wg_mis_point_list.append(Wg_mis_point)
                                          
            if mis==50:
                break_mis=1
                break
        if break_mis==1:
            break

    finall_Wg_addr=Wg_mis_point_list.index(min(Wg_mis_point_list))
    finall_Wg=Wg_list[finall_Wg_addr]#50次迭代中最优Wg
    
    Wg_mis_point_test=get_mis_num(data_test,finall_Wg)
    error=Wg_mis_point_test/float(len(data_test))
    print '第%d次测试,错误率为%f'%(j,error) 
    sum_error+=error
mean_error=sum_error/2000.0
print '平均错误率%f'%mean_error
 
   #   0.116826
        