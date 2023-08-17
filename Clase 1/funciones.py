#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:01:48 2023

@author: clinux01
"""

import numpy as np

A = np.array([[1,2],[3,4]])

def esCuadrada(B):
    nline,ncol = B.shape
    return nline == ncol

def traza(A):
    #Chequear que es cuadrada
    if esCuadrada(A):
        nline, ncol= A.shape
        tr = 0
        for i in range(nline):
            for j in range(ncol):
                if i == j:
                    tr = tr + A[i,j]
    else:
        print("La matriz no es cuadrada")
        tr = -9999
    return tr
    
def esSimetrica(A):
    nline, ncol = A.shape
    res = True
    if esCuadrada(A):
        for i in range(nline):
            for j in range(i+1,ncol):
                if A[i][j] != A[j][i]:
                    res = False
    else:
        print("La matriz no es cuadrada")
        res = False
    return res
                    