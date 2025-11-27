# Atividade 2 – Rede de Transporte Público (Grafos)

## 🎯 Objetivo
Modelar um sistema de transporte público (como Metrô ou Ônibus) utilizando **Grafos Ponderados**, onde:
- **Vértices** são as estações.
- **Arestas** são as conexões entre estações.
- **Peso** das arestas representa o tempo de deslocamento em minutos.

O objetivo final é implementar o algoritmo de **Dijkstra** para sugerir ao usuário o trajeto mais rápido entre duas estações e visualizar essa rota graficamente.

---

## 📘 Descrição da Solução

### 1. Estrutura de Dados (`RedeTransporte`)
O grafo foi implementado utilizando **listas de adjacência** para garantir performance na busca de conexões. O código segue princípios de *Clean Code*, com nomes semânticos (`adicionar_estacao`, `buscar_caminho`).

### 2. Caminho Mínimo (Dijkstra)
A lógica central utiliza uma **fila de prioridade** (`heapq`) para explorar sempre a estação mais próxima (menor tempo acumulado) primeiro, garantindo que o resultado final seja matematicamente o mais rápido possível.

### 3. Visualização (Graphviz)
O script gera um diagrama da rede de transporte.
- **Nós retangulares** representam as estações.
- **Setas** representam o sentido da linha.
- **Linhas Vermelhas** destacam o trajeto sugerido pelo algoritmo.

---

## 🧪 Cenário de Teste

A execução padrão cria uma rede fictícia com cruzamentos de linhas:
1. **Linha Azul:** Central → Sé → Paraíso → Ana Rosa
2. **Linha Verde:** Consolação → Paraíso → Klabin
3. **Linha Amarela (Atalho):** Central → Consolação

**Desafio:** Ir da **Central** até **Klabin**.
- Opção A (Via Sé): 3 + 4 + 3 = 10 minutos.
- Opção B (Via Consolação): 6 + 5 + 3 = 14 minutos.

O algoritmo deve escolher (e desenhar) a **Opção A**.

---

## ▶️ Como executar

### 1. Pré-requisitos
```bash
pip install graphviz
```
> (Necessário ter o software Graphviz instalado no sistema operacional)

### 2. Executar o script
```bash
python rede_transporte.py
```

---

## 📦 Arquivos desta pasta

- **rede_transporte.py** → código fonte com a classe RedeTransporte
- **mapa_metro.png** → imagem gerada pelo script
- **README.md** → Documentação