import numpy as np
import matplotlib.pyplot as plt 
import math

x=1

def f(x):
    return x*(x-1)

def d_of_f(x,delta):
    d=(f(x+delta)-f(x))/delta
    return d

def error(d):
    e=abs(d-1)
    return e

def main():
    deltas=[10**(-2),10**(-4),10**(-6),10**(-8),10**(-10),10**(-12),10**(-14)]
    deltas=np.array(deltas)
    errors=[]
    errors=np.array(errors)
    for delta in deltas:
        d=d_of_f(x,delta)
        e=error(d)
        errors=np.append(errors,e)
    print(np.log10(deltas))
    print(np.log10(errors))
    plt.scatter(np.log10(deltas),np.log10(errors))
    plt.xlabel(r"$log_{10} \delta$")
    plt.ylabel(r"$log_{10} error")
    plt.show()
    
if __name__=="__main__":
    main()

