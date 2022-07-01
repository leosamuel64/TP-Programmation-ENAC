# a,b,c = int(input("valeur de a :")),int(input("valeur de b :")),int(input("valeur de c :"))

# if a ==0:
#     print('a doit être non-nul')
# else:
#     delta = b**2-4*a*c
#     if delta ==0:
#         print("Racine double :"+str(-b/(2*a)))
#     elif delta < 0:
#         print("Pas de racines réelles")
#     else:
#         print("il y a deux racines : " +
#                             str((-b+delta**(1/2))/(2*a)) + "et" +
#                             str((-b-delta**(1/2))/(2*a))
#             )  


def resEqua1(a,b,c):
    if a ==0:
        print('a doit être non-nul')
    else:
        delta = b**2-4*a*c
        if delta ==0:
            print("Racine double :"+str(-b/(2*a)))
        elif delta < 0:
            print("Pas de racines réelles")
        else:
            print("il y a deux racines : " +
                                str((-b+delta**(1/2))/(2*a)) + 
                                "et" +
                                str((-b-delta**(1/2))/(2*a))
                )  


def resEqua2(a,b,c):
    if a ==0:
        if b==0:
            if c==0:
                print("Tout x est solution")
            else:
                print("impossible")
        else:
            print("Une solution : "+str(-c/b))
    else:
        delta = b**2-4*a*c
        if delta ==0:
            print("Racine double :"+str(-b/(2*a)))
        elif delta < 0:
            print("Pas de racines réelles")
        else:
            print("il y a deux racines : " +
                                str((-b+delta**(1/2))/(2*a)) + 
                                "et" +
                                str((-b-delta**(1/2))/(2*a)))
                
resEqua2(0,0,0)