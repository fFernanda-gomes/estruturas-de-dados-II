from collections import deque

try:
    from graphviz import Graph
    TEM_GRAPHVIZ = True
except ImportError:
    TEM_GRAPHVIZ = False

class RedeSocial:
    """
    Representa uma rede social onde:
    - Vértices: Usuários
    - Arestas: Amizades (Conexão bidirecional)
    """
    def __init__(self):
        # { 'Alice': {'Bob', 'Carol'}, 'Bob': {'Alice'} }
        self.grafo = {}

    def adicionar_usuario(self, nome):
        """Cadastra um novo usuário se não existir."""
        if nome not in self.grafo:
            self.grafo[nome] = set()

    def adicionar_amizade(self, u1, u2):
        """Cria uma conexão de amizade entre dois usuários."""
        if u1 not in self.grafo: self.adicionar_usuario(u1)
        if u2 not in self.grafo: self.adicionar_usuario(u2)
        
        self.grafo[u1].add(u2)
        self.grafo[u2].add(u1)

    def listar_amigos(self, usuario):
        return list(self.grafo.get(usuario, []))

    def sugerir_amigos(self, usuario):
        if usuario not in self.grafo:
            return []

        amigos_diretos = self.grafo[usuario]
        sugestoes = set()

        for amigo in amigos_diretos:
            for amigo_do_amigo in self.grafo[amigo]:
                # Regras para sugerir:
                # 1. Não pode ser o próprio usuário
                # 2. Não pode ser alguém que já é amigo
                if amigo_do_amigo != usuario and amigo_do_amigo not in amigos_diretos:
                    sugestoes.add(amigo_do_amigo)
        
        return list(sugestoes)

    def verificar_conexao(self, inicio, fim):
        if inicio not in self.grafo or fim not in self.grafo:
            return False, []

        fila = deque([(inicio, [inicio])])
        visitados = set([inicio])

        while fila:
            atual, caminho = fila.popleft()

            if atual == fim:
                return True, caminho

            for vizinho in self.grafo[atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append((vizinho, caminho + [vizinho]))
        
        return False, []

    # VISUALIZAÇÃO
    def draw_tree(self, nome_arquivo="rede_social", destaque_usuario=None):
        if not TEM_GRAPHVIZ:
            print("Aviso: Graphviz não instalado. Visualização pulada.")
            return

        dot = Graph(comment="Rede Social", strict=True) 
        dot.attr(layout='neato')
        dot.attr('node', shape='circle', style='filled', color='lightblue', fontname='Arial')

        arestas_desenhadas = set()

        for usuario, amigos in self.grafo.items():
          # Cor especial se for o usuário em destaque
          cor_no = 'lightblue'
          if destaque_usuario and usuario == destaque_usuario:
              cor_no = 'gold'
          elif destaque_usuario and usuario in self.grafo[destaque_usuario]:
              cor_no = 'lightgreen' # Amigos diretos em verde

          dot.node(usuario, usuario, color=cor_no)

          for amigo in amigos:
              conexao = tuple(sorted((usuario, amigo)))
              if conexao not in arestas_desenhadas:
                  dot.edge(usuario, amigo)
                  arestas_desenhadas.add(conexao)

        try:
          dot.render(nome_arquivo, format='png', view=False, cleanup=True)
          print(f"Grafo salvo em: {nome_arquivo}.png")
        except Exception as e:
            print(f"Erro ao salvar imagem: {e}")

# MAIN
if __name__ == "__main__":
    rede = RedeSocial()

    print("\n--- 1. Criando a Rede ---")
    rede.adicionar_amizade("Ana", "Beatriz")
    rede.adicionar_amizade("Ana", "Carlos")
    rede.adicionar_amizade("Beatriz", "Daniel")
    rede.adicionar_amizade("Carlos", "Eduardo")
    rede.adicionar_amizade("Eduardo", "Fabio")
    rede.adicionar_amizade("Fabio", "Gabriel")

    rede.adicionar_usuario("Zeca")

    print("Usuários cadastrados:", list(rede.grafo.keys()))

    print("\n--- 2. Sugestões de Amizade ---")
    usuario_analise = "Ana"
    sugestoes = rede.sugerir_amigos(usuario_analise)
    print(f"Amigos de {usuario_analise}: {rede.listar_amigos(usuario_analise)}")
    print(f"Sugestões para {usuario_analise} (Amigos de amigos): {sugestoes}")

    print("\n--- 3. Verificando Conexões (Graus de Separação) ---")
    # Existe conexão entre Ana e Gabriel?
    conectados, caminho = rede.verificar_conexao("Ana", "Gabriel")
    if conectados:
        print(f"Caminho entre Ana e Gabriel: {' -> '.join(caminho)}")
    else:
        print("Ana e Gabriel não estão conectados.")

    print(f"\nConexão Ana -> Zeca: {rede.verificar_conexao('Ana', 'Zeca')[0]}")

    print("\n--- 4. Gerando Visualização ---")
    # Gera o grafo destacando a Ana (ouro) e seus amigos (verde)
    rede.draw_tree("rede_social_ana", destaque_usuario="Ana")