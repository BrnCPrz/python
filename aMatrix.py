############
# BuildAMatrix (built under Python 2.7)
# 
# A function to build a relationship matrix from a pedigree
#
# Pedigree file must be reordered and renumbered
#
# Missing parents must be coded zero (int 0)
#
# Adapted from Gota Morota's R function to build an A matrix
#
# Input - vector of sire ids 
#       - vector of dam ids
#
############


import numpy as np

def BuildAMatrix(sirev, damv):
        n = len(sirev)
        N = n + 1
        A = np.zeros((N, N))

        sirev[sirev == 0] = N
        damv[damv == 0] = N
        sirev[sirev !=0] -= 1
        damv[damv !=0] -= 1

        for a in range(0, n):
            A[a, a] = 1 + (A[sirev[a], damv[a]]) / 2
            for j in range(a + 1, n):
                if j > n:
                    pass
                A[a, j] = (A[a, sirev[j]] + A[a, damv[j]]) / 2
                A[j, a] = A[a, j]

        return A[0:n,0:n]
