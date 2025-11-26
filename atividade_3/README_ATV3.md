# Atividade 3 – Travessias em Árvores Binárias

## 🎯 Objetivo
Implementar e demonstrar os três principais métodos de travessia em profundidade (DFS) em uma árvore binária:

- In-Order (Esquerda – Raiz – Direita)

- Pre-Order (Raiz – Esquerda – Direita)

- Post-Order (Esquerda – Direita – Raiz)

Além disso, visualizar graficamente as duas árvores utilizadas na atividade.

---

## 📘 Descrição da Atividade

A atividade consiste em:

### ✔️ 1. Árvore com valores fixos  
Com os valores:

```
[55, 30, 80, 20, 45, 70, 90]
```

---

### ✔️ 2. Impressão das Travessias  
Para essa árvore fixa, o código exibe:

- Sequência In-Order

- Sequência Pre-Order

- Sequência Post-Order

### ✔️ 3. Construção de uma Árvore Aleatória

Gera uma lista de 10 números inteiros aleatórios e insere na árvore.

### ✔️ 4. Travessias da Árvore Aleatória

Exibe também os resultados dos três métodos de DFS.

### ✔️ 5. Visualização Gráfica

Ambas as árvores são renderizadas usando Graphviz.

---

## 🧠 Conceitos Utilizados

- **Árvores Binárias**
- **Nós e filhos**
- **Recursão**
- **Inserção em árvore**
- **Visualização com Graphviz**

---

## ▶️ Como executar a atividade

### 1. Instalar dependências

```bash
pip install graphviz
```

> ⚠️ É necessário ter o Graphviz instalado no sistema:  
https://graphviz.org/download/

### 2. Executar o script

```bash
python atividade_3.py
```

### 3. Arquivos gerados

- `tree_fixa.png` — árvore da expressão fixa  
- `tree_random.png` — árvore da expressão aleatória  

Essas imagens representam visualmente as estruturas construídas.

---

## 📦 Arquivos desta pasta

- **atividade_3.py** → implementação completa  
- **tree_fixa.png** → imagem da árvore fixa  
- **tree_random.png** → imagem da árvore aleatória  
- **README.md** → documentação da atividade  

---

## 📝 Observações
- As travessias são implementadas de forma recursiva.
- Os valores aleatórios são diferentes a cada execução
