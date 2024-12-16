# Definir as variáveis
preco_unitario = float(input("Preço unitário do item: R$ "))
quantidade = int(input("Quantidade de itens: "))

# Calcular o total
total = preco_unitario * quantidade

# Definir o percentual de desconto
desconto_percentual = 10  # exemplo de 10%

# Calcular o valor do desconto
desconto = total * (desconto_percentual / 100)

novo_valor = total - desconto

# Exibir os resultados
print(f"Valor total: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"O novo valor dos itens vai ser: R$ {novo_valor}")
193