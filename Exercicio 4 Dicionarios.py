agenda = {"Luiz": ["(19) 987654321", "(19) 123456789"], 
              "Carlos": ["(19) 11111111111", "(19) 00000000000"], 
              "Silva": ["(19) 2222222222", "(19) 33333333333333"]}
# print(dicionario)
for nome, telefones in agenda.items():
    print(f"\nContato: {nome}")
    for telefone in telefones:
        print(f" - Telefone: {telefone}")