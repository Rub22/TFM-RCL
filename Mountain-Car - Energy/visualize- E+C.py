#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit
from scipy.interpolate import splev, splrep

plt.rc('text', usetex=True)
font = {'size':15}
plt.rc('font',**font)
plt.rc('legend',**{'fontsize':14})


R=10

Iterations=1000
T=1000
save=False
save=True
sizes = [7,8,10,14,22,38,70]

Nbetas=30
#betas=10**np.linspace(-1,1,Nbetas)
betas=np.linspace(0.01,3.01,Nbetas)

Ev=np.zeros((len(sizes),30))
C=np.zeros((len(sizes),30))

for s,size in enumerate(sizes):


	for bind in range(Nbetas):
			
		Nsensors=4
		Nmotors=2

		filename='H/network-size_'+str(size)+'-sensors_'+str(Nsensors)+'-motors_'+str(Nmotors)+'-T_'+str(T)+'-Iterations_'+str(Iterations)+'-bind_'+str(bind)+'T010000.npz'
		data=np.load(filename)	
		#Ev[bind] = data['E']
		Ev[s,bind] = data['E']
		C[s,bind] = data['C']

fig, ax = plt.subplots(1,1,figsize=(4,3))
plt.rc('text', usetex=True)
plt.plot(betas,Ev[3],'k',label="size=10",color="black",linewidth=2.5)
plt.plot(betas,Ev[4],'k',label="size=22",color="green",linewidth=2.5)
plt.plot(betas,Ev[5],'k',label="size=38",color="red",linewidth=2.5)
plt.plot(betas,Ev[6],'k',label="size=70",color="blue",linewidth=2.5)
plt.legend(loc='upper right')
plt.ylabel(r'$E$',fontsize=18, rotation=0)
plt.xlabel(r'$beta$',fontsize=18)
plt.axis([0,3.1,-50,5])
plt.savefig('img/fig4_size'+str(size)+'.pdf',bbox_inches='tight')


fig, ax = plt.subplots(1,1,figsize=(4,3))
plt.rc('text', usetex=True)
plt.plot(betas,C[3],'k',label="size=10",color="black",linewidth=2.5)
plt.plot(betas,C[4],'k',label="size=22",color="green",linewidth=2.5)
plt.plot(betas,C[5],'k',label="size=38",color="red",linewidth=2.5)
plt.plot(betas,C[6],'k',label="size=70",color="blue",linewidth=2.5)
plt.legend(loc='upper right')
plt.legend(loc='upper right')
plt.ylabel(r'$C$',fontsize=18, rotation=0)
plt.xlabel(r'$beta$',fontsize=18)
plt.axis([0,3.1,0,120])
plt.savefig('img/fig5_size'+str(size)+'.pdf',bbox_inches='tight')

plt.show()

