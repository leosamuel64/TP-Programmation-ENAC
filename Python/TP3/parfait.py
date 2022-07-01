def est_parfait(n):
    i=2
    somme=1
    while i <= n**0.5:
        if n%i==0:
            somme+=i + n/i
        i+=1
    return somme==n


def est_premier(n):
    i=2
    premier=True
    while premier and i <= n**0.5:
        if n%i==0:
            premier=False
        else:
            i+=1
    return premier and n>1


# print(est_parfait(28))

def ensemble_nb_parfait(a,b):
    res=[]
    for i in range (a,b+1):
        if est_parfait(i):
            res.append(i)
    return res
        
# print(ensemble_nb_parfait(2,10000))


def parfait_puissance(nmax):
    res=[]
    for n in range(1,nmax+1):
        if est_premier(2**(n+1)-1):
            res.append((2**n)*(2**(n+1)-1))
    return res

print(parfait_puissance(29))
