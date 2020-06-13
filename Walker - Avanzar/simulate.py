#!/usr/bin/env python

from embodied_ising import ising,bool2int
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations


N=62

Nsensors=24
Nmotors=4
size=N+Nsensors+Nmotors

ind=10

beta=1
#beta=1
Iterations=1000
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

T=3600
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
''
nsize=size
I.env.reset()
T0=10000

for t in range(T0):
 	I.SequentialUpdate()
I.env.reset()
for t in range(T):
	I.SequentialUpdate()
	s[t]=I.get_state_index('input')
	a[t]=I.get_state_index('non-sensors')
	h[t]=I.get_state_index('hidden')
	m[t]=I.get_state_index('motors')
	print(I.env.hull.position[0],I.env.hull.linearVelocity[0])
	spd[t]=I.env.hull.linearVelocity[0]
	pos[t]=I.env.hull.position[0]
		
			
	if visualize:
		I.env.render()

fig, ax = plt.subplots(1,1,figsize=(4,2))
plt.rc('text', usetex=True)
plt.plot(pos,'k')
plt.ylabel(r'$x$',fontsize=18, rotation=0)
plt.xlabel(r'$t$',fontsize=18)
plt.axis([0,len(pos),0,20])
plt.savefig('img/1fig6'+str(Iterations)+'1.pdf',bbox_inches='tight')

fig, ax = plt.subplots(1,1,figsize=(4,2))
plt.rc('text', usetex=True)
plt.plot(spd,'k')
plt.ylabel(r'$v$',fontsize=18, rotation=0)
plt.xlabel(r'$t$',fontsize=18)
plt.axis([0,len(pos),-5,5])
plt.savefig('img/1fig6'+str(Iterations)+'1.pdf',bbox_inches='tight')

plt.show()

