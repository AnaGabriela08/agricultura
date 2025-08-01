cult1 = "Arroz"
cult2 = "feijao"
cult3 = "tomates"
cult4 = "macaxeira"
cult5 = "abacaxi"

investimento1 = {"arrendamento": 8000.0, "maodeobra": 6400.0, "mudas": 1500.0, "energia": 754.0, "insumos": 1080.0}
venda1 = {"valor_quilo": 20.00, "quantidade": 2800.0}
lucrobruto1 = venda1["valor_quilo"] * venda1["quantidade"]
custo1 = investimento1["arrendamento"] + investimento1["maodeobra"] + investimento1["energia"] + investimento1["insumos"]
lucroliquido1 = lucrobruto1 - custo1

investimento2 = {"arrendamento": 650.0, "maodeobra": 1020.0, "mudas": 26020.0, "energia": 130.0, "insumos": 2300.0}
venda2 = {"valor_quilo": 5.0, "quantidade": 2600.0}
lucrobruto2 = venda2["valor_quilo"] * venda2["quantidade"]
custo2 = investimento2["arrendamento"] + investimento2["maodeobra"] + investimento2["energia"] + investimento2["insumos"]
lucroliquido2 = lucrobruto2 - custo2

investimento3 = {"arrendamento": 650.0, "maodeobra": 3600.0, "mudas": 8000.0, "energia": 380.0, "insumos": 9000.0}
venda3 = {"valor_unidade": 1.50, "quantidade": 15080.0}
lucrobruto3 = venda3["valor_unidade"] * venda3["quantidade"]
custo3 = investimento3["arrendamento"] + investimento3["maodeobra"] + investimento3["energia"] + investimento3["insumos"]
lucroliquido3 = lucrobruto3 - custo3  

investimento4 = {"arrendamento": 600.0, "maodeobra": 610.0, "mudas": 50200.0, "energia": 760.0, "insumos": 1500.0}
venda4 = {"valor_quilo": 35.00, "quantidade": 120400.0}
lucrobruto4 = venda4["valor_quilo"] * venda4["quantidade"]
custo4 = investimento4["arrendamento"] + investimento4["maodeobra"] + investimento4["energia"] + investimento4["insumos"]
lucroliquido4 = lucrobruto4 - custo4

investimento5 = {"arrendamento": 460.0, "maodeobra": 300.0, "mudas": 10560.0, "energia": 1200.0, "insumos": 6000.0}
venda5 = {"valor_unidade": 2.50, "quantidade": 300000.0}
lucrobruto5 = venda5["valor_unidade"] * venda5["quantidade"]
custo5 = investimento5["arrendamento"] + investimento5["maodeobra"] + investimento5["energia"] + investimento5["insumos"]
lucroliquido5 = lucrobruto5 - custo5


menu = f"Bem-vindo ao sistema de produção Agropop!\n" \
         f"1. {cult1}\n" \
         f"2. {cult2}\n" \
         f"3. {cult3}\n" \
         f"4. {cult4}\n" \
         f"5. {cult5}\n"
print(menu)
escolha = input("Escolha uma cultura : ")
hectares = float(input("Informe a área em hectares: "))

investimento1 = {k: v * hectares for k, v in investimento1.items()}
investimento2 = {k: v * hectares for k, v in investimento2.items()}
investimento3 = {k: v * hectares for k, v in investimento3.items()}
investimento4 = {k: v * hectares for k, v in investimento4.items()}  
investimento5 = {k: v * hectares for k, v in investimento5.items()}

if escolha == "1":
    print(f"Cultura selecionada: {cult1}")
    print("Custos:")
    for gasto, valor in investimento1.items():
        if gasto in ["arrendamento", "maodeobra", "energia", "insumos"]:
            print(f"{gasto}: R$ {valor:.2f}")
    print(f"Lucro Bruto: R$ {lucrobruto1:.2f}")
    print(f"Lucro Líquido: R$ {lucroliquido1:.2f}")

elif escolha == "2":
    print(f"Cultura selecionada: {cult2}")
    print("Gastos:")
    for gasto, valor in investimento2.items():
        if gasto in ["arrendamento", "maodeobra", "energia", "insumos"]:
            print(f"{gasto}: R$ {valor:.2f}")
    print(f"Lucro Bruto: R$ {lucrobruto2:.2f}")
    print(f"Lucro Líquido: R$ {lucroliquido2:.2f}")

elif escolha == "3":
    print(f"Cultura selecionada: {cult3}")
    print("Gastos:")
    for gasto, valor in investimento3.items():
        if gasto in ["arrendamento", "maodeobra", "energia", "insumos"]:
            print(f"{gasto}: R$ {valor:.2f}")
    print(f"Lucro Bruto: R$ {lucrobruto3:.2f}")
    print(f"Lucro Líquido: R$ {lucroliquido3:.2f}")

elif escolha == "4":
    print(f"Cultura selecionada: {cult4}")
    print("Gastos:")
    for gasto, valor in investimento4.items():
        if gasto in ["arrendamento", "maodeobra", "energia", "insumos"]:
            print(f"{gasto}: R$ {valor:.2f}")
    print(f"Lucro Bruto: R$ {lucrobruto4:.2f}")
    print(f"Lucro Líquido: R$ {lucroliquido4:.2f}")

elif escolha == "5":
    print(f"Cultura selecionada: {cult5}")
    print("Gastos:")
    for gasto, valor in investimento5.items():
        if gasto in ["arrendamento", "maodeobra", "energia", "insumos"]:
            print(f"{gasto}: R$ {valor:.2f}")
    print(f"Lucro Bruto: R$ {lucrobruto5:.2f}")
    print(f"Lucro Líquido: R$ {lucroliquido5:.2f}")

else:
    print(ValueError("tipo de cultura nâo encontrado! Por favor, escolha outro tipo."))

