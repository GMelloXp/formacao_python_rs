
#Lista é uma coleção de elementos ordenáveis e mutáveis

#Declaração

minha_lista = [1, 2, 3, 4, 5, "Gabriel", True, False]

#Exibindo a lista
print("Minha lista de exemlo", minha_lista)

#Exibindo elementos da lista
print("Elemento da lista[5]:", minha_lista[5])

#slice -> "fatia" um pedaço da lista e retorna ela
print("Minha lista [1:7]",minha_lista[1:7]) #aqui, a lista retorna os elementos do índice 1 até o indice 6, ou seja,
                        #o intervalo tem que ir do índice do elemento que vc quer fatiar primeiro, até o
                        #até o índice + 1 do último elemento da "fatia".
print("Minha lista [:6]", minha_lista[:6]) #quando não passa o primeiro parâmetro do colchete, entende-se que é
                                           #do índice [0] até o elemento de índice [6], sendo que o último elemento a ser fatiado é o anterior a ele.
print("Minha lista [2:]", minha_lista[2:]) #quando não passa o segundo parâmetro do colchete, entende-se que é do índice marcado no primeiro colchete [2] em diante

#mudando elementos da lista
minha_lista[0] = "Python"
print("Minha lista modificada",minha_lista)

#Métodos de lista

#método append(): adiciona um elemento ao final da lista
minha_lista.append(9)
print("Minha lista após append(9)", minha_lista)

#método index(): retorna o índice de um elemento da lista
indice = minha_lista.index(5)
print("Índice do elemento 5 em minha lista:", indice)

#método insert(): insere um elemento em um índice específico
minha_lista.insert(3, "ABC")
print("Minha lista apos insert(ABC):", minha_lista)
"""
  nesse caso temos que colocar primeiro o índice que queremos modificar
  e depois colocar o novo elemento que queremos inserir naquele índice
"""
#método pop(): remove e retorna o elemento de um índice específico
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Minha lista após pop(5):", minha_lista)

#método remove(): remove um elemento específico da lista
minha_lista.remove(False)
print("minha lista após remove(False):", minha_lista)

#método sort -> organiza a lista em ordem crescente

nova_lista = [4, 6, 2, 3, 7, 10, 5]
nova_lista.sort()
print("Nova lista após o sort()", nova_lista)
