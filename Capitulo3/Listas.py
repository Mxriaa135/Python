marca=[]
modelo=[]
motor=[]
potencia=[]

resposta = "SIM"
while resposta == "SIM":
    marca.append(input("Digite a marca do carro: "))
    modelo.append(input("O modelo: "))
    motor.append(input("O motor: "))
    potencia.append(input("A potencia: "))
    resposta=input("Deseja adicionar mais algum carro?(SIM/NÃO): ").upper()

for carro in range(0,len(marca),1):
    print("Marca:", marca[carro])
    print("Modelo:", modelo[carro])
    print("motor:", motor[carro])
    print("potencia:", potencia[carro])
    print("--------------------------------------")
