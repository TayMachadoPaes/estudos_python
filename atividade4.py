#Variaveis Globais#
id_global = 0
lista_colaborador = []

def cadastrar_colaborador(id):
  print('MENU CADASTAR COLABORADOR')
  print('Id do Colaborador(a): {}' .format(id))
  nome = input('Entre com o NOME do(a) colaborador(a): ')
  setor = input('Entre com o SETOR do(a) colaborador(a): ')
  salario = int(input('Entre com o SALARIO do colaborador(a): '))
  dicionario_colaborador = {'id' : id,
                        'nome' : nome,
                        'setor' : setor,
                        'salario' : salario}
  lista_colaborador.append(dicionario_colaborador.copy())

def consultar_colaborador():
    print('MENU CONSULTAR COLABORADOR')
    while True:
      menu_consultar = input('\nEscolha a opção desejada: \n' +
                          '1 - Consultar TODOS os Colaboradores \n' +
                          '2 - Consultar Colaborador por ID \n' +
                          '3 - Colsultar Colaborador por SETOR \n' +
                          '4 - Retornar ao menu anterior \n' +
                          '>>')
      if menu_consultar == '1':
        print('Consultando TODOS os colaboradores...')
        for colaborador in lista_colaborador:
          print('\n▬▬▬▬▬▬▬▬▬▬▬▬ • ▬▬▬▬▬▬▬▬▬▬▬▬')
          for key, value in colaborador.items():
            print('\n{}: {}' .format(key, value))
      elif menu_consultar == '2':
        print('Consultando colaborador(es) por ID...')
        id_desejado = int(input('Entre com o ID do colaborador: '))
        for colaborador in lista_colaborador:
          if colaborador['id'] == id_desejado:
            print('\n▬▬▬▬▬▬▬▬▬▬▬▬ • ▬▬▬▬▬▬▬▬▬▬▬▬')
            for key, value in colaborador.items():
              print('\n{}: {}' .format(key, value))
      elif menu_consultar == '3':
        print('Consultando colaborador(es) por SETOR...')
        setor_desejado = input('Entre com o SETOR do colaborador: ')
        for colaborador in lista_colaborador:
          if colaborador['setor'] == setor_desejado:
            print('\n▬▬▬▬▬▬▬▬▬▬▬▬ • ▬▬▬▬▬▬▬▬▬▬▬▬')
            for key, value in colaborador.items():
              print('\n{}: {}' .format(key, value))
      elif menu_consultar == '4':
        print('Retornando ao menu anterior...')
        return
      else:
        print('Opção inválida! Entre com a opção novamente...')
        continue

def remover_colaborador():
  print('MENU REMOVER COLABORADOR(ES)')
  id_desejado = int(input('Entre com o ID do colaborador que deseja remover: '))
  for colaborador in lista_colaborador:
    if colaborador['id'] == id_desejado:
      lista_colaborador.remove(colaborador)
      print('Colaborador Removido com Sucesso!')


#Programa Principal#
print('Olá, bem vindo(a) ao controle de funcionários da Taynara Paes')
while True:
  menu_principal = input('\nEscolha a opção desejada: \n' +
                         '1 - Cadastrar Colaborador(es) \n' +
                         '2 - Consultar Colaborador(es) \n' +
                         '3 - Remover Colaborador(es) \n' +
                         '4 - Sair \n'
                         '>>')
  if menu_principal == '1':
    id_global = id_global + 1
    cadastrar_colaborador(id_global)
  elif menu_principal == '2':
    consultar_colaborador()
  elif menu_principal == '3':
    remover_colaborador()
  elif menu_principal == '4':
    print('Encerrando o programa... Obrigado!')
    break
  else:
    print('Opção inválida! Entre com a opção novamente...')
    continue