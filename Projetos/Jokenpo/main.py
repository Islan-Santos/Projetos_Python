# Um jogo de infancia para praticar um pouco minha programacao :)


import random

seq = ["Pedra", "Papel", "Tesora"]
computador = random.choice(seq)

pessoa = input("Escolha pedra, papel, ou tesoura: ")

print("O computador escolheu: ", computador)


if pessoa == "Pedra" or pessoa =="pedra":
    if computador == "Pedra":
        print("Empatou :) ")
    elif computador == "Papel":
        print("Perdeu :(")
    elif computador == "Tesora":
        print("Ganhou, uhuull")  
elif pessoa == "Papel" or pessoa =="papel":
    if computador == "Pedra":
        print("Ganhou, uhuull ")
    elif computador == "Papel":
        print("Empatou :) ")
    elif computador == "Tesora":
        print("Perdeu :(")       
elif pessoa == "Tesora" or pessoa =="tesora":
    if computador == "Pedra":
        print("Perdeu :( ")
    elif computador ==  "Papel":
        print("Ganhou, uhuull")
    elif computador == "Tesora":
        print("Empatou :)")     
    

    