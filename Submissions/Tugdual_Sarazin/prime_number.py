def prime_numbers(max):
    start = 2
    end = max + 1
    n = [True for i in range(start, end)]

    for a in range(start, end):
        if n[a - start]:
            for b in range(a + 1, end):
                # print(a, b, n[b - start], b % a)
                if b % a == 0:
                    n[b - start] = False

    nn = []
    for i in range(start, end):
        if n[i - start]:
            nn.append(i)

    return nn


assert prime_numbers(10) == [2, 3, 5, 7]

assert prime_numbers(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                              89, 97]

print(prime_numbers(100))