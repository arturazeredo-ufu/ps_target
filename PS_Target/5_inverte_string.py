# Programa que inverte uma string

# Função que transforma uma string em uma lista
def string_para_lista(string):
    lista = []
    for letras in string:
        lista.append(letras)
    return lista

# Função que inverte uma string


def inverte_string(string):
    lista_invertida = []
    lista_nao_invertida = string_para_lista(string)
    i = len(lista_nao_invertida)
    while i > 0:
        lista_invertida.append(lista_nao_invertida[i-1])
        i -= 1
    return ''.join(map(str, lista_invertida))


# MAIN
palavra = input("Digite uma palavra a ser invertida: ")
string_invertida = inverte_string(palavra)
print(string_invertida)
