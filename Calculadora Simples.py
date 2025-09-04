def calcular():
    while True:
        print("\n--- Calculadora Luiz Carlos ---")
        print("Selecione a operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha == '5':
            print("Encerrando a calculadora.")
            break

        if escolha not in ('1', '2', '3', '4'):
            print("Opção inválida. Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Use apenas números.")
            continue

        if escolha == '1':
            resultado = num1 + num2
            operacao = '+'
        elif escolha == '2':
            resultado = num1 - num2
            operacao = '-'
        elif escolha == '3':
            resultado = num1 * num2
            operacao = '*'
        elif escolha == '4':
            if num2 == 0:
                print("Erro: divisão por zero.")
                continue
            resultado = num1 / num2
            operacao = '/'

        print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")

# Inicia a calculadora
calcular()
