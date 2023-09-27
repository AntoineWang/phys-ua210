import timeit
from numpy import zeros
import numpy as np
import matplotlib.pyplot as plt

    
def main():
    N = 10 #size of the matrix in the first measurement
    testNumber = 15 #number of measurements
    N_list = np.zeros(testNumber,int)
    dt_list = np.zeros((2,testNumber),float)
    for i in range(testNumber):
        N_list[i] = 10 + 10*i  #create a list of progressive array sizes
    i = 0 #set counter to update the dt_list array
    for n in N_list: #perform the multiplication 10 times
        dt = time(n)
        dt_2 = time_2(n)
        dt_list[0,i] = dt
        dt_list[1,i] = dt_2
        i += 1
    plt.scatter(N_list,(dt_list[0,])**(1/3),label = "manually")
    plt.scatter(N_list,(dt_list[1,])**(1/3),label = "numpy dot function")
    plt.xlabel("size of the matrix")
    plt.ylabel("cube root of time consumed / s")
    plt.legend()
    plt.show()


    
    
def time(N):
    A = np.full((N, N), 1)
    B = np.full((N, N), 2)
    C = zeros([N,N],float)
    start = timeit.default_timer()
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i,j] += A[i,k]*B[k,j]
    dt = timeit.default_timer()-start
    return dt

def time_2(N):
    A = np.full((N, N), 1)
    B = np.full((N, N), 2)
    start = timeit.default_timer()
    C = np.dot(A,B)
    dt = timeit.default_timer()-start
    return dt

if __name__ =="__main__":
    main()
