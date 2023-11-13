import numpy as np
from scipy import optimize

func = lambda x: (x-0.3)**2*np.exp(x)
    
def brent(func,astart,bstart,tol=1.e-9,eps=1.e-7):
    #the first condition is not applicable to this problem
    #if func(astart)*func(bstart)>=0:
        #print("aha")
        #return
    
    if abs(func(astart))<abs(func(bstart)):
        temp=astart
        astart=bstart
        bstart=temp

    cstart = astart
    mflag = True  #set this condition to be tested later

    while (func(bstart)<tol or abs(bstart-astart)<tol)==False:
        if func(astart)!=func(cstart) or func(bstart)!=func(cstart):
            #let n denote numerators and d denote denominators
            #inverse quadratic interpolation
            n1=astart*func(bstart)*func(cstart)
            d1=(func(astart)-func(bstart))*(func(astart)-func(cstart))
            if d1==0:
                d1=eps #avoid division by 0
            n2=bstart*func(astart)*func(cstart)
            d2=(func(bstart)-func(astart))*(func(bstart)-func(cstart))
            if d2==0:
                d2=eps #avoid division by 0
            n3=cstart*func(astart)*func(bstart)
            d3=(func(cstart)-func(astart))*(func(cstart)-func(bstart))
            if d3==0:
                d3=eps #avoid division by 0
            s=n1/d1+n2/d2+n3/d3
        else:
            #secant method
            s=bstart-func(bstart)*(bstart-astart)/(func(bstart)-func(astart))
            
        #set conditions to check later
        cond1=(s<(3*astart+bstart)/4 and s<bstart) or (s>(3*astart+bstart)/4 and s>bstart)
        cond2=((mflag==True) and abs(s-bstart)>=abs((bstart-cstart)/2))
        cond3=((mflag==False) and abs(s-bstart)>=abs((cstart-dstart)/2))
        cond4=((mflag==True) and abs(bstart-cstart)<abs(tol))
        cond5=((mflag==False) and abs(cstart-dstart)<abs(tol))
        if cond1 or cond2 or cond3 or cond4 or cond5:
            #use bisection method
            s=(astart+bstart)/2
            mflag=True
        else:
            mflag=False

        dstart=cstart #define dstart for the first time
        cstart=bstart

        if func(astart)*func(s)<0:
            bstart=s
        else:
            astart=s

        if abs(func(astart))<abs(func(bstart)):
            temp=astart
            astart=bstart
            bstart=temp
            
    return bstart

root_b = brent(func,-1.,5)
root_scipy = optimize.brent(func,brack=(-0.5,3))
print(root_b)
print(root_scipy)

        
        
            
