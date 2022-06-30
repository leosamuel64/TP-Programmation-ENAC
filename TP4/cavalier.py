def affiche(p):
    print(' -'+('---'*len(p[0]))+'- ')
    for ligne in p:
        res="|  "
        for char in ligne:
            res+=str(char)+'  '
        print(res+'|')
    print(' -'+('---'*len(p[0]))+'- ')

def cases_accessibles(X):
    '''
    Renvoie la liste des cases accessibles
    '''
    x,y=X
    res=[]
    l=[(x-1,y-2),(x+1,y-2),(x-1,y+2),(x+1,y+2),(x-2,y-1),(x-2,y+1),(x+2,y-1),(x+2,y+1)]
    for (i,j) in l:
        if i<8 and i>=0 and j<8 and j>=0:
            res.append((i,j))
    return res

def explore(deja_vues, pos, board,tour):
    if len(deja_vues)==64:
        return True
    else:
        if pos not in deja_vues:
            deja_vues.append(pos)
            board[pos[0]][pos[1]]=tour
            tour+=1
            a_visiter=cases_accessibles(pos)
            if len(a_visiter)==0:
                return False
            res=False
            for noeud in a_visiter:
                res= res or explore(deja_vues,noeud,board,tour)
            return res
        else:
            return False
    
board=[['X' for _ in range(8)] for _ in range(8)]
print(explore([],(5,5),board,0))
affiche(board)
    