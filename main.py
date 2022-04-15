estoque = {
    
    "101" : ["Frankstein", 32.5],
    "102" : ["Grande Sertão: Veredas", 65.7],
    "103" : ["O Guarani",17.7]
    
}

relatorio = []

def novaVenda():
    
    subtotalDaVenda = 0
    
    print("---- NOVA VENDA ----")
    
    while (True):
        cache = []
        
        opcaoNovaVenda = input("Informe o código do livro (0 para sair):")
        if(opcaoNovaVenda == "0"): 
            break
        quantidade = int(input("Informe a quantidade:"))
        subtotalDaVenda += (estoque[opcaoNovaVenda][1])*quantidade
        print("Item “{}” adicionada à sacola".format(estoque[opcaoNovaVenda][0]))
        print("Subtotal da venda: R$ {:.2f}".format(subtotalDaVenda))
        
        cache.append(opcaoNovaVenda)
        cache.append(quantidade)
        relatorio.append(cache)
        
    print("--- Venda finalizada ---")
    
def relatorioDeVendas():
    
    print("""
    
-----------------------------------------------------
RELATÓRIO DE VENDAS
-----------------------------------------------------

    """)
    
    totalCompras = 0
    
    for i in range (len(relatorio)):
        numeroPedido = i + 1
        
        cache = relatorio[i]
        
        nomeProduto = estoque[cache[0]][0]
        quantidadeProduto = cache[1]
        subtotalProduto = (estoque[cache[0]][1]) * quantidadeProduto
        totalCompras += subtotalProduto
        
        print("**** Pedido #{}".format(numeroPedido))
        print("{} X {} .... R$ {:.2f}".format((nomeProduto),(quantidadeProduto),(subtotalProduto)))
        print("TOTAL: R$ {:.2f}".format(totalCompras))
    
while (True):
    
    print("""
    
    LIVRARIA PAPIRUS
    1 - Nova venda
    2 - Relatório de vendas
    0 - Sair
    
    """)
    opcao = int(input())
    
    
    if(opcao == 0): 
        break
    elif(opcao == 1):
        novaVenda()
    elif(opcao == 2):
        relatorioDeVendas()