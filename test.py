delta = 0
delta_small = 0
gamma = 0

x_n = 200
x = [0, 15, 20, 40, 55, 60, 80, 100]

deltas = []
deltas_small = []
gammas = []

for n in x:
    # delta = (gamma * x_n) / 100
    if n != 0:
        delta_small = (2.0 + 0.5 * ((200 / n) - 1))
    else:
        delta_small = 'infinity'
    if isinstance(delta_small, int):
        delta = (delta_small * n) / 100
        gamma = (delta / x_n) * 100
    else:
        delta = 'infinity'
        gamma = 'infinity'

    deltas.append(delta)
    deltas_small.append(delta_small)
    gammas.append(gamma)

print('\t'.join(map(str, x)))
print('\t'.join(map(str, deltas)))
print('\t'.join(map(str, deltas_small)))
print('\t'.join(map(str, gammas)))
