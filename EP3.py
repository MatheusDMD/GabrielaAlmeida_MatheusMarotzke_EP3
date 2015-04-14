# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:43:11 2015

Gabriela Almeida
Matheus Dias M.
"""
lista = []
b = open('alimentos.csv', encoding='latin1')
al = b.readlines()

for i in al:
    ali = i.strip().split(',')
    lista.append(ali)
lista.remove(lista[0])

l1 = [a[0] for a in lista]
l2 = [a[1:] for a in lista]

alimentos = dict(zip(l1,l2))
print(alimentos)
