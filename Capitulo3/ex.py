import os 
os. system("cls")
equipamentos=[]
serial=[]
valor=[]

resposta = "SIM"
while resposta == "SIM":
    equipamentos.append(input("Equipamento: "))
    serial.append(input("Serial: "))
    valor.append(int(input("Valor: ")))
    resposta = input("Deseja adicionar mais algum equipamento?(Sim/Não): ").upper()


os. system("cls")
escolha = input("Deseja depreciar um equipamento ou excluir-lo?: ").upper()
if escolha == "DEPRECIAR":   
    busca = input("Digite o(s) nome(s) do(s) equipamento(s) que deseja depreciar 10% do seu valor: \n")
    for indice in range(0,len(equipamentos)):
        if busca == equipamentos[indice]:
            novoValor = valor[indice] - valor[indice]*0.10
            print(f"Serial: {serial[indice]}")
            print(f"Valor antigo: R${valor[indice]}")
            print(f"Novo valor: R${novoValor}")
            print(("*")*60,"\n")
        else:
            print("Nome inválido ou não existente")
elif escolha == "EXCLUIR":
    busca = input("Digite o(s) serial do(s) equipamento(s) que deseja excluir: \n")
    for indice in range(0,len(serial)):
        if busca == serial[indice]:
            del equipamentos[indice]
            del serial[indice]
            del valor[indice]
            print("Equipamento excluído com sucesso")
            break
        else:
            print("Serial inválido ou não existente")
else:
    print("Dado inválido")