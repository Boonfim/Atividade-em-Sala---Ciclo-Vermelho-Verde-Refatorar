def calcular_preco_final(preco_base, categoria):
    if categoria == "Livro":
        imposto = 0.0
        desconto = 0.10
    elif categoria == "Eletrônico":
        imposto = 0.20
        desconto = 0.05
    elif categoria == "Alimento":
        imposto = 0.05
        desconto = 0.0
    else:
        raise ValueError("Categoria inválida")

    preco_final = preco_base + (preco_base * imposto) - (preco_base * desconto)
    return preco_final