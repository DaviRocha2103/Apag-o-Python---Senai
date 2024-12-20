
user = {
    "nome": "Davi",
    "senha": "davi123",
}

player = {
    "nick": "DVzad",
    "classe": {
        "principal": "Mago",
        "segundario": "Assassino"
    },
    "arma": ["cajado", "espada", "adaga"],
    "nivel": 10
}

'''
print(user.keys(), player.keys())

print(user.values(), player.values())

print(user.items())
print(player.items())
'''
usuario = user.get("nome")
senha = user.get("senha")

__user__ = str(input("Insira seu Usuário: "))
__password__ = str(input("Insira sua Senha: "))

__classe__ = player.get("classe")
print(__classe__.keys())
__principal__ = __classe__.get("principal")
__secundaria__ = __classe__.get("secundario")

if __user__ == usuario and __password__ == senha:
    print("Bem-Vindo, " + user.get("nome") + "!")
    print(f"Você é um(a) {__principal__} / {__secundaria__} nivel: [ {player.get("nivel")} ]")

    armas = player.get("arma")
    print(armas)
    item_0 = armas[0]
    item_1 = armas[1]
    item_2 = armas[2]

    __inventario__ = [item_0, item_1, item_2]

    print(f"Inventario: {__inventario__[0]}")
    print(f"            {__inventario__[1]}")
    print(f"            {__inventario__[2]}")


else: 
    print("usuario invalido")

