#!/usr/bin/env python

from embodied_ising import ising
import numpy as np
import matplotlib.pyplot as plt
from info_theory import Entropy
from sys import argv


sizes = [21,23,28,30,35,40,50]
Nsensors = 16
Nmotors =4
T=5000
Iterations = 300

R=10

Nbetas=30
#betas=10**np.linspace(-1,1,Nbetas)
betas=np.linspace(0.01,3.01,Nbetas)
print(betas)

E=0

for a,size in enumerate(sizes):

	print(size,'_size')

	Em=0
	Em2=0
	E2=0

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
		Ecuadrado=np.zeros(T1)
		t=0
		I.randomize_position()
		T0=int(T1/10)
		for t0 in range(T0):
			I.SequentialUpdate()
		
		F=0
		for t in range(T1):
			
			I.SequentialUpdate()
			E[t]=-np.dot(I.h,I.s) - np.dot(I.s, np.dot(I.J,I.s))
			Ecuadrado[t]=E[t]**2
			#print(E[t])
		Em =np.mean(E)
		Em2=Em**2  # (E(s))^2
		E2=np.mean(Ecuadrado) #E^2(s)
		C=((I.Beta)**2)*(E2-Em2)
		#print(Em,Em2,E2,C,"beta_",betas[ind],"size_",size)

		#print('Entropy agent',Ha[ind],'Entropy sensor',Hs[ind],'Entropy sensor',Hn[ind])
		
		filename='H/network-size_'+str(size)+'-sensors_'+str(Nsensors)+'-motors_'+str(Nmotors)+'-T_'+str(T)+'-Iterations_'+str(Iterations)+'-bind_'+str(ind)+'.npz'
		np.savez(filename,betas=betas,Nbetas=Nbetas,E=Em,Em2=Em2,E2=E2,C=C)

