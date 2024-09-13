#Você está criando um programa em Python para simular um jogo simples de adivinhação. O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar. O jogador terá até 3 tentativas para acertar o número.

#Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas até acertar ou atingir o limite de tentativas. Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.

#Variaveis para  armazenar o número secreto e o número de tentativas

numero_secreto = 7
tentativas = 0
max_tentativas = 3

#Estrutura de repetiçao  while para permitir que o jogador faça múltiplas tentativas

while tentativas < max_tentativas:
    tentativas += 1

    palpite = int (input(f"Tentativa {tentativas} de {max_tentativas}: Adivinhe o número (entre 1 e 10):")) #Variavel  para armazenar o palpite do jogador

# Estrutura  de condicional para verificar se o palpite do jogador está correto ou não

    if palpite == numero_secreto: 
        print(f"Você acertou! O número secreto!")
        break
else:
    print(f"Tente novamente ! O número secreto era {numero_secreto}.")  #Mensagem de encorajamento caso o jogador acerte


  



