# função que converte um número para binário, octal ou hexadecmal a critério do usuário

# solicitando o número a ser convertido
numero = int(input("Escreva um númro para ser convertido: "))

# questionando para qual base será convertido
print("Para qual base de conversão?")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")
baseConversao = int(input("Digite o correspondente: "))

# calculando a partir da escolha
if (baseConversao == 1):
  print("O número convertido para binário é:" , bin(numero)[2:])
elif (baseConversao == 2):
  print("O número convertido para octal é:" , oct(numero))
elif (baseConversao == 3):
  print("O número convertido para hexadecimal é:" , hex(numero))
else: 
  print("Você não apertou nenhuma opção valida!") # caso o usuário não escolha nenhuma das opções apresentadas