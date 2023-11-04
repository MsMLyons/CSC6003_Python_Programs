def quad(a, b, c):
    if 4 * a * c > b ** 2:
        print("Sorry, this one's complex!")
    else:
        x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
quad(3, 4, 4)

