import socket
import threading

# Definição de host e porta
HOST = '127.0.0.1'
PORT = 8080

# Lista para armazenar os clientes conectados
clients = []

# Função para enviar mensagens a todos os clientes, exceto o remetente
def broadcast(message, _client):
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                clients.remove(client)

# Função para lidar com cada cliente
def handle_client(client):
    while True:
        try:
            # Recebe mensagens do cliente
            message = client.recv(1024)
            if message:
                print(f"Mensagem recebida: {message.decode()}")
                broadcast(message, client)
        except:
            # Remove o cliente em caso de erro ou desconexão
            clients.remove(client)
            client.close()
            break

# Função principal para gerenciar as conexões
def main():
    # Criação do socket do servidor
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Servidor iniciado em {HOST}:{PORT}...")

    while True:
        # Aceita novas conexões
        client, addr = server.accept()
        print(f"Conectado com {addr}...")
        clients.append(client)
        # Inicia uma thread para o cliente conectado
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    main()