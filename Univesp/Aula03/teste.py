# acum = 0
# for i in range(1,101):
#    if i % 2 == 0:
#        acum += i

#str_list = ['João', 'Roberto', 'Rafael']
#
#for nome in str_list:
#    for c in nome:
#        if c in 'aeiou':
#            print(c) 

# def nfat(L):
#     n = 0
#     fat = 1
#     while fat <= L:
#         n+= 1 
#         fat *= n
#     return n-1
# 
# print(nfat(20))

# frase = 'Algoritmos e ProgramaçãO de Computadores I'
# contLetra = 0
# for c in frase:
#     if c in  'oO':
#         print('Vogal: ', c)
#         contLetra += 1
# print('Total de lestras o ou O: ', contLetra)

def transposta(m):
    nlinhas = len(m)
    ncolunas = len(m[0])

    matriz_transposta = []
     
    for i in range(ncolunas):
        nova_linha = []
        for j in range(nlinhas):
            nova_linha.append(m[j][i])
        matriz_transposta.append(nova_linha)
    return matriz_transposta

matriz = [[1,2,3],[2,4,5],[3,5,3]]
print(matriz)
transp = transposta(matriz)
print(transp)