import numpy as np
import matplotlib.pyplot as plt

def main():
    N=100
    x=np.linspace(-2,2,num=N)
    y=np.linspace(-2,2,num=N)

    c=x[:,np.newaxis]+1j*y

    grid=np.zeros((N,N)) #2d array
    for row in range(N):
        for col in range(N):
            z=0 #this is the value we're starting with
            n=0
            this_c=c[row,col]
            while n<100:
                z=np.real(z**2)+1j*(np.imag(z**2))+np.real(this_c)+1j*(np.imag(this_c))
                size=abs(z)
                n+=1
                if size>2:
                    grid[col,row]=n
                    n=101
    plt.imshow(grid)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.jet()
    plt.colorbar(label="n")
    plt.savefig("Mandlebrot.png")

main()


        
        


    
