import heapq
try:
    from graphviz import Digraph
    TEM_GRAPHVIZ = True
except ImportError:
    TEM_GRAPHVIZ = False

class GrafoRotas:
    """
    Representa uma rede de rotas aéreas onde:
    - Vértices = Aeroportos
    - Arestas = Voos (com peso representando distância ou tempo)
    """
    def __init__(self):
        # Estrutura: { 'Origem': { 'Destino': peso, 'Destino2': peso } }
        self.adjacencia = {}

    def adicionar_aeroporto(self, aeroporto):
        if aeroporto not in self.adjacencia:
            self.adjacencia[aeroporto] = {}
        else:
            print(f"Aviso: Aeroporto {aeroporto} já existe.")

    def adicionar_rota(self, origem, destino, peso):
        if origem not in self.adjacencia:
            self.adicionar_aeroporto(origem)
        if destino not in self.adjacencia:
            self.adicionar_aeroporto(destino)
        
        # Adiciona a rota
        self.adjacencia[origem][destino] = peso

    def remover_aeroporto(self, aeroporto):
        if aeroporto in self.adjacencia:
            del self.adjacencia[aeroporto]
            for origem in self.adjacencia:
                if aeroporto in self.adjacencia[origem]:
                    del self.adjacencia[origem][aeroporto]

    def consultar_voos_diretos(self, aeroporto):
        """Retorna dicionário de destinos diretos a partir de um aeroporto."""
        return self.adjacencia.get(aeroporto, {})

    def dijkstra_rota_mais_rapida(self, inicio, fim):
        if inicio not in self.adjacencia or fim not in self.adjacencia:
            return float('inf'), []

        fila = [(0, inicio)]
        
        distancias = {v: float('inf') for v in self.adjacencia}
        distancias[inicio] = 0
        predecessores = {v: None for v in self.adjacencia}
        
        visitados = set()

        while fila:
            dist_atual, atual = heapq.heappop(fila)

            if atual == fim:
                break
            
            if atual in visitados:
                continue
            visitados.add(atual)

            for vizinho, peso in self.adjacencia[atual].items():
                nova_dist = dist_atual + peso
                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist
                    predecessores[vizinho] = atual
                    heapq.heappush(fila, (nova_dist, vizinho))

        caminho = []
        passo = fim
        while passo is not None:
            caminho.append(passo)
            passo = predecessores[passo]
        caminho.reverse()

        if distancias[fim] == float('inf'):
            return float('inf'), []
        
        return distancias[fim], caminho

    # VISUALIZAÇÃO COM GRAPHVIZ
    def draw_tree(self, nome_arquivo="grafo_rotas", caminho_destaque=None):
        if not TEM_GRAPHVIZ:
            print("Aviso: Graphviz não instalado. Visualização pulada.")
            return
        dot = Digraph(comment="Rotas Aéreas")
        dot.attr(rankdir='LR')
        dot.attr('node', shape='ellipse', style='filled', color='lightblue2')

        # Adiciona nós e arestas
        for origem, destinos in self.adjacencia.items():
            dot.node(origem, origem)
            for destino, peso in destinos.items():
                cor = "black"
                espessura = "1"
                if caminho_destaque:
                    # Se origem e destino estão no caminho e são consecutivos
                    if origem in caminho_destaque and destino in caminho_destaque:
                        idx_origem = caminho_destaque.index(origem)
                        # Confere se o destino é o próximo na lista
                        if idx_origem + 1 < len(caminho_destaque) and caminho_destaque[idx_origem+1] == destino:
                            cor = "red"
                            espessura = "2.5"

                dot.edge(origem, destino, label=str(peso), color=cor, penwidth=espessura)

        try:
            dot.render(nome_arquivo, format='png', view=False, cleanup=True)
            print(f"Grafo salvo em: {nome_arquivo}.png")
        except Exception as e:
            print(f"Erro ao salvar imagem: {e}")

# MAIN
if __name__ == "__main__":
    sistema = GrafoRotas()

    print("\n--- 1. Adicionando rotas ---")
    sistema.adicionar_rota("GRU", "MIA", 8)  # São Paulo -> Miami (8h)
    sistema.adicionar_rota("GRU", "LIS", 10) # São Paulo -> Lisboa (10h)
    sistema.adicionar_rota("MIA", "JFK", 3)  # Miami -> Nova York (3h)
    sistema.adicionar_rota("MIA", "LHR", 9)  # Miami -> Londres (9h)
    sistema.adicionar_rota("JFK", "LHR", 7)  # Nova York -> Londres (7h)
    sistema.adicionar_rota("LIS", "LHR", 2)  # Lisboa -> Londres (2h)
    sistema.adicionar_rota("LIS", "CDG", 2.5)# Lisboa -> Paris (2.5h)
    
    print("Rotas cadastradas com sucesso.")

    print("\n--- 2. Consultando Voos de GRU ---")
    voos_gru = sistema.consultar_voos_diretos("GRU")
    print(f"Destinos a partir de GRU: {voos_gru}")

    print("\n--- 3. Calculando Melhor Rota (Dijkstra) ---")
    
    inicio = "GRU"
    fim = "LHR"
    custo, trajeto = sistema.dijkstra_rota_mais_rapida(inicio, fim)

    if custo < float('inf'):
        print(f"Melhor rota de {inicio} para {fim}:")
        print(f"Caminho: {' -> '.join(trajeto)}")
        print(f"Custo Total: {custo}")
        
        print("\n--- 4. Gerando Imagem com Rota Destacada ---")
        sistema.draw_tree("mapa_rotas", caminho_destaque=trajeto)
    else:
        print(f"Não existe rota entre {inicio} e {fim}.")