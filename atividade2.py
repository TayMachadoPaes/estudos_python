print('⊹⊱•••••••••••《 Olá, seja bem vindo(a) a loja de sorvetes da Taynara Paes 》•••••••••••⊰⊹')
print('----------------------------------------- CARDÁPIO -----------------------------------------')
print('| Nº DE BOLAS  |  Sabor Tradicional (tr)  |    Sabor Premium (pr)  |  Sabor Especial (es)  |')
print('|      1       |         R$ 6,00          |         R$ 7,00        |       R$ 8,00         |')
print('|      2       |         R$ 11,00         |         R$ 13,00       |       R$ 15,00        |')
print('|      3       |         R$ 15,00         |         R$ 18,00       |       R$ 21,00        |')
print('--------------------------------------------------------------------------------------------')

acumulador = 0 #Variável acumulador para guardar o valor total do pedido#
while True:
  sabor = input('Entre com o sabor desejado (tr/pr/es): ')
  if sabor != 'tr' and sabor != 'TR' and sabor != 'pr' and sabor != 'PR' and sabor != 'es' and sabor != 'ES':
    print('Sabor Inválido. Tente novamente!')
    continue #Caso o usuário digite algo errado possa entrar com a opção desejada novamente#

  numero_bolas = input('Entre com o número de bolas de sorvete desejado(1/2/3): ')
  if numero_bolas != '1' and numero_bolas != '2' and numero_bolas != '3':
    print('Número de bolas de sorvete inválido. Tente Novamente.')
    continue
 #Número de bolas de sorvete: 1#
  if numero_bolas == '1' and sabor == 'tr':
    print('Você pediu 1 bola de sorvete no sabor TRADICIONAL: R$ 6,00')
    continuar = input('Deseja mais algum sorteve? (s/digite outra tecla): ') #Variável para verificar se o usuário deseja continuar#
    if continuar == 's': #Condição com o if para que o usuário possa refazer seu pedido caso desejar#
      acumulador = acumulador + 6 #Variável acumuladora recebe ela mesma mais o valor do pedido#
      continue #Para que possa volar para o inicio do programa e refazer o pedido se o usuário desejar#
    else: #Condição else para encerrrar o programa se o usuário desejar#
      acumulador = acumulador + 6 #No caso do usuário desejar sair a variável acumulador irá fazer o calculo do mesmo jeito, por isso repeti aqui o calculo da variável acumuladora#
      print('O valor total a ser pago: {},00' .format(acumulador))
      break
  elif numero_bolas == '1' and sabor == 'pr':
    print('Você pediu 1 bola de sorvete no sabor PREMIUM: R$ 7,00')
    continuar = input('Deseja mais algum sorteve? (s/digite outra tecla): ')
    if continuar == 's':
      acumulador = acumulador + 7
      continue
    else:
      acumulador = acumulador + 7
      print('O valor total a ser pago: {},00' .format(acumulador))
      break
  elif numero_bolas == '1' and sabor == 'es':
    print('Você pediu 1 bola de sorvete no sabor ESPECIAL: R$ 8,00')
    continuar = input('Deseja mais algum sorteve? (s/digite outra tecla): ')
    if continuar == 's':
        acumulador = acumulador + 8
        continue
    else:
      acumulador = acumulador + 8
      print('O valor total a ser pago: {},00' .format(acumulador))
      break
 #Numero de bolas de sorvete: 2#
  if numero_bolas == '2' and sabor == 'tr':
    print('Você pediu 2 bolas de sorvete no sabor TRADICIONAL: R$ 11,00')
    continuar = input('Deseja mais algum sorteve? (s/digite outra tecla): ')
    if continuar == 's':
      acumulador = acumulador + 11
      continue
    else:
      acumulador = acumulador + 11
      print('O valor total a ser pago: {},00' .format(acumulador))
      break
  elif numero_bolas == '2' and sabor == 'pr':
    print('Você pediu 2 bolas de sorvete no sabor PREMIUM: R$ 13,00')
    continuar = input('Deseja mais algum sorteve? (s/digite outra tecla): ')
    if continuar == 's':
      acumulador = acumulador + 13
      continue
    else:
      acumulador = acumulador + 13
      print('O valor total a ser pago: {},00' .format(acumulador))
      break
  elif numero_bolas == '2' and sabor == 'es':
    print('Você pediu 2 bolas de sorvete no sabor ESPECIAL: R$ 15,00')
    continuar = input('Deseja mais algum sorteve? (s/digite outra tecla): ')
    if continuar == 's':
      acumulador = acumulador + 15
      continue
    else:
      acumulador = acumulador + 15
      print('O valor total a ser pago: {},00' .format(acumulador))
      break
  #Numero de bolas de sorvete: 3#
  if numero_bolas == '3' and sabor == 'tr':
    print('Você pediu 3 bolas de sorvete no sabor TRADICIONAL: R$ 15,00')
    continuar = input('Deseja mais algum sorteve? (s/digite outra tecla): ')
    if continuar == 's':
      acumulador = acumulador + 15
      continue
    else:
      acumulador = acumulador + 15
      print('O valor total a ser pago: {},00' .format(acumulador))
      break
  elif numero_bolas == '3' and sabor == 'pr':
    print('Você pediu 3 bolas de sorvete no sabor PREMIUM: R$ 18,00')
    continuar = input('Deseja mais algum sorteve? (s/digite outra tecla): ')
    if continuar == 's':
      acumulador = acumulador + 18
      continue
    else:
      acumulador = acumulador + 18
      print('O valor total a ser pago: {},00' .format(acumulador))
      break
  elif numero_bolas == '3' and sabor == 'es':
    print('Você pediu 3 bolas de sorvete no sabor ESPECIAL: R$ 21,00')
    continuar = input('Deseja mais algum sorteve? (s/digite outra tecla): ')
    if continuar == 's':
      acumulador = acumulador + 21
      continue
    else:
      acumulador = acumulador + 21
      print('O valor total a ser pago: {},00' .format(acumulador))
      break