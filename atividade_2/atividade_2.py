from graphviz import Digraph
import random

#  NÓ DA ÁRVORE
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#  ÁRVORE BINÁRIA DE BUSCA (BST)
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # INSERÇÃO
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # BUSCA
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    # REMOÇÃO
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        # procurar o valor
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)

        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)

        else:
            # -> caso 1: nó folha 
            if node.left is None and node.right is None:
                return None

            # -> caso 2: mm filho
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # -> caso 3: dois filhos -----
            successor = self._min_value_node(node.right)
            node.value = successor.value
            node.right = self._delete_recursive(node.right, successor.value)

        return node

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    # ALTURA DA ÁRVORE
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1  # altura de árvore vazia é -1
        return 1 + max(self._height_recursive(node.left),
                       self._height_recursive(node.right))

    # PROFUNDIDADE (depth)
    def depth(self, value):
        return self._depth_recursive(self.root, value, 0)

    def _depth_recursive(self, node, value, nivel):
        if node is None:
            return None
        if node.value == value:
            return nivel
        if value < node.value:
            return self._depth_recursive(node.left, value, nivel + 1)
        else:
            return self._depth_recursive(node.right, value, nivel + 1)

    # VISUALIZAÇÃO COM GRAPHVIZ
    def visualize(self, filename="bst"):
        dot = Digraph()
        if self.root:
            self._add_nodes(dot, self.root)
        dot.render(filename, format='png', cleanup=True)
        print(f"árvore gerada: {filename}.png")

    def _add_nodes(self, dot, node):
        if node is None:
            return
        dot.node(str(node.value), str(node.value))
        if node.left:
            dot.edge(str(node.value), str(node.left.value))
            self._add_nodes(dot, node.left)
        if node.right:
            dot.edge(str(node.value), str(node.right.value))
            self._add_nodes(dot, node.right)

if __name__ == "__main__":

    print("\n===== Árvore Fixa =====\n")

    fixed_values = [55, 30, 80, 20, 45, 70, 90]
    bst1 = BinarySearchTree()

    for v in fixed_values:
        bst1.insert(v)

    bst1.visualize("arvore_fixa")

    # busca
    print("\nbuscando valor 45...")
    print("Encontrado?" , bst1.search(45))

    # remoção
    print("\nremovendo o valor 30...")
    bst1.delete(30)
    bst1.visualize("arvore_fixa_apos_delete")

    # nova inserção
    print("\ninserindo o valor 50...")
    bst1.insert(50)
    bst1.visualize("arvore_fixa_apos_insert")

    # altura
    print("\naltura da árvore fixa:", bst1.height())

    # profundidade de 45
    print("profundidade do nó 45:", bst1.depth(45))


    print("\n===== Árvore Aleatória =====\n")

    bst2 = BinarySearchTree()
    random_values = random.sample(range(1, 200), 15)

    print("valores aleatórios gerados:", random_values)

    for v in random_values:
        bst2.insert(v)

    bst2.visualize("arvore_random")

    print("\naltura da árvore aleatória:", bst2.height())
