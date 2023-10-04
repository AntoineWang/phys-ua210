def f(x):
    return x**4 - 2*x +1

def integral(N):
    a = 0.0
    b = 2.0
    h = (b-a)/N

    s = 0.5*f(a) + 0.5*f(b)
    for k in range(1,N):
        s += f(a+k*h)

    return h*s

def main():
    int_10 = integral(10)
    print("the integral with 10 slices is " + str(int_10))
    int_20 = integral(20)
    print("the integral with 20 slices is " + str(int_20))
    error = abs((1/3)*(int_20 - int_10))
    error_real = abs(22/5 - int_10)
    print("the error with method 2.8 is " + str(error))
    print("the real error is " + str(error_real))

if __name__ == "__main__":
    main()
