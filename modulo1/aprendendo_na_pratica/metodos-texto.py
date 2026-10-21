nome = "Gabriel"
sobrenome = "Melo"
nome_completo = "Gabriel Melo"

#método Upper

print(nome.upper())
#retorna todas as letras em maiúsculo

#método Lower

print(nome.lower())
#retorna todas as letras em minúsculo

#esses métodos não alteram o valor da variável

print(nome[0])

#método count (retorna a quantidade de vezes de uma ocorrência em uma string)
print(nome_completo.count("e"))

#método find (retorna o número da posição da ocorrência)
print(nome_completo.find("l"))

#método encode (codifica em bytes)
print(nome.encode())

#método decode (decodifica o que tava em bytes)
print(nome.encode().decode())

#método replace (substitui uma letra da string por outra)
print(nome_completo.replace("e", "&"))

#método join (adiciona um separador a cada caractere)
print("-".join(nome))

#método split (divide a string em uma lista, com base em um caractere alvo que é passado)
print(nome_completo.split(" ")) #o alvo foi o espaço. Pode tbm deixar vazio em caso do alvo ser o espaço

#método strip (retira cacteres adjacentes ao texto principal da string)
outro_nome_completo = "1Gabriel Resende1"
print(outro_nome_completo)
print(outro_nome_completo.strip("1"))
print(outro_nome_completo.rstrip("1")) #retira apenas o da direita
print(outro_nome_completo.lstrip("1")) #retira apenas o da esquerda

#método startswith (diz se uma string começa com um caractere ou cadeia de caracteres e retorna uma valor booleano)
print(nome_completo.startswith("Ga"))

#método in (verifica se existe um termo dentro da variável que queremos comparar)
print("o" in nome_completo)

#método not in
print("Ga" not in nome_completo)
