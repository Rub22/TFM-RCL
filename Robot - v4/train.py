
#!/usr/bin/env python

from embodied_ising import ising
import numpy as np
from sys import argv

# argv = "50","400","12","12","1000","20","9"

# if len(argv) < 7:
#     print(
#         "Usage: " +
#         argv[0] +
#         " <network size>" +
#         " <number of sensors>" +
#         " <number of motors>" +
#         " <Simulation time>"
#         " <Number of iterations>" +
#         " <Number of repetitions>")
#     exit(1)

# size = int(argv[1])
# Nsensors = int(argv[2])
# Nmotors = int(argv[3])
# T = int(argv[4])
# Iterations = int(argv[5])
# repetitions = int(argv[6])


size = 90
Nsensors = 24
Nmotors = 4
T=3600
Iterations = 10000
rep = 10
#Nbetas=10
#betas=10**np.linspace(-1,1,Nbetas)
#betas=np.linspace(0.01,2.01,Nbetas)
filename = 'correlations-ising2D-size400.npy'
Cdist = np.load(filename)
print(len(Cdist))

#for a,size in enumerate(sizes):

#	print(size,Nsensors,Nmotors,T,Iterations,repetitions)

	#for rep in range(repetitions):
I = ising(size, Nsensors, Nmotors)
#I.Beta = betas[rep]
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
#print(a,size)
