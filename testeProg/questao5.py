print("de acordo com a tabela informe seu codigo:")
print("1 = Secretario")
print("2 = Professor")
print("3 = Coordenador")
print("4 = Diretor")
print("5 = Atendente")
codigo = int(input("Informe seu codigo relacionado ao seu cargo:"))


if codigo == 1:
    print(f"seu salário é de:{(codigo*10)/100}")
elif codigo == 2:
    print(f"seu salário é de:{(codigo*25)/100}")
elif codigo == 3:
    print(f"seu salário é de:{(codigo*11)/100}")
elif codigo == 4:
    print(f"seu salário é de:{codigo}")
elif codigo == 5:
    print(f"seu salário é de:{(codigo*15)/100}")
