import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ContaBancaria:
    def __init__(self, titular, conta, saldo):
        self.titular = titular
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def consultar_saldo(self):
        return self.saldo

def inserir_conta():
    conta = entrada_nova_conta.get()
    titular = entrada_novo_titular.get()

    if not titular or not conta:
        messagebox.showinfo('Mensagem', 'Preencha todos os campos')
    elif conta in contas:
        messagebox.showinfo('Mensagem', 'Número de conta já cadastrado')
    else:
        contas[conta] = ContaBancaria(titular, conta, 0)
        messagebox.showinfo('Mensagem', 'Conta cadastrada com sucesso')
    limpar_campos()

def verificar_conta():
    numero_conta = entrada_conta.get()
    if numero_conta in contas:
        saldo = contas[numero_conta].consultar_saldo()
        messagebox.showinfo('Mensagem', f'Seu saldo é: R${saldo:.2f}')
    else:
        messagebox.showinfo('Mensagem', 'Conta não encontrada')
    limpar_campos()

def novo_deposito():
    numero_conta = entrada_conta.get()
    valor = entrada_valor.get()

    if numero_conta in contas:
        try:
            valor = float(valor)
            contas[numero_conta].depositar(valor)
            messagebox.showinfo('Mensagem', 'Depósito realizado com sucesso')
            messagebox.showinfo('Mensagem', f'Seu saldo é: R${contas[numero_conta].consultar_saldo():.2f}')
        except ValueError:
            messagebox.showinfo('Mensagem', 'Digite um valor válido')
    else:
        messagebox.showinfo('Mensagem', 'Conta não encontrada')
    limpar_campos()

def novo_saque():
    numero_conta = entrada_conta.get()
    valor = entrada_valor.get()

    if numero_conta in contas:
        try:
            valor = float(valor)
            if contas[numero_conta].sacar(valor):
                messagebox.showinfo('Mensagem', 'Saque realizado com sucesso')
                messagebox.showinfo('Mensagem', f'Seu saldo é: R${contas[numero_conta].consultar_saldo():.2f}')
            else:
                messagebox.showinfo('Mensagem', f'Saldo insuficiente. Saldo atual: R${contas[numero_conta].consultar_saldo():.2f}')
        except ValueError:
            messagebox.showinfo('Mensagem', 'Digite um valor válido')
    else:
        messagebox.showinfo('Mensagem', 'Conta não encontrada')
    limpar_campos()

def limpar_campos():
    entrada_conta.delete(0, tk.END)
    entrada_valor.delete(0, tk.END)
    entrada_nova_conta.delete(0, tk.END)
    entrada_novo_titular.delete(0, tk.END)

contas = {
    '1234': ContaBancaria('Erick', '1234', 0),
    '5678': ContaBancaria('Orlando', '5678', 0),
}

# Configuração da Janela Principal
root = tk.Tk()
root.title('Caixa Eletrônico')
root.geometry('600x400')
root.resizable(False, False)
root.configure(bg='#f0f0f0')

# Estilos
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12), background='#f0f0f0')
style.configure('TButton', font=('Arial', 12), padding=5)
style.configure('Header.TLabel', font=('Arial', 16, 'bold'))

# Seção: Operações com Conta
ttk.Label(root, text='Operações com a Conta', style='Header.TLabel').grid(row=0, column=1, pady=10)

ttk.Label(root, text='Número da Conta:').grid(row=1, column=0, sticky='e', padx=10)
entrada_conta = ttk.Entry(root, width=30)
entrada_conta.grid(row=1, column=1, pady=5)

ttk.Label(root, text='Valor:').grid(row=2, column=0, sticky='e', padx=10)
entrada_valor = ttk.Entry(root, width=30)
entrada_valor.grid(row=2, column=1, pady=5)

frame_botoes = tk.Frame(root, bg='#f0f0f0')
frame_botoes.grid(row=3, column=1, pady=10)

ttk.Button(frame_botoes, text='Mostrar Saldo', command=verificar_conta).grid(row=0, column=0, padx=5)
ttk.Button(frame_botoes, text='Depositar', command=novo_deposito).grid(row=0, column=1, padx=5)
ttk.Button(frame_botoes, text='Sacar', command=novo_saque).grid(row=0, column=2, padx=5)

# Separador
ttk.Separator(root, orient='horizontal').grid(row=4, column=0, columnspan=3, pady=20, sticky='ew')

# Seção: Cadastro de Nova Conta
ttk.Label(root, text='Cadastro de Nova Conta', style='Header.TLabel').grid(row=5, column=1, pady=10)

ttk.Label(root, text='Número da Conta:').grid(row=6, column=0, sticky='e', padx=10)
entrada_nova_conta = ttk.Entry(root, width=30)
entrada_nova_conta.grid(row=6, column=1, pady=5)

ttk.Label(root, text='Titular:').grid(row=7, column=0, sticky='e', padx=10)
entrada_novo_titular = ttk.Entry(root, width=30)
entrada_novo_titular.grid(row=7, column=1, pady=5)

ttk.Button(root, text='Adicionar Conta', command=inserir_conta).grid(row=8, column=1, pady=10)

# Inicialização da Interface
root.mainloop()
