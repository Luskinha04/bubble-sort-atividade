def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        print("Iteração normal:", i, lista)
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def bubble_sort_otimizado(lista):
    n = len(lista)
    for i in range(n - 1):
        trocou = False
        print("Iteração otimizada:", i, lista)
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            print("Lista já estava ordenada! Parando na iteração:", i)
            break
