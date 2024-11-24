from libs.my_fraction import Fraction


def main():
    # Création de fractions
    f1 = Fraction(3, 4)
    f2 = Fraction(5, 6)
    print(f"Fraction 1: {f1}")
    print(f"Fraction 2: {f2}")

    # Addition
    result_add = f1 + f2
    print(f"Addition: {f1} + {f2} = {result_add}")

    # Soustraction
    result_sub = f1 - f2
    print(f"Soustraction: {f1} - {f2} = {result_sub}")

    # Multiplication
    result_mul = f1 * f2
    print(f"Multiplication: {f1} * {f2} = {result_mul}")

    # Division
    result_div = f1 / f2
    print(f"Division: {f1} / {f2} = {result_div}")

    # Puissance
    result_pow = f1 ** 2
    print(f"Puissance: {f1}^2 = {result_pow}")

    # Représentation en nombre mixte
    mixed = result_add.as_mixed_number()
    print(f"Nombre mixte de {result_add}: {mixed}")

    # Comparaison
    are_equal = f1 == f2
    print(f"{f1} == {f2}: {are_equal}")

    # Décimal
    decimal_value = float(f1)
    print(f"Valeur décimale de {f1}: {decimal_value}")

    # Valeur absolue
    f3 = Fraction(-3, 4)
    abs_value = abs(f3)
    print(f"Valeur absolue de {f3}: {abs_value}")

    # Vérifications des propriétés
    print(f"{f1} est-il un entier ? {f1.is_integer()}")
    print(f"{f1} est-il propre ? {f1.is_proper()}")
    print(f"{f1} est-il unitaire ? {f1.is_unit()}")
    print(f"{f1} est-il adjacent à {f2} ? {f1.is_adjacent_to(f2)}")

if __name__ == "__main__":
    main()

