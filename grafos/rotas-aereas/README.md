# Atividade 1 – Rotas Aéreas (Grafos e Dijkstra)

## 🎯 Objetivo
Implementar um sistema de rotas aéreas utilizando a estrutura de dados **Grafo**, onde:
- **Vértices** representam aeroportos (ex: GRU, JFK).
- **Arestas** representam voos diretos com um **peso** (tempo ou distância).

O sistema deve permitir a visualização gráfica da rede e calcular o **caminho mais rápido** entre dois aeroportos utilizando o algoritmo de **Dijkstra**.

---

## 📘 Funcionalidades Implementadas

### ✔️ 1. Gestão de Rotas (Grafo Direcionado)
O grafo é implementado utilizando **listas de adjacência** (dicionário de dicionários em Python).
- `adicionar_aeroporto(codigo)`: Insere um nó.
- `adicionar_rota(origem, destino, peso)`: Insere uma aresta com peso.
- `consultar_voos_diretos(aeroporto)`: Lista conexões diretas.

### ✔️ 2. Algoritmo de Dijkstra
Para encontrar a rota mais eficiente, foi implementado o algoritmo clássico de Dijkstra com uma **Fila de Prioridade** (`heapq`).
- Calcula o menor custo acumulado da origem até o destino.
- Retorna tanto o custo total quanto a lista ordenada de aeroportos a percorrer.

### ✔️ 3. Visualização Inteligente
Utiliza a biblioteca **Graphviz** para gerar um mapa visual (`.png`).
- Diferencial: O código recebe o caminho calculado pelo Dijkstra e **pinta de vermelho** as arestas que compõem a melhor rota na imagem final.

---

## 🧪 Exemplo de Execução

Considerando o seguinte cenário de voos:
- GRU -> MIA (8h)
- GRU -> LIS (10h)
- MIA -> LHR (9h)
- LIS -> LHR (2h)

Ao buscar a rota de **GRU para LHR**:
1. Caminho via Miami: 8 + 9 = 17h
2. Caminho via Lisboa: 10 + 2 = 12h (**Escolhido**)

### Arquivos Gerados
- `mapa_rotas.png`: Imagem contendo todos os aeroportos, com a rota **GRU -> LIS -> LHR** destacada em vermelho.

---

## ▶️ Como executar

### 1. Instalar dependências
```bash
pip install graphviz
```
> (Necessário ter o software Graphviz instalado no sistema operacional)

### 2. Executar o script
```bash
python rotas.py
```

---

## 📦 Arquivos desta pasta

- **rotas.py** → código fonte com a classe GrafoRotas
- **mapa_rotas.png** → imagem gerada pelo script
- **README.md** → Documentação