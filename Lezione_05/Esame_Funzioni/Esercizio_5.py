def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    return [x[i] + y[i] for i in range(len(x))]


print(somma_elementi([1, 2, 3], [4, 5, 6]))

