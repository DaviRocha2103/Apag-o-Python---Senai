import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import sv_ttk

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class EDAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Análise Exploratória de Dados")
        self.root.geometry("900x800")
        
        # Aplicando o tema sv-ttk
        sv_ttk.set_theme("dark")

        # Botão para carregar arquivo
        self.load_button = ttk.Button(root, text="Carregar Arquivo", command=self.load_csv)
        self.load_button.pack(pady=10)

        # Tabela para exibir os dados
        self.tree = ttk.Treeview(root)
        self.tree.pack(pady=20, fill='both', expand=True)

        # Botão para mostrar estatísticas
        self.stats_button = ttk.Button(root, text="Mostrar Estatísticas", command=self.show_stats)
        self.stats_button.pack(pady=10)

        # Botão para mostrar gráficos
        self.plot_button = ttk.Button(root, text="Plotar Gráficos", command=self.plot_data)
        self.plot_button.pack(pady=10)

        # DataFrame inicial vazio
        self.df = None

    def load_csv(self):
        # Abrir diálogo para carregar arquivo CSV
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return
        try:
            self.df = pd.read_csv(file_path)
            self.display_data()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível carregar o arquivo: {e}")

    def display_data(self):
        if self.df is not None:
            # Limpar a tabela antes de exibir novos dados
            self.tree.delete(*self.tree.get_children())
            self.tree["columns"] = list(self.df.columns)
            self.tree["show"] = "headings"

            # Configurar cabeçalhos e colunas
            for col in self.df.columns:
                self.tree.heading(col, text=col)
                self.tree.column(col, anchor="center")

            # Inserir as primeiras 10 linhas no Treeview
            for i in range(min(len(self.df), 15)):
                self.tree.insert('', 'end', values=list(self.df.iloc[i]))

    def show_stats(self):
        if self.df is not None:
            # Calcular estatísticas descritivas
            stats = self.df.describe()

            # Criar uma nova janela para exibir as estatísticas
            stats_window = tk.Toplevel(self.root)
            stats_window.title("Estatísticas")

            # Caixa de texto para mostrar os dados estatísticos
            text = tk.Text(stats_window, wrap="none", width=100, height=20)
            text.insert("1.0", stats.to_string())
            text.pack(padx=10, pady=10)
        else:
            messagebox.showwarning("Aviso", "Arquivo não carregado!")
    
    def plot_data(self):
        if self.df is not None:
            # Obter nomes das colunas numéricas
            column_names = self.df.select_dtypes(include="number").columns.tolist()
            if not column_names:
                messagebox.showwarning("Aviso", "Não há colunas numéricas!")
                return

            # Criar nova janela para o gráfico
            plot_window = tk.Toplevel(self.root)
            plot_window.title("Gráficos")

            # Criar figura e eixo do Matplotlib
            fig, ax = plt.subplots()

            # Plotar histograma da primeira coluna numérica
            self.df[column_names[0]].plot(kind='hist', ax=ax, title=f"Histograma de {column_names[0]}")
            
            # Adicionar o gráfico ao Tkinter
            canvas = FigureCanvasTkAgg(fig, plot_window)
            canvas.draw()
            canvas.get_tk_widget().pack(padx=10, pady=10)
        else:
            messagebox.showwarning("Aviso", "Por favor, carregue o arquivo primeiro!")

if __name__ == '__main__':
    root = tk.Tk()
    app = EDAApp(root)
    root.mainloop()