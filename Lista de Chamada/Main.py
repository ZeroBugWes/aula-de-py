def main():
    quantAlunos = int(input("Digite a quantidade de alunos: "))

    while quantAlunos < 1:
        print("Número inválido, digite novamente")
        quantAlunos = int(input("Dígite a quantidade de alunos: "))

    nomes = [""] * quantAlunos

    i = 0 

    for i in range(len(nomes)):
     
     nomes[i] = input("Digite o nome do aluno:  ")
     
    print(nomes)
    return 0
main()
