import textwrap

def menu():
    selecao_menu = """ \n
    ===================== TIPO DE PRODUTO =====================
    [A] - \tAlimentação
    [L] - \tLimpeza
    [V] - \tVestuário
    [C] - \tCancelar Compra
    ============================================================
    """
    return input(textwrap.dedent(selecao_menu)).strip().upper()

def valores (preco_produto, tipo_produto, refrigeracao_produto):
    #Valores adicionais utilizando dicionário
    valor_adicional = {
        'N': {
            'A': (2.00, 5.00),
            'L': (1.50, 2.50),
            'V': (3.00, 2.50)
        },
        'S': {
            'A': 8.00,
            'L': 0.00,
            'V': 0.00
        }
    }

    #calculo de imposto
    imposto = 0.05 if preco_produto < 25.00 else 0.08

    #valor adicional de acordo com tipo e refrigeração
    if refrigeracao_produto == 'N':
        if preco_produto < 15.00:
            adicional = valor_adicional['N'][tipo_produto][0]
        else:
            adicional = valor_adicional['N'][tipo_produto][1]
    else:
        adicional = valor_adicional['S'][tipo_produto]

    #imposto sobre o preço
    valor_imposto = preco_produto * imposto

    #preco de custo (preco + imposto)
    preco_custo = preco_produto + valor_imposto

    #descontos
    desconto = 0.03 if tipo_produto == 'A' and refrigeracao_produto == 'S' else 0.00

    #calculo de novo preco
    valor_desconto = preco_custo * desconto
    preco_final = preco_custo + adicional - valor_desconto

    #classificacao de preço
    if preco_final <= 50.00:
        classificacao = 'Barato'
    elif 50.00 < preco_final < 100.00:
        classificacao = 'Normal'
    else:
        classificacao = 'Caro'

    return preco_final, classificacao

#ao inserir valor de produto com virgula, substitui por ponto - reconhecimento de float
def entrada_produto(valor):
   return valor.replace(",", ".")

#interação com usuário
def main():
    preco_produto = entrada_produto(input("Qual o preço do produto? "))
    preco_produto = float(preco_produto)
    tipo_produto = menu()
    if tipo_produto == 'C':
        print("Compra cancelada!")
        exit()
    refrigeracao_produto = input("O produto precisa de refrigeração? [S/N] ").strip().upper()

    preco_final, classificacao = valores(preco_produto, tipo_produto, refrigeracao_produto)

    print(f"O preço final do produto é R${preco_final:.2f} e a classificação é {classificacao}.\n Obrigado por comprar conosco!")

if __name__ == '__main__':
    main()
