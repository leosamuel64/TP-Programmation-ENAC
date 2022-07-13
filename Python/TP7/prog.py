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
        gcd = gcd1(a,b)
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

# print(fraction(4,8)+fraction(6,7))

# L=[fraction(8,(4*n+1)*(4*n+3)) for n in range(10001)]

def sum_rationals(l):
    somme=fraction(0,1)
    for frac in l:
        somme+=frac
    return somme

def sum_approximate(L):
    somme=0
    for frac in L:
        somme+=frac.approximate()
    return somme
        
# print(sum_rationals(L).approximate())

# print(sum_approximate(L))


class Inode:
    def __init__(self,n):
        """
        n doit être de type string
        """
        self.name=n
        self.path=""

    def full_path(self):
        return self.path+'/'+self.name
    
    def get_size(self):
        return 0
    
    def set_path(self,chaine):
        self.path=chaine
        
class File(Inode):
    def __init__(self,size,name):
        super().__init__(name)
        self.size=size
      
    def get_size(self):
        return self.size
    
    
# fichier=File(438,'source.list')

# print(File.full_path(fichier))

class Directory(Inode):
    def __init__(self, name):
        super().__init__(name)
        self.contents=[]
        
    def get_size(self):
        return sum([fichier.get_size() for fichier in self.contents])
    
    def add_inode(self, fichier):
        self.contents.append(fichier)
        fichier.set_path(self.full_path()+'/'+fichier.name)
        
    def set_path(self, chaine):
        for fichier in self.contents:
            fichier.path=chaine
        self.path=chaine
        
def type_fichier(fichier):
    try:
        fichier.contents
        return 'Directory'
    except:
        return 'File'            

                         
fichier1=File(438,'a')
fichier2=File(438,'b')

root=Directory('root')
home=Directory('home')
etc=Directory('etc')
apt=Directory('apt')
fichierSource=File(438,'source.list')
fichierImg=File(17*(10**6),'initrd.img')

apt.add_inode(fichierSource)
etc.add_inode(apt)
root.add_inode(home)
root.add_inode(etc)
root.add_inode(fichierImg)
