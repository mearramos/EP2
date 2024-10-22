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
