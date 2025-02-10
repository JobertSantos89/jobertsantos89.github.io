class Carro:
    def __init__(
        self, 
        marca: str, 
        modelo: str, 
        ano: int, 
        cor: str, 
        velocidade_maxima: float
    ):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, velocidade: float) -> bool:
        if self.velocidade_atual + velocidade >= self.velocidade_maxima:
            self.velocidade_atual = self.velocidade_maxima
        else:
            self.velocidade_atual += velocidade

        pode_acelerar = self.velocidade_atual != self.velocidade_maxima
        return pode_acelerar
        
    def frear(self, velocidade: float) -> bool:
        if self.velocidade_atual - velocidade <= 0:
            self.velocidade_atual = 0
        else:
            self.velocidade_atual -= velocidade
        
        pode_frear = self.velocidade_atual != 0
        return pode_frear


print('Você acabou de comprar um carro...')

marca = input('De qual marca é? ')
modelo = input('De qual modelo é? ')
ano = int(input('De qual ano é? '))
cor = input('De qual cor é?')
velocidade_maxima = float(input('De qual é a velocidade maxima do carro?'))

carro = Carro(marca, modelo, ano, cor, velocidade_maxima)

print('Você está saindo da concessionária, e acabou de entrar no carro...')
while True:
    print(f'Velocidade Atual: {carro.velocidade_atual} km/h')
    print(f'Velocidade Máxima: {carro.velocidade_maxima} km/h')

    print('O que deseja fazer?')
    print('[1] - Acelerar')
    print('[2] - Frear')
    print('[3] - Sair do Carro')
    opcao = input('--> ')

    if opcao == '1':
        velocidade = float(input('Quanto deseja acelerar?'))
        pode_acelerar = carro.acelerar(velocidade)
        
        if not pode_acelerar:
            print('Você atingiu a velocidade máxima.')

    elif opcao == '2':
        velocidade = float(input('Quanto deseja frear?'))

        pode_frear = carro.frear(velocidade)
        if not pode_frear:
            print('Você parou o carro.')

    elif opcao == '3':
        print('Você saiu do carro.')

        if carro.velocidade_atual != 0:
            print('Você morreu porque saiu do carro em movimento. BURRO')

        break
