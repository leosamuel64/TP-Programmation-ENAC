n=int(input("Saisir un nombre : "))
if n<2:
    flag= False
else:
    flag=True


i=2
premier=True
while premier and i <= n**0.5 and flag:
    if n%i==0:
        premier=False
    else:
        i+=1

        
if flag:
    if premier:
        print(n,' est premier')
    else:
        print(n," n'est pas premier")
else:
    print('Le nombre est strictement inférieur à 2')
