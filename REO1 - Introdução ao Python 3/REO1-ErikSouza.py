#!/usr/bin/env python
# coding: utf-8

# Esse script é o produto do REO1 - Lista de exercícios - da disciplina de Avanços em Genética e Melhoramento de Plantas (PGM848) do Período letivo 2020/1.
# Para mais informações, acesse:
#     https://github.com/VQCarneiro/Visao-Computacional-no-Melhoramento-de-Plantas

#                                 UNIVERSIDADE FEDERAL DE LAVRAS - UFLA
#                                     DEPARTAMENTO DE BIOLOGIA - DBI
#                         PROGRAMA DE PÓS-GRADUÇÃO EM GENÉTICA E MELHORAMENTO DE PLANTAS
#                 DISCIPLINA PGM848 - AVANÇOS CIENTÍFICOS EM GENÉTICA E MELHORAMENTO DE PLANTAS
#                                 DOCENTE DSc. VINÍCIUS QUINTÃO CARNEIRO
#                                  DISCENTE ERIK MICAEL DA SILVA SOUZA
#                                     REO1 - INTRODUÇÃO AO PYTHON 3
# 
#                                         LISTA DE EXERCÍCIOS

# Obs.: Importar as bibliotecas necessárias para resolução desta lista de exercícios: numpy, math & matplotlib.

# In[104]:


import numpy as np
import math
import matplotlib.pyplot as plt


# **EXERCÍCIO 01:**
# 
# **a) Declare os valores 43.5, 150.30, 17, 28, 35, 79, 20, 99.07, 15 como um array numpy.**

# In[105]:


array_1a = np.array([43.5, 150.30, 17, 28, 35, 79, 20, 99.07, 15])
print('Resposta:')
print('O meu vetor 1a é composto por {}.' .format(array_1a))


# **b) Obtenha as informações de dimensão, média, máximo, mínimo e variância deste vetor.**

# In[106]:


dim_1a = len(array_1a)
mean_1a = np.mean(array_1a)
max_1a = max(array_1a)
min_1a = min(array_1a)
var_1a = np.var(array_1a)
print('Resposta:')
print('Este é um vetor com {} elementos (dimensão), com média igual a {} e com valores de máximo e minímo iguais a {} e {}, respectivamente. Este vetor também apresenta  uma variância igual a {}.'.format(dim_1a, np.around(mean_1a, 2), max_1a, min_1a, np.around(var_1a, 2)))


# **c) Obtenha um novo vetor em que cada elemento é dado pelo quadrado da diferença entre cada elemento do vetor declarado na letra a e o valor1 da média deste.**

# In[107]:


array_1c = (array_1a - mean_1a)**2
print('Resposta:')
print('O novo vetor ou vetor 1c é composto por {}.'.format(np.around(array_1c,3)))


# **d) Obtenha um novo vetor que contenha todos os valores superiores a 30.**

# In[108]:


maiorq30 = array_1a > 30
array_1d = array_1a[maiorq30] #Filtrar os valores superiores a 30 do vetor 1a.
print('Resposta:')
print('O novo vetor apresenta os valores superiores a 30 do vetor 1a e é composto por {}.'.format(array_1d))


# **e) Identifique quais as posições do vetor original possuem valores superiores a 30.**

# In[109]:


pos_maiorq30 = np.where(array_1a > 30)
print('Resposta:')
print('As posições do valores superiores a 30 no vetor 1a são {}'.format(pos_maiorq30))


# **f) Apresente um vetor que contenha os valores da primeira, quinta e última posição.**

# In[110]:


array_1f = [array_1a[0], array_1a[4], array_1a[-1]] #A base será o vetor 1a
print('Resposta:')
print('O vetor 1f apresenta valores dos elementos da primeira, quinta e última posição do vetor 1a, respectivamente, e é composto por {}' .format(array_1f))


# **g) Crie uma estrutura de repetição usando o for para apresentar cada valor e a sua respectiva posição durante as iterações.**

# In[111]:


print('Resposta:')
it = 0
for i in range(0, len(array_1a), 1): #O total de interações corresponde a dimensão do vetor.
    it = it + 1
    print('Iteração {}'.format(it))
    print('O valor {} encontra-se na posição {}.'.format(array_1a[i],i+1))


# **h) Crie uma estrutura de repetição usando o for para fazer a soma dos quadrados de cada valor do vetor.**

# In[112]:


print('Resposta:')
it = 0
for i in range(0, len(array_1a)):
    it = it + 1
    print('Iteração {}'.format(it))
    print('A soma de quadrados do valor da posição {} do vetor 1a é igual a: {}'.format(i+1,np.around(sum(array_1a[:i+1]**2), 2)))


# **i) Crie uma estrutura de repetição usando o while para apresentar todos os valores do vetor.**

# In[113]:


print('Resposta:')
pos = 0
while array_1a[pos] != 100:
    print('O elemento na posição {} é igual a {}.' .format(pos+1,array_1a[pos]))
    pos = pos+1
    if pos == len(array_1a):
        break


# **j) Crie um sequência de valores com mesmo tamanho do vetor original e que inicie em 1 e o passo seja também 1.**

# In[114]:


seq = range(1, len(array_1a)+1, 1)
array_1j = np.array(seq)
print('Resposta:')
print('A sequência de valores é {}.'.format(array_1j))


# **h) Concatene o vetor da letra a com o vetor da letra j.**

# In[115]:


array_1h = np.concatenate((array_1a, array_1j))
print('Resposta:')
print('Vetor da letra a com o vetor da letra j é composto por {}.'.format(array_1h))


# **EXERCÍCIO 02:**
# 
# **a) Declare a matriz abaixo com a biblioteca numpy.**

# In[116]:


array_2a = np.array([[1, 3, 22], [2, 8, 18], [3, 4, 22], [4, 1, 23], [5, 2, 52], [6, 2, 18], [7, 2, 25]])
print('Resposta:')
print('A matriz:')
print(array_2a)


# **b) Obtenha o número de linhas e de colunas desta matriz.**

# In[117]:


nlinhas,ncolunas = np.shape(array_2a)
print('Resposta:')
print('A matriz deste apresenta {} linhas e {} colunas, isto é, uma matriz {}x{}.'.format(nlinhas, ncolunas, nlinhas, ncolunas))


# **c) Obtenha as médias das colunas 2 e 3.**

# In[118]:


print('Resposta:')
for i in range(1, ncolunas, 1): #Este comando para repetir a operação.
    print('A média da coluna {} da matriz é igual a {} .' .format(i+1, np.around(np.mean(array_2a[:, i]), 2)))


# **d) Obtenha as médias das linhas considerando somente as colunas 2 e 3.**

# In[119]:


print('Resposta:')
for i in range(0, nlinhas, 1):
    print('Considerando apenas as colunas 2 e 3, a média da linha {} é igual a {}.' .format(i+1, (np.mean(array_2a[i,[1, 2]]))))


# **e) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade inferior a 5.**

# In[120]:


nota_menorq5 = array_2a[:, 1] < 5
array_2e = array_2a[nota_menorq5]
print('Resposta:')
print('De acordo com a escala de nota de severidade, os genótipos {} apresentaram nota inferior a 5 para a doença em estudo.'.format(array_2e[:, 0]))


# **f) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de peso de 100 grãos superior ou igual a 22.**

# In[121]:


peso_maiorigual22 = array_2a[:, 2] >= 22
array_2f = array_2a[peso_maiorigual22]
print('Resposta:')
print('De acordo com o peso de 100 grãos, os genótipos {} apresentaram peso superior ou igual a 22.'.format(array_2f[:, 0]))


# **g) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade igual ou inferior a 3 e peso de 100 grãos igual ou superior a 22.**

# In[122]:


nota_menorigual3 = array_2a[:, 1]
array_2g = array_2a[nota_menorigual3 & peso_maiorigual22]
print('Resposta:')
print('Neste estudo, os genótipos {} apresentaram nota de severidade da doença inferior ou igual a 3 e peso de 100 grãos superior ou igual a 22.'.format(array_2g[:,0]))


# **h) Crie uma estrutura de repetição com uso do for (loop) para apresentar na tela cada uma das posições da matriz e o seu respectivo valor. Utilize um iterador para mostrar ao usuário quantas vezes está sendo repetido. Apresente a seguinte mensagem a cada iteração: Na linha X e na coluna Y ocorre o valor: Z. Nesta estrutura crie uma lista que armazene os genótipos com peso de 100 grãos igual ou superior a 25.**

# In[123]:


print(' ')
print('Resposta:')
itr = 0
for i in np.arange(0, nlinhas, 1):
    for j in np.arange(0, ncolunas, 1):
        itr = itr + 1
        print('___ Iteração {} ___'.format(itr))
        print('Na linha {} e na coluna {} ocorre o valor {}.'.format(i+1, j+1, array_2a[int(i), int(j)]))

print(' ')       
peso_maiorigual25 = (array_2a[:, 2] >= 25)
array_2h = (array_2a[peso_maiorigual25])
print('De acordo com o peso de 100 grãos, os genótipos {} apresentaram peso superior ou igual a 25.'.format(array_2h[:,0]))


# **EXERCÍCIO 03:**
# 
# **a) Crie uma função em um arquivo externo (outro arquivo .py) para calcular a média e a variância amostral um vetor qualquer, baseada em um lopp (for).**

# In[124]:


print('Resposta:')
from fcREO1 import amostrar
array_3a = amostrar(np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),tamanho_amostra=5,numero_amostragens = 5)


# **b) Simule três arrays com a biblioteca numpy de 10, 100, e 1000 valores e com distribuição normal com média 100 e variância 2500. Pesquise na documentação do numpy por funções de simulação.**

# In[125]:


array_3b1 = np.random.normal(100, math.sqrt(2500), 10)#Array com 10 valores
array_3b2 = np.random.normal(100, math.sqrt(2500), 100)#Array com 100 valores
array_3b3 = np.random.normal(100, math.sqrt(2500), 1000)#Array com 100 valores
print('Resposta:')
print('array_3b1 = np.random.normal(100, math.sqrt(2500), 10) # Array criado com 10 valores.')
print('array_3b2 = np.random.normal(100, math.sqrt(2500), 100) # Array criado com 100 valores.')
print('array_3b3 = np.random.normal(100, math.sqrt(2500), 1000) # Array criado com 1000 valores.')


# **c) Utilize a função criada na letra a para obter as médias e variâncias dos vetores simulados na letra b.**

# In[126]:


print('Resposta:')
print('Utilizando o array_3b1:')
print(' ')
array_3c1 = amostrar(array_3b1, 10, 1) #informações da função amostrar(vetor, tamanho da amostra, número de amostragens)
print(' ')
print('Utilizando o array_3b2:')
print(' ')
#array_3c1 = amostrar(array_3b2, 100, 1) # Para não afetar na estética do trabalho, optei por não executar a amostra (muito grande).
print(' ')
print('Utilizando o array_3b3:')
print(' ')
#array_3c1 = amostrar(array_3b3, 1000, 1) # Para não afetar na estética do trabalho, optei por não executar a amostra (muito grande).


# **d) Crie histogramas com a biblioteca matplotlib dos vetores simulados com valores de 10, 100, 1000 e 100000.**

# In[127]:


print('Resposta:')
print('h10 = plt.hist(array_3b1)')
print('h100 = plt.hist(array_3b2)')
print('h1000 = plt.hist(array_3b3)')
print('h10000 = plt.hist(np.random.normal(100, math.sqrt(2500), 10000))')
fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.hist(array_3b1, color="tab:purple")
ax0.set_title('Tamanho amostral (n) = 10')
ax1.hist(array_3b2, color="tab:red")
ax1.set_title('Tamanho amostral (n) = 100')
ax2.hist(array_3b3, color="tab:orange")
ax2.set_title('Tamanho amostral (n) = 1000')
ax3.hist(np.random.normal(100, math.sqrt(2500), 10000), color="tab:blue")
ax3.set_title('Tamanho amostral (n) = 10000')
fig.tight_layout()
plt.show()


# **EXERCÍCIO 04:**
# 
# **a) O arquivo dados.txt contem a avaliação de genótipos (primeira coluna) em repetições (segunda coluna) quanto a quatro variáveis (terceira coluna em diante). Portanto, carregue o arquivo dados.txt com a biblioteca numpy, apresente os dados e obtenha as informações de dimensão desta matriz.**

# In[128]:


print('Resposta: ')
dados = np.loadtxt('dados.txt')
#dados = np.array([1,1,249.75,604.15,404.48,348.49,281.31],[1,2,227.56,527.36,414.52,324.32,210.29],[1,3,368.18,711.87,490.14,331.84,297.12],[2,1,615.42,548.00,359.91,376.66,593.01],[2,2,756.11,59.78, 363.74,351.99,523.45],[2,3,481.54,464.04,415.98,317.41,447.33],[3,1,610.40,529.91,389.65,385.01,253.22],[3,2,534.73,436.40,439.23,400.99,241.25],[3,3,488.87,277.88,414.90,367.00,77.56],[4,1,587.84,186.90,399.76,556.27,55.25],[4,2,627.27,478.44,470.98,501.10,312.92],[4,3,594.91,454.60,409.16,429.03,268.36],[5,1,358.48,480.34,530.92,273.63,321.65],[5,2,341.18,238.63,414.71,344.45,370.12],[5,3,409.65,537.39,566.61,278.46,417.95],[6,1,530.40,430.57,309.84,245.79,552.34],[6,2,644.79,352.27,311.07,226.46,437.38],[6,3,619.42,256.40,287.13,294.35,714.34],[7,1,592.22,563.79,298.57,260.88,508.33],[7,2,588.89,862.62,502.44,260.02,351.95],[7,3,627.72,521.22,400.76,256.94,432.98],[8,1,605.05,420.44,303.72,265.78,549.18],[8,2,620.72,519.95,303.81,321.96,451.01],[8,3,711.55,375.29,274.21,227.00,459.69],[9,1,493.93,425.79,361.44,300.38,29.60],[9,2,457.53,450.88,335.19,286.33,239.92],[9,3,366.90,264.96,434.37,285.10,14.92],[10,1, 479.98,611.18,302.20,336.88,700.12],[10,2,671.50,372.21,270.94,302.40,461.48],[10,3, 471.44,284.37,300.48,383.68,851.41])
print('Conjunto de dados')
print('    Gen    Rep    v1     v2     v3     v4     v5')
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
print(str(dados))
print(' ')
print('Dimensões dos conjunto de dados')
nlin, ncol = dados.shape
print('Número de linhas: {}'.format(nlin))
print('Número de colunas: {}'.format(ncol))


# **b) Pesquise sobre as funções np.unique e np.where da biblioteca numpy.**

# In[129]:


print('Resposta:')
print('help(np.unique) <- Este comando dará as instruções em inglês sobre a função np.unique da biblioteca numpy.')
print(' ')
help(np.unique)
print(' ')
print('help(np.where) <- Este comando dará as instruções em inglês sobre a função np.where da biblioteca numpy.')
print(' ')
help(np.where)


# **c) Obtenha de forma automática os genótipos e quantas repetições foram avaliadas.**

# In[130]:


print('Resposta:')
print('Os Genótipos {} foram avaliados em experimento com {} repetições por genótipo.'.format(np.unique(dados[:, 0]),int(max(dados[:, 1]))))


# **d) Apresente uma matriz contendo somente as colunas 1, 2 e 4.**

# In[131]:


dados_v2 = dados[:, [0, 1, 3]]
print('Respota:')
print('Matriz com informações de Genótipos, Repetições e dados coletados da v2:')
print(' ')
print('   Gen    Rep     v2')
print(dados_v2)


# **e) Obtenha uma matriz que contenha o máximo, o mínimo, a média e a variância de cada genótipo para a variavel da coluna 4. Salve esta matriz em bloco de notas.**

# In[132]:


print('Resposta:')
matriz_v2 = np.zeros((len(np.unique(dados_v2[:, 0])), 5))
it = 0
for i in range(0, len(np.unique(dados_v2[:, 0])), 1):
    it = it + 1
    print(' ')
    print('O genótipo {} apresenta as seguintes informaçãos para a variável da coluna 4 (v2):'.format(it))
    print('Valor máximo: {} '.format(np.max((dados_v2[dados_v2[:, 0] == i + 1])[:, 2])))
    print('Valor minímo: {} '.format(np.min((dados_v2[dados_v2[:, 0] == i + 1])[:, 2])))
    print('Média: {} '.format(np.around(np.mean((dados_v2[dados_v2[:, 0] == i + 1])[:, 2]), 2)))
    print('Variância: {} '.format(np.around(np.var((dados_v2[dados_v2[:, 0] == i + 1])[:, 2]), 2)))
    matriz_v2[i, 0] = i + 1
    matriz_v2[i, 1] = np.max((dados_v2[dados_v2[:, 0] == i + 1])[:, 2])
    matriz_v2[i, 2] = np.min((dados_v2[dados_v2[:, 0] == i + 1])[:, 2])
    matriz_v2[i, 3] = np.around(np.mean((dados_v2[dados_v2[:, 0] == i + 1])[:, 2]), 2)
    matriz_v2[i, 4] = np.around(np.var((dados_v2[dados_v2[:, 0] == i + 1])[:, 2]), 2)

np.savetxt('Matriz_4e.txt', matriz_v2, fmt='%2.2f', delimiter='\t')
print(' ')
print(' ')
print('Informações da matriz:')
print(' ')
print('  Genótipo   Máximo   Minímo   Média   Variância')
print(matriz_v2)
print(' ')
print(' ')

print('f) Obtenha os genótipos que possuem média (médias das repetições) igual ou superior a 500 da matriz gerada na letra anterior.')
print(' ')
u_maiorq500 = matriz_v2[:, 3] >= 500
matriz_v2_maiorq500 = matriz_v2[u_maiorq500]
print('Quanto a v2, Os genótipos {} apresentaram as médias iguais ou superiores a 500.'.format(matriz_v2_maiorq500[:, 0]) )


# **g) Apresente os seguintes graficos:**
# 
# **- Médias dos genótipos para cada variável. Utilizar o comando plt.subplot para mostrar mais de um grafico por figura:**

# In[133]:


matriz_completa = np.zeros((len(np.unique(dados[:, 0])), 6))
it = 0
for i in range(0, len(np.unique(dados[:, 0])), 1):
    it = it + 1
    matriz_completa[i, 0] = i + 1
    matriz_completa[i, 1] = np.around(np.mean((dados[dados[:, 0] == i + 1])[:, 2]), 2)
    matriz_completa[i, 2] = np.around(np.mean((dados[dados[:, 0] == i + 1])[:, 3]), 2)
    matriz_completa[i, 3] = np.around(np.mean((dados[dados[:, 0] == i + 1])[:, 4]), 2)
    matriz_completa[i, 4] = np.around(np.mean((dados[dados[:, 0] == i + 1])[:, 5]), 2)
    matriz_completa[i, 5] = np.around(np.mean((dados[dados[:, 0] == i + 1])[:, 6]), 2)

print(' ')
print('Resposta:')
print('As médias dos genótipos em cada variável:')
print(' ')
print(' Genótipo    v1     v2     v3     v4     v5')
print(matriz_completa)
print(' ')
print(' ')


plt.figure('As médias dos genótipos em cada variável')
plt.subplot(2, 3, 1)
plt.bar(x=matriz_completa[:, 0], height=matriz_completa[:, 1], width=0.5, align='center', color="tab:purple")
plt.title('v1')
plt.xticks(matriz_completa[:, 0])
plt.ylabel("média")

plt.subplot(2, 3, 2)
plt.bar(x=matriz_completa[:, 0], height=matriz_completa[:, 2], width=0.5, align='center', color="tab:red")
plt.title('v2')
plt.xticks(matriz_completa[:, 0])
plt.ylabel("média")

plt.subplot(2, 3, 3)
plt.bar(x=matriz_completa[:, 0], height=matriz_completa[:, 3], width=0.5, align='center', color="tab:orange")
plt.title('v3')
plt.xticks(matriz_completa[:, 0])
plt.ylabel("média")

plt.subplot(2, 3, 4)
plt.bar(x=matriz_completa[:, 0], height=matriz_completa[:, 4], width=0.5, align='center', color="tab:blue")
plt.title('v4')
plt.xticks(matriz_completa[:, 0])
plt.ylabel("média")

plt.subplot(2, 3, 5)
plt.bar(x=matriz_completa[:, 0], height=matriz_completa[:, 5], width=0.5, align='center', color="tab:purple")
plt.title('v5')
plt.xticks(matriz_completa[:, 0])
plt.ylabel("média")
fig.tight_layout()
plt.show()


# **- Disperão 2D da médias dos genótipos (Utilizar as três primeiras variáveis). No eixo X uma variável e no eixo Y outra.**

# In[134]:


cores = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown','tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

plt.style.use('ggplot')
plt.figure('2D Scatter Graph')

plt.subplot(2, 2, 1)
for i in np.arange(0, len(np.unique(dados[:, 0])), 1):
    plt.scatter(matriz_completa[i, 1], matriz_completa[i, 2], s=50, alpha=0.8, label=int(matriz_completa[i, 0]), c=cores[i])
plt.xlabel('v1')
plt.ylabel('v2')

plt.subplot(2, 2, 2)
for i in np.arange(0, len(np.unique(dados[:, 0])), 1):
    plt.scatter(matriz_completa[i, 1], matriz_completa[i, 3], s=50, alpha=0.8, label=int(matriz_completa[i, 0]), c=cores[i])
plt.xlabel('v1')
plt.ylabel('v3')

plt.subplot(2, 2, 3)
for i in np.arange(0, len(np.unique(dados[:, 0])), 1):
    plt.scatter(matriz_completa[i, 2], matriz_completa[i, 3], s=50, alpha=0.8, label=int(matriz_completa[i, 0]), c=cores[i])
plt.xlabel('v2')
plt.ylabel('v3')

plt.legend(bbox_to_anchor=(2.08, 0.7), title='Genótipo', borderaxespad=0., ncol=5)
plt.show()


# In[ ]:




