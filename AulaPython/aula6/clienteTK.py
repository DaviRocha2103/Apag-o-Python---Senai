import socket
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

HOST = '127.0.0.1'
PORT = 8080

class ChatClient(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title('Chat Client')
        self.geometry('400x400')

        # Área do chat
        self.chat_area = scrolledtext.ScrolledText(self, state='normal', wrap='word')
        self.chat_area.pack(padx=10, pady=10, fill='both', expand=True)


        # Campo para digitar mensagens
        self.msg_entry = ttk.Entry(self)
        self.msg_entry.pack(padx=10, pady=10, fill='x')
        self.msg_entry.bind("<Return>", self.send_message)

        # Botão de envio
        self.send_button = ttk.Button(self, text="Enviar", command=self.send_message)
        self.send_button.pack(pady=5)

        # Conexão com o servidor
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((HOST, PORT))
            threading.Thread(target=self.receive_messages, daemon=True).start()
        except Exception as e:
            self.display_message(f"Erro ao conectar ao servidor: {e}")

    def send_message(self, event=None):
        message = self.msg_entry.get()
        if message:
            try:
                self.client.send(message.encode())
                self.msg_entry.delete(0, 'end')
            except:
                self.display_message("Erro ao enviar mensagem. Conexão encerrada.")
                self.client.close()

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode()
                if message:
                    self.display_message(message)
            except:
                self.display_message("Conexão com o servidor foi encerrada.")
                self.client.close()
                break

    def display_message(self, message):
        """Método auxiliar para exibir mensagens no chat."""
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + '\n')
        self.chat_area.config(state='disable')
        self.chat_area.yview(tk.END)

class App(tk.Tk): 
    def __init__(self):
        super().__init__()
        self.title("Chat GUI Client/Server")
        self.geometry("300x200")

        # Botão para abrir o chat
        tk.Button(self, text="Abrir Chat", command=self.open_chat).pack(pady=20)
  
    def open_chat(self):
        ChatClient(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()
