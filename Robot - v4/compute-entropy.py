#!/usr/bin/env python

from embodied_ising import ising
import numpy as np
import matplotlib.pyplot as plt
from info_theory import Entropy
from sys import argv

# argv = "50","50","4","2","3600","20","100"

# if len(argv) < 3:
#     print("Usage: " + argv[0] + " <N> + <bind>")
#     exit(1)

# #N=int(argv[1])

# size = int(argv[1])
# Nsensors = int(argv[2])
# Nmotors = int(argv[3])
# T = int(argv[4])
# Iterations = int(argv[5])
# repetitions = int(argv[6])

# ind=99
# bind = 100
#bind=int(argv[2])
#size=6*N
#Nsensors=2*N
#Nmotors=N


sizes = [21,23,28,30,35,40,50]
Nsensors = 16
Nmotors =4
T=1000
Iterations = 1000
#bind = 10

#for b in range(bind):

	#for a,size in enumerate(sizes):

#	print(b,size)
R=10

Nbetas=30
#betas=10**np.linspace(-1,1,Nbetas)
betas=np.linspace(0.01,3.01,Nbetas)
print(betas)
#Ha=np.zeros(R)
#Hn=np.zeros(R)
#Hs=np.zeros(R)
#Hp=np.zeros(R)
E=0

for a,size in enumerate(sizes):

	for ind in range(Nbetas):
		
		I=ising(size,Nsensors,Nmotors)
		filename='files/network-size_'+str(size)+'-sensors_'+str(Nsensors)+'-motors_'+str(Nmotors)+'-T_'+str(T)+'-Iterations_'+str(Iterations)+'-ind_'+str(R)+'.npz'

		data=np.load(filename)
		I.h=data['h']
		I.J=data['J']

		beta=betas[ind]
		I.Beta=betas[ind]
		#T1=100000*size
		T1=1000*size
		s=np.zeros(T1)
		m=np.zeros(T1)
		h=np.zeros(T1)
		a=np.zeros(T1)
		E=np.zeros(T1)
		t=0
		I.randomize_position()
		T0=int(T1/10)
		for t0 in range(T0):
			I.SequentialUpdate()
		
		F=0
		for t in range(T1):
			
			I.SequentialUpdate()
			#s[t]=I.get_state_index('sensors')
			#m[t]=I.get_state_index('motors')
			#h[t]=I.get_state_index('non-sensors')
			#a[t]=I.get_state_index()

			E[t]=-np.dot(I.h,I.s) - np.dot(I.s, np.dot(I.J,I.s))
			#print(E[t])
		Em=np.mean(E)
		print(Em,E,"size_",size,"betas_",ind)
			#Hi= I.h + np.dot(I.s,I.J)+ np.dot(I.J,I.s)
			#Fi=beta*Hi*np.tanh(beta*Hi)-np.log(2*np.cosh(beta*Hi))
			#F+=np.sum(Fi[Nsensors:])
		#F/=T1
		#Hp[ind]=F
			
		#Ha[ind]=Entropy(a)
		#Hs[ind]=Entropy(s)
		#Hn[ind]=Entropy(h)

			

		#print('Entropy agent',Ha[ind],'Entropy sensor',Hs[ind],'Entropy sensor',Hn[ind])
		
		filename='H/network-size_'+str(size)+'-sensors_'+str(Nsensors)+'-motors_'+str(Nmotors)+'-T_'+str(T)+'-Iterations_'+str(Iterations)+'-bind_'+str(ind)+'.npz'
		np.savez(filename,betas=betas,Nbetas=Nbetas,E=Em)

