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
sizes = [7,10,20,30,50,70]

ind=9

beta=1
#beta=1
Iterations=1000
T=3600
visualize=True
# visualize=False

T=3600
p=np.zeros(T)
s=np.zeros(T)
m=np.zeros(T)
h=np.zeros(T)
a=np.zeros(T)
n=np.zeros(T,int)
spd=np.zeros(T)
pos=np.zeros(T)
height=np.zeros(T)
recorrido=[]
recorrido.append(0)
CambioDireccion = 0
ejex=[]
exponentes=np.linspace(-1,1.6,100)
ejex=10**exponentes
ejex[0]=0

T0=10000
count = -1

for a,size in enumerate(sizes):
	CambioDireccion = 0
	recorrido=[]
	recorrido.append(0)
	I=ising(size,Nsensors,Nmotors)

	filename='files/network-size_'+str(size)+'-sensors_'+str(Nsensors)+'-motors_'+str(Nmotors)+'-T_'+str(T)+'-Iterations_'+str(Iterations)+'-ind_'+str(ind)+'.npz'
	directorio='_'+str(size)+'_'+str(Nsensors)+'_'+str(Nmotors)+'_'+str(T)+'_'+str(Iterations)+'_'+str(ind)
	data=np.load(filename)
	I.h=data['h']
	I.J=data['J']

	count +=1

	for t in range(T0*10):
		I.SequentialUpdate()
	for t in range(T):
		I.SequentialUpdate()
		spd[t]=I.speed
		pos[t]=I.env.state[0]
		height[t]=I.height
		if t>0:
			if (spd[t]>0 and spd[t-1]<=0) or (spd[t]<=0 and spd[t-1]>0):
				CambioDireccion += 1
				recorrido.append(0)
			recorrido[CambioDireccion] += abs(pos[t] - pos[t-1])
			if (pos[t] - pos[t-1])>10:
				recorrido[CambioDireccion] -= 4*np.pi
			#print(CambioDireccion)	
		#if visualize:
		#	I.env.render()
		
	print(CambioDireccion)
	plt.figure()
	plt.hist(recorrido,ejex,color='gray',label='size = '+str(size))
	plt.xlabel(r'$L$',fontsize=18)
	plt.ylabel(r'$Frecuencia$',fontsize=18)
	plt.gca().set_xscale("log")
	plt.savefig('img/histVarV4_size_'+str(size)+'.pdf',bbox_inches='tight')

# # fig, ax = plt.subplots(1,1,figsize=(4,2))
# # plt.rc('text', usetex=True)
# # plt.plot(pos,'k')
# # plt.ylabel(r'$x$',fontsize=18, rotation=0)
# # plt.xlabel(r'$t$',fontsize=18)
# # plt.axis([0,len(pos),-np.pi/2-0.05,np.pi/6+0.05])
# # plt.savefig('img/fig6'+letter+'1'+directorio+'.pdf',bbox_inches='tight')

# fig, ax = plt.subplots(1,1,figsize=(4,2))
# plt.rc('text', usetex=True)
# plt.plot(spd,'k')
# plt.ylabel(r'$v$',fontsize=18, rotation=0)
# plt.xlabel(r'$t$',fontsize=18)
# plt.axis([0,len(spd),-.4,.4])
# plt.savefig('img/fig6'+letter+'1'+directorio+'.pdf',bbox_inches='tight')


plt.show()

