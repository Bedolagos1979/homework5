a = ('угу', 'работа', 'трудно', 'ага', 'ара', 'привет', 'мир')


def spil(x):
    if x == x[::-1]:
        return x


a_1 = list(filter(spil, a))
print(a_1)
