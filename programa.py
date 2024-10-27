from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida

nova_frota = [
    {"nome": "porta-aviões", "tamanho": 4, "quantidade": 1},
    {"nome": "navio-tanque", "tamanho": 3, "quantidade": 2},
    {"nome": "contratorpedeiro", "tamanho": 2, "quantidade": 3},
    {"nome": "submarino", "tamanho": 1, "quantidade": 4}
]

def posicionar_frota():
    frota = {}
    
    for navio in nova_frota:
        nome = navio["nome"]
        tamanho = navio["tamanho"]
        quantidade = navio["quantidade"]
        
        for i in range(quantidade):
            while True:
                print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
                
                linha = int(input("Digite a linha: "))
                coluna = int(input("Digite a coluna: "))
                
                if tamanho > 1:
                    orientacao = int(input("Digite a orientação (1 para vertical, 2 para horizontal): "))
                    orientacao = 'vertical' if orientacao == 1 else 'horizontal'
                else:
                    orientacao = 'vertical' #tipo assim mds
                
                if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                    frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                    break
                else:
                    print("Esta posição não está válida!")
    
    return frota

frota_jogador = posicionar_frota()
print(frota_jogador)
