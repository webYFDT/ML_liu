# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#二维图
data=np.array([(2,8,1),(1,10,1),(-1,2,1),(-1,3,1),(-2,0,1),(-4,-4.8,1),
               (1,-0.1,1),(2,6,1),(3,8.5,1),(3.5,-1,1),(4,5,1),(4.5,10,1),(-3,-3.2,1)])
label=np.array([-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1])
label_color=[]
label_marker=[]

X=np.random.randint(-5,6,size=(10))
Y=2*X+3
for i in label:
    if i==-1:
        label_color.append('k')
        #label_marker.append('x')
    else:
        label_color.append('r')
        #label_marker.append('o')
#print label_color,label_marker

#plt.plot(data[:6,0],data[:6,1],'x',data[6:,0],data[6:,1],'ro')
plt.scatter(data[:,0],data[:,1],color=label_color,marker='o')
plt.plot(X,Y,'r')
#plt.show()
plt.close()

#三维图

x0_line=np.ones(10)
x0=np.random.randint(-5,6,size=(100))
x1=np.random.randint(-5,6,size=(100))#x1==>x
x2=2*x1+3*x0#x2==>y
fig=plt.figure()
ax=Axes3D(fig)
#x1,x2 = np.meshgrid(x1, x2)
#ax.plot_surface(x1, x2, x0, rstride=1, cstride=1, cmap='rainbow')#三维面
#ax.plot_trisurf(x1, x2, x0,color='y')#f三维面
ax.plot(X,Y,x0_line,'r')#f三维线
ax.scatter(data[:,0],data[:,1],data[:,2],color=label_color,marker='o')#训练数据点
#ax.plot_trisurf(data[:,0],data[:,1],data[:,2])#训练数据点三维面





Wg=np.matrix([0,0,0])
for j in xrange(1000):
    mis=0
    for i in xrange(13):
        #print i
        data_X=np.matrix(data[i])
        WgX=Wg*(data_X.T)
        #print WgX,data[i]
        if WgX==0:
            hX=0
        elif WgX>0:
            hX=1
        else:
            hX=-1
        if label[i]!=hX:
            mis=mis+1
            Wg=Wg+label[i]*data[i]
    
    if mis==0:
        print j
        #print 'end'
        break
Wg_arr=np.array(Wg)
Xg=np.random.randint(-5,6,size=(10))
X0g=np.ones(10)
Yg=(-Wg_arr[0][0]*Xg-Wg_arr[0][2]*X0g)/Wg_arr[0][1]
print 'xxxxxxxxxxxx'

ax.plot(Xg,Yg,X0g,'b')#g三维线

        
ax.set_xlabel('X') #坐标轴
ax.set_ylabel('Y')
ax.set_zlabel('X0')

  
plt.show()

