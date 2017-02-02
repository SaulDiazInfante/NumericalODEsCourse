# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 19:14:21 2016

@author: lsanc_000
"""
import numpy as np

n = raw_input('Ingresar un entero positivo: ')
n = int(n)

Primos = np.ones(n+1)

for i in range(2, n+1):
    for j in range(2*i, n+1, i):
        Primos[j] = 0
    if Primos[i]:
        print i
