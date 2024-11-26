import math

def method_a(a,b,c):
    if b**2-4*a*c<0:
        raise Exception("please input a quadratic equation that has"
                        "real solutions.")
    else:
        d=math.sqrt(b**2-4*a*c)
        x_1=(-b+d)/(2*a)
        x_2=(-b-d)/(2*a)
        return x_1,x_2

def method_b(a,b,c):
    if b**2-4*a*c<0:
        raise Exception("please input a quadratic equation that has"
                        "real solutions.")
    else:
        d=math.sqrt(b**2-4*a*c)
        x_1=(2*c)/((-b)-d)
        x_2=(2*c)/((-b)+d)
        return x_1,x_2

def method_c(a,b,c):
    if b**2-4*a*c<0:
        raise Exception("please input a quadratic equation that has"
                        "real solutions.")
    else:
        d=math.sqrt(b**2-4*a*c)
        x_1=(-b+d)/(2*a)
        x_2=(2*c)/((-b)+d)
        return x_1,x_2
def main():
    print(method_a(0.001,1000,0.001))
    print(method_b(0.001,1000,0.001))
    print("I noticed that in method a, the first solution is more accurate"
      "and in method b, the second solution is more accurate."
      "Since b is much greater than a and c, it dwarfs the 4ac term in the"
      "discriminant. Therefore in method a the numerator is essentially -b plus"
      "or minus another b term. When it's -b-b, it's very inaccurate because"
      "the denominator is so small in comparison. That's why the first solution"
      "is more accurate in method a. In method b, it's the same reasoning.")
    print(method_c(0.001,1000,0.001))
    

      
