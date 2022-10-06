def liste(k):
    L=[]
    u=1 # On initialise la suite avec la vaeur U0 = 1
    for i in range(0, k+1): 
        L.append(u)
        u = u / (1 + u)
    return(L)



liste(2)
