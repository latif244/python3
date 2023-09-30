def add(a , b):
    result = a + b
    return result


def multiplication(a, b):
    return a * 10
    return b * 2


def remainder(a, b):
    return a % b

def add10(a,b):
    results1= a * 10
    results2 = b * 10
    return (results1, results2)


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime(a, b):
    if is_prime(a) and is_prime(b):
        return "Both numbers are prime"
    elif is_prime(a):
        return f"{a} is prime, but {b} is not"
    elif is_prime(b):
        return f"{b} is prime, but {a} is not"
    else:
        return f"Neither {a} nor {b} is prime"


