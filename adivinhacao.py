print("*********************************")
print("Bem-Vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentivas = 3
tentativa = 1

while(tentativa <= total_tentivas):
    print("Tentativa", tentativa,  "de", total_tentivas)
    chutestr = input("Digite um número: ")
    chute = int(chutestr)

    print("Você digitou o número:", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto")
    tentativa = tentativa + 1

print("***************")
print("O jogo terminou")
print("***************")