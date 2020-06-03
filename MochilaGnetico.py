import random
import argparse
import array
from math import ceil, log
import numpy as np
import datetime


items = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10),
    )


x_max = 400
x_min = 0
t_poblacion = 10
n_generaciones = 10
largoCrom = 22 


#Función para generar las posibles soluciones 
def poblacion_inicial(Tpo,TEle):
    poblacion = []
    for i in range(t_poblacion):
        individuo=[]
        for j in range (largoCrom):
            individuo.append(random.randint(0,1))
           # print (individuo)
        # print (individuo)
        poblacion.append(individuo)

    return poblacion


def fenotipo(genes):
  fen = []
  adp = []
  for i in genes:
    c=0
    pesoTotal = 0
    valorTotal = 0
    print(i)
    for e in i:
      if e == 1:
        pesoTotal=pesoTotal+items[c][1]
        valorTotal=valorTotal+items[c][2]
      c=c+1
    print("Fenotipo ", pesoTotal)
    print("adaptacion", valorTotal)
    fen.append(pesoTotal)
  return fen
 
    

def MetodoSeleccionElite(Tpo,poblacion):
    sel_super = []
    elites = []
    Tamañoelite = int(ceil(Tpo*2/100))
    print ("Tamaño de elite",Tamañoelite)
    #sel_elite[0 for i in range(0 , Tamañoelite)]
    #for i in range(0,Tpo):
     #   elites.append(False)

def Ruleta(poblacion):
    ValorAdaptacion=0
    print(poblacion_inicial)
    TotalIndividuos=len(poblacion_inicial)
    for i in range(TotalIndividuos):
        ValorAdaptacion+=poblacion[i].adaptacion
        print (ValorAdaptacion)        

def ProbabilidadCruce():
    Prob_cruce = 0.6
    prob_mutacion = 0.01
         


pobla = []
pobla = poblacion_inicial(t_poblacion,largoCrom)
F=fenotipo(pobla)
