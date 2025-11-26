# Atividade 5 – Implementação de Árvore AVL

## 🎯 Objetivo
Implementar do zero a lógica de uma **Árvore AVL** em Python, incluindo:

1. Operações de **inserção e deleção** com auto-balanceamento.
2. Funções auxiliares de **busca por intervalo** e **cálculo de profundidade**.

E gerar **imagens PNG** dos estados da árvore (pós-inserção e pós-deleção) utilizando a biblioteca **Graphviz**.

---

## 📘 Descrição da Atividade

A atividade consiste em:

### ✔️ 1. Lógica de Balanceamento (Rotações)
Implementação das rotações necessárias para manter a propriedade AVL (diferença de altura máxima de 1 entre subárvores):
- **Rotação Simples** (Direita e Esquerda)
- **Rotação Dupla** (Esquerda-Direita e Direita-Esquerda)

### ✔️ 2. Inserção e Visualização
O script insere uma sequência de chaves (`10, 20, 30, 40, 50, 25`) que força o desbalanceamento, acionando as rotações automaticamente.
A árvore resultante é salva como:
➡️ **avl_insercao.png**

### ✔️ 3. Deleção e Rebalanceamento
O código remove um nó específico (ex: `40`), verifica o fator de balanceamento dos ancestrais e aplica novas rotações se necessário.
A árvore resultante é salva como:
➡️ **avl_delecao.png**

---

## 🧠 Conceitos Utilizados

- **Árvores AVL** (Adelson-Velsky e Landis)
- **Fator de Balanceamento** (Altura Esq - Altura Dir)
- **Rotações de Árvore** (LL, RR, LR, RL)
- **Recursão**
- **Travessia em-ordem (In-order traversal)**
- **Visualização com Graphviz**

---

## ▶️ Como executar a atividade

### 1. Instalar dependências

```bash
pip install graphviz
```
> ⚠️ **É necessário ter o Graphviz instalado no sistema:** > https://graphviz.org/download/ 

---

### 2. Executar o script

```bash
python atividade_5.py
```

---

### 3. Arquivos gerados

- `avl_insercao.png` — estado da árvore após as inserções
- `avl_delecao.png` — estado da árvore após a remoção de um nó

As imagens exibem em cada nó o valor da **chave** e sua **altura (h)** atual.

---

## 📦 Arquivos desta pasta

- **atividade_5.py** → implementação completa da AVL
- **avl_insercao.png** → imagem gerada pelo script
- **avl_delecao.png** → imagem gerada pelo script
- **README.md** → documentação da atividade

---

## 📝 Observações
- A visualização inclui o atributo `h` (altura) dentro de cada nó para facilitar a conferência do balanceamento visualmente.