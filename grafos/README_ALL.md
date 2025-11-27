# 📦 Algoritmos e Estruturas de Dados: Grafos

Este repositório contém uma coleção de atividades práticas focadas na implementação de **Grafos** em Python. Cada projeto aborda um problema do mundo real resolvido através de diferentes algoritmos clássicos (Dijkstra, BFS, Ordenação Topológica).

Todas as implementações incluem **visualização gráfica** automática das estruturas geradas utilizando a biblioteca `Graphviz`.

---

## 📂 Projetos Disponíveis

### ✈️ 1. Rotas Aéreas (`/rotas-aereas`)
Sistema de controle de tráfego aéreo e navegação.
- **Tipo de Grafo:** Direcionado e Ponderado.
- **Algoritmo Principal:** **Dijkstra** (Caminho mais curto/rápido).
- **Funcionalidade:** Calcula o menor tempo de voo entre aeroportos internacionais e destaca a rota no mapa.

### 🚇 2. Rede de Transporte Público (`/rede_transporte`)
Modelagem de linhas de metrô e conexões urbanas.
- **Tipo de Grafo:** Direcionado e Ponderado.
- **Algoritmo Principal:** **Dijkstra** (Otimizado para conexões).
- **Funcionalidade:** Encontra o trajeto mais rápido entre estações, considerando baldeações.

### 👥 3. Rede Social (`/rede_social`)
Simulação de conexões de amizade e influência.
- **Tipo de Grafo:** Não-Direcionado.
- **Algoritmo Principal:** **BFS (Busca em Largura)** e Lógica de Sets.
- **Funcionalidade:** Sistema de **sugestão de amigos** (amigos de amigos) e verificação de graus de separação.

### 🎓 4. Grade Curricular (`/grade_curricular`)
Gerenciamento de disciplinas e pré-requisitos acadêmicos.
- **Tipo de Grafo:** Direcionado Acíclico (DAG).
- **Algoritmo Principal:** **Ordenação Topológica (Kahn)** e Detecção de Ciclos (DFS).
- **Funcionalidade:** Gera um plano de estudos linear respeitando as dependências e valida se a grade é possível (sem ciclos).

---

## 🛠️ Pré-requisitos

Para executar a visualização dos grafos, é necessário instalar a biblioteca `graphviz` e ter o software instalado no sistema operacional.

```bash
pip install graphviz
```
> ⚠️ Nota: Certifique-se de baixar e instalar o executável do Graphviz aqui e adicioná-lo ao PATH do sistema

---

## ▶️ Como Executar

Cada projeto funciona de forma independente. Navegue até a pasta desejada e execute o script Python correspondente.

**Exemplo (Rodando o projeto de Rotas Aéreas):**

```bash
cd rotas-aereas
python rotas.py
```

---

## 🖼️ Exemplos de Visualização

Os scripts geram arquivos `.png` automaticamente na pasta de execução, permitindo visualizar:

- Rotas destacadas em **vermelho**.
- Hierarquias de disciplinas (Fluxogramas).
- Clusters de amizades.