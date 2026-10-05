def fatorar(n):
    fatores = {}
    d = 2

    while d * d <= n:
        while n % d == 0:
            fatores[d] = fatores.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2  # 2, depois só ímpares

    if n > 1:
        fatores[n] = fatores.get(n, 0) + 1

    return fatores


def gerador_fatores_comuns(a, b):
    fa = fatorar(a)
    fb = fatorar(b)

    for p in sorted(set(fa) & set(fb)):
        vezes = min(fa[p], fb[p])
        for _ in range(vezes):
            yield p


# Exemplo
a, b = 40, 60
lista = list(gerador_fatores_comuns(a, b))

print(f"40 = {fatorar(40)}")
print(f"60 = {fatorar(60)}")
print(f"Fatores comuns = {lista}")
print(f"MDC = {40} e {60} -> {__import__('math').prod([p for p in lista])}")