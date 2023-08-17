#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:15:16 2023

@author: clinux01
"""

import funciones
import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B =  np.array([[1,1,5],[1,2,3],[5,3,4]])

print("Traza de A: ", funciones.traza(A))
print("Es simetrica?", funciones.esSimetrica(B))
print("Es simetrica?", funciones.esSimetrica(A))
