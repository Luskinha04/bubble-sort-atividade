from bubblesort import bubble_sort, bubble_sort_otimizado

# Lista simples para testar
lista = [0, 1, 2, 3, 4, 5]

print("====== Versão Normal ======")
lista_normal = lista.copy()
print("Lista original:", lista_normal)
bubble_sort(lista_normal)
print("Lista ordenada (normal):", lista_normal)

print("\n====== Versão Otimizada ======")
lista_otimizada = lista.copy()
print("Lista original:", lista_otimizada)
bubble_sort_otimizado(lista_otimizada)
print("Lista ordenada (otimizada):", lista_otimizada)
