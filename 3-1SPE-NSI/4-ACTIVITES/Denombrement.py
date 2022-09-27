def CRCount(N):
    N =  int(N)
    if(N <= 0): return 0
    
    ex = len(str(N))   
    D  = int(10**(ex-1))
    Q  = (N - D)+1
    CR = int(Q*ex)
    if ( Q > 0):
        S = CRCount(N-Q)
    else:
        S= 0
    CR += S
    return CR


N= 2021
CR= CRCount(N)
print("Pour écrire de 1 à {}, on a besoin de {} chiffre(s).".format(N, CR))




