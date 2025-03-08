# função que lê o ano de nascimento e determina qual a categoria do usuário em um "X" esporte

from datetime import datetime
dataAtual = datetime.now()
anoAtual = dataAtual.year

anoNasc =  int(input("Digite seu ano de nascimento para saber sua categoria: "))

# calculando a idade
idade = anoAtual - anoNasc

# categorias
if(idade <= 9):
  print("Sua categoria é MIRIM")
elif(idade <= 14 & idade > 9):
  print("Sua categoria é INFANTIL")
elif(idade <= 19 & idade > 14):
  print("Sua categoria é JUNIOR")
elif(idade <= 20 & idade > 19):
  print("Sua categoria é SÊNIOR")
else:
  print("Sua categoria é MASTER")

