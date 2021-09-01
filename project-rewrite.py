def minimal(a, b):
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a

def maximum(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a

def length(a):
    x = 0
    for elem in a:
        x += 1
    return x

def multiply(a, b):
    x = 0
    for c in range(b):
        x += a 
    return x

def power(a, b):
    x = 1
    for c in range(0, b):
        x = x * a
    return x

def division_modulo(a, b):
    x = 0
    while a - b > 0:
        a -= b
        x += 1
    return (x, a)

if __name__ == "__main__":
    print("minimal")
    print(minimal(1, 2))
    print("maximum")
    print(maximum(6, 7))
    print("length")
    print(length(input()))
    print("multiply")
    print(multiply(9, 2))
    print("power")
    print(power(5, 3))
    print("division modulo")
    print(division_modulo(8, 3))