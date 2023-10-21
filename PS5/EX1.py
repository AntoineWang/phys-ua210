import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quadrature


#part (a)
def integrand(x,a):
    return x**(a-1)*np.e**(-x)

def plot_integrand():
    N = 100
    x = np.linspace(0,5,N)
    y = np.zeros((3,N))
    for a in [2,3,4]:
        for i in range(100):
            y[a-2,i]= integrand(x[i],a)
    
    plt.plot(x,y[0],label="a=2")
    plt.plot(x,y[1],label="a=3")
    plt.plot(x,y[2],label="a=4")
    plt.legend()
    plt.title("gamma functions from x=0 to x=5")
    plt.show()


#part (b)
#part (c) c = a-1
#part (d)
#part (e)
#part (f)
def z(a,x):
    z = x/((a-1)+x)
    return z

def z_integrand(z,a):
    return np.e**((a-1)*np.log(z*(a-1)/(1-z))-z*(a-1)/(1-z))*((a-1)/(1-z)**2)

def gamma(a):
    f = lambda z:np.e**((a-1)*np.log(z*(a-1)/(1-z))-z*(a-1)/(1-z))*((a-1)/(1-z)**2)
    res = quadrature(f,0.,1.)
    print(res)

def main():
    plot_integrand()
    gamma(3/2)
    gamma(3)
    gamma(6)
    gamma(10)

if __name__ == "__main__":
    main()
    

