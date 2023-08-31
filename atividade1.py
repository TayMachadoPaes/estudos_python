print('⊹⊱•••《 Olá, seja bem vindo(a) a loja da Taynara Paes 》•••⊰⊹')
valor = int(input('Entre com o valor do produto: (ex: 10/100) '))
quantidade = int(input('Entre com a quantidade do produto: (ex: 10/100) '))

if (quantidade < 200): #Estrutura de condição com if#
  total = quantidade * valor
  print('O valor SEM desconto: R${}.0' .format(total))
  print('O valor COM desconto: R${}.0' .format(total))
  print('Menos de 200 unidades não há desconto algum...')
elif (quantidade >= 200) and (quantidade < 1000): #Estrutura de condição com elif#
  total = quantidade * valor #Calculo para saber o valor total da compra#
  desconto = total * 0.05  #Calculo para determinar o desconto#
  valor_cdesconto = total - desconto #Calculo para aplicar o desconto a compra final#
  print('Valor SEM desconto: R${}.00' .format(total))
  print('Valor COM desconto: R${}0' .format(valor_cdesconto))
elif (quantidade >= 1000) and (quantidade < 2000): #Estrutura de condição com elif#
  total = quantidade * valor #Calculo para saber o valor total da compra#
  desconto = total * 0.1  #Calculo para determinar o desconto#
  valor_cdesconto = total - desconto #Calculo para aplicar o desconto a compra final#
  print('Valor SEM desconto: R${}.00' .format(total))
  print('Valor COM desconto: R${}0' .format(valor_cdesconto))
elif (quantidade > 2000): #Estrutura de condição com elif#
  total = quantidade * valor #Calculo para saber o valor total da compra#
  desconto = total * 0.15  #Calculo para determinar o desconto#
  valor_cdesconto = total - desconto #Calculo para aplicar o desconto a compra final#
  print('Valor SEM desconto: R${}.00' .format(total))
  print('Valor COM desconto: R${}0' .format(valor_cdesconto))
else:
  print('Ops, valor de entrada inválido.')