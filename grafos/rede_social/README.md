# Atividade 3 – Rede Social de Usuários (Grafos)

## 🎯 Objetivo
Modelar uma rede social simples utilizando a estrutura de **Grafo Não-Direcionado**, onde:
- **Vértices** representam usuários.
- **Arestas** representam laços de amizade.

O projeto deve permitir adicionar amigos, visualizar a rede e utilizar algoritmos para **sugerir novas conexões** (amigos de amigos) e verificar o distanciamento entre usuários.

---

## 📘 Funcionalidades

### 1. Gestão de Amizades
Implementada com listas de adjacência (usando `set` em Python para performance).
- As conexões são bidirecionais (se A é amigo de B, B é amigo de A).

### 2. Algoritmo de Sugestão
Uma funcionalidade clássica de redes sociais. O algoritmo percorre os vizinhos de primeiro nível para encontrar os vizinhos de segundo nível (amigos dos amigos) que ainda não possuem conexão com o usuário original.

### 3. Verificação de Conexão (BFS)
Utiliza **Busca em Largura (Breadth-First Search)** para encontrar o menor caminho entre dois usuários, útil para calcular "graus de separação".

### 4. Visualização (Layout Neato)
Utiliza o Graphviz com o algoritmo de layout `neato`, que é ideal para redes sociais orgânicas, distribuindo os nós de forma a minimizar sobreposições.
- **Destaque Visual:** O usuário principal é pintado de **Dourado**, e seus amigos diretos de **Verde**.

---

## 🧪 Cenário de Teste

A rede montada no exemplo possui dois grupos conectados por um "hub" (Carlos):
- **Grupo A:** Ana, Beatriz, Carlos, Daniel.
- **Grupo B:** Eduardo, Fabio, Gabriel.

**Teste de Sugestão:**
- Ao analisar **Ana** (amiga de Beatriz e Carlos), o sistema sugere **Daniel** (amigo de Beatriz) e **Eduardo** (amigo de Carlos).

**Teste de Caminho:**
- O sistema consegue traçar a rota de **Ana** até **Gabriel**: `Ana -> Carlos -> Eduardo -> Fabio -> Gabriel`.

---

## ▶️ Como executar

### 1. Instalar dependências
```bash
pip install graphviz
```
> (Necessário ter o software Graphviz instalado no sistema operacional)

### 2. Executar o script
```bash
python rede_social.py
```

---

## 📦 Arquivos desta pasta

- **rede_social.py** → código fonte com a classe RedeSocial
- **rede_social_ana.png** → imagem gerada pelo script
- **README.md** → Documentação