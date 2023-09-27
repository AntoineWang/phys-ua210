import numpy as np
import matplotlib.pyplot as plt

tau = 3.053*60 #convert the half-life to seconds
mu= np.log(2)/tau
h=1
N=1000

t_uniform = np.random.rand(N)
print(t_uniform)
print(t_uniform.size)
t_decay = (-1/mu)*np.log(1-t_uniform)
t_decay = np.sort(t_decay)

N = np.arange(0,N,h)

#print(t_decay)
#print(N)

plt.plot(t_decay,1000-N)  #how to fix the negative t problem

plt.xlabel("time / s")
plt.ylabel("Number of Tl 208 atoms left")
plt.show()
