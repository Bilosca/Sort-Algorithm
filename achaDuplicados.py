
import random 

# Lista Random usando List Comprehension
listaRandom = [(random.randint(0, 50)) for _ in range(15)]
print(listaRandom)


# Funcao que recebe os repetidos de uma Lista e os retorna
def achaRepetidos(lista):

    jaVistos = {}
    repetidos = []

    for i in lista:

        # se  o Numero nao tiver no Dict "JaVisto"
        # ele sera adicionado com o Valor inicial 1 (qtd de vezes ja vista)
        if i not in jaVistos:
            jaVistos[i] = 1
        
        # Caso o numero ja esteja no Dict "Javisto"
        else:

            # Se o o Valor for igual a 1 (qtd de vezes ja vista)
            # Ele sera adicionado na lista Repetidos e entao somado mais 1
            if jaVistos[i] == 1:
                repetidos.append(i)
            jaVistos[i] += 1
        
    return repetidos

listaAtualizada = achaRepetidos(listaRandom)

print(f"Repetidos: {listaAtualizada}")

tamanhoLista = len(listaAtualizada)

# Ordena a Lista
for j in range(tamanhoLista -1):
    for i in range(tamanhoLista -1):

        if listaAtualizada[i] > listaAtualizada[i + 1]:
            listaAtualizada[i], listaAtualizada[i + 1] = listaAtualizada[i+1], listaAtualizada[i]

print(f"Ordenados: {listaAtualizada}")

    


