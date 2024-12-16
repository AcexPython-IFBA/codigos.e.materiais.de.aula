# Definir as variáveis
preco_unitario = float(input("Preço unitário do item: R$ "))
quantidade = int(input("Quantidade de itens: "))

# Calcular o total
total = preco_unitario * quantidade

# Definir o percentual de desconto
desconto_percentual = 10  # exemplo de 10%

# Calcular o valor do desconto
desconto = total * (desconto_percentual / 100)

# Exibir os resultados
print(f"Valor total: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
