transacao = int(input("Informe quantas transações financeiras foram realizadas: "))
total_transacao = 0.0

for x in range(transacao):
    valor_transacao = float(input("Informe o valor da transação: R$ "))
    total_transacao += valor_transacao

print(f"Você realizou {transacao} transações financeiras e gastou o total de R$ {total_transacao:,.2f} \n"
      f"Em média R$ {total_transacao/transacao:,.2f} por transação")
