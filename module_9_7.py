#Декоратор
def is_prime(func):
    def wrapper(*args):
        tmp_res = func(*args)
        if tmp_res > 1:
            for i in range(2, tmp_res):
                if tmp_res % i == 0:
                    print('Составное')
                    break
                else:
                    print('Простое')
                    break
        return tmp_res
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

@is_prime
def sum_many(*args):
    return sum(args)

result = sum_three(2, 4, 6)
print(result)

result_1 = sum_many(2, 4, 6, 10, 3, 8)
print(result_1)