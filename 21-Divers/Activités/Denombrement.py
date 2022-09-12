

def Digits(N, S, E, K):
    CR =0
    V = S
    while( (V <= E) and (V <= N)):
        CR += K
        V += 1
    return V, CR

    
def DenBoucle(N):   
    N =  int(N)
    if(N <= 0): return 0 
    i  = 0
    CR =0
    VX =0
    S= [[0,9],[10,99],[100,999],[1000,9999],[10000, 99999],[100000,999999]]
    while( S[i][0] < N):
        VX, CX = Digits(N, S[i][0], S[i][1], i+1)
        CR += CX
        i += 1
        if( S[i-1][0] < S[i][0]):
            pass
            #print("CR {} = {}".format(i, CR))
    return CR-1 


def DenExplicite(N, ex):  
    N =  int(N)
    if(N <= 0): return 0 
    D  = int(10**(ex-1))
    Q  = (N - D)+1
    CR = int(Q*ex)
    if ( Q > 0):
        S = DenExplice(N-Q, ex-1)
    else:
        S= 0
    #print("CR {}) =  {}".format(ex, CR))
    CR += S
    return CR

def DenExplicite2(N):
    N =  int(N)
    if(N <= 0): return 0
    
    ex = len(str(N))   
    D  = int(10**(ex-1))
    Q  = (N - D)+1
    CR = int(Q*ex)
    if ( Q > 0):
        S = DenExplicite2(N-Q)
    else:
        S= 0
    CR += S
    return CR


N= 2021
CR= DenExplicite2(N)
print("Pour écrire de 1 à {}, on a besoin de {} chiffre(s).".format(N, CR))




