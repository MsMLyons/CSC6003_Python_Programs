

def quadratic_formula():
    a = float(input("Please enter a value for a: "))
    b = float(input("Please enter a value for b: "))
    c = float(input("Please enter a value for c: "))

    determinant = b ** 2 - 4 * a * c
    x1 = (-b + (determinant) ** 0.5) / (2 * a)
    x2 = (-b - (determinant) ** 0.5) / (2 * a)

    print(f"The lesser value of x is equal to {x1} and the greater value is equal to {x2}.")
quadratic_formula()