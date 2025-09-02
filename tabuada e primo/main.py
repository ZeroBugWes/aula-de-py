def main():
    inicio = int( input("Digite o inicio do seu intervalo: "))
    fim = int( input("Digite o fim do seu intervalo: "))

    if inicio <= fim:
        while inicio <= fim:
            i = 1
            print("Tabuada do ", inicio)
            while i < 11:
                print(inicio, "X", i, "=", inicio * i)
                i += 1
            inicio += 1
            print("\n")
    else: 
        while inicio >= fim:
            i = 1
            print("Tabuada do ", inicio)

            while i <= 10:
                print(inicio, "X", i, "= ",inicio*i) 
                i += 1  
            inicio -= 1
            print("\n")

            
    num = int (input("Digite um número: "))

    i = 2

    while num != i and num > 1:
        if num % i == 0:
            break
        i += 1
    
    if num == i:
        print("O numero ", num, " é primo")
    else:
        print("O número ", num, " não é primo")

    return 0

    return 0
main()