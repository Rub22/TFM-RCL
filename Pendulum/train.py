
#!/usr/bin/env python

from embodied_ising import ising
import numpy as np
from sys import argv


#sizes = []
size = 70
Nsensors = 4
Nmotors =2
T=3600
Iterations = 1000
#repetitions = 9
rep = 9
filename = 'correlations-ising2D-size400.npy'
Cdist = np.load(filename)
print(len(Cdist))

#for a,size in enumerate(sizes):

	#print(size,Nsensors,Nmotors,T,Iterations,repetitions)

	#for rep in range(repetitions):
I = ising(size, Nsensors, Nmotors)
I.m1 = np.zeros(size)
I.Cint = np.zeros((size, size - 1))
for i in range(size):
	c = []
	for j in range(size - 1):
		ind = np.random.randint(len(Cdist))
		c += [Cdist[ind]]
	I.Cint[i, :] = -np.sort(-np.array(c))

I.CriticalLearning(Iterations, T)

filename = 'files/network-size_' + str(size) + '-sensors_' + str(Nsensors) + '-motors_' + str(
    Nmotors) + '-T_' + str(T) + '-Iterations_' + str(Iterations) + '-ind_' + str(rep) + '.npz'
np.savez(filename, J=I.J, h=I.h, m1=I.m1, Cint=I.Cint)
