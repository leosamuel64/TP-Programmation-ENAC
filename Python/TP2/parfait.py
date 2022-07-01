n=int(input("Saisir un nombre : "))
if n<2:
    flag= False
else:
    flag=True
i=2
somme=1
while i <= n**0.5 and flag:
    if n%i==0:
        somme+=i + n/i
    i+=1
    
if somme==n and flag:
    print(n," est parfait")
elif flag:
    print(n," n'est pas parfait")
else:
    print('Le nombre est strictement inférieur à 2')
    
