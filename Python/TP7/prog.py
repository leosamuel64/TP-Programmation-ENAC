# ---------- Q1 ----------

from tkinter import N


def gcd1(n1,n2):
    a,b=n1,n2
    while b>0:
        n1=b
        n2= a % b
        a=n1
        b=n2
    return a

# print(gcd1(1029,1071))

def gcd2(n1,n2):
    match (n1,n2):
        case (n,0):
            return n
        case (a,b):
            return gcd2(b,a%b)
        
# print(gcd2(1029,1071))

# ---------- Q2 ----------

def fact(n):
    if n in [0,1]:
        return 1
    else:
        return n*fact(n-1)
    
# print(fact(6))

# ---------- Q3 ----------

def precision(x,ε):
    return abs(x)<=ε

# ---------- Q4 ----------

def sqrt(x,ε):
    s=x/2
    e=(x-s**2)/(2*s)
    while not precision(e,ε):
        e=(x-s**2)/(2*s)
        s+=e
    return s

# print(sqrt(2,10**(-12)))
        
# ---------- Q5 ----------

def pi(ε):
    n=0
    ts=1/(2*(n+1)+1)
    somme=0
    signe=1
    while not precision(ts,ε):
        somme+=signe/(2*n+1)
        ts=1/(2*(n+1)+1)
        n+=1
        signe*=-1
    return 4*somme
        
# print(pi(10**(-6)))

# ---------- Classe fraction ----------

class fraction:
    def __init__(self,a,b):
        gcd = gcd2(a,b)
        self.numerator=a//gcd
        self.denominator=b//gcd
    def __repr__(self):
        return str(self.numerator)+'/'+str(self.denominator)
        
    def approximate(self):
        return self.numerator/self.denominator
    
    def __add__(self,other):
        n1,n2,d1,d2=self.numerator, other.numerator, self.denominator, other.denominator
        n1f=n1*d2
        d1f=d1*d2
        n2f=n2*d1
        return fraction(n1f+n2f,d1f)
    
api=fraction(104348,33215)
# print(api)

# print(fraction(6,8))
# print(fraction(6,8).approximate())

print(fraction(4,8)+fraction(6,7))






        
        



        
            


        
            

