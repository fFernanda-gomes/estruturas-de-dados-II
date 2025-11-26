from graphviz import Digraph
import random

# -------------------------------------------------------
# ÁRVORE FIXA
# -------------------------------------------------------

def build_fixed_tree():
    """
    Constrói manualmente a árvore da expressão:
        ((7 + 3) * (5 - 2))

    Retorna um dicionário representando nós e filhos.
    """
    return {
        "value": "*",
        "left": {
            "value": "+",
            "left": {"value": "7", "left": None, "right": None},
            "right": {"value": "3", "left": None, "right": None},
        },
        "right": {
            "value": "-",
            "left": {"value": "5", "left": None, "right": None},
            "right": {"value": "2", "left": None, "right": None},
        }
    }


# -------------------------------------------------------
# EXPRESSÃO ALEATÓRIA
# -------------------------------------------------------

def generate_random_expression():
    """
    Gera expressões simples no formato:
        ( a op1 b op2 c )

    a, b, c ∈ [1..9]
    op1, op2 ∈ {+, -, *, /}
    """

    operadores = ["+", "-", "*", "/"]
    operandos = [str(random.randint(1, 9)) for _ in range(3)]
    ops = random.choices(operadores, k=2)

    expr = f"( {operandos[0]} {ops[0]} {operandos[1]} {ops[1]} {operandos[2]} )"
    return expr


# -------------------------------------------------------
# PARSER — transforma expressão em árvore
# -------------------------------------------------------

def parse_expression(expr):
    """
    Converte uma expressão com parênteses em uma árvore binária.
    Espera uma expressão no formato:
        ( 4 * 2 + 1 )
    """

    # Garantir que "(" e ")" sejam tokens separados
    tokens = expr.replace("(", "( ").replace(")", " )").split()

    def parse(tokens):
        token = tokens.pop(0)

        # Quando encontra "(", começa um novo subexpressão
        if token == "(":
            left = parse(tokens)     # parse do operando esquerdo
            op = tokens.pop(0)       # operador
            right = parse(tokens)    # operando direito
            tokens.pop(0)            # remove ")"
            return {"value": op, "left": left, "right": right}

        # Caso contrário é número (folha da árvore)
        else:
            return {"value": token, "left": None, "right": None}

    return parse(tokens)


# -------------------------------------------------------
# DESENHAR ÁRVORE
# -------------------------------------------------------

def draw_tree(tree, filename):
    dot = Digraph()
    dot.attr("node", shape="circle")

    def add_nodes_edges(node, id_counter=[0]):
        """
        Função recursiva que adiciona:
        - nós na imagem (dot.node)
        - arestas entre pai e filho (dot.edge)
        """

        if node is None:
            return None

        # Cada nó recebe um id único
        node_id = str(id_counter[0])
        id_counter[0] += 1

        # Cria o nó
        dot.node(node_id, label=node["value"])

        # Ligações com filhos
        if node["left"]:
            left_id = add_nodes_edges(node["left"])
            dot.edge(node_id, left_id)

        if node["right"]:
            right_id = add_nodes_edges(node["right"])
            dot.edge(node_id, right_id)

        return node_id

    add_nodes_edges(tree)

    # Exporta para PNG
    dot.render(filename, format="png", cleanup=True)
    print(f"Árvore salva em: {filename}.png")


# -------------------------------------------------------
# MAIN — execução
# -------------------------------------------------------

if __name__ == "__main__":
    print("\n===== Árvore Fixa =====\n")
    fixed_tree = build_fixed_tree()
    draw_tree(fixed_tree, "tree_fixa")

    print("\n===== Árvore Aleatória =====\n")
    expr = generate_random_expression()
    print("Expressão gerada:", expr)

    random_tree = parse_expression(expr)
    draw_tree(random_tree, "tree_random")
