#declaração

nome_completo = "Gabriel Melo"

#segunda forma de declaração

nome_completo_aspas = """Gabriel
Melo"""

#terceira forma

nome_completo_quebra = "Gabriel \
Melo"

nome = "Gabriel"
sobrenome = "Melo"

# print(nome_completo)
# print(nome_completo_aspas)
# print(nome_completo_quebra)

#Formatação

print("Nome completo (1a forma): ", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Gabriel" + "Melo")
print("Nome completo (4a forma):" + "Gabriel", "Melo")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s " % (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}") #format
print("Nome completo (10a forma): {} {}".format(nome, sobrenome)) #função format
