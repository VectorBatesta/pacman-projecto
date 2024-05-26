import copy





class nodeState:
    def __init__(self, matriz, pai = None, movimento = None, nivel = 0):
        self.matriz = matriz
        self.filhos = []
        self.pai = pai
        self.movimento = movimento
        self.nivel = nivel
        self.errados = 0
        self.heuristico = 0
        # ...












def gerar_filhos(nodePai: nodeState):
    listaGerada = []
    
    posicao = -1
    #acha a posicao do zero pra fazer trocas
    for i in range(9):
        if nodePai.matriz[i] == 0:
            posicao = i
            break
    if posicao == -1:
        exit(f'caceta cade o zero: {nodePai.matriz}')

    #[XX ]
    #[XX ]
    #[XX ]
    #troca direita
    if posicao in (0, 1, 3, 4, 6, 7):
        novoFilho = copy.deepcopy(nodePai) #cria copia ao inves de fazer referencia
        novoFilho.matriz[posicao] = novoFilho.matriz[posicao + 1]
        novoFilho.matriz[posicao + 1] = 0
        novoFilho.movimento = 'direita'
        novoFilho.nivel += 1
        novoFilho.pai = nodePai #apenas referencia do pai
        nodePai.filhos.append(novoFilho)
        
        listaGerada.append(novoFilho)
        # print(novoFilho.matriz)

    #[ XX]
    #[ XX]
    #[ XX]
    #troca esquerda
    if posicao in (1, 2, 4, 5, 7, 8):
        novoFilho = copy.deepcopy(nodePai) #cria copia ao inves de fazer referencia
        novoFilho.matriz[posicao] = novoFilho.matriz[posicao - 1]
        novoFilho.matriz[posicao - 1] = 0
        novoFilho.movimento = 'esquerda'
        novoFilho.nivel += 1
        novoFilho.pai = nodePai #apenas referencia do pai
        nodePai.filhos.append(novoFilho)
        
        listaGerada.append(novoFilho)
        # print(novoFilho.matriz)

    #[XXX]
    #[XXX]
    #[   ]
    #troca baixo
    if posicao in (0, 1, 2, 3, 4, 5):
        novoFilho = copy.deepcopy(nodePai) #cria copia ao inves de fazer referencia
        novoFilho.matriz[posicao] = novoFilho.matriz[posicao + 3]
        novoFilho.matriz[posicao + 3] = 0
        novoFilho.movimento = 'baixo'
        novoFilho.nivel += 1
        novoFilho.pai = nodePai #apenas referencia do pai
        nodePai.filhos.append(novoFilho)
        
        listaGerada.append(novoFilho)
        # print(novoFilho.matriz)

    #[   ]
    #[XXX]
    #[XXX]
    #troca cima
    if posicao in (3, 4, 5, 6, 7, 8):
        novoFilho = copy.deepcopy(nodePai) #cria copia ao inves de fazer referencia
        novoFilho.matriz[posicao] = novoFilho.matriz[posicao - 3]
        novoFilho.matriz[posicao - 3] = 0
        novoFilho.movimento = 'cima'
        novoFilho.nivel += 1
        novoFilho.pai = nodePai #apenas referencia do pai
        nodePai.filhos.append(novoFilho)
        
        listaGerada.append(novoFilho)
        # print(novoFilho.matriz)
        
    return listaGerada









def printanode(X: nodeState):
    for i in range(9):
        if X.matriz[i] == 0:
            X.matriz[i] = ' '
    
    print(f'matriz: ', end='')
    for i in range(3):
        print(f'{X.matriz[i]}, ', end='')
    print(f'   nivel: {X.nivel}\t   movimento: {X.movimento}\t   errados: {X.errados}\theuristico: {X.heuristico}\n        ', end='')
    for i in range(3, 6):
        print(f'{X.matriz[i]}, ', end='')
    print(f'\n        ', end='')
    for i in range(6, 9):
        print(f'{X.matriz[i]}, ', end='')
    print(f'\n')
          
    for i in range(9):
        if X.matriz[i] == ' ':
            X.matriz[i] = 0














def arrumaMelhorPai(nodeFilho: nodeState, nodePai1: nodeState, nodePai2: nodeState):
    if nodePai1.nivel < nodePai2.nivel:
        nodeFilho.pai = nodePai1
        return 1
    elif nodePai2.nivel < nodePai1.nivel:
        nodeFilho.pai = nodePai2
        return 2




#escolhe melhor da lista
def escolheMelhor(lista):
    if lista == []:
        exit(f'bro pq q a lista ta empty')

    node_escolhido = None
    menorvalor = 999

    #acha o nó da lista com menor .errados
    for node in lista:
        if node.errados < menorvalor:
            menorvalor = node.errados
            node_escolhido = node

    lista.remove(node_escolhido)
    return node_escolhido #envia o nó da lista com errados menor pro return







def atualizaErrados(node: nodeState, matrizobj):
    node.errados = 0

    for i in range(9):
        if node.matriz[i] != matrizobj[i]:
            node.errados += 1

    return node.errados   






def printaCaminhoAteRaiz(filhoFinal: nodeState):
    movimentos = []
    while filhoFinal.pai != None:
        movimentos.append(filhoFinal.movimento)
        filhoFinal = filhoFinal.pai
    
    for i in reversed(range(len(movimentos))):
        print(f'{movimentos[i]}, ', end='')