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


utils.compare_fonction([tri_fusion, triFusion, sorted],
                       ["Tri fusion match","Tri fusion classique", "Tri timsort"],
                       [genere_liste(i) for i in range(1,1000,100)],
                       10
                       )
