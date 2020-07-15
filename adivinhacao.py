print("*********************************")
print("Bem-Vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentivas = 3

for tentativa in range(1, total_tentivas + 1):
    print("Tentativa {} de {}".format(tentativa, total_tentivas))
    chutestr = input("Digite um número entre 0 e 100:")
    print("Você digitou o número:", chutestr)
    chute = int(chutestr)

    if(chute < 1 or chute > 100):
        print("O número precisa ser maior que ou igual a 1 e menor que 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto")

print("***************")
print("O jogo terminou")
print("***************")