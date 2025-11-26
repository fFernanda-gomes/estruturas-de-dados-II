# -*- coding: utf-8 -*-
from graphviz import Digraph

class No:
    """
    Representa um nó na Árvore AVL.
    """
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1 

class ArvoreAVL:
    """
    Implementa a estrutura e as operações de uma Árvore AVL.
    """
    def __init__(self):
        self.raiz = None

    # ===============================================================
    # TAREFA 0: MÉTODOS AUXILIARES E ROTAÇÕES
    # ===============================================================

    def obter_altura(self, no):
        if no is None:
            return 0
        return no.altura

    def obter_fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.obter_altura(no.esquerda) - self.obter_altura(no.direita)

    def _atualizar_altura(self, no):
        if no is None:
            return
        no.altura = 1 + max(self.obter_altura(no.esquerda), self.obter_altura(no.direita))

    def obter_no_valor_minimo(self, no):
        atual = no
        while atual and atual.esquerda:
            atual = atual.esquerda
        return atual

    def _rotacao_direita(self, no_pivo):
        x = no_pivo.esquerda
        T2 = x.direita

        x.direita = no_pivo
        no_pivo.esquerda = T2

        self._atualizar_altura(no_pivo)
        self._atualizar_altura(x)

        return x

    def _rotacao_esquerda(self, no_pivo):
        y = no_pivo.direita
        T2 = y.esquerda

        y.esquerda = no_pivo
        no_pivo.direita = T2

        self._atualizar_altura(no_pivo)
        self._atualizar_altura(y)

        return y

    # ===============================================================
    # TAREFA 1: INSERÇÃO E DELEÇÃO COM BALANCEAMENTO
    # ===============================================================

    def inserir(self, chave):
        self.raiz = self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no_atual, chave):
        if no_atual is None:
            return No(chave)

        if chave < no_atual.chave:
            no_atual.esquerda = self._inserir_recursivo(no_atual.esquerda, chave)
        elif chave > no_atual.chave:
            no_atual.direita = self._inserir_recursivo(no_atual.direita, chave)
        else:
            return no_atual # Duplicatas não permitidas

        self._atualizar_altura(no_atual)
        fator = self.obter_fator_balanceamento(no_atual)

        # Caso 1: Esq-Esq
        if fator > 1 and chave < no_atual.esquerda.chave:
            return self._rotacao_direita(no_atual)

        # Caso 2: Dir-Dir
        if fator < -1 and chave > no_atual.direita.chave:
            return self._rotacao_esquerda(no_atual)

        # Caso 3: Esq-Dir
        if fator > 1 and chave > no_atual.esquerda.chave:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        # Caso 4: Dir-Esq
        if fator < -1 and chave < no_atual.direita.chave:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        return no_atual

    def deletar(self, chave):
        self.raiz = self._deletar_recursivo(self.raiz, chave)

    def _deletar_recursivo(self, no_atual, chave):
        if no_atual is None:
            return no_atual

        if chave < no_atual.chave:
            no_atual.esquerda = self._deletar_recursivo(no_atual.esquerda, chave)
        elif chave > no_atual.chave:
            no_atual.direita = self._deletar_recursivo(no_atual.direita, chave)
        else:
            if no_atual.esquerda is None:
                temp = no_atual.direita
                no_atual = None
                return temp
            elif no_atual.direita is None:
                temp = no_atual.esquerda
                no_atual = None
                return temp

            temp = self.obter_no_valor_minimo(no_atual.direita)
            no_atual.chave = temp.chave
            no_atual.direita = self._deletar_recursivo(no_atual.direita, temp.chave)

        if no_atual is None:
            return no_atual

        self._atualizar_altura(no_atual)
        fator = self.obter_fator_balanceamento(no_atual)

        if fator > 1 and self.obter_fator_balanceamento(no_atual.esquerda) >= 0:
            return self._rotacao_direita(no_atual)

        if fator > 1 and self.obter_fator_balanceamento(no_atual.esquerda) < 0:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        if fator < -1 and self.obter_fator_balanceamento(no_atual.direita) <= 0:
            return self._rotacao_esquerda(no_atual)

        if fator < -1 and self.obter_fator_balanceamento(no_atual.direita) > 0:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        return no_atual

    # ===============================================================
    # TAREFA 2 E 3: BUSCAS
    # ===============================================================

    def encontrar_nos_intervalo(self, chave1, chave2):
        resultado = []
        def _em_ordem_intervalo(no):
            if no is None: return
            if chave1 < no.chave: _em_ordem_intervalo(no.esquerda)
            if chave1 <= no.chave <= chave2: resultado.append(no.chave)
            if no.chave < chave2: _em_ordem_intervalo(no.direita)
        _em_ordem_intervalo(self.raiz)
        return resultado

    def obter_profundidade_no(self, chave):
        nivel = 0
        atual = self.raiz
        while atual is not None:
            if chave == atual.chave: return nivel
            elif chave < atual.chave: atual = atual.esquerda
            else: atual = atual.direita
            nivel += 1
        return -1

    # ===============================================================
    # FUNÇÃO DE VISUALIZAÇÃO (DENTRO DA CLASSE)
    # ===============================================================
    def draw_tree(self, filename):
        """
        Gera um arquivo PNG visualizando a estrutura atual da árvore.
        """
        dot = Digraph()
        dot.attr("node", shape="circle")

        def add(no):
            # Se o nó for nulo, retorna
            if no is None:
                return

            # Cria o nó visual. 
            # ID = chave convertida para string
            # Label = chave + altura
            label_visual = f"{no.chave}\n(h={no.altura})"
            dot.node(str(no.chave), label_visual)

            # Desenha aresta esquerda
            if no.esquerda:
                dot.edge(str(no.chave), str(no.esquerda.chave))
                add(no.esquerda)

            # Desenha aresta direita
            if no.direita:
                dot.edge(str(no.chave), str(no.direita.chave))
                add(no.direita)

        # Inicia a recursão a partir da raiz da própria classe
        add(self.raiz)
        
        # Gera o arquivo
        dot.render(filename, format="png", cleanup=True)
        print(f"Árvore salva em: {filename}.png")


# --- Bloco de Teste ---
if __name__ == "__main__":
    arvore_avl = ArvoreAVL()
    
    print("\n--- ATIVIDADE PRÁTICA: ÁRVORE AVL ---")
    
    print("\n--- 1. Inserindo nós ---")
    # Inserção que força rotações (AVL)
    chaves = [10, 20, 30, 40, 50, 25]
    for c in chaves:
        arvore_avl.inserir(c)
    
    print(f"Inseridos: {chaves}")
    
    # Chama o método de dentro da instância
    arvore_avl.draw_tree("avl_insercao")

    print("\n--- 2. Deletando nó 40 ---")
    arvore_avl.deletar(40)
    
    arvore_avl.draw_tree("avl_delecao")
    
    print("\n--- 3. Testes Extras ---")
    print("Intervalo [20, 30]:", arvore_avl.encontrar_nos_intervalo(20, 30))
    print("Profundidade do 30:", arvore_avl.obter_profundidade_no(30))