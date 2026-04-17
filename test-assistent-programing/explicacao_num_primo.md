# Verificação de Números Primos

## Código

```python
def eh_primo(n):
    """Verifica se um número é primo."""
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False

    return True

if __name__ == "__main__":
    try:
        numero = int(input("Digite um número: "))
        resultado = "é primo" if eh_primo(numero) else "não é primo"
        print(f"{numero} {resultado}")
    except ValueError:
        print("Digite apenas números inteiros")
```

## Como Usar

```bash
python num_primo.py
Digite um número: 17
17 é primo
```

## Algoritmo

- Números menores que 2 não são primos
- 2 é primo
- Pares maiores que 2 não são primos
- Verifica divisores ímpares até √n
