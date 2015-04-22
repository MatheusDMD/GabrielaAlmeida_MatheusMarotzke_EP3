# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:19:59 2015

@author: gabialmeida
"""
arquivo = open('imc.txt','w+',encoding = 'utf-8')

def HBH(p,h,i,f):
    HB = 88.36+(13.4*p)+(4.8*(h*100))-(5.7*i)
    if f == 'grau mínimo' or f == 'mínimo' or f == 'minimo':
        HB*=1.2
    if f == 'baixo':
        HB*=1.375
    if f == 'médio' or f == 'medio':
        HB*=1.55
    if f == 'alto':
        HB*=1.725
    if f == 'muito alto':
        HB*=1.9
    '''
    Calcula a "Energia de Repouso" de um homem
    >>> HBM(72,1.78,25,'médio')
    2735
    '''
    return HB
    
def HBM(p,h,i,f):
    HB = 447.6+(9.2*p)+(3.1*(h*100))-(4.3*i)
    if f == 'grau mínimo' or f == 'mínimo' or f == 'minimo':
        HB*=1.2
    if f == 'baixo':
        HB*=1.375
    if f == 'médio' or f == 'medio':
        HB*=1.55
    if f == 'alto':
        HB*=1.725
    if f == 'muito alto':
        HB*=1.9
    '''
    Calcula a "Energia de Repouso" de um homem
    >>> HBM(50,1.72,25,'alto')
    2299
    '''
    return HB