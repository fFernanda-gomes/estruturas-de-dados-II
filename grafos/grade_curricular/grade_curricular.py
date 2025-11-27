from collections import deque

try:
    from graphviz import Digraph
    TEM_GRAPHVIZ = True
except ImportError:
    TEM_GRAPHVIZ = False

class GradeCurricular:
    """
    Representa uma grade de disciplinas e seus pré-requisitos.
    - Vértices: Disciplinas
    - Arestas: Dependências (A -> B significa que A é pré-requisito de B)
    """
    def __init__(self):
        self.adjacencia = {}
        
        # Armazena quantos pré-requisitos cada matéria tem (Grau de Entrada)
        # Usado para Ordenação Topológica
        self.grau_entrada = {}

    def adicionar_disciplina(self, disciplina):
        if disciplina not in self.adjacencia:
            self.adjacencia[disciplina] = []
            self.grau_entrada[disciplina] = 0

    def adicionar_pre_requisito(self, pre_req, disciplina):
        """
        Define que 'pre_req' é necessário para cursar 'disciplina'.
        """
        if pre_req not in self.adjacencia: self.adicionar_disciplina(pre_req)
        if disciplina not in self.adjacencia: self.adicionar_disciplina(disciplina)

        self.adjacencia[pre_req].append(disciplina)
        self.grau_entrada[disciplina] += 1

    def detectar_ciclo(self):
        """
        Verifica se existe dependência circular (ex: A -> B -> A).
        Retorna True se houver ciclo (Grade Inválida).
        """
        visitados = set()
        pilha_recursao = set()

        def _tem_ciclo(v):
            visitados.add(v)
            pilha_recursao.add(v)

            for vizinho in self.adjacencia[v]:
                if vizinho not in visitados:
                    if _tem_ciclo(vizinho):
                        return True
                elif vizinho in pilha_recursao:
                    return True
            
            pilha_recursao.remove(v)
            return False

        for disciplina in self.adjacencia:
            if disciplina not in visitados:
                if _tem_ciclo(disciplina):
                    return True
        
        return False

    def obter_ordem_estudo(self):
        """
        Realiza uma ORDENAÇÃO TOPOLÓGICA (Algoritmo de Kahn).
        Retorna a lista de disciplinas na ordem que devem ser cursadas.
        """
        if self.detectar_ciclo():
            return None

        fila = deque([d for d in self.grau_entrada if self.grau_entrada[d] == 0])
        ordem = []

        graus_temp = self.grau_entrada.copy()

        while fila:
            atual = fila.popleft()
            ordem.append(atual)

            for vizinho in self.adjacencia[atual]:
                graus_temp[vizinho] -= 1
                if graus_temp[vizinho] == 0:
                    fila.append(vizinho)
        
        return ordem

    # VISUALIZAÇÃO
    def draw_tree(self, nome_arquivo="fluxograma_curso"):
        if not TEM_GRAPHVIZ:
            print("Aviso: Graphviz não instalado. Visualização pulada.")
            return

        
        dot = Digraph(comment="Grade Curricular")
        # Layout 'dot' é hierárquico, perfeito para pré-requisitos (Top-Down)
        dot.attr(rankdir='TB') 
        dot.attr('node', shape='box', style='filled', color='lightyellow', fontname='Arial')

        for disciplina, dependentes in self.adjacencia.items():
            dot.node(disciplina, disciplina)
            for dep in dependentes:
                # Aresta: Pré-requisito -> Matéria
                dot.edge(disciplina, dep)
                
        try:
          dot.render(nome_arquivo, format='png', view=False, cleanup=True)
          print(f"Fluxograma salvo em: {nome_arquivo}.png")
        except Exception as e:
            print(f"Erro ao salvar imagem: {e}")

# MAIN
if __name__ == "__main__":
    curso = GradeCurricular()

    print("\n--- 1. Montando a Grade (Ciência da Computação) ---")
    
    # 1º Semestre
    curso.adicionar_disciplina("Logica de Programacao")
    curso.adicionar_disciplina("Matematica Discreta")
    
    # 2º Semestre (Dependem do 1º)
    curso.adicionar_pre_requisito("Logica de Programacao", "Estrutura de Dados I")
    curso.adicionar_pre_requisito("Matematica Discreta", "Algebra Linear")
    
    # 3º Semestre
    curso.adicionar_pre_requisito("Estrutura de Dados I", "Estrutura de Dados II")
    curso.adicionar_pre_requisito("Estrutura de Dados I", "Banco de Dados")
    
    # 4º Semestre (TCC depende de quase tudo)
    curso.adicionar_pre_requisito("Estrutura de Dados II", "TCC")
    curso.adicionar_pre_requisito("Banco de Dados", "TCC")

    print("Disciplinas cadastradas.")

    print("\n--- 2. Verificando Consistência ---")
    if curso.detectar_ciclo():
        print("ERRO: O curso possui dependências circulares (impossível formar).")
    else:
        print("Grade válida! Sem ciclos detectados.")

    print("\n--- 3. Ordem Recomendada de Estudo (Ordenação Topológica) ---")
    ordem = curso.obter_ordem_estudo()
    if ordem:
        print(" -> ".join(ordem))
    
    print("\n--- 4. Gerando Fluxograma ---")
    curso.draw_tree("fluxograma_curso")