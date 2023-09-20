import numpy as np
import math
import timeit
import numpy.ma as ma

L=100
a=1 #0.563nm#
vMultiplier=1 #e/4*pi*epsilon#
def createList(L):
    i=np.arange(-L/2,L/2+1).tolist()
    return i

def calcDist(i,j,k):
    distance = a*math.sqrt(i**2+j**2+k**2)
    return distance
    
def for_loop(i,j,k,V):
    for m in i:
        for n in j:
            for o in k:
                if m==0 and n==0 and o==0:
                    V+=0
                else:
                    distance = calcDist(m,n,o)
                    sign=(m+n+o)%2
                    V+=1/(((-1)**sign)*distance)
    return V

def main():
    i=createList(L)
    j=createList(L)
    k=createList(L)
    V=0
    start=timeit.default_timer()
    V=for_loop(i,j,k,V)
    dt=timeit.default_timer()-start
    print(V)
    print(dt)


