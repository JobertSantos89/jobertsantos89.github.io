# Crie uma lista chamada numeros contendo os números de 1 a 5
numeros = [1, 2, 3, 4, 5]

# Acesse o terceiro elemento da lista numeros e atribua-o à variável terceiro_numero
terceiro_numero = numeros[2]

# Altere o valor do segundo elemento da lista numeros para 10
numeros[1] = 10

# Crie uma segunda lista chamada outra_lista com três números diferentes
outra_lista = [7, 8, 9]

# Concatene as listas numeros e outra_lista em uma nova lista chamada todas_as_listas
todas_as_listas = numeros + outra_lista

# Verifique o comprimento da lista todas_as_listas
comprimento_todas_as_listas = len(todas_as_listas)

# Utilize um loop for para imprimir cada elemento da lista todas_as_listas
print("Elementos da lista todas_as_listas:")
for elemento in todas_as_listas:
    print(elemento)

# Ordene a lista todas_as_listas em ordem decrescente e atribua o resultado a uma nova lista chamada lista_ordenada
lista_ordenada = sorted(todas_as_listas, reverse=True)

# Realize um slicing na lista lista_ordenada para obter uma sublista com os três maiores números
tres_maiores_numeros = lista_ordenada[:3]

# Imprima a sublista com os três maiores números
print("Três maiores números:", tres_maiores_numeros)