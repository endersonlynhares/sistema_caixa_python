from PySimpleGUI import PySimpleGUI as sg
import json

#LAYOUT
sg.theme("DarkBlue2")
layout = [
    [sg.Text("Produto: ", size=(9, 0)), sg.Input(key="produto")],
    [sg.Text("Valor ", size=(9, 0)), sg.Input(key="preco")],
    [sg.Button("Adicionar ao carrinho"),sg.Button("Somar carrinho") , sg.Button("Finalizar compra")]
]

#WINDOW
janela = sg.Window("CAIXA PYTHON", layout)

#CAMPO DE VARIAVEIS
total_produtos = [] #variavel que guarda os produtos dentro de uma venda
soma_produtos = [] #variavel que guarda a soma total do preco do produto de uma venda
total_vendas = [] #variavel que guarda todas as vendas

#EVENTOS E VALORES
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Adicionar ao carrinho":
        preco_produto = float(valores["preco"])
        total_produtos.append(
            {
                "Produto": valores["produto"],
                "Preço": valores["preco"]
            }
        )
        soma_produtos.append(preco_produto)
        print(f'O produto {valores["produto"]} com preço de R${preco_produto:.2f} foi adicionado ao carrinho!')
    if eventos == "Somar carrinho":
        total = sum(soma_produtos)
        sg.popup(f'A soma dos produtos deram: R${total:.2f}',)
    if eventos == "Finalizar compra":
        total_vendas.append(total_produtos)
        sg.popup("VENDA FINALIZADA! VEJA O JSON ou o SITE")
        print("###COMPRA FINALIZADA###")
        with open("vendas.json",'w', encoding='utf-8') as f:
            json.dump(total_vendas,f, ensure_ascii=False, indent=4)

        total_produtos = []
        soma_produtos = []
