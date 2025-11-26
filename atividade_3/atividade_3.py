from graphviz import Digraph
import random

# Nodo da árvore
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Árvore Binária de Busca (BST)
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Inserção
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)

        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

    # TRAVESSIAS (DFS)

    def inorder(self):
        # Esquerda - Raiz - Direita
        resultado = []
        self._inorder(self.root, resultado)
        return resultado

    def _inorder(self, node, resultado):
        if node:
            self._inorder(node.left, resultado)
            resultado.append(node.value)
            self._inorder(node.right, resultado)

    def preorder(self):
        # Raiz - Esquerda - Direita
        resultado = []
        self._preorder(self.root, resultado)
        return resultado

    def _preorder(self, node, resultado):
        if node:
            resultado.append(node.value)
            self._preorder(node.left, resultado)
            self._preorder(node.right, resultado)

    def postorder(self):
        # Esquerda - Direita - Raiz
        resultado = []
        self._postorder(self.root, resultado)
        return resultado

    def _postorder(self, node, resultado):
        if node:
            self._postorder(node.left, resultado)
            self._postorder(node.right, resultado)
            resultado.append(node.value)

# Função para gerar imagem da árvore
def draw_tree(root, filename):
    dot = Digraph()
    dot.attr("node", shape="circle")

    def add(node):
        if node is None:
            return

        # nó usa o valor como id
        dot.node(str(node.value), str(node.value))

        if node.left:
            dot.edge(str(node.value), str(node.left.value))
            add(node.left)

        if node.right:
            dot.edge(str(node.value), str(node.right.value))
            add(node.right)

    add(root)
    dot.render(filename, format="png", cleanup=True)
    print(f"Árvore salva em: {filename}.png")

if __name__ == "__main__":

    print("\n===== Árvore Fixa =====\n")

    valores_fixos = [55, 30, 80, 20, 45, 70, 90]

    arvore_fixa = BinarySearchTree()
    for v in valores_fixos:
        arvore_fixa.insert(v)

    draw_tree(arvore_fixa.root, "tree_fixa")

    print("in-Order (E-R-D)  :", arvore_fixa.inorder())
    print("pre-Order (R-E-D) :", arvore_fixa.preorder())
    print("post-Order (E-D-R):", arvore_fixa.postorder())

    print("\n===== Árvore Aleatória =====\n")

    valores_random = random.sample(range(1, 200), 10)

    arvore_random = BinarySearchTree()
    for v in valores_random:
        arvore_random.insert(v)

    draw_tree(arvore_random.root, "tree_random")

    print("valores inseridos:", valores_random)
    print("in-Order (E-R-D)  :", arvore_random.inorder())
    print("pre-Order (R-E-D) :", arvore_random.preorder())
    print("post-Order (E-D-R):", arvore_random.postorder())
