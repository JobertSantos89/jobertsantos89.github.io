def calcular_imc(peso: float, altura: float) -> float:
    return peso / altura ** 2

def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return 'ABAIXO_DO_PESO'
    elif imc < 25:
        return 'PESO_IDEAL'
    elif imc < 30:
        return 'SOBREPESO'
    elif imc < 35:
        return 'OBESIDADE_I'
    elif imc < 40:
        return 'OBESIDADE_II'
    else:
        return 'OBSIDADE_III'


peso = float(input('Digite um peso: '))
altura = float(input('Digite uma altura: '))

imc = calcular_imc(peso, altura)
situacao = classificar_imc(imc)

print(f'O seu imc é: {imc:.2f}')
print(f'Situação: {situacao}')