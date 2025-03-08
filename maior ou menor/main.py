# função que determina qual dos dois números inserido é maior

print("Digite dois números inteiros para serem comparados")
valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
# comparando
if (valor1 > valor2):
  print("O primeiro nnúmero é maior")
elif (valor1 < valor2):
  print("O segundo número é maior")
else:
  print("Não existe valor maior ou menor, pois os dois são iguais")