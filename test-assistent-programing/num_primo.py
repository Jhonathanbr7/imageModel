def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Verifica divisores ímpares até √n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        # Solicita número ao usuário
        numero = input("Digite um número inteiro: ")

        numero = int(numero)

        if eh_primo(numero):
            print(f"{numero} é um número primo! ✓")
        else:
            print(f"{numero} não é um número primo. ✗")

    except ValueError:
        print("Erro: Digite apenas números inteiros.")
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
