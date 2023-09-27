from random import random
from numpy import arange
import matplotlib.pyplot as plt

NBi_213 = 10000
NTl = 0
NPb = 0
NBi_209 = 0
#list of tau in order of [Bi,TI,Pb]
tau = [46*60,2.2*60,3.3*60]
h=1.0
p=[0,0,0]
#list of probability of decay in order of [Bi,TI,Pb]
for i in range(3):
    p[i] = 1 - 2**(-h/tau[i])
tmax = 20000

#lists of plot points
tpoints = arange (0.0,tmax,h)
NBi_213_points = []
NTl_points = []
NPb_points = []
NBi_209_points = []

#Main loop
for t in tpoints:
    NBi_213_points.append(NBi_213)
    NTl_points.append(NTl)
    NPb_points.append(NPb)
    NBi_209_points.append(NBi_209)

    #calculate the number of atoms that decay
    #(a) do the decay of Pb_209 first

    decay = 0
    for i in range(NPb):
        if random()<p[2]: #p(2) is the probability of Pb_209 decay
            decay += 1
    NPb -= decay
    NBi_209 += decay

    #(b) do the decay of TI_209 second
    decay = 0
    for i in range(NTl):
        if random()<p[1]:#p(1) is the probability of Tl_209 decay
            decay += 1
    NTl -= decay
    NPb += decay

    #(c) do the decay of Bi_213 last
    decay_Pb = 0 #number of Bi_213 that decays to Pb_209
    decay_Tl = 0 #number of Bi_213 that decays to Tl_209
    for i in range(NBi_213):
        if random()<p[0]:#p[0] is the probability that Bi_213 decays "at all"
            if random()<0.9791: #this is the probability that it decays to Pb_209
                decay_Pb += 1
            else:
                decay_Tl += 1
    NPb += decay_Pb
    NTl += decay_Tl
    NBi_213 -= (decay_Pb + decay_Tl)
        
            

#Make the graph
#plt.plot(tpoints,NBi_213_points,label=r'$\prescript{213}{} {\mathbf{Bi}}$')
plt.plot(tpoints, NBi_213_points, label = r"$^{213}\mathrm{Bi}$")
plt.plot(tpoints,NTl_points,label = r"$^{209}\mathrm{Tl}$")
plt.plot(tpoints,NPb_points,label = r"$^{209}\mathrm{Pb}$")
plt.plot(tpoints,NBi_209_points,label = r"$^{209}\mathrm{Bi}$")

#\prescript{238}{92}{\mathbf{U}}

plt.xlabel("Time")
plt.ylabel("Number of atoms")
plt.legend()
plt.show()
