transacoes = ['luz', 'agua','mercado','lazer','educação']
preco = [500,300,1500,100,800]
data = ['03/06/2026','23/06/2026','05/06/2026','10/07/2026','08/07/2026']

#Montando o menu de opções do sistema
while True:
     print("Olá eu sou o seu primeiro assitente financeiro")
     print("\n" + "=" *30)
     print("1 - Visualiza o extrato da conta")
     print("2 - Adiciona uma nova transação")
     print("3 - Vero total de gastos")
     print("Digite 'q' para sair do sistema")
     print("\n" + "=" *30 )
     opcao = input("Escolha uma opção").strip().lower()
     if opcao == 'q':
          print("\n saindo do sistema")
          break
     elif opcao == '1':
      print("\n = 1- Visualiza o extrato atual")
      for i, item_transacoes, preco_item, item_data in zip(range(len(transacoes)),transacoes,preco,data):
        print (f'posicao{i}Processamentos dos dados de pagamento: {item_transacoes},{preco_item},{item_data}')
     
     elif opcao == '2':
          print("\n Cadastrar uma nova transação:")
          novo_item = input("Digite o nome do gasto:(ex: Luz)")
          novo_preco = input (float(input("Informe o preço")))
          nova_data = input ("Digite a data:(ex 10-05-2026)")
          transacoes.append(novo_item)
          preco.append(novo_preco)
          data.append(nova_data)
          print(f"\n Sucesso!'{novo_item}' foi adicionado!  ")

     elif opcao=="3":
         print("o Total é: ")
         total=sum(preco)
         print()
         print(f"O total acumulado das suas despesas é: R$ {total:.2f}")
     else:
        print("\nOpção inválida! Por favor, escolha 1, 2, 3 ou q.")