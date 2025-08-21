def main():
    altura = float( input("Digite sua altura:  "))
    idade = int (input ("Digite sua idade:  "))
    isCasado =  input("Voce é casado?")
    nome = input("digite seu nome:  ")
    peso = float (input ("Digite seu peso: "))
    cpf = input("digite seu cpf:  ")
    sexo = input("digite seu sexo:  ")

    print("o ", nome, "mede ", altura, "m de altura, tem ", idade, "anos de idade")
    print("É do sexo ", sexo, ", pesa ",peso, " e seu CPF é: ", cpf)


    if isCasado == "S" or isCasado  ==  "s":
        print("O  ", nome, " é casado")
    elif isCasado  == "Sou" or isCasado  == "Sou":
        print("Ele é casado")
    else:
        print("O ", nome, "não é casado")


    return 0
main()
    
