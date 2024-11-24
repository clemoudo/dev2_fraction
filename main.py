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
    print(f"Soustraction: {f1} - {f2} = {f1 - f2}")

    # Multiplication
    print(f"Multiplication: {f1} * {f2} = {f1 * f2}")

    # Division
    print(f"Division: {f1} / {f2} = {f1 / f2}")

    # Puissance
    my_pow = 2
    print(f"Puissance: {f1}^{my_pow} = {f1 ** my_pow}")

    # Mixed number
    mixed = result_add.as_mixed_number()
    print(f"Nombre mixte de {result_add}: {mixed}")

    # Egalité
    print(f"{f1} == {f2}: {f1 == f2}")

    # Float
    print(f"Valeur décimale de {f1}: {float(f1)}")

    # Valeur absolue
    f3 = Fraction(-3, 4)
    print(f"Valeur absolue de {f3}: {abs(f3)}")

    # Vérifications des propriétés
    print(f"{f1} est-il un entier ? {f1.is_integer()}")
    print(f"{f1} est-il propre ? {f1.is_proper()}")
    print(f"{f1} est-il unitaire ? {f1.is_unit()}")
    print(f"{f1} est-il adjacent à {f2} ? {f1.is_adjacent_to(f2)}")

if __name__ == "__main__":
    main()
