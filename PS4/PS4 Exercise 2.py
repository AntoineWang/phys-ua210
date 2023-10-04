import math
import numpy as np
import matplotlib.pyplot as plt
import gaussxw

m = 1

def f(a,x):
    integrand = math.sqrt(8*m/(a**4-x**4))
    return integrand

def calculate_period(b): #b is the upper bound of the integral
    N = 100
    a = 0
    x,w = gaussxw.gaussxwab(N,a,b)
    # Perform the integration
    s = 0.0
    for k in range (N) :
        s += w[k]*f(b,x[k])
    return s

def main():
    x_list = np.arange(0,2,0.1,float)
    v_list = np.zeros(20,float)
    for i in range(20):
        v_list[i] = calculate_period(x_list[i])
    plt.plot(x_list,v_list)
    plt.xlabel("a : Amplitude")
    plt.ylabel("T : period")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()



