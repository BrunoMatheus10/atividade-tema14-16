# Programa para calcular a soma dos números pares entre zero e um número par fornecido

# Leitura do número par fornecido pelo usuário
numero = int(input("Digite um número par: "))

# Verificação se o número é par
if numero % 2 != 0:
    print("Por favor, digite um número par.")
else:
    # Cálculo da soma dos números pares
    soma_pares = sum(i for i in range(0, numero + 1, 2))

    # Exibição do resultado
    print("A soma dos números pares entre 0 e", numero, "é:", soma_pares)
