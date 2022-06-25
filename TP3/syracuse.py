def temps_de_vol(u0):
    u=u0
    n=0
    while u>1:
        if u%2==0:
            u = u//2
        else:
            u = 3*u+1
        n+=1
    return n

# print(temps_de_vol(127))

def altitude_max(u0):
    u=u0
    maxi=u0
    while u>1:
        if u%2==0:
            u = u//2
        else:
            u = 3*u+1
        if u>maxi:
            maxi=u
    return maxi

# print(altitude_max(127))

def altitude_record(m):
    maxi=1
    res=1
    for u in range(1,m+1):
        altmax = altitude_max(u)
        if altmax>maxi:
            maxi=altmax
            res=u
    return res,maxi

# print(altitude_record(1000))