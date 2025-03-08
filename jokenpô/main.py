# função para jogar pedra, papel, tesoura

from random import randint
itens = ("pedra", "papel", "tesoura") # uma lista para se referir as opções escolidas
def jokenpo():
  jogadaRandom = randint(0, 2) # determina a jogada do computador

  print("Game - jokenpô contra o computador")
  print("0 - Pedra")
  print("1 - Papel")
  print("2 - Tesoura")
  jogadaUser = int(input("Digite sua jogada: ")) # recebendo a jogada do usuário

  print("-" * 15)
  print("Player jogou {}" .format(itens[jogadaUser])) # o que o usuário escolheu
  print("Computador jogou {}" .format(itens[jogadaRandom])) # o que o computador escolheu
  print("-" * 15)

  if (jogadaUser == 0): # se o usuário jogou pedra
    if (jogadaRandom == 0 ):
      print("EMPATE")
    elif (jogadaRandom == 1):
      print("DERROTA")
    elif(jogadaRandom == 2):
      print("VITÓRIA")

  elif (jogadaUser == 1): # se o usuário jogou papel
    if (jogadaRandom == 0 ):
      print("VITÓRIA")
    elif (jogadaRandom == 1):
      print("EMPATE")
    elif (jogadaRandom == 2):
      print("DERROTA")

  elif (jogadaUser == 2): # se o usuário jogou tesoura
    if (jogadaRandom == 0 ):
      print("DERROTA")
    elif (jogadaRandom == 1):
      print("VITÓRIA")
    elif (jogadaRandom == 2):
      print("EMPATE")

while True: # para o usuário jogar infinitamente
    jokenpo()
    print("~" * 15)
    jogarDenovo = input("Deseja jogar novamente? (s/n): ").lower()
    if jogarDenovo != 's':
        print("Obrigado por jogar! Até a próxima.")
        break