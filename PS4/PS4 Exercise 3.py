import math
import numpy as np
import matplotlib.pyplot as plt
import gaussxw
def hermite_polynomial(n,x):
    if n == 0:
        return 1
    elif n == 1:
        return 2*x
    else:
        return (2*x*hermite_polynomial(n-1,x)-2*(n-1)*hermite_polynomial(n-2,x))

def harmonic_oscillator(n,x):
    psi = 1/(np.sqrt(2**n*math.factorial(n)*np.sqrt(math.pi)))*np.e**(-x**2/2)*hermite_polynomial(n,x)
    return psi

def f_z2(n,z):
    integrand = (1+z**2)/((1-z**2)**2)*((z/(1-z**2))**2)*abs(harmonic_oscillator(n,(z/(1-z**2))))**2
    return integrand

def f_z(n,z): #this is the change of variable function which returns the new integrand
    integrand = (np.tan(z)**2)*(abs(harmonic_oscillator(n,np.tan(z))**2)/(np.cos(z)**2))
    return integrand

def main():
    #part a
    N = 2000 #number of data points of x we're taking
    x_list = np.linspace(-4,4,N)
    list_of_psi_for_all_n=[]
    for n in range(4):
        list_of_psi_for_n = []
        for x in x_list:
            psi = harmonic_oscillator(n,x)
            list_of_psi_for_n.append(psi)
        list_of_psi_for_all_n.append(list_of_psi_for_n)
    
    for i in range(4):
        plt.plot(x_list,list_of_psi_for_all_n[i],label="n = "+str(i))
    plt.legend()
    plt.show()

    #part b
    N = 1000
    x_list = np.linspace(-10,10,N)
    list_of_psi = harmonic_oscillator(30,x_list)
    plt.plot(x_list,list_of_psi, label = "n = 30")
    plt.legend()
    plt.show()

    #part c
    N = 100
    a = -np.pi/2 #lower bound
    b = np.pi/2  #upper bound
    x,w = gaussxw.gaussxwab(N,a,b)
    # Perform the integration
    s = 0.0
    for k in range (N) :
        s += w[k]*f_z(5,x[k]) #choose n = 5 here
    print(np.sqrt(s))

    #part c using f_z2 change of variable
    N = 100
    a = -1.0 #lower bound
    b = 1.0  #upper bound
    x,w = gaussxw.gaussxwab(N,a,b)
    # Perform the integration
    s = 0.0
    for k in range (N) :
        s += w[k]*f_z2(5,x[k]) #choose n = 5 here
    print(np.sqrt(s))
    
if __name__ == "__main__":
    main()
    
        
        
