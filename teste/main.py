# Crie um programa em Python que calcule a média final de um estudante a partir de duas notas e determine sua situação (aprovado ou reprovado).

# solicitando as notas do aluno

nota1 = float(input('Digite sua nota do primeiro trimestre: '))
nota2 = float(input('Digite sua nota do segundo trimestre: '))

# calculando a média

media = (nota1 + nota2) / 2

# possibilidades

if (media >= 7): 
  print('Você está aprovado, sua media foi ', media)
else:
  print('Você está reprovado, sua media foi ', media)
