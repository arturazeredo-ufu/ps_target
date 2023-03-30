# tamanho máximo presente na sequencia
tamanho_maximo = int(input("Digite o valor máximo presente na sequência: "))
fibonacci = []  # array que armazenará os valores da sequência
# número a ser avaliado se está dentro da sequencia
no = int(input("Digite um número: "))


# sequencia de fibonacci

anterior = 0
proximo = 0

while (proximo < tamanho_maximo+1):
    fibonacci.append(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    if (proximo == 0):
        proximo += 1

if no in fibonacci:
    print("Seu número pertence à sequência de Fibonacci!")
else:
    print("Este número NÃO pertence à sequência de Fibonacci!")

print(fibonacci)
