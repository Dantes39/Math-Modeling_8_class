import numpy as np
def massiv(A):
    S=1
    for i in np.arange(0,len(A),1):
        S = S*A[i]
    print(S)
    A=[1,2,3,4]
massiv(A)