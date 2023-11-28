conta = float(input("Quantos minutos foi utilizado?"))
if conta < 200:
    print(f"sua conta é de:{conta*0.20}")
elif conta > 200 and conta < 400:
    print(f"sua conta é de:{conta*0.18}")
elif conta > 400 :
    print(f" sua conta é de:{conta*0.15}")