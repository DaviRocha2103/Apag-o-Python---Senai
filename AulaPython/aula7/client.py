import tkinter as tk
from tkinter import ttk
import sv_ttk
from tkinter import messagebox
import socketio
import requests

# Configurações do cliente e servidor
sio = socketio.Client()
SERVER_URL = 'http://localhost:5000'

# Conectar ao servidor
def connect_server():
    try:
        sio.connect(SERVER_URL)
        lbl_status.config(text="Conectado ao servidor", foreground="green")

        # Eventos do servidor
        sio.on('update_clients', update_clients)
        sio.on('receive_message', receive_message)
    except Exception as e:
        lbl_status.config(text=f"Erro ao conectar: {e}", foreground="red")

# Atualiza a lista de clientes conectados
def update_clients(data):
    listbox_clients.delete(0, tk.END)
    for client in data:
        listbox_clients.insert(tk.END, client)

# Exibe mensagens recebidas no chat
def receive_message(data):
    chat_history.insert(tk.END, f"{data['username']}: {data['message']}")

# Enviar mensagens no chat
def send_message():
    if not username.get():
        messagebox.showwarning("Aviso", "Configure seu nome de usuário primeiro!")
        return

    message = entry_message.get()
    if message:
        sio.emit('send_message', {'username': username.get(), 'message': message})
        entry_message.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "A mensagem não pode estar vazia.")

# Configurar o nome de usuário
def set_username():
    if username.get():
        sio.emit('set_username', {'username': username.get()})
        lbl_status.config(text="Nome de usuário configurado", foreground="green")
    else:
        messagebox.showwarning("Aviso", "O nome de usuário não pode estar vazio.")

# Criar usuário via REST API
def create_user():
    name = entry_name.get()
    age = entry_age.get()

    if name and age:
        try:
            response = requests.post(f'{SERVER_URL}/users', json={'name': name, 'age': age})
            if response.status_code == 201:
                lbl_status_crud.config(text="Usuário cadastrado com sucesso!", foreground="green")
            else:
                lbl_status_crud.config(text="Erro ao cadastrar usuário.", foreground="red")
        except Exception as e:
            lbl_status_crud.config(text=f"Erro ao conectar ao servidor: {e}", foreground="red")
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos.")

    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)

# Buscar usuários cadastrados
def fetch_users():
    try:
        response = requests.get(f'{SERVER_URL}/users')
        if response.status_code == 200:
            users = response.json()
            listbox_users.delete(0, tk.END)
            for user in users:
                listbox_users.insert(tk.END, f"Nome: {user['name']}, Idade: {user['age']}")
        else:
            messagebox.showerror("Erro", "Erro ao buscar usuários no servidor.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao servidor: {e}")

# Iniciar a interface Tkinter
root = tk.Tk()
root.title("Chat e Gerenciador de Usuários")
root.geometry("800x600")
sv_ttk.use_dark_theme()  # Aplicar tema escuro

# Notebook (abas)
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Abas: Chat, Configuração de Usuário e CRUD de Usuários
frame_chat = ttk.Frame(notebook, padding=10)
frame_user = ttk.Frame(notebook, padding=10)
frame_crud = ttk.Frame(notebook, padding=10)

notebook.add(frame_chat, text="Chat")
notebook.add(frame_user, text="Configurar Usuário")
notebook.add(frame_crud, text="Gerenciar Usuários")

# Layout da aba Chat
ttk.Label(frame_chat, text="Histórico do Chat", font=("Helvetica", 12)).pack()
chat_history = tk.Listbox(frame_chat, width=60, height=15, bg="#121212", fg="white", font=("Helvetica", 10))
chat_history.pack(pady=10)

entry_message = ttk.Entry(frame_chat, width=40)
entry_message.pack(side=tk.LEFT, padx=5, pady=5)
btn_send = ttk.Button(frame_chat, text="Enviar", command=send_message)
btn_send.pack(side=tk.LEFT, padx=5, pady=5)

ttk.Label(frame_chat, text="Usuários conectados", font=("Helvetica", 12)).pack(pady=10)
listbox_clients = tk.Listbox(frame_chat, width=50, height=10, bg="#121212", fg="white", font=("Helvetica", 10))
listbox_clients.pack()

# Layout da aba Configurar Usuário
ttk.Label(frame_user, text="Nome de Usuário", font=("Helvetica", 12)).pack(pady=5)
username = tk.StringVar()
entry_username = ttk.Entry(frame_user, textvariable=username, width=30)
entry_username.pack(pady=5)

btn_set_username = ttk.Button(frame_user, text="Entrar no Chat", command=set_username)
btn_set_username.pack(pady=10)

lbl_status = ttk.Label(frame_user, text="Status: Desconectado", font=("Helvetica", 10), foreground="red")
lbl_status.pack(pady=5)

# Layout da aba Gerenciar Usuários
ttk.Label(frame_crud, text="Cadastrar Novo Usuário", font=("Helvetica", 12)).pack(pady=5)

ttk.Label(frame_crud, text="Nome").pack(pady=2)
entry_name = ttk.Entry(frame_crud, width=30)
entry_name.pack(pady=5)

ttk.Label(frame_crud, text="Idade").pack(pady=2)
entry_age = ttk.Entry(frame_crud, width=30)
entry_age.pack(pady=5)

btn_create_user = ttk.Button(frame_crud, text="Cadastrar", command=create_user)
btn_create_user.pack(pady=10)

lbl_status_crud = ttk.Label(frame_crud, text="", font=("Helvetica", 10))
lbl_status_crud.pack(pady=5)

ttk.Label(frame_crud, text="Usuários Cadastrados", font=("Helvetica", 12)).pack(pady=10)
btn_fetch_users = ttk.Button(frame_crud, text="Atualizar Lista", command=fetch_users)
btn_fetch_users.pack(pady=5)

listbox_users = tk.Listbox(frame_crud, width=50, height=10, bg="#121212", fg="white", font=("Helvetica", 10))
listbox_users.pack()

# Conectar ao servidor e iniciar a interface
connect_server()
root.mainloop()
