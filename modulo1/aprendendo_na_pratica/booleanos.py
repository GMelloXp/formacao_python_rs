#condição verdadeira
True
#condição Falsa
False

#exemplo
if False:
  print("Bloco IF executado")
else:
  print("Bloco ELSE executado")

#Operadores lógicos and e or

#and -> precisa que as duas condições sejam verdadeiras

if True and True:
  print("Bloco executado")
if True and False:
  print("Bloco não executado")
if False and False:
  print("Bloco não executado")

#or -> precisa que uma das condições seja verdadeira

if True or True:
  print("Bloco executado")
if True or False:
  print("Bloco executado")
if False or False:
  print("Bloco não executado")
if True or True:
  print("Bloco executado")
