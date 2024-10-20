# Listas
lista = ['Lucas', 'Ricardo', 'Pedro']

# Iterando a Lista (Diretamente)
# Quando utilizamos o "FOR" com uma lista, assim como em uma string, ele irá pegar cada elemento da lista, e para cada elemento irá executar o seu bloco de código
print('---- Nomes Inseridos ----')
for nome in lista:
    print(f'- {nome}')


# Iterando a Lista (Indiretamente)
# Também podemos iterar as listas utilizando os seus indíces
# No exemplo abaixo estou utilizando a função "LEN" para buscar o final do range (Como o final é -1, não preciso me preocupar porque o range sempre terá os mesmos indices da lista)
# Então, dentro do for, acessamos o elemento na posição do indice, em ordem.
for i in range(len(lista)):
    print(f'- {lista[i]}')

