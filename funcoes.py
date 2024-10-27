def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        elif orientacao == "horizontal":
            posicoes.append([linha, coluna + i])

    return posicoes

def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
    resultado_define = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome in frota:
        frota[nome].append(resultado_define)
    else:
        frota[nome] = [resultado_define]
    
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro_novo = [[0 for i in range(10)] for i in range(10)]
    for nome, posicoes in frota.items():
        for posicao in posicoes:
            for linha, coluna in posicao:
                tabuleiro_novo[linha][coluna] = 1

    return tabuleiro_novo

def afundados(frota, tabuleiro):
    navios = 0
    for info, posicao in frota.items():
        for posicoes in posicao:
            if all (tabuleiro[linha][coluna] == "X" for linha, coluna in posicoes):
                navios += 1
    return navios



