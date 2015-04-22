# -*- coding: utf-8 -*-
"""
Gabriela Almeida
Matheus Dias M.
"""
from datetime import *
import doctest
import matplotlib.pyplot as plt
from pylab import *

arquivo = open('imc.txt','w+',encoding = 'utf-8')

def HBH(p,h,i,f):
    HB = 88.36+(13.4*p)+(4.8*(h*100))-(5.7*i)
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
    '''
    Calcula a "Energia de Repouso" de um homem
    >>> HBM(72,1.78,25,'média')
    2735
    '''
    return HB
    
def HBM(p,h,i,f):
    HB = 447.6+(9.2*p)+(3.1*(h*100))-(4.3*i)
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
    '''
    Calcula a "Energia de Repouso" de um homem
    >>> HBM(50,1.72,25,'alto')
    2299
    '''
    return HB


def IMC(n, p, h):
    IMC= (1.3*p)/(h**2.5)
    
    if IMC<18.5:
        arquivo.write("Ola %s, seu IMC é %5.2f! Voce esta Abaixo do peso" % (nome, IMC))
    elif IMC<24.99:
        arquivo.write("Ola %s, seu IMC é %5.2f! Voce esta com Peso normal" % (nome, IMC))
    elif IMC<29.99:
        arquivo.write("Ola %s, seu IMC é %5.2f! Voce esta Acima do Peso" % (nome, IMC))
    elif IMC>30:
        arquivo.write("Ola %s, seu IMC é %5.2f! Voce esta Obeso" % (nome, IMC))
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

for i in range(1,len(r)):
    if r[i][0] not in data_comida_cal:
        data_comida_cal[r[i][0]] = [[r[i][1],r[i][2]]]
    else:
        data_comida_cal[r[i][0]].append([r[i][1],r[i][2]])

for i in data_comida_cal:
    total_cal=0
    total_prot=0
    total_carb=0
    total_gord=0
    for j in data_comida_cal[i]:
        total_cal+=(float(alimentos[j[0]][1])/float(alimentos[j[0]][0]))*float(j[1])
        total_prot+=(float(alimentos[j[0]][2])/float(alimentos[j[0]][0]))*float(j[1])
        total_carb+=(float(alimentos[j[0]][3])/float(alimentos[j[0]][0]))*float(j[1])
        total_gord+=(float(alimentos[j[0]][4])/float(alimentos[j[0]][0]))*float(j[1])
    data_comida_cal[i] = [total_cal,total_prot,total_carb,total_gord]

for i in data_comida_cal.keys():
    d1 = datetime.datetime.strptime(i, '%d/%m/%Y').strftime("%d/%m/%Y")
    dias.append(d1)
dias.sort()

cal_ordem = []
prot_ordem = []
carb_ordem = []
gord_ordem = []
for i in dias:
    cal_ordem.append(data_comida_cal[i][0])
    prot_ordem.append(data_comida_cal[i][1])
    carb_ordem.append(data_comida_cal[i][2])
    gord_ordem.append(data_comida_cal[i][3])

if sexo == 'M':
    kcal_esperado = HBM(peso,altura,idade,fator)
elif sexo == 'H':
    kcal_esperado = HBH(peso,altura,idade,fator)

dias_n = list(range(len(dias)))
lista_kcal_esperado = [kcal_esperado]*len(dias_n)

img = imread('diet.png')
imgplot = plt.imshow(img)
plt.axis('off')
plt.show()

plt.plot(dias_n, cal_ordem, 'b-')
plt.plot(dias_n, lista_kcal_esperado, 'r-')
plt.xlabel('dias da semana')
plt.ylabel('calorias[kcal]')
plt.title('Calorias da semana')   
plt.show()

plt.plot(dias_n, carb_ordem, 'r-')
plt.xlabel('dias da semana')
plt.ylabel('carboidratos [g]')
plt.title('Carboidratos da semana')  
plt.show()

plt.plot(dias_n, gord_ordem, 'y-')
plt.xlabel('dias da semana')
plt.ylabel('gorduras [g]')
plt.title('Gorduras da semana')  
plt.show()

plt.plot(dias_n, prot_ordem, 'g-')
plt.xlabel('dias da semana')
plt.ylabel('proteinas [g]')
plt.title('Proteinas da semana')  
plt.show()

IMC(nome,peso, altura)

