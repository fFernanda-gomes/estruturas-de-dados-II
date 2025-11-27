# Atividade 7 – Solucionador de Labirintos (BFS Interativo)

## 🎯 Objetivo

Criar uma aplicação gráfica interativa capaz de:

- Permitir ao usuário desenhar labirintos personalizados.
- Executar e visualizar, passo a passo, o algoritmo de Busca em Largura (BFS) encontrando o caminho mais curto.

---

## 📘 Funcionalidades

### 🖱️ Modo Edição

O usuário pode interagir com a grade (30x20) utilizando o mouse para desenhar:

- **Paredes (#):** Obstáculos intransponíveis (Azul Escuro).
- **Início (S):** Ponto de partida (Verde). Só pode existir um.
- **Fim (E):** Ponto de destino (Vermelho). Só pode existir um.
- **Borracha:** Remove elementos criando caminhos livres.

---

### 🌊 Modo Simulação (Algoritmo BFS)

Ao iniciar a busca, o programa utiliza o algoritmo **Breadth-First Search** com uma fila (`deque`):

- **Onda de Expansão:** As células visitadas ficam azul-claro e a fronteira de busca (fila) fica em azul mais escuro.
- **Animação:** O uso do agendador de eventos (`.after`) permite visualizar a lógica do algoritmo em tempo real sem travar a interface.
- **Backtracking:** Ao encontrar o **Fim**, o sistema usa um dicionário de predecessores para reconstruir e pintar o caminho mais curto em dourado.

---

## ⚙️ Estrutura Técnica

**Biblioteca Gráfica:** `tkinter` (nativa do Python).

**Estruturas de Dados Utilizadas:**

- **Matriz 2D:** Representação lógica do labirinto.
- **Deque (Fila):** Gerenciamento da fronteira do BFS.
- **Set (Conjunto):** Controle de nós visitados para evitar ciclos.
- **Dict (Dicionário):** Rastreamento de pais/predecessores para reconstruir o caminho.

---

## ▶️ Como Executar

### 1. Pré-requisitos
Nenhuma biblioteca externa é necessária (o `tkinter` já vem instalado com o Python).

### 2. Executar o script
```bash
python maze_editor_GUI.py
```

### 3. Como Usar

- Selecione uma ferramenta no menu lateral (ex: **Parede**).
- Clique ou arraste na área branca para desenhar.
- Certifique-se de colocar um **"S"** e um **"E"**.
- Clique em **"Iniciar BFS"** para ver a mágica acontecer.

---

## 📦 Arquivos do Projeto

- **maze_editor_GUI.py** → Código fonte completo da aplicação.
- **README.md** → Documentação.
