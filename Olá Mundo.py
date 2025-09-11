while True:
    n = int(input("digite o primeiro numero inteiro\n"))
    m = int(input("digite o segundo numero inteiro\n"))
    soma = n + m
    if n == 0 or m == 0:
        print("Programa encerrado")
        break
    else:
        print("A soma entre", n, "e", m, "é igual a", soma)
