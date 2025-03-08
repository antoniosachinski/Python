# fumção que verifica sé é possível aprovar um emprestimo bancário

# entendendo a situação do comprador
valorCasa = float(input("Qual o valor ad casa? ")) 
salario = float(input("Qual seu salário? "))
mesesParaPagar = 12 * (int(input("Em quantos anos pretende pagar? "))) # tempo para pagar já arredondado para meses

# verificando se a compra é compativel com o salário
if ((valorCasa / mesesParaPagar) < (salario * 30 / 100)): # se a parcela for menor que 30% do salário ele pode realizar o emprestimo
  print("Você pode realizar o empréstimo!!")
else:
  print("Você não pode realizar o empréstimo. Pois sua prestação mensal vai exceder 30% do seu salário")

