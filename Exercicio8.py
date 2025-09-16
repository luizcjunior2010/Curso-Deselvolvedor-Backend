X = float(input("Digite a nota\n"))
if X > 0 and X < 100:    
    if X >= 70:
        print("Aprovado com excelência")    
    elif X < 70 and X >= 50:   
        print("Aprovado")
    else:
        print("Reprovado")
else:
    print("Nota inválida")



