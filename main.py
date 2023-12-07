def pegar_dados():
    peso = input("Informe seu peso: ")
    altura =input("Informe sua altura: ")

    if not peso or not altura:
        print("Informe peso e altura!")
        return pegar_dados()

    peso = float(peso)
    altura = float(altura)

    return peso, altura


def calcula_dados(peso, altura):
    imc = peso / (altura ** 2) * 10000
    resultado = round(imc, 2)

    if resultado < 18.5:
        print(f"Seu imc e de {resultado}. Adulto com baixo peso.")
    elif resultado < 25:
        print(f"Seu imc e de {resultado}. Adulto com peso adequado")
    elif resultado < 30:
        print(f"Seu imc e de {resultado}. Adulto com sobrepeso")
    elif resultado > 30:
        print(f"Seu imc e de {resultado}. Adulto com obesidade")


def main():
    peso, altura = pegar_dados()
    calcula_dados(peso, altura)


if __name__ == "__main__":
    main()
