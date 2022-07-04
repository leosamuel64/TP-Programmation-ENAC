from ast import Try
from random import randint
import utils

def fibo(n):
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case n:
            return fibo(n-1)+fibo(n-2)
        
        
def somme_liste(l):
    match l:
        case []:
            return 0
        case [t,*q]:
            return t + somme_liste(q)
        
# print(somme_liste([1,2,3,4,5,6,7,8,9]))


# Tri Fusion avec des match

def divise_rec(l):
    match l:
        case []:
            return [],[]
        case [a]:
            return l,[]
        case [a,b,*c]:
            l1,l2=divise_rec(c)
            return [a,*l1],[b,*l2]
        
# print(divise([1,2,3,4,5,6]))

def fusion_rec(l1,l2):
    match l1,l2:
        case [],_:
            return l2
        case _,[]:
            return l1
        case [t1,*q1],[t2,*q2]:
            if t1<t2:
                return [t1,*fusion_rec(q1,l2)] 
            else:
                return [t2,*fusion_rec(l1,q2)]
            
# print(fusion([1,3,5,7],[2,4,6]))

def tri_fusion(l):
    match l:
        case []:
            return []
        case [a]:
            return l
        case _:
            l1,l2 = divise_rec(l)
            return fusion_rec(tri_fusion(l1),tri_fusion(l2))
        

def partition(t):
  return t[0:len(t)//2],t[len(t)//2:len(t)]

# print(partitionne([1,4,3,2,4]))

def fusion(t1,t2):
  if len(t1)==0:
    return t2
  elif len(t2)==0:
    return t1
  elif t1[0]<t2[0]:
    return [t1[0]]+fusion(t1[1:],t2)
  else:
    return [t2[0]]+fusion(t1,t2[1:])

def triFusion(t):
  if len(t)<=1:
    return t
  t1,t2=partition(t)
  return fusion(triFusion(t1),triFusion(t2))
# print(tri_fusion([1,7,3,5,2,8,4,6,2,7,3,7]))

def genere_liste(longueur):
    res=[]
    for i in range(longueur):
        res.append(randint(0,100))
    return res

def tri_fusion_1(l):
    res = genere_liste(l)
    return tri_fusion(res)

def tri_fusion_2(l):
    res = genere_liste(l)
    return triFusion(res)

def tri_timsort_l(l):
    res = genere_liste(l)
    return sorted(res)


# res=genere_liste(20)
# print(tri_fusion(res),sorted(res))

# print([genere_liste(i) for i in range(1000)])


# utils.compare_fonction([tri_fusion, triFusion, sorted],
#                        ["Tri fusion match","Tri fusion classique", "Tri timsort"],
#                        [genere_liste(i) for i in range(1,1000,100)],
#                        10
#                        )


class arbre_binaire():
    def __init__(self,filsg,valeur,filsd):
        self.valeur=valeur
        self.fg = filsg
        self.fd = filsd
    
    def __str__(self):
        fg=self.fg
        fd=self.fd
        v=self.valeur
        
        return '('+str(fg)+','+str(v)+','+str(fd)+')'
    
    def __add__(self,other):
        match (self.fg,self.valeur,self.fd),(other.fg,other.valeur,other.fd):
            case (None,a,None),(None,b,None):
                return arbre_binaire(None,a+b,None)
            case (fg1,a,fd1),(fg2,b,fd2):
                res=[]
                for f in [fg1,fd1,fg2,fd2]:
                    if f==None:
                        res.append(arbre_binaire(None,0,None))
                    else:
                        res.append(f)
                        
                return arbre_binaire(res[0]+res[1],a+b,res[2]+res[3])
    def __eq__(self, other):
        try:
            fg1,v1,fd1,fg2,v2,fd2 = self.fg,self.valeur,self.fd,other.fg,other.valeur,other.fd
            return v1==v2 and fg1==fg2 and fd1==fd2
        except:
            return False
        
    
          
    def profondeur(a):
        match (a.fg,a.valeur,a.fd):
            case (None,_,None):
                return 1
            case (None,_,fd):
                return 1+fd.profondeur()
            case (fg,_,None):
                return 1 + fg.profondeur()
            case (fg,_,fd):
                return max(1+fg.profondeur(),1+fd.profondeur())
            
    def est_complet(self):
        match (self.fg,self.valeur,self.fd):
            case (None,_,None):
                return True
            case (None,_,_):
                return False
            case (_,_,None):
                return False
            case(fg,_,fd):
                return (fg.est_complet() and fd.est_complet())
        
    
        

def arbre_alea_aux(ab,p,pmax=10,a=0,b=10):
    if p==pmax-1:
        return ab
    else:
        fg=arbre_binaire(None,randint(a,b),None)
        fd=arbre_binaire(None,randint(a,b),None)
        
    return arbre_binaire(arbre_alea_aux(fg,p+1,pmax,a,b),
                         ab.valeur,
                         arbre_alea_aux(fd,p+1,pmax,a,b)
                        ) 
    
def arbre_alea(pmax,a,b):
    return arbre_alea_aux(arbre_binaire(None,randint(a,b),None),0,pmax,a,b)
    
def liste_vers_arbre(l):
    match l:
        case []:
            return None
        case [t,*q]:
            return arbre_binaire(liste_vers_arbre(q[:len(q)//2]),t,liste_vers_arbre(q[len(q)//2:len(q)]))


def somme_valeurs_arbre2(a):
    match (a.fg,a.valeur,a.fd):
        case(None,v,None):
            return v
        case(fg,v,fd):
            return v + somme_valeurs_arbre2(fg) + somme_valeurs_arbre2(fd)
        


        
#                   ----- Test -----       

# a=arbre_alea(2,0,9)
a=liste_vers_arbre([1,2,3])
b=liste_vers_arbre([1,2])
# print(b.est_complet())
# print(b.est_complet())
# print((a+b).est_complet())
