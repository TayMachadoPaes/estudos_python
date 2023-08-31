def cachorro_peso(): #Função para determinar a base de preço a partir do peso#
  print('╔╦══════════════ ⋆ ⋆ ✦ ⋅ MENU 1/3 - Peso do Cachorro ⋅ ✦ ⋆ ⋆ ══════════════╦╗')
  while True:
    try: #Try utilizado para testar se o usuário irá entrar com os dados suportados pela variável#
      peso = int(input('Entre com o peso do cachorro (APENAS NÚMEROS EX: 5/10/30): '))
      if (peso < 3): #Estrutura de condição utilizando if/elif/else para determinar o intervalo#
        base = 40
        return base
      elif (peso >= 3) and (peso < 10):
        base = 50
        return base
      elif (peso >= 10) and (peso < 30):
        base = 60
        return base
      elif (peso >= 30) and (peso < 50):
        base = 70
        return base
      else:
        print('ATENÇÃO: Não aceitamos cachorros com 50kg ou mais. ')
        print('Entre com o peso do cachorro novamente por favor')
        continue
    except ValueError: #Expect caso o usuário entre com algum dado não suportado pela variável#
      print('Coloque apenas número inteiro (sem ponto ou vírgula)')



def cachorro_pelo(): #Função para determinar o multiplicador a partir do tipo de pelo do cachorro#
  print('╔╦══════════════ ⋆ ⋆ ✦ ⋅ MENU 2/3 - Pelagem do Cachorro ⋅ ✦ ⋆ ⋆ ══════════════╦╗')

  while True: #Laço de repetição para repetir a entrada caso o usuário digite algo inválido#
    print('INDIQUE O TIPO DE PELO')
    print('C - Curto.')
    print('M - Médio.')
    print('L - Longo.')
    opp = input('Entre com a pelagem do seu cachorro: ')
    opp = opp.upper() #Função para mudar o caractere caso o usuário digite em letra minúscula#
    opp = opp.strip() #Função para retirar os espaços caso o usuário digite com espaços desnecessários#
    if (opp == 'C'):
      return 1.00
    elif (opp == 'M'):
      return 1.5
    elif (opp == 'L'):
      return 2.00
    else:
      print('Opção inválida... Digite APENAS C/M/L')
      continue


def cachorro_extra(): #Função para os adicionais extras caso o usuário queira#
  print('╔╦══════════════ ⋆ ⋆ ✦ ⋅ MENU 1/3 - Serviços Adicionais ⋅ ✦ ⋆ ⋆ ══════════════╦╗')

  acumulador = 0 #Variável acumuladora importante para a soma dos adicionais#
  while True: #Laço de repetição infinito para ter a possibilidade de ter mais de um adicional#
    print('Se desejar indique o serviço adicional...')
    print('1 - Cortar Unhas')
    print('2 - Escovar os Dentes')
    print('3 - Limpar as Orelhas')
    print('0 - Não quero nenhum adicional')
    adicional = input('Entre com o adicional (Ex: 1/2/3/0): ')
    if (adicional == '0'):
      return acumulador
    elif (adicional == '1'):
      acumulador = acumulador + 10
      continue
    elif (adicional == '2'):
      acumulador = acumulador + 12
      continue
    elif (adicional == '3'):
      acumulador = acumulador + 15
      continue
    else:
      print('Entre com o adicional (Ex: 1/2/3/0): ')
      continue
#Programa Princial

print('⊹⊱•••••••••••《 Olá, seja bem vindo(a) ao Pet Shop da Taynara Paes 🐶 》•••••••••••⊰⊹')
print('⊹⊱••••••••••••••《 Aguarde já vamos te atender! 》••••••••••••••⊰⊹')
nome = input('Qual o seu nome?')
print('Olá {}. Seja muito bem vindo(a) ao nosso Pet Shop!'.format(nome))
base = cachorro_peso()
multiplicador = cachorro_pelo()
extra = cachorro_extra()
total = (base * multiplicador) + extra
print('🦴 Total a pagar(R$): {}0 (peso: {} * pelo: {} + adicionais: {} ) ' .format(total, base, multiplicador, extra))
print('╚╩════════════⋆ ⋆ ✦ ⋅ Obrigado(a) {} pela confiança no nosso atendimento! ⋅ ✦ ⋆ ⋆ ════════════╩╝' .format(nome))