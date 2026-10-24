
#Tupla é uma coleção ordenada e imutavel de elementos

#Criando uma tupla de exemplo
minha_tupla = (1, 2, 3, 5, 8, 2, 4, 2, 5, 5, 3)

print("Minha tupla:", minha_tupla)
print("Minha tupla[2]:", minha_tupla[2])
print("Minha tupla[0]:", minha_tupla[0])
print("Minha tupla[-1]:", minha_tupla[-1])


#você não pode alterar o valor de um elemento dentro de uma tupla
#Ex.: nao funcionaria
#minha_tupla[1] = 4
#o valor não seria alterado


#Método count() -> retorna o número de ocorrências de um elemento dentro da tupla
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

#Método index() -> retorna o índice da primeira ocorrência de um elemento
indice = minha_tupla.index(2)
print("Indice da primeira ocorrência do elemento 2:", indice)
