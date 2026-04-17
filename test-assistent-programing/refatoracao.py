def summarize_numbers(numbers):
    """Return total, average, maximum and minimum values for a list of numbers."""
    if not numbers:
        raise ValueError("A lista de números não pode ser vazia.")

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum


def main():
    values = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, average, highest, lowest = summarize_numbers(values)

    print("Total:", total)
    print("Média:", average)
    print("Maior:", highest)
    print("Menor:", lowest)


if __name__ == "__main__":
    main()