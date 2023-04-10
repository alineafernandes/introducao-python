import random

print("********************************")
print("Bem vindo ao jogo da adivinhação")
print("********************************")

numero_secreto = random.randrange(1,101)
tentativas = 0
pontos = 1000

print ("Qual nível de dificuldade?")
print ("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina um nível:"))

if (nivel == 1):
    tentativas = 20
elif (nivel == 2):
    tentativas = 10
else:
    tentativas = 5


for rodadas in range(1, tentativas + 1):
     print("Rodada {} de {}".format(rodadas, tentativas))

     chute_str = input("Digite seu número entre 1 e 100:")
     print("Você digitou", chute_str)
     chute = int(chute_str)

     if(chute < 1 or chute > 100):
         print("Você deve digitar um número entre 1 e 100!")
         continue

     acertou = chute == numero_secreto
     maior   = chute > numero_secreto
     menor   = chute < numero_secreto

     if (acertou):
        print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
        break
     else:
        if(maior):
            print("Não foi dessa vez! Seu chute foi maior do que o número secreto")
            if (rodadas == tentativas):
                print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
        elif(menor):
            print("Não foi dessa vez! Seu chute foi menor do que o número secreto")
            if (rodadas == tentativas):
                print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


print("Fim de jogo")