import numpy as np
import matplotlib.pyplot as plt

h = 1e-18
hbar = 1.0546e-34
L = 1e-8
M = 9.109e-31
N = 1000
a = L/N

a1 = 1 + h*1j*hbar/(2*M*(a**2))
a2 = -h*hbar*1j/(4*M*(a**2))
b1 = 1 - h*1j*hbar/(2*M*(a**2))
b2 = h*hbar*1j/(4*M*(a**2))

x0 = L/2
sigma = 1e-10
k = 5e10
x = np.linspace(0, L, 1000)
psi = np.exp(-(x-x0)**2/(2*sigma**2))*np.exp(1j*k*x)
psi[0] = psi[-1] = 0


A1_diag = np.full(N, a1)
A2_diag = np.full(N-1, a2)
A = np.diag(A2_diag, 1)+np.diag(A2_diag, -1)+np.diag(A1_diag)

B1_diag = np.full(N, b1)
B2_diag = np.full(N-1, b2)
B = np.diag(B2_diag, 1)+np.diag(B2_diag, -1)+np.diag(B1_diag)

U = np.linalg.inv(A)@B

#t_list = np.arange(0, h*itr, h)

psi_list = np.array([])


plt.plot(np.real(psi))
plt.show()

itr = 10000
for i in range(itr):
	psi = U@psi
	psi[0] = psi[-1] = 0

plt.plot(np.real(psi))
plt.show()
