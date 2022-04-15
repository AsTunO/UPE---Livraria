estoque = {
    
    "101" : ["Frankstein", 32.5],
    "102" : ["Grande Sertão: Veredas", 65.7],
    "103" : ["O Guarani",17.7]
    
}

relatorio = []

def novaVenda():
    
    subtotalDaVenda = 0
    numeroCompra = 0
    
    print("---- NOVA VENDA ----")
    
    while (True):
        cache = []
        
        print("N° da compra : {}".format(numeroCompra + 1))
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
        
        opcaoRemove = input("Deseja cancerla alguma compra ? [1 - sim | 0 - não] :")
        
        if(opcaoRemove == "1"):
            opcaoNumeroCompra = int(input("Digite o numero da compra para cancelar : "))
            del(relatorio[(numeroCompra - 1)])
            
        numeroCompra += 1
        
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
    
def cadastrarLivros():
    print("""
-----------------------------------------------------
CADASTRAR LIVRO
-----------------------------------------------------
    """)
    while (True):
        confirmacaoCadastro = int(input("Deseja Cadastrar um livro: [1 - Sim | 0 - Sair] "))
        if(confirmacaoCadastro == 0):
            break
        else:
            idLivro = input("Informe o id do livro : ")
            nomeLivro = input("Informe o nome do livro : ")
            preco = float(input("Informe o valor do livro : "))
            cache = {idLivro : [nomeLivro, preco]}
            estoque.update(cache)

def rank():
    print("""
-----------------------------------------------------
RANK DOS LIVROS
-----------------------------------------------------
    """)
    rankLivros = {}
    for i in range(len(relatorio)):
        cacheRank = relatorio[i]
        idLivroRank = cacheRank[0]
        quantidadeLivroRank = cacheRank[1]
        cacheLivroAux = {idLivroRank : quantidadeLivroRank}
        rankLivros.update(cacheLivroAux)
    count = 1
    for i in sorted(rankLivros, key = rankLivros.get, reverse=True):
        print("{} - {} ".format(count, estoque[i][0]))
        count += 1
    

while (True):
    
    print("""
    
    LIVRARIA PAPIRUS
    1 - Nova venda
    2 - Relatório de vendas
    3 - Cadastrar novos Livros
    4 - Rank dos mais vendidos
    0 - Sair
    
    """)
    opcao = int(input())
    
    
    if(opcao == 0): 
        break
    elif(opcao == 1):
        novaVenda()
    elif(opcao == 2):
        relatorioDeVendas()
    elif(opcao == 3):
        cadastrarLivros()
    elif(opcao == 4):
        rank()
