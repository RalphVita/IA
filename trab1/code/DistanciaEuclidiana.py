import numpy as np

def SomaDistanciaEuclidia(X, centroide):
    return sum([np.linalg.norm(x-centroide) for x in X])

def SSE(groups):
    print(groups)
    return sum([SomaDistanciaEuclidia(g['X'],g['centroide']) for g in groups.values()])
        
def Centroide(X):
    return sum(X)/len(X)