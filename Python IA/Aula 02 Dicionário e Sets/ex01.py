# Ex01. Faça um programa onde o usuário deve inserir 5 frutas, ao finalizar a inserção, mostre todas as frutas unicas que foram inseridas. (Remova os Duplicados)

frutas = []

for _ in range(5):
    fruta = input('Digite uma fruta: ')
    frutas.append(fruta.capitalize())

frutas = list(set(frutas))

print('Frutas Inseridas: ')
for fruta in frutas:
    print(f'- {fruta}')