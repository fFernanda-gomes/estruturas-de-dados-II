# Atividade 4 – Rede de Disciplinas (Grafos e Ordenação Topológica)

## 🎯 Objetivo
Modelar a grade curricular de um curso utilizando **Grafos Direcionados (DAGs)**, onde:
- **Vértices** representam as disciplinas.
- **Arestas Direcionadas** representam os pré-requisitos (Matéria A → Matéria B).

O sistema deve ser capaz de detectar inconsistências (ciclos) e sugerir a **ordem correta de estudo** para o aluno se formar.

---

## 📘 Funcionalidades

### 1. Gestão de Pré-requisitos
Permite construir a grade definindo quais matérias dependem de quais.
- Exemplo: *Lógica de Programação* é pré-requisito para *Estrutura de Dados*.

### 2. Detecção de Ciclos
Um problema clássico em grades curriculares: se A depende de B, e B depende de A, o aluno nunca consegue se formar. O sistema implementa um algoritmo de **DFS (Busca em Profundidade)** com pilha de recursão para identificar esses erros lógicos.

### 3. Ordenação Topológica (Plano de Estudo)
Utiliza o **Algoritmo de Kahn** (baseado no grau de entrada dos nós) para gerar uma lista linear de disciplinas, respeitando todas as dependências. É a base para montar o cronograma do aluno.

### 4. Visualização Hierárquica
Utiliza o Graphviz para gerar um fluxograma vertical (`TB` - Top to Bottom), facilitando a visualização do que vem antes e depois.
- Matérias base ficam no topo.
- Matérias avançadas ficam na parte inferior.

---

## 🧪 Cenário de Teste

A grade montada simula um curso de Computação simplificado:
1. **Base:** Lógica de Programação, Matemática Discreta.
2. **Intermediário:** Estrutura de Dados I, Álgebra Linear.
3. **Avançado:** Estrutura de Dados II, Banco de Dados.
4. **Final:** TCC.

O algoritmo deve gerar uma ordem onde o **TCC** apareça obrigatoriamente por último, e **Lógica** apareça antes de **Estrutura**.

---

## ▶️ Como executar

### 1. Instalar dependências
```bash
pip install graphviz
> (Necessário ter o software Graphviz instalado no sistema operacional)

### 2. Executar o script
```bash
python grade_curricular.py
```

---

## 📦 Arquivos desta pasta

- **grade_curricular.py** → código fonte com a classe GradeCurricular
- **fluxograma_curso.png** → imagem gerada pelo script
- **README.md** → Documentação