import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy.linalg as linalg

data_file = pd.read_csv('signal.dat', sep='|')
data = pd.DataFrame(data_file)
time = data.iloc[:,1]
signal = data.iloc[:,2]

#part(a)
plt.scatter(time,signal)
plt.xlabel("time (s)")
plt.ylabel("signal (1)")
plt.title("Signal Versus Time")
plt.show()

#part(b)
A = np.zeros((len(time),4))
A[:,0] = 1.0
A[:,1] = time
A[:,2] = time**2
A[:,3] = time**3

(u,w,vt) = np.linalg.svd(A,full_matrices=False)
#notice we have 0 here for values of w, so we compute the inverse manually
winv = w
for i in range(4):
    if w[i]>=1.e-15:
        winv[i]=1.0/winv[i]
ainv= vt.transpose().dot(np.diag(winv)).dot(u.transpose())
c = ainv.dot(signal)
ym = A.dot(c)
plt.plot(time,signal,'.',label='data')
plt.plot(time,ym,'.',label='model')
plt.xlabel("Time (s)")
plt.ylabel("Signal (1)")
plt.title("SVD fitting of Data with polynomail of order 3")
plt.legend()
plt.show()
condition_number = max(winv)/np.min(winv[np.nonzero(winv)])
print(str(condition_number)+"for n=3")
    
#part(c)
residuals = (ym - signal)
plt.plot(time,residuals,'.',label='Residuals')
plt.plot(time,signal,'.',label='Data')
plt.xlabel("Time (s)")
plt.ylabel("Signal (1)")
plt.title("Data with Residuals for polynomials of order 3")
plt.legend()
plt.show()

#part(d)
#try a order 9 polynomial
A = np.zeros((len(time),10))
A[:,0]=1.0
A[:, 1] = time 
A[:, 2] = time**2
A[:, 3] = time**3
A[:, 4] = time**4
A[:, 5] = time**5
A[:, 6] = time**6
A[:, 7] = time**7
A[:, 8] = time**8
A[:, 9] = time**9

(u,w,vt) = np.linalg.svd(A,full_matrices=False)
winv = w
for i in range(10):
    if w[i]>=1.e-15:
        winv[i]=1.0/winv[i]
ainv= vt.transpose().dot(np.diag(winv)).dot(u.transpose())
c = ainv.dot(signal)
ym = A.dot(c)
plt.plot(time,signal,'.',label='data')
plt.plot(time,ym,'.',label='model')
plt.xlabel("Time (s)")
plt.ylabel("Signal (1)")
plt.title("SVD fitting of Data with polynomial of order 10")
plt.legend()
plt.show()

residuals = (ym - signal)
plt.plot(time,residuals,'.',label='Residuals')
plt.plot(time,signal,'.',label='Data')
plt.xlabel("Time (s)")
plt.ylabel("Signal (1)")
plt.title("Data with Residuals for polynomial of order 10")
plt.legend()
plt.show()

#condition number is defined by the ratio of the maximum to the non-zero minimum
condition_number = max(winv)/np.min(winv[np.nonzero(winv)])
print(str(condition_number)+"for n=10")

#part(e)
#fundamental frequency
freq = 1/(2*np.max(time))
#we use 12 harmonics here
N = 12
A = np.zeros((len(time),2*N+2))
A[:,0] = 1
for i in range(1,N+1):
    A[:,2*i] = np.cos(i*2*np.pi*freq*time)
    A[:,2*i-1] = np.sin(i*2*np.pi *freq*time)

(u,w,vt) = np.linalg.svd(A,full_matrices=False)
winv = w
for i in range(2*N+1):
    if w[i]>=1.e-15:
        winv[i]=1.0/winv[i]
ainv= vt.transpose().dot(np.diag(winv)).dot(u.transpose())
c = ainv.dot(signal)
ym = A.dot(c)
plt.plot(time,signal,'.',label='data')
plt.plot(time,ym,'.',label='model')
plt.xlabel("Time (s)")
plt.ylabel("Signal (1)")
plt.title("SVD fitting of Data for sin and cos")
plt.legend()
plt.show()

residuals = (ym - signal)
plt.plot(time,residuals,'.',label='Residuals')
plt.plot(time,signal,'.',label='Data')
plt.xlabel("Time (s)")
plt.ylabel("Signal (1)")
plt.title("Data with Residuals for sin and cos")
plt.legend()
plt.show()



