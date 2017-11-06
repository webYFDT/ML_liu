# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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
fig,ax=plt.subplots()
line,=ax.plot([],[],'k')

#line,=ax.plot([],[],lw=2)
#plt.plot(data[:6,0],data[:6,1],'x',data[6:,0],data[6:,1],'ro')
ax.scatter(data[:,0],data[:,1],color=label_color,marker='o')
ax.plot(X,Y,'r')

ax.grid()
def data_gen():#产生每次更新的数据
    Wg=np.matrix([0,0,0])
    j=0
    while j < 110:
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

                yield Wg               
        if mis==0:
            #print j
            #print 'end'
            break
def update_g(data):#更新线段
    Wg=data
    Wg_arr=np.array(Wg)
    Xg=np.random.randint(-5,6,size=(10))
    X0g=np.ones(10)
    Yg=(-Wg_arr[0][0]*Xg-Wg_arr[0][2]*X0g)/Wg_arr[0][1]
    line.set_data(Xg,Yg)
    return line
def init():#初始设置
    #ax.set_ylim(-10,15)
    #ax.set_xlim(-10,10)
    #ax.set_zlim(0,9)
    line.set_data([],[])
    return line

ani = animation.FuncAnimation(fig, update_g, data_gen,interval=2,repeat=False,init_func=init)  
#ani.save('anim3.gif', writer='imagemagick')
plt.show()



