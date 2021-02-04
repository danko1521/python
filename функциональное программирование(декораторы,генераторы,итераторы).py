# def fibonacci(n):
#     resualt = []
#     a, b = 0, 1
#     for _ in range(n):
#         resualt.append(a)
#         a, b = b, a + b
#     return resualt
#
#
# fib = fibonacci(n=10)
# print(fib)
# for value in fib:
#     print(value)


# class Fibonacci:
#     """Итератор последовательности фибоначчи до N элементов"""
#
#     def __init__(self, n):
#         self.i, self.a, self.b, self.n = 0, 0, 1, n
#
#     def __iter__(self):
#         self.i, self.a, self.b, = 0, 0, 1
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > 1:
#             if self.i > self.n:
#                 raise StopIteration()
#             self.a, self.b = self.b, self.a + self.b
#         return self.a
#
#
# fib_iterator = Fibonacci(n=10)
# print(fib_iterator)
# for value in fib_iterator:
#     print(value)
# print(13 in fib_iterator)

# ____________________________________________Итератор_________________________________


import time


def time_track(func, *args, **kwargs):
    started_at = time.time()

    result = func(*args, **kwargs)

    ended_at = time.time()
    elapsed = round(ended_at - started_at, 4)
    print(f'Функция работала {elapsed} секунд(ы)')
    return result


def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


result = time_track(digits, 3141, 5926, 2718, 2818)
print(result)



#--------------------------------Декоратор------------------------------------------------