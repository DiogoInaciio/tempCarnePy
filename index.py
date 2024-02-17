temp_cel = int(input('Qual é a temperatura da carne? '))

if temp_cel < 48:
  Print("Cozinhar por mais algum tempo.")
elif temp_cel in range(48, 53):
  print('Selada')
elif temp_cel in range(54, 59):
  print('Ao ponto para mal')
elif temp_cel in range(60, 64):
  print('Ao ponto ')
elif temp_cel in range(65, 70):
  print('Ao ponto para o bem')
elif temp_cel in range(71, 74):
  print('Bem passada')
elif temp_cel >= 75:
  print('Passou do ponto')