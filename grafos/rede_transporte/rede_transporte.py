import heapq
try:
    from graphviz import Digraph
    TEM_GRAPHVIZ = True
except ImportError:
    TEM_GRAPHVIZ = False

class RedeTransporte:
    """
    Representa uma rede de transporte público (Metrô/Ônibus).
    - Vértices: Estações
    - Arestas: Conexões entre estações (com peso em minutos)
    """

    def __init__(self):
        # Grafo: { 'Estacao A': {'Estacao B': 5, 'Estacao C': 10} }
        self.grafo = {}

    def adicionar_estacao(self, nome):
        """Cria uma nova estação na rede se ela não existir."""
        if nome not in self.grafo:
            self.grafo[nome] = {}

    def adicionar_conexao(self, origem, destino, tempo_minutos):
        """
        Cria uma conexão unidirecional. 
        Para linhas de mão dupla, chame a função duas vezes (A->B e B->A).
        """
        if origem not in self.grafo:
            self.adicionar_estacao(origem)
        if destino not in self.grafo:
            self.adicionar_estacao(destino)
        
        self.grafo[origem][destino] = tempo_minutos

    def buscar_caminho_mais_rapido(self, inicio, fim):
        """
        Algoritmo de Dijkstra para encontrar o trajeto de menor tempo.
        Retorna: (tempo_total, lista_de_estacoes)
        """
        if inicio not in self.grafo or fim not in self.grafo:
            return float('inf'), []

        # Fila de prioridade: (tempo_acumulado, estacao_atual)
        fila = [(0, inicio)]
        
        tempos = {estacao: float('inf') for estacao in self.grafo}
        tempos[inicio] = 0
        
        predecessores = {estacao: None for estacao in self.grafo}
        visitados = set()

        while fila:
            tempo_atual, estacao_atual = heapq.heappop(fila)

            if estacao_atual == fim:
                break
            
            if estacao_atual in visitados:
                continue
            visitados.add(estacao_atual)

            for vizinho, tempo_trecho in self.grafo[estacao_atual].items():
                novo_tempo = tempo_atual + tempo_trecho
                
                if novo_tempo < tempos[vizinho]:
                    tempos[vizinho] = novo_tempo
                    predecessores[vizinho] = estacao_atual
                    heapq.heappush(fila, (novo_tempo, vizinho))

        caminho = []
        passo = fim
        while passo is not None:
            caminho.append(passo)
            passo = predecessores[passo]
        caminho.reverse()

        if tempos[fim] == float('inf'):
            return float('inf'), []

        return tempos[fim], caminho

    def draw_tree(self, nome_arquivo="mapa_metro", trajeto_destaque=None):
        if not TEM_GRAPHVIZ:
            print("Aviso: Graphviz não instalado. Visualização pulada.")
            return

        dot = Digraph(comment="Rede de Transporte")
        dot.attr(rankdir='LR')
        dot.attr('node', shape='rect', style='rounded,filled', color='lightgray', fontname='Arial')

        for origem, conexoes in self.grafo.items():
            dot.node(origem, origem)
            
            for destino, tempo in conexoes.items():
                cor = "black"
                espessura = "1"
                label = f"{tempo} min"

                # Verifica se a conexão faz parte do caminho destaque
                if trajeto_destaque:
                    if origem in trajeto_destaque and destino in trajeto_destaque:
                        idx = trajeto_destaque.index(origem)
                        if idx + 1 < len(trajeto_destaque) and trajeto_destaque[idx+1] == destino:
                            cor = "red"
                            espessura = "3"
                            label += " (Melhor)"

                dot.edge(origem, destino, label=label, color=cor, penwidth=espessura)

        try:
            dot.render(nome_arquivo, format='png', view=False, cleanup=True)
            print(f"Mapa salvo em: {nome_arquivo}.png")
        except Exception as e:
            print(f"Erro ao salvar imagem: {e}")

# MAIN
if __name__ == "__main__":
    metro = RedeTransporte()
    
    print("\n--- Construindo Linhas de Metrô ---")
    
    # Linha Azul (Fictícia)
    metro.adicionar_conexao("Central", "Sé", 3)
    metro.adicionar_conexao("Sé", "Paraíso", 4)
    metro.adicionar_conexao("Paraíso", "Ana Rosa", 2)
    
    # Linha Verde (Cruzando)
    metro.adicionar_conexao("Consolação", "Paraíso", 5)
    metro.adicionar_conexao("Paraíso", "Klabin", 3)
    
    # Atalho (Linha Amarela)
    metro.adicionar_conexao("Central", "Consolação", 6)
    
    # Conexões de volta (Mão dupla simplificada)
    metro.adicionar_conexao("Consolação", "Central", 6)
    
    print("Rede montada.")

    inicio = "Central"
    fim = "Klabin"
    
    print(f"\n--- Calculando rota de {inicio} para {fim} ---")
    tempo, rota = metro.buscar_caminho_mais_rapido(inicio, fim)

    if tempo < float('inf'):
        print(f"Melhor trajeto encontrado ({tempo} min):")
        print(" -> ".join(rota))
        
        metro.draw_tree("mapa_metro", trajeto_destaque=rota)
    else:
        print("Não há rota disponível entre essas estações.")