from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)

# Base de dados local
clients = {}
messages = []

# Simulador de banco de dados
users = []

# Rota CRUD para criar e listar usuários
@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'POST':
        data = request.get_json()  # Corrigido para chamar a função corretamente
        if not data or not isinstance(data, dict):  # Validação de dados
            return jsonify({"message": "Dados inválidos"}), 400
        if 'name' not in data or 'age' not in data:
            return jsonify({"message": "Campos obrigatórios: name e age"}), 400
        users.append(data)
        return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201
    return jsonify(users), 200

# Evento Socket.IO ao conectar
@socketio.on('connect')
def handle_connect():
    client_id = request.sid
    clients[client_id] = "Anônimo"
    emit('update_clients', list(clients.values()), broadcast=True)

# Evento Socket.IO ao desconectar
@socketio.on('disconnect')
def handle_disconnect():
    client_id = request.sid
    if client_id in clients:
        clients.pop(client_id)
        emit('update_clients', list(clients.values()), broadcast=True)

# Evento Socket.IO para configurar o nome de usuário
@socketio.on('set_username')
def set_username(data):
    client_id = request.sid
    username = data.get('username', "Anônimo")
    clients[client_id] = username
    emit('update_clients', list(clients.values()), broadcast=True)

# Evento Socket.IO para enviar mensagens em tempo real
@socketio.on('send_message')
def handle_message(data):
    username = clients.get(request.sid, "Anônimo")
    message = {
        'username': username,
        'message': data.get('message', '')
    }
    messages.append(message)
    emit('receive_message', message, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)
