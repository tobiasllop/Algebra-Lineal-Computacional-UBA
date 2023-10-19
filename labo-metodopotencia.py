#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:38:50 2023

@author: El tobe
"""
import numpy as np

A = np.array([[-6, 9, 3],
             [0, 8, -2],
             [0, -1, 7]])

B = np.array([[5, 9, 6],
              [-3, -7, -6],
              [0, 0, -1]])


lambdasA, vA = np.linalg.eig(A)
print("avals A\n", lambdasA)
print("avecs A\n", vA)

lambdasB, vB = np.linalg.eig(B)
print("avals B\n", lambdasB)
print("avecs B\n", vB)


def metodo_potencia(A, x0):
    x = x0
    r_ant = 0
    while True:
        x_nuevo = (A @ x) / np.linalg.norm(A @ x)
        r_actual = x_nuevo @ A @ x_nuevo
        if np.abs(r_actual - r_ant) < 1e-8:
            break
        x = x_nuevo
        r_ant = r_actual
    return x, r_actual



x0 = np.random.rand(3)

#Ejecutamos el metodo de la potencia para A
resultadoA, autovalorA = metodo_potencia(A, x0)
print("Autovector:", resultadoA)
print("Autovalor mas grande:", autovalorA)

#Ejecutamos el metodo de la potencia para B
resultadoB, autovalorB = metodo_potencia(B, x0)
print("Autovector:", resultadoB)
print("Autovalor mas grande:", autovalorB)