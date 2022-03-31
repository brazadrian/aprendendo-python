#AT1 - Dev. de Interfaces
#Gilmar Adrian de Souza Braz
print("•—•" * 12, sep=" ")
print("Bem vindo ao jogo da adivinhação!")

### melhorar com randomização do numero_secreto
numero_secreto = 620
numero_tentativa_usuario = 0
diferenca_tentativa_de_secreto = 0

#diferença entre a tentativa do usuário para o número secreto
    #quando maior, pedir para o usuário diminuir as tentativas e vice-versa

	# nas condições a seguir, são estabelicods 3 (três) parâmetros para CADA diferença, positiva ou negativa
	# se a diferença é maior que 20
    # se a diferença é até 20
    # se a diferença é até 6

### melhorar informando ao usuário a quantidade de tentativas restantes
for cont in range(0, 9):
  numero_tentativa_usuario = int(input("Adivinhe qual é o número oculto: "))

  diferenca_tentativa_de_secreto = numero_tentativa_usuario - numero_secreto

  if (diferenca_tentativa_de_secreto <= 20 and diferenca_tentativa_de_secreto > 6):
    print("Ainda está um pouco longe, é um número MENOR (-)\n")
  
  elif (diferenca_tentativa_de_secreto >= -20 and diferenca_tentativa_de_secreto < -6):
    print("Ainda está um pouco longe, é um número MAIOR (+)\n")
  
  elif (diferenca_tentativa_de_secreto <= 6 and diferenca_tentativa_de_secreto > 0):
    print("Você está bem pertinho! É um número um pouco MENOR [-]\n")
  
  elif (diferenca_tentativa_de_secreto >= -6 and diferenca_tentativa_de_secreto < 0):
    print("Você está bem pertinho! É um número um pouco MAIOR [+]\n")
  
  elif (diferenca_tentativa_de_secreto < 20 and diferenca_tentativa_de_secreto != 0):
    print("Você está muito longe... tente números mais ALTOS {+} \n")
  
  elif (diferenca_tentativa_de_secreto > 20 and diferenca_tentativa_de_secreto != 0):
    print("Você está muito longe... tente números mais BAIXOS {-}\n")
  
  else:
    print("Parabéns! Você descobriu o número secreto.")
    print("—•—" * 12, sep=" ")
    break
