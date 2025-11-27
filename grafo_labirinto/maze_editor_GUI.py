import tkinter as tk
from tkinter import messagebox
from collections import deque

# CONFIGURAÇÕES E CONSTANTES
LARGURA_GRADE = 30
ALTURA_GRADE = 20
TAMANHO_CELULA = 25
DELAY_ANIMACAO = 20

CORES = {
    'PAREDE': "#1E3A5F",
    'CAMINHO': "#FFFFFF",
    'INICIO': "#4CAF50",
    'FIM': "#F44336",
    'FRONTEIRA': "#AED6F1",
    'VISITADO': "#D6EAF8",
    'CAMINHO_FINAL': "#FFD700"
}

class MazeEditorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Solucionador de Labirintos - BFS Interativo")
        
        # --- MODELO DE DADOS ---
        # Matriz 20x30 inicializada com caminhos vazios (' ')
        self.labirinto = [[' ' for _ in range(LARGURA_GRADE)] for _ in range(ALTURA_GRADE)]
        
        # Matriz para guardar os IDs dos retângulos do Canvas (para mudar cor depois)
        self.grid_ids = [[None for _ in range(LARGURA_GRADE)] for _ in range(ALTURA_GRADE)]
        
        # Estado do jogo
        self.pos_inicio = None
        self.pos_fim = None
        self.em_simulacao = False
        self.fila = deque()
        self.visitados = set()
        self.predecessores = {}
        self.job_animacao = None

        # Variável para ferramenta selecionada
        # Valores: '#', ' ', 'S', 'E'
        self.ferramenta_var = tk.StringVar(value='#')

        self._criar_interface()
        self._desenhar_grade_inicial()

    def _criar_interface(self):
        """Monta o layout: Painel lateral de controle e Canvas."""
        
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        controls_frame = tk.Frame(main_frame, width=200)
        controls_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        tk.Label(controls_frame, text="Ferramentas de Edição", font=("Arial", 10, "bold")).pack(pady=(0, 5))

        # Radiobuttons
        opcoes = [
            ("Parede (#)", '#'),
            ("Caminho ( )", ' '),
            ("Início (S)", 'S'),
            ("Fim (E)", 'E')
        ]

        for text, value in opcoes:
            rb = tk.Radiobutton(controls_frame, text=text, variable=self.ferramenta_var, value=value, indicatoron=0, width=20, selectcolor="#DDDDDD")
            rb.pack(pady=2, ipady=3)

        # Separador
        tk.Frame(controls_frame, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=15)

        # Botões de Ação
        tk.Label(controls_frame, text="Simulação", font=("Arial", 10, "bold")).pack(pady=(0, 5))
        
        self.btn_iniciar = tk.Button(controls_frame, text="▶ Iniciar BFS", bg="#4CAF50", fg="white", command=self.iniciar_busca)
        self.btn_iniciar.pack(fill=tk.X, pady=2)

        self.btn_reset_busca = tk.Button(controls_frame, text="↺ Resetar Busca", command=self.resetar_busca)
        self.btn_reset_busca.pack(fill=tk.X, pady=2)

        self.btn_limpar = tk.Button(controls_frame, text="🗑 Limpar Labirinto", bg="#F44336", fg="white", command=self.limpar_labirinto)
        self.btn_limpar.pack(fill=tk.X, pady=(15, 2))

        # ÁREA DE DESENHO
        canvas_width = LARGURA_GRADE * TAMANHO_CELULA
        canvas_height = ALTURA_GRADE * TAMANHO_CELULA
        
        self.canvas = tk.Canvas(main_frame, width=canvas_width, height=canvas_height, bg="white", highlightthickness=1, highlightbackground="black")
        self.canvas.pack(side=tk.RIGHT)

        # Eventos de Mouse
        self.canvas.bind("<Button-1>", self._evento_clique)   # Clique único
        self.canvas.bind("<B1-Motion>", self._evento_clique)  # Arrastar

    def _desenhar_grade_inicial(self):
        """Cria os retângulos no canvas uma única vez."""
        for l in range(ALTURA_GRADE):
            for c in range(LARGURA_GRADE):
                x1 = c * TAMANHO_CELULA
                y1 = l * TAMANHO_CELULA
                x2 = x1 + TAMANHO_CELULA
                y2 = y1 + TAMANHO_CELULA
                
                rect_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=CORES['CAMINHO'], outline="#E0E0E0")
                self.grid_ids[l][c] = rect_id

    # LÓGICA DE EDIÇÃO
    def _evento_clique(self, event):
        """Manipula cliques e arrastos para editar o labirinto."""
        if self.em_simulacao:
            return

        # Converte coordenada de pixel para índice da matriz
        c = event.x // TAMANHO_CELULA
        l = event.y // TAMANHO_CELULA

        # Verifica limites
        if 0 <= l < ALTURA_GRADE and 0 <= c < LARGURA_GRADE:
            ferramenta = self.ferramenta_var.get()
            self._pintar_celula(l, c, ferramenta)

    def _pintar_celula(self, l, c, tipo):
        """Atualiza o modelo lógico e visual de uma célula."""
        
        # Regra de Unicidade para S e E
        if tipo == 'S':
            if self.pos_inicio:
                old_l, old_c = self.pos_inicio
                self.labirinto[old_l][old_c] = ' '
                self.canvas.itemconfig(self.grid_ids[old_l][old_c], fill=CORES['CAMINHO'])
            self.pos_inicio = (l, c)
        
        elif tipo == 'E':
            if self.pos_fim:
                old_l, old_c = self.pos_fim
                self.labirinto[old_l][old_c] = ' '
                self.canvas.itemconfig(self.grid_ids[old_l][old_c], fill=CORES['CAMINHO'])
            self.pos_fim = (l, c)
        
        if (l, c) == self.pos_inicio and tipo not in ['S']:
            self.pos_inicio = None
        if (l, c) == self.pos_fim and tipo not in ['E']:
            self.pos_fim = None

        # Atualiza Lógica
        self.labirinto[l][c] = tipo
        
        # Atualiza Visual
        cor = CORES['CAMINHO']
        if tipo == '#': cor = CORES['PAREDE']
        elif tipo == 'S': cor = CORES['INICIO']
        elif tipo == 'E': cor = CORES['FIM']
        
        self.canvas.itemconfig(self.grid_ids[l][c], fill=cor)

    # LÓGICA DE SIMULAÇÃO
    def iniciar_busca(self):
        """Prepara e inicia o algoritmo BFS."""
        if not self.pos_inicio or not self.pos_fim:
            messagebox.showwarning("Atenção", "Defina o Ponto de Início (S) e o Ponto de Fim (E) antes de começar.")
            return

        if self.em_simulacao:
            return

        self.resetar_busca(manter_labirinto=True)
        self.em_simulacao = True
        self._alternar_controles(estado="disabled")

        self.fila = deque([self.pos_inicio])
        self.visitados = {self.pos_inicio}
        self.predecessores = {self.pos_inicio: None}

        self.processar_passo_bfs()

    def processar_passo_bfs(self):
        """Executa UM passo do BFS e se agenda novamente (Loop de Animação)."""
        if not self.fila:
            self.em_simulacao = False
            self._alternar_controles(estado="normal")
            messagebox.showinfo("Resultado", "Caminho não encontrado! O destino é inalcançável.")
            return

        # 1. Retira da fila
        atual = self.fila.popleft()
        l, c = atual

        # Se encontrou o fim
        if atual == self.pos_fim:
            self.reconstruir_caminho()
            self.em_simulacao = False
            self._alternar_controles(estado="normal")
            return

        # 2. Visualização: Marca como Visitado (exceto se for o Início)
        if atual != self.pos_inicio:
            self.canvas.itemconfig(self.grid_ids[l][c], fill=CORES['VISITADO'])

        # 3. Explorar Vizinhos (Cima, Baixo, Esquerda, Direita)
        vizinhos = [(l-1, c), (l+1, c), (l, c-1), (l, c+1)]

        for vl, vc in vizinhos:
            # Verifica limites, se não é parede e se não foi visitado
            if (0 <= vl < ALTURA_GRADE and 
                0 <= vc < LARGURA_GRADE and 
                self.labirinto[vl][vc] != '#' and 
                (vl, vc) not in self.visitados):

                self.visitados.add((vl, vc))
                self.predecessores[(vl, vc)] = atual
                self.fila.append((vl, vc))
                
                # Visualização: Marca como Fronteira (Na fila) - Exceto se for o Fim
                if (vl, vc) != self.pos_fim:
                    self.canvas.itemconfig(self.grid_ids[vl][vc], fill=CORES['FRONTEIRA'])

        # 4. Agenda o próximo passo
        self.job_animacao = self.root.after(DELAY_ANIMACAO, self.processar_passo_bfs)

    def reconstruir_caminho(self):
        """Rastreia de volta do Fim ao Início usando os predecessores."""
        atual = self.predecessores.get(self.pos_fim)
        
        while atual is not None and atual != self.pos_inicio:
            l, c = atual
            self.canvas.itemconfig(self.grid_ids[l][c], fill=CORES['CAMINHO_FINAL'])
            # Pequeno delay visual no backtracking também, se quiser (opcional)
            # self.root.update() 
            # self.root.after(50)
            atual = self.predecessores.get(atual)

    # CONTROLES GERAIS
    def resetar_busca(self, manter_labirinto=False):
        """Limpa as cores da busca, mantendo paredes, S e E."""
        # Cancela animação pendente se houver
        if self.job_animacao:
            self.root.after_cancel(self.job_animacao)
            self.job_animacao = None
        
        self.em_simulacao = False
        self._alternar_controles(estado="normal")

        for l in range(ALTURA_GRADE):
            for c in range(LARGURA_GRADE):
                char = self.labirinto[l][c]
                # Se for visitado, fronteira ou caminho final, restaura cor original
                # Note que S, E e # (Parede) não mudam
                if char not in ['S', 'E', '#']:
                    self.canvas.itemconfig(self.grid_ids[l][c], fill=CORES['CAMINHO'])
                elif char == 'S':
                    self.canvas.itemconfig(self.grid_ids[l][c], fill=CORES['INICIO'])
                elif char == 'E':
                    self.canvas.itemconfig(self.grid_ids[l][c], fill=CORES['FIM'])

    def limpar_labirinto(self):
        """Reseta tudo para o estado zero."""
        self.resetar_busca()
        self.labirinto = [[' ' for _ in range(LARGURA_GRADE)] for _ in range(ALTURA_GRADE)]
        self.pos_inicio = None
        self.pos_fim = None
        
        for l in range(ALTURA_GRADE):
            for c in range(LARGURA_GRADE):
                self.canvas.itemconfig(self.grid_ids[l][c], fill=CORES['CAMINHO'])

    def _alternar_controles(self, estado):
        """Habilita ou desabilita botões durante a simulação."""
        self.btn_iniciar.config(state=estado)
        self.btn_limpar.config(state=estado)
        # O btn_reset_busca geralmente fica ativo para permitir cancelar, 
        # mas aqui vamos deixar ativo sempre.

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeEditorGUI(root)
    
    # Centraliza a janela
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 1000
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    root.mainloop()