# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 10:26:53 2020

@author: Erik_Souza
"""

# Funções do REO1 - Avanços científicos em genética e melhoramento de plantas
import numpy as np
import random

def amostrar(vetor,tamanho_amostra = None,numero_amostragens = None):
    vetor = list(vetor)
    if tamanho_amostra == None:
        tamanho_amostra = len(vetor)
    else:
        tamanho_amostra = tamanho_amostra

    print('Vetor: ' +str(vetor))
    print('Tamanho da Amostra: ' + str(tamanho_amostra))

    somador = 0
    it = 0
    matriz_resultado = np.zeros((numero_amostragens,6))
    for i in np.arange(0,numero_amostragens,1):
        print(
            '-----------------------------------------------------------------------------------------------------------------')
        it += 1  # it = it+1
        print('Amostragem: ' + str(it))
        print('Vetor: ' + str(vetor))
        print('Tamanho da Amostra: ' + str(tamanho_amostra))

        matriz_resultado[i,0] = it

        amostra = random.sample(vetor, tamanho_amostra)
        #if len(amostra)<=10:
        print('Amostra:'+str(amostra))
        #else:
        #print('Amostra: '+str(amostra[:,3],'..., '+str(amostra[-1]))

        u = np.mean(amostra)
        matriz_resultado[i, 1] = u

        va = np.var(amostra)
        matriz_resultado[i, 2] = va

        mx = np.max(amostra)
        matriz_resultado[i, 3] = mx

        mn = np.min(amostra)
        matriz_resultado[i, 4] = mn

        amp = mx-mn
        matriz_resultado[i, 5] = amp

        print('Média: ' + str(u))
        print('Variância: ' + str(va))
        #print('Máximo: ' + str(mx))
        #print('Minimo: ' + str(mn))
        #print('Amplitude: ' + str(amp))


    return matriz_resultado
    