transacoes = ['luz', 'agua','mercado','lazer','educação']
preco = [500,300,1500,100,800]
data = ['03/06/2026','23/06/2026','05/06/2026','10/07/2026','08/07/2026']

#criando um range para mostrar a quantidade de posições 
posicao = range(5)


for i, item_transacoes, preco_item, item_data in zip(transacoes,preco,data):
    print (f'posicao{i},Processamentos dos dados de pagamento: {item_transacoes}, {preco_item}, {item_data}')