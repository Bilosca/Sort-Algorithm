def bubbleSort(lista):
    #tamanho da lista para fazer a iteracao
    tamanhoLista = len(lista)

    #loop para repetir a funcao de acordo com o tamanho da lista passada
    for j in range(tamanhoLista -1):

        # loop para fazer a iteracao e checagem dos indices
        for i in range(tamanhoLista -1):
            if lista[i] > lista[i +1]:

                #Troca de elementos nas posicoes i e  i+1
                lista[i], lista[i + 1] = lista[i +1], lista[i]
    return lista