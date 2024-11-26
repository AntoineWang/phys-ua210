import astropy.io.fits as fit
import numpy as np
import matplotlib.pyplot as plt
import timeit

hdu_list = fit.open('/Users/antoine/Desktop/nyu/Computational Physics/Problem Set 6/specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data

#(a)
plt.plot(logwave,flux[0,:],label="1st galaxy")
plt.plot(logwave,flux[1,:],label="2nd galaxy")
plt.plot(logwave,flux[2,:],label="3rd galaxy")
plt.plot(logwave,flux[3,:],label="4th galaxy")
plt.plot(logwave,flux[4,:],label="5th galaxy")
plt.xlabel("Wavelength (Angstrom)")
plt.ylabel("Flux (10^_17 erg s^-1 cm^-2 Angstrom^-1")
plt.legend(loc="best")
#plt.show()

#(b)
flux_sum = np.sum(flux,axis=0)
flux_normalized = flux/flux_sum

#(c)
flux_mean = np.mean(flux_normalized,axis = 0)
residuals = flux_normalized - flux_mean

#(d) calculating PCA
start=timeit.default_timer()
residuals_T = np.transpose(residuals)
c_matrix = residuals_T.dot(residuals)
eigval,eigvec = np.linalg.eig(c_matrix)
dt_1 = timeit.default_timer()-start
eig_labels = ["1st eigenvecotr","2nd eigenvector","3rd eigenvector",
          "4th eigenvector","5th eigenvector"]
for i in range(5):
    plt.plot(eigvec[i,:],label = eig_labels[i])
    plt.legend(loc="best")
plt.title("eigenvectors calculated from covariance matrix")
#plt.show()

#(e)
start=timeit.default_timer()
(u,w,vt) = np.linalg.svd(residuals)
v = np.transpose(vt)
dt_2=timeit.default_timer()-start
for i in range(5):
    plt.plot(v[i,:],label = eig_labels[i])
    plt.legend(loc="best")
plt.title("eigenvectors calculated from SVD")
#plt.show()

print("The time it took for covariance matrix is "+str(dt_1)+"s and "
      +str(dt_2)+"s for SVD")

c_number_matrix = np.max(eigval)/np.min(eigval[np.nonzero(eigval)])
c_number_svd = np.max(w)/np.min(w[np.nonzero(w)])
print(c_number_matrix,c_number_svd)

