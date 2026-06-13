transacoes = ['Luz', 'Água', 'Mercado', 'Lazer', 'Educação']
preco = [500, 300, 1500, 100, 800]
data = ['3/06/2026', '01/06/2026', '19/06/2026', '25/06/2026', '30/05/2026']

# CORREÇÃO: range(5) gera a sequência numérica [0, 1, 2, 3, 4]
posicoes = range(5) 

# Agora o zip consegue combinar tudo perfeitamente!
for i, item_transacoes, preco_item, item_data in zip(posicoes, transacoes, preco, data):
    print(f'Posição {i} - Processamento dos dados de pagamento: {item_transacoes}, {preco_item}, {item_data}')

#Implementar consulta de lista