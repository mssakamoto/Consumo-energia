#Entrada das informações
Aparelho = input("Digite o nome do aparelho ( Ex: Geladeira):")
Potência = float(input("Digite a potência do aparelho em Watts(W):"))
HorasDia = float(input("Digite o tempo médio de uso em horas:"))
TarifaEnergia = float(input("Digite o valor da tarifa de energia R$/KWH (Ex:0.95):"))
#Processamento ( realização do cálculo)
ConsumoMensal = Potência*HorasDia*30/1000
ContaEnergia = ConsumoMensal*TarifaEnergia
#Saida - exibindo as informações
print(f"Aparelho: {Aparelho}")
print(f"Consumo estimado:{ConsumoMensal:.2f} KWH/mês")
print(f"A sua conta de energia será de R$/mês: {ContaEnergia: .2f}")