def check_number(num):
    if is_prime(num):
        return str(num) + " is a prime number\n"
    else:
        return str(num) + " is not a prime number\n"

def is_prime(num):
    if num <= 1:
        return False
    divisor = 2
    while divisor <= num // 2:
        if num % divisor == 0:
            return False
        divisor += 1
    return True

num: int = 181
status: str = check_number(num)
print(status)