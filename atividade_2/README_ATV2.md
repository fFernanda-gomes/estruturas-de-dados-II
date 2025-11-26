# **Atividade 2 — Implementação de Árvore Binária de Busca (BST)**

### *Construção, busca, remoção e visualização de uma BST com valores fixos e aleatórios.*

---

## 🎯 Objetivo

Implementar uma **Árvore Binária de Busca (BST)** em Python, aplicando operações fundamentais como **inserção**, **busca**, **remoção**, **altura** e **profundidade**, além de gerar visualizações gráficas da estrutura da árvore com valores fixos e aleatórios.

---

## 📘 Descrição da Atividade

A atividade consiste na criação de uma classe `BinarySearchTree` que implementa:

- Inserção de valores (`insert`)
- Busca (`search`)
- Remoção (`delete`) cobrindo todos os casos
- Cálculo da altura (`height`)
- Profundidade de um nó (`depth`)
- Visualização usando Graphviz

### Entrada
- Lista fixa: `[55, 30, 80, 20, 45, 70, 90]`
- Lista aleatória com 15 números entre 1 e 200

### Processamento
- Inserção, busca, remoção e nova inserção
- Cálculo da altura e profundidade
- Geração visual das árvores

### Saída
- Prints no terminal
- Imagens `.png` das árvores geradas

### Estruturas de dados usadas
- Árvore Binária de Busca
- Nós contendo: valor, filho esquerdo, filho direito

### Algoritmos envolvidos
- Inserção recursiva
- Busca recursiva
- Remoção com sucessor in-order
- DFS para altura e profundidade
- Geração gráfica com Graphviz

---

## 🧠 Conceitos Utilizados
- BST
- Recursão
- Altura e profundidade
- Sucessor in-order
- DFS
- Representação gráfica

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
python atividade_2.py
```

### 3. Arquivos gerados

- `arvore_fixa.png`
- `arvore_fixa_apos_delete.png`
- `arvore_fixa_apos_insert.png`
- `arvore_random.png`

Essas imagens representam visualmente as estruturas construídas.

---

## 📝 Observações
- O caso de remoção com dois filhos exige mais atenção.
- As imagens são sobrescritas a cada execução.
- Código organizado em classe única para clareza.
