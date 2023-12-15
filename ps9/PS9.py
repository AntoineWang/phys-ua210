import numpy as np
import matplotlib.pyplot as plt
from banded import banded

h = 1e-17
hbar = 1.0546e-34
L = 1e-8
M = 9.109e-31
N = 1000
a = L/N

a1 = 1 + h**1j*hbar/(2*M*(a**2))
a2 = -h*hbar*1j/(4*M*(a**2))
b1 = 1 - h*1j*hbar/(2*M*(a**2))
b2 = h*hbar*1j/(4*M*(a**2))

x0 = L/2
sigma = 1e-10
k = 5e10
x = np.linspace(0, L, 1001)
psi = np.exp(-(x-x0)**2/(2*sigma**2))*np.exp(1j*k*x)
psi[0] = psi[-1] = 0


A = np.empty((3, N), complex)
A[0, :] = a2
A[1, :] = a1
A[2, :] = a2


itr = 2000
t_list = np.arange(0, h*itr, h)

psi_list = []

for i in range(len(t_list)):
	t = t_list[i]
	psi_list.append(psi)
	counter = psi
	counter = np.concatenate(([0],psi,[0]))
	v = b1*counter[1:N] + b2*(counter[2:N+1]+counter[:N-1])
	print(np.mean(v))
	psi[1:N] = banded(A, v, 1, 1)


psi_real = np.real(psi_list)
