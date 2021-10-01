refeicao = int(input("Informe quantas refeições foram feitas: "))
caloria_total = 0.0

for x in range(1, refeicao + 1):
    caloria_refeicao = float(input(f"Informe a quantidade de calorias da {x}ª refeição: "))
    caloria_total = caloria_total + caloria_refeicao

print(f"Você consumiu {caloria_total:,.2f} calorias, {caloria_total/refeicao:,.2f} calorias em média por refeição.")

