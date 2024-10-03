nome = input("Digite o nome do herói: ")
nivelExperiencia = int(input("Digite o xp do herói: "))

texto = f"O herói de nome {nome} está no nível de "

if (nivelExperiencia <= 1000):
    print(texto + "Ferro")
elif (nivelExperiencia > 1000 and nivelExperiencia <= 2000):
    print(texto + "Bronze")
elif (nivelExperiencia > 2000 and nivelExperiencia <= 5000):
    print(texto + "Prata")
elif (nivelExperiencia > 5000 and nivelExperiencia <= 7000):
    print(texto + "Ouro")
elif (nivelExperiencia > 7000 and nivelExperiencia <= 8000):
    print(texto + "Platina")
elif (nivelExperiencia > 8000 and nivelExperiencia <= 9000):
    print(texto + "Ascendente")
elif (nivelExperiencia > 9000 and nivelExperiencia <= 10000):
    print(texto + "Imortal")
elif (nivelExperiencia > 10000):
    print(texto + "Radiante")

