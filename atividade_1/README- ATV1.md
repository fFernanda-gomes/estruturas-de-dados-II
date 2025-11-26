# Atividade 1 – Construção de Árvore de Expressão Aritmética

## 🎯 Objetivo
Implementar uma árvore binária de expressão a partir de:

1. Uma **expressão aritmética fixa**.  
2. Uma **expressão aritmética gerada aleatoriamente**.  

E gerar **imagens PNG** das duas árvores utilizando a biblioteca **Graphviz**.

---

## 📘 Descrição da Atividade

A atividade consiste em:

### ✔️ 1. Árvore com valores fixos  
Usando a expressão:

```
((7 + 3) * (5 - 2))
```

O script constrói manualmente a árvore binária onde:

- Nós internos → operadores (`+`, `-`, `*`)
- Folhas → operandos (`7`, `3`, `5`, `2`)

A árvore é renderizada em um arquivo:  
➡️ **tree_fixa.png**

---

### ✔️ 2. Árvore com valores aleatórios  
O código gera automaticamente uma expressão com:

- Pelo menos **2 operadores**
- Pelo menos **3 operandos**

Exemplo gerado automaticamente:

```
( 8 * 3 - 2 )
```

Em seguida, um parser transforma essa string em uma árvore binária.  
A imagem da árvore é salva como:  
➡️ **tree_random.png**

---

## 🧠 Conceitos Utilizados

- **Árvores Binárias**
- **Nós, filhos e raiz**
- **Recursão**
- **Parsing de expressões**
- **Visualização com Graphviz**
- **Construção programática de grafos**

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
python atividade_1.py
```

### 3. Arquivos gerados

- `tree_fixa.png` — árvore da expressão fixa  
- `tree_random.png` — árvore da expressão aleatória  

Essas imagens representam visualmente as estruturas construídas.

---

## 📦 Arquivos desta pasta

- **atividade_1.py** → implementação completa  
- **tree_fixa.png** → imagem da árvore fixa  
- **tree_random.png** → imagem da árvore aleatória  
- **README.md** → documentação da atividade  

---

## 📝 Observações
- O parser implementado é simples e funciona para expressões binárias totalmente parentesisadas.
- A atividade segue todos os requisitos solicitados pela disciplina.
