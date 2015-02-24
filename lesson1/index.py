# 1
import this


# 2
import math
print(math.factorial(100))


# 3
data = [
    "Hello World!",
    "Hi pythonistas.",
    "Hello phpists and bye",
    "HELLO AND GOODBYE.",
    "Abracadabra",
    "import antigravity",
    ]
# 3.1
print(max(data, key=lambda x: x.count("a")))
# 3.2
print(data[::2])
# 3.3
for i in data:
    if i.lower().startswith("hello") and not i.lower().endswith("bye"):
        print(i)
# 3.4
print(" ".join(sorted(data)))


# 4
d = {"q": 3, "w": 8, "e": "z", "r": "5", "t": 3}
# 4.1
print({v: k for k, v in d.items()})
# 4.2
for k in sorted(d): print(d[k])
# 4.3
for k, v in d.items():
    if isinstance(v, int):
        d[k] = v + 1
    elif isinstance(v, str):
        d[k] = v + "b"
print(d)


# 5
input = ["a", 1, "b", 2]
print(dict(zip(input[0::2], input[1::2])))


# 6
def get_prime_numbers(n):
    res = []
    for i in range(2, n + 1):
        for j in res:
            if i % j == 0:
                break
        else:
            res.append(i)
    return res
print(get_prime_numbers(12))


# 7
def get_sum_args(*args):
    return sum(args)
print(get_sum_args(1, 5, 10))


# 8
input = [1, 2, 3, 4, [4, 5, [6, 7]], 8]
def get_simle_list(lst, res=None):
    if res is None:
        res = []
    for i in lst:
        if isinstance(i, list):
            get_simle_list(i, res=res)
        else:
            res.append(i)
    return res
print(get_simle_list(input))