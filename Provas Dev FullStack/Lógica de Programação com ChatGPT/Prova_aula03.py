#Você está criando um programa em Python para simular um jogo simples de adivinhação. O programa deve ter um número fixo, por exemplo, 7, 
#que o jogador deve adivinhar. O jogador terá até 3 tentativas para acertar o número. Implemente o jogo utilizando um loop while para 
#permitir que o jogador faça múltiplas tentativas até acertar ou atingir o limite de tentativas. Utilize a estrutura else para exibir 
#uma mensagem de encorajamento caso o jogador acerte e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.

# Definir o número fixo a ser adivinhado
numero_secreto = 7

# Definir o número máximo de tentativas
tentativas_restantes = 3

# Loop while para permitir múltiplas tentativas
while tentativas_restantes > 0:
    # Solicitar a tentativa do jogador
    palpite = int(input("Tente adivinhar o número (entre 1 e 10): "))

    # Verificar se o palpite está correto
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
    else:
        tentativas_restantes -= 1
        print(f"Errado! Você tem {tentativas_restantes} tentativas restantes.")

# Usar o else para dar uma mensagem final
else:
    print("Que pena! Você esgotou suas tentativas. O número era 7.")
