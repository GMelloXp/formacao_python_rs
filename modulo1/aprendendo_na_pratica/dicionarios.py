

#Coleção não ordenada de pares chave e valor

#Criando um dicionário de exemplo
pessoa = {"nome": "Pedro", "idade": "25", "cidade": "São Paulo"} #{"chave": "valor"}

#Exibindo o docionário
print("Meu dicionário de exemplo:", pessoa)

#Acesssando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

#Atribuindo um valor ao dicionário após ele ser criado
pessoa["sobrenome"] = "Pescador"
print("Sobrenome:", pessoa["sobrenome"])
