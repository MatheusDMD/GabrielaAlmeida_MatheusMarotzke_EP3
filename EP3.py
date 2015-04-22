# -*- coding: utf-8 -*-
"""
Gabriela Almeida
Matheus Dias M.
"""
from datetime import *
import doctest
import matplotlib.pyplot as plt
from pylab import *
from Funcoes import *

def IMC(n, p, h):
    IMC= (1.3*p)/(h**2.5) #calcula IMC
    
    if IMC<18.5:
        arquivo.write("Ola %s, seu IMC é %5.2f! Voce esta Abaixo do peso \n" % (nome, IMC))
    elif IMC<24.99:
        arquivo.write("Ola %s, seu IMC é %5.2f! Voce esta com Peso normal \n" % (nome, IMC))
    elif IMC<29.99:
        arquivo.write("Ola %s, seu IMC é %5.2f! Voce esta Acima do Peso \n" % (nome, IMC))
    elif IMC>30:
        arquivo.write("Ola %s, seu IMC é %5.2f! Voce esta Obeso \n" % (nome, IMC))

arquivo = open('imc.txt','w+',encoding = 'utf-8') #Abre um arquivo como IMC calculado
    
lista = [] #cria lista vazia
lis = []
delta_cal=[]
r = [] # leitura do arquivo "usuario"
dias = [] #cria lista para colocar dias
data_comida_cal = {} # cria dicionario vazio

b = open('alimentos.csv', encoding='latin1')
al = b.readlines() 
for i in al: #cria lista de alimentos
    ali = i.strip().split(',') 
    lista.append(ali)
lista.remove(lista[0])
l1 = [a[0] for a in lista]
l2 = [a[1:] for a in lista]
alimentos = dict(zip(l1,l2)) #cria o dicionario dos alimentos e suas respectivas informacoes

c = open('usuario.csv')
us = c.readlines()
for i in us:
    lis = i.strip().split(';')
    r.append(lis)
r.remove(r[0])
r.remove(r[1])

nome = r[0][0] #coleta dados do usuario
idade = float(r[0][1])
peso = float(r[0][2])
sexo = r[0][3]
altura = float(r[0][4])
fator = r[0][5]

for i in range(1,len(r)): #cria dicionario com datas e suas respectivas informacoes
    if r[i][0] not in data_comida_cal:
        data_comida_cal[r[i][0]] = [[r[i][1],r[i][2]]]
    else:
        data_comida_cal[r[i][0]].append([r[i][1],r[i][2]])

for i in data_comida_cal:#calcula informacoes do usuario
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

for i in data_comida_cal.keys(): #coleta as datas das keys e as tranforma em datetime para ordena-los
    d1 = datetime.datetime.strptime(i, '%d/%m/%Y').strftime("%d/%m/%Y")
    dias.append(d1)
dias.sort()

cal_ordem = []
prot_ordem = []
carb_ordem = []
gord_ordem = []
for i in dias: #adiciona as informacoes ao dicionario data_comida_cal
    cal_ordem.append(data_comida_cal[i][0])
    prot_ordem.append(data_comida_cal[i][1])
    carb_ordem.append(data_comida_cal[i][2])
    gord_ordem.append(data_comida_cal[i][3])

if sexo == 'M':
    kcal_esperado = HBM(peso,altura,idade,fator)
elif sexo == 'H':
    kcal_esperado = HBH(peso,altura,idade,fator)

dias_n = list(range((len(dias)-7), len(dias)))
dias_n = list(range(len(dias_n)))
cals_ordem = cal_ordem[(len(cal_ordem)-7):]
carbs_ordem =carb_ordem[(len(carb_ordem)-7):]
prots_ordem= prot_ordem[(len(prot_ordem)-7):]
gords_ordem= gord_ordem[(len(gord_ordem)-7):]
lista_kcal_esperado = [kcal_esperado]*len(dias_n)

img = imread('diet.png') #plota o logo
imgplot = plt.imshow(img)
plt.axis('off')
plt.show()

plt.plot(dias_n, cals_ordem)
plt.plot(dias_n, lista_kcal_esperado)
plt.plot(dias_n, cals_ordem, 'b', label='Calorias consumidas')
plt.plot(dias_n, lista_kcal_esperado, 'r', label='Calorias ideas')
plt.xlabel('dias da semana')
plt.ylabel('calorias[kcal]')
plt.title('Calorias da semana') 
plt.legend(loc="center right") 
plt.show()

plt.plot(dias_n, carbs_ordem, 'r-')
plt.xlabel('dias da semana')
plt.ylabel('carboidratos [g]')
plt.title('Carboidratos da semana')  
plt.show()

plt.plot(dias_n, gords_ordem, 'y-')
plt.xlabel('dias da semana')
plt.ylabel('gorduras [g]')
plt.title('Gorduras da semana')  
plt.show()

plt.plot(dias_n, prots_ordem, 'g-')
plt.xlabel('dias da semana')
plt.ylabel('proteinas [g]')
plt.title('Proteinas da semana')  
plt.show()

plt.plot(dias_n, carbs_ordem, dias_n, gords_ordem, dias_n, prots_ordem)
plt.ylabel('gramas [g]')
plt.xlabel('dias da semana')
plt.plot(dias_n, carbs_ordem, 'r', label='carboidrato')
plt.plot(dias_n, gords_ordem, 'y', label='gordura')
plt.plot(dias_n, prots_ordem, 'g', label='proteina')
plt.title('Carboidratos, gorduras e proteinas')
plt.legend(loc="upper left")
plt.show()

IMC(nome,peso, altura)

for i in range (len(cal_ordem)):
    delta_cal.append(int(kcal_esperado)-int(cal_ordem[i]))
    if cal_ordem[i] > kcal_esperado:
        arquivo.write('\n Voce ingeriu %d a mais do que o ideal, no dia %s \n' %(delta_cal[i],dias[i]))
    else:
        arquivo.write('\n Voce ingeriu %d a menos do que o ideal, no dia %s \n' %(delta_cal[i],dias[i]))
arquivo.close()
