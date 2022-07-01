def affiche(p):
    print(' -'+('---'*len(p[0]))+'- ')
    for ligne in p:
        res="|  "
        for char in ligne:
            res+=char+'  '
        print(res+'|')
    print(' -'+('---'*len(p[0]))+'- ')
        
        
def est_sur_ligne(a,b):
    if a[0]==b[0] or a[1]==b[1]:
        return True 
    
    
def est_sur_diago(a,b):
    Δx=a[0]-b[0]
    Δy=a[1]-b[1]
    if abs(Δx)==abs(Δy):
        return True
    

def position(i,j):
    plateau=[['O' for _ in range(8)] for _ in range(8)]
    for x in range(len(plateau[0])):
        for y in range(len(plateau)):
            if est_sur_ligne((i,j),(x,y)):
                plateau[x][y]='X'
                
            if est_sur_diago((i,j),(x,y)):
                plateau[x][y]='X'
    plateau[i][j]='R'
    affiche(plateau)
    return plateau
    
position(4,2)