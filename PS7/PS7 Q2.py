import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

ages=np.array(np.loadtxt("survey.csv",skiprows=1,usecols=0,delimiter=","))
response=np.array(np.loadtxt("survey.csv",skiprows=1,usecols=1,delimiter=","))

def pmf(x,beta0,beta1):
    return 1/(1+np.exp(-(beta0+beta1*x)))

#add epsilon so to never take log to 0
eps=1.e-9
def likelihood(beta0,beta1,x,f):
    sum_of_prob=0
    for i in range(len(ages)):
        prob=f[i]*np.log(pmf(x[i],beta0,beta1)/(1-pmf(x[i],beta0,beta1))+eps)+np.log(1-pmf(x[i],beta0,beta1)+eps)
        sum_of_prob+=prob
    return sum_of_prob

beta=np.array([0.01,0.01])
result=optimize.minimize(lambda beta,ages,response:(-likelihood(beta[0],beta[1],ages,response)),beta,args=(ages,response))

covariance=result.hess_inv*result.fun/(len(ages))

error=np.sqrt(np.diag(covariance))

beta0,beta1=result.x
x=np.arange(1,max(ages))
plt.plot(x,pmf(x,beta0,beta1))

print(result.x)
print(error)
print(covariance)
plt.xlabel("Age (year)")
plt.ylabel("Response")
plt.title("Maximum Likelihood Data")
plt.show()


        
    
