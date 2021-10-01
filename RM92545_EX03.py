num = int(input("Digite um número: "))
anterior = 0
proximo = 1
soma = 0
resultado = 0

print(soma)

while proximo < num:
    print(proximo)
    soma = proximo + anterior
    anterior = proximo
    proximo = soma

if num == proximo:
    print(soma)
    print(f"Você digitou {num}. Ação bem sucedida!")
else:
    print(f"Você digitou {num}. A ação falhou...")



