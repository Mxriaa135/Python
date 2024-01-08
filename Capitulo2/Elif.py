nome=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))
doencaContagiosa=input("Suspeita de doença contagiosa?: ").upper()
if idade >= 65 and doencaContagiosa == "NÃO":
    print(nome + ", o senhor(a) tem direito ao atendimento prioritário!")
elif idade >= 65 and doencaContagiosa == "SIM":
    print(nome + ", aguarde na sala de espera reservada com direito ao atendimento prioritário!")
elif doencaContagiosa == "SIM":
    print(nome + ", aguarde na sala de espera reservada!")
else:
    print(nome + ", aguarde na sala de espera comum!")
