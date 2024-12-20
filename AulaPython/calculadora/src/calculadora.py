from meu_pacote import meu_modulo as modulo
from meu_pacote import meu_modulo_saudacao as saudacao

_control_ = False

nome = str(input("Para começar digite seu nome: "))
while _control_ == False:


    print("Calculadora Python")
    print(saudacao.saudacao(nome))
    num1 = float(input("Insira o primeiro numero: "))
    num2 = float(input("Insira o segundo numero: "))

    print(saudacao.escolha(nome))

    print("1 - Adicao")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("5 - Potencia")
    print("6 - Porcentagem")
    print("7 - Raiz quadrada")
    print("0 - Sair")
    opcao = int(input("Insira a opcao: "))

  

    if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5 or opcao == 6 or opcao == 7 or opcao == 0:
        match opcao:
            case 1:
                print(saudacao.resposta(nome))
                print(f"A soma dos números {num1} e {num2} é: {modulo.adicionar(num1, num2):.2f}")
            case 2:
                print(saudacao.resposta(nome))
                print(f"A subtração dos números {num1} e {num2} é: {modulo.subtrair(num1, num2):.2f}")
            case 3:
                print(saudacao.resposta(nome))
                print(f"A multiplicação dos números {num1} e {num2} é: {modulo.multiplicar(num1, num2):.2f}")
            case 4:
                print(saudacao.resposta(nome))
                print(f"A divisão dos números {num1} e {num2} é: {modulo.dividir(num1, num2):.2f}")
            case 5:
                print(saudacao.resposta(nome))
                print(f"A potência dos números {num1} e {num2} é: {modulo.potencia(num1, num2)}")
            case 6:
                print(saudacao.resposta(nome))
                print(f"{num1} porcento de {num2} é: {modulo.porcentagem(num1, num2):.2f}")
            case 7:
                print(saudacao.resposta(nome))
                print(f"A raiz quadrada de {num1} é: {modulo.raiz(num1):.2f}, e a raiz do {num2} é: {modulo.raiz(num2):.2f}")
            case 0:
                print("Encerrando...")
                _control_ = True
    else:
        print("Escolha errada")