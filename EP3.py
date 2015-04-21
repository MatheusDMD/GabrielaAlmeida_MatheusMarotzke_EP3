# -*- coding: utf-8 -*-
"""
Gabriela Almeida
Matheus Dias M.
"""
from datetime import *

arquivo = open('imc.txt','w+',encoding = 'utf-8')

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

def IMC(n, p, h):
    IMC= p/(h**2) 
    
    if IMC<17:
        arquivo.write("Ola %s, seu IMC é %5.2f! Voce esta muito abaixo de peso" % (nome, IMC))
    elif IMC<18.49:
        arquivo.write("Ola %s, seu IMC é %5.2f! Voce esta Abaixo do peso" % (nome, IMC))
    elif IMC<24.99:
        arquivo.write("Ola %s, seu IMC é %5.2f! Voce esta com Peso normal" % (nome, IMC))
    elif IMC<29.99:
        arquivo.write("Ola %s, seu IMC é %5.2f! Voce esta Acima do Peso" % (nome, IMC))
    elif IMC<34.99:
        arquivo.write("Ola %s, seu IMC é %5.2f! Voce esta com Obesidade tipo I" % (nome, IMC))
    elif IMC<39.99:
        arquivo.write("Ola %s, seu IMC é %5.2f! Voce esta com Obesidade tipo II" % (nome, IMC))
    elif IMC>40:
        arquivo.write("Ola %s, seu IMC é %5.2f! Voce esta com Obesidade tipo III" % (nome, IMC))
    arquivo.close()
    
    
lista = []
lis = []
r = []
e = []
dias = []
data_comida_cal = {}
tdcal = []

b = open('alimentos.csv', encoding='latin1')
al = b.readlines()
for i in al:
    ali = i.strip().split(',')
    lista.append(ali)
lista.remove(lista[0])
l1 = [a[0] for a in lista]
l2 = [a[1:] for a in lista]
alimentos = dict(zip(l1,l2))

c = open('usuario.csv')
us = c.readlines()
for i in us:
    lis = i.strip().split(';')
    r.append(lis)
r.remove(r[0])
r.remove(r[1])

nome = r[0][0]
idade = float(r[0][1])
peso = float(r[0][2])
sexo = r[0][3]
altura = float(r[0][4])
fator = r[0][5]


x = HBM(peso,altura,idade,fator)

for i in range(1,len(r)):
    if r[i][0] not in data_comida_cal:
        data_comida_cal[r[i][0]] = [[r[i][1],r[i][2]]]
    else:
        data_comida_cal[r[i][0]].append([r[i][1],r[i][2]])

for i in data_comida_cal:
    total=0
    for j in data_comida_cal[i]:
        total+=(float(alimentos[j[0]][1])/float(alimentos[j[0]][0]))*float(j[1])
    data_comida_cal[i] = total

for i in data_comida_cal.keys():
    d1 = datetime.strptime(i, '%d/%m/%Y')
    dias.append(d1)
dias.sort()
print(dias)