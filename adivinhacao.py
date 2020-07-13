print("*********************************")
print("Bem-Vindo ao jogo de adivinhação!")
print("*********************************")

numerosecreto = 42

chutestr = input("Digite um número: ")

chute = int(chutestr)

print("Você digitou o número: ", chute)

if(chute == numerosecreto):
    print("Você acertou!")
else:
    print("Você errou!")

print("***************")
print("O jogo terminou")
print("***************")