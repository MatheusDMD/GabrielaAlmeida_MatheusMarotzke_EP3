# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:43:11 2015

Gabriela Almeida
Matheus Dias M.
"""
def HBH(p,h,i,f):
    HB = 88.36+(13.4*p)+(4.8*h)-(5.7*i)
    if f == 'grau mínimo' or f == 'mínimo' or f == 'minimo':
        HB*=1.2
    if f == 'baixo':
        HB*=1.375
    if f == 'média' or f == 'media':
        HB*=1.55
    if f == 'alto':
        HB*=1.725
    if f == 'muito alto':
        HB*=1.9
    return HB
    
def HBM(p,h,i,f):
    HB = 447.6+(9.2*p)+(3.1*h)-(4.3*i)
    if f == 'grau mínimo' or f == 'mínimo' or f == 'minimo':
        HB*=1.2
    if f == 'baixo':
        HB*=1.375
    if f == 'média' or f == 'media':
        HB*=1.55
    if f == 'alto':
        HB*=1.725
    if f == 'muito alto':
        HB*=1.9
    return HB
    
lista = []
c = open('usuario.csv')
b = open('alimentos.csv', encoding='latin1')
al = b.readlines()
us = c.readlines()
print(us)
for i in al:
    ali = i.strip().split(',')
    lista.append(ali)
lista.remove(lista[0])

l1 = [a[0] for a in lista]
l2 = [a[1:] for a in lista]

alimentos = dict(zip(l1,l2))


