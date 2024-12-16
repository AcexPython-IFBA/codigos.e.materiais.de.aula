
# Solicita dimensões do retângulo
### A função input() permite ao usuário digitar algo no terminal e retorna isso como uma string
largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

# Calcula o perímetro
perimetro = 2 * (largura + altura)

# Exibe o resultado
print(f"O perímetro do retângulo é: {perimetro}cm")