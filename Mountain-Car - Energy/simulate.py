#!/usr/bin/env python

from embodied_ising import ising,bool2int
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

plt.rc('text', usetex=True)
font = {'family':'serif','size':12, 'serif': ['computer modern roman']}
plt.rc('font',**font)
plt.rc('legend',**{'fontsize':16})

N=64

Nsensors=4
Nmotors=2
size=N+Nsensors+Nmotors

ind=10

#beta=1.2
beta=1
Iterations=100
T=3600
visualize=True
# visualize=False


I=ising(size,Nsensors,Nmotors)
I.Beta=beta


filename='files/network-size_'+str(size)+'-sensors_'+str(Nsensors)+'-motors_'+str(Nmotors)+'-T_'+str(T)+'-Iterations_'+str(Iterations)+'-ind_'+str(ind)+'.npz'
directorio='_'+str(size)+'_'+str(Nsensors)+'_'+str(Nmotors)+'_'+str(T)+'_'+str(Iterations)+'_'+str(ind)


data=np.load(filename)
I.h=data['h']
I.J=data['J']


T=4000*2
if beta>1:
	T*=5
p=np.zeros(T)
s=np.zeros(T)
m=np.zeros(T)
h=np.zeros(T)
a=np.zeros(T)
n=np.zeros(T,int)
spins=np.zeros((size,T))
spd=np.zeros(T)
pos=np.zeros(T)
height=np.zeros(T)
recorrido=[]
CambioDireccion = 0

nsize=size
I.env.reset()
T0=10000

for t in range(T0):
	I.SequentialUpdate()
for t in range(T):
	I.SequentialUpdate()
	spd[t]=I.speed
	pos[t]=I.env.state[0]
	height[t]=I.height
	if t!=0:
		if (spd[t]>0 and spd[t-1]<=0) or (spd[t]<=0 and spd[t-1]>0):
			CambioDireccion += 1
		recorrido[CambioDireccion] += pos[t] - pos[t-1]
		print(CambioDireccion,recorrido00)
			
	if visualize:
		I.env.render()

plt.figure()
plt.

print("1")

if beta==1:
	letter='b'
elif beta<1:
	letter='a'
else:
	letter='c'
fig, ax = plt.subplots(1,1,figsize=(4.6,3.8))
plt.rc('text', usetex=True)
plt.plot(pos,spd,'k')
plt.ylabel(r'$v$',fontsize=18, rotation=0)
plt.xlabel(r'$x$',fontsize=18)
plt.title(r'$\beta='+str(beta)+'$',fontsize=36)
plt.axis([-np.pi/2-0.05,np.pi/6+0.05,-0.05,0.05])
plt.savefig('img/fig6'+letter+directorio+'.pdf',bbox_inches='tight')
print("2")

fig, ax = plt.subplots(1,1,figsize=(4,2))
plt.rc('text', usetex=True)
plt.plot(pos,'k')
plt.ylabel(r'$x$',fontsize=18, rotation=0)
plt.xlabel(r'$t$',fontsize=18)
plt.axis([0,len(pos),-np.pi/2-0.05,np.pi/6+0.05])
plt.savefig('img/fig6'+letter+'1'+directorio+'.pdf',bbox_inches='tight')


plt.show()

