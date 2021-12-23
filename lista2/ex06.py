valor_por_hora = int(input("Digite o valor da sua hora: "))
horas_trabalhadas = int(input('Digite quantas horas você trabalhou esse mês: '))
valor_mensal_bruto = valor_por_hora * horas_trabalhadas
ir = 11/100
inss = 8/100
sindicato = 5/100
print(f'Seu salárfiol bruto é de R$ {valor_mensal_bruto}')
valor_ir = (valor_mensal_bruto * ir)
valor_inss = (valor_mensal_bruto * inss)
valor_sindicato = (valor_mensal_bruto * sindicato)
print(f'Você pagou R$ {valor_ir: .2f} de Imposto de Renda')
print(f'Você pagou R$ {valor_inss: .2f} de INSS')
print(f'Você pagou R$ {valor_sindicato: .2f} de contribuição sindical')
salario_liquido = valor_mensal_bruto - valor_ir - valor_inss - valor_sindicato
print(f'Seu salário líquido é de R$ {salario_liquido}')