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

ind=9

beta=1
#beta=1

Iterations=1000
T=3600
visualize=True
# visualize=False


I=ising(size,Nsensors,Nmotors)
I.Bveta=beta



filename='files/network-size_'+str(size)+'-sensors_'+str(Nsensors)+'-motors_'+str(Nmotors)+'-T_'+str(T)+'-Iterations_'+str(Iterations)+'-ind_'+str(ind)+'.npz'
directorio='_'+str(size)+'_'+str(Nsensors)+'_'+str(Nmotors)+'_'+str(T)+'_'+str(Iterations)+'_'+str(ind)


data=np.load(filename)
I.h=data['h']
I.J=data['J']

p=np.zeros(T)
s=np.zeros(T)
m=np.zeros(T)
h=np.zeros(T)
a=np.zeros(T)
n=np.zeros(T,int)
spins=np.zeros((size,T))
spd=np.zeros(T+1)
posX=np.zeros(T+1)
posY=np.zeros(T+1)
th=np.zeros(T+1)
acel=np.zeros(T+1)
recorrido=[]
recorrido.append(0)
CambioDireccion = 0
ejex=[]
exponentes=np.linspace(-1,1.6,100)
ejex=10**exponentes
ejex[0]=0

nsize=size
I.env.reset()
T0=10000

spd[0] = 0
posX[0] = 0
posY[0] = -I.env.l
th[0] = 3*np.pi/2
acel[0] = 0

for t in range(T0):
 	I.SequentialUpdate()
for t in range(T):
	I.SequentialUpdate()
	s[t]=I.get_state_index('input')
	a[t]=I.get_state_index('non-sensors')
	h[t]=I.get_state_index('hidden')
	m[t]=I.get_state_index('motors')
	spd[t+1]=I.speed
	posX[t+1]=I.positionX
	posY[t+1]=I.positionY
	th[t+1]=I.env.state[0]
	acel[t+1]=I.env.a
	#height[t+1]=I.height
	if t>0:
		if (spd[t]>0 and spd[t-1]<=0) or (spd[t]<=0 and spd[t-1]>0):
			CambioDireccion += 1
			recorrido.append(0)
		recorrido[CambioDireccion] += abs(th[t] - th[t-1])

#	if visualize:
#		I.env.render()

# fig, ax = plt.subplots(1,1,figsize=(4,2))
# plt.rc('text', usetex=True)
# plt.plot(th%(2*np.pi)-(np.pi),'k')
# plt.ylabel(r'$theta$',fontsize=18, rotation=0)
# plt.xlabel(r'$t$',fontsize=18)
# plt.axis([0,len(posY),-5,5])
# plt.savefig('img/fig6'+letter+'2'+directorio+'.pdf',bbox_inches='tight')

# fig, ax = plt.subplots(1,1,figsize=(4,2))
# plt.rc('text', usetex=True)
# plt.plot(np.sin(th%(2*np.pi)-(3*np.pi/2))*I.env.l,'k')
# plt.ylabel(r'$y$',fontsize=18, rotation=0)
# plt.xlabel(r'$t$',fontsize=18)
# plt.axis([0,len(posY),-1.1,1.1])
# plt.savefig('img/fig6'+letter+'3'+directorio+'.pdf',bbox_inches='tight')

# # fig, ax = plt.subplots(1,1,figsize=(4,2))
# # plt.rc('text', usetex=True)
# # plt.plot(acel,'k')
# # plt.ylabel(r'$acel$',fontsize=18, rotation=0)
# # plt.xlabel(r'$t$',fontsize=18)
# # plt.axis([0,len(posX),-2.02,2.02])
# # plt.savefig('img/fig6'+letter+'4'+directorio+'.pdf',bbox_inches='tight')

# fig, ax = plt.subplots(1,1,figsize=(4,2))
# plt.rc('text', usetex=True)
# plt.plot(spd,'k')
# plt.ylabel(r'$w$',fontsize=18, rotation=0)
# plt.xlabel(r'$t$',fontsize=18)
# plt.axis([0,len(posY),-5.5,5.5])
# plt.savefig('img/fig6'+letter+'5'+directorio+'.pdf',bbox_inches='tight')

plt.figure()
plt.hist(recorrido,ejex,color='gray',label='Histograma de theta') #if visualize:
plt.xlabel(r'$theta$',fontsize=18)
plt.ylabel(r'$Frecuencia$',fontsize=18)
plt.gca().set_xscale("log")
plt.savefig('img/histLCont_beta_size70.pdf',bbox_inches='tight')


plt.show()

