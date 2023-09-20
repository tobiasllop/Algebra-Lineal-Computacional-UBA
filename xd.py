#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

A = np.array([[4, 2, -2],
              [2, 5, 5],
              [-2, 5, 11]])

def descompLU(A):
    n = A.shape[0]
    A_moño = np.zeros((n,n))
    
    if n == 1:
        return np.array([[1]]), A.copy()
    
    L, U = descompLU(A)
    
    while n >= 2:
        for i in range(1, n):
            A_moño[0][0] = A[0][0]
            A_moño[0][n] = A[0][n]
            ´
    
    
    
