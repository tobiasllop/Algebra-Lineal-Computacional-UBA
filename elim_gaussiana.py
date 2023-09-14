#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
#Ejercicio 3
#a)
def ly(l, y):
    b = np.zeros((l.shape[0],1))
    for j in range(l.shape[0]):
        for i in range(j+1):
            b[j] += y[i][0] * l[j][i]  
    return b     

mat_triang_inf = np.array([[1, 0 , 0],
                           [2, 3 , 1],
                           [1, 2, 3]])

y = np.array([[1],
             [1],
             [1]])

print(ly(mat_triang_inf, y))

#b)
def ux(u, x):
    y = np.zeros((u.shape[0],1))
    for j in range(u.shape[0]):
        for i in range(j, u.shape[1]):
            y[j] += x[i][0] * u[j][i]  
    return y     

mat_triang_sup = np.array([[1, 2, 3],
                           [0, 3 , 1],
                           [0, 0 , 1]])

x = np.array([[1],
             [1],
             [1]])

print(ux(mat_triang_sup, x))

#EJercicio 4
#a)
def lu(m):
    res = m.copy()
    for i in range(m.shape[0]):
        for j in range(i):
            res[i][j] = m[i][j] + hallark(m[i,j]) * m[j][j] 

def hallark(n):
       


"""
Eliminacion Gausianna
"""
import numpy as np

def elim_gaussiana(A):
    cant_op = 0
    m=A.¨shape[0]
    n=A.shape[1]
    Ac = A.copy()
    
    if m!=n:
        print('Matriz no cuadrada')
        return
    
    ## desde aqui -- CODIGO A COMPLETAR





                
    ## hasta aqui
            
    L = np.tril(Ac,-1) + np.eye(A.shape[0]) 
    U = np.triu(Ac)
    
    return L, U, cant_op


def main():
    n = 7
    B = np.eye(n) - np.tril(np.ones((n,n)),-1) 
    B[:n,n-1] = 1
    print('Matriz B \n', B)
    
    L,U,cant_oper = elim_gaussiana(B)
    
    print('Matriz L \n', L)
    print('Matriz U \n', U)
    print('Cantidad de operaciones: ', cant_oper)
    print('B=LU? ' , 'Si!' if np.allclose(np.linalg.norm(B - L@U, 1), 0) else 'No!')
    print('Norma infinito de U: ', np.max(np.sum(np.abs(U), axis=1)) )

if __name__ == "__main__":
    main()
    
    