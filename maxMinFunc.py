def maxMin (elements, x, maximum, minimum):
    maxi = maximum; mini = minimum 
    if x == len (elements):
        return mini, maxi
    if (maxi < elements [x]):
        maxi = elements [x]
    if (mini > elements [x]):
        mini = elements [x]
    return maxMin (elements, x + 1, maxi, mini)

def readList (elements):
    if len (elements) == 1:
        return elements [0], elements[0]
    else:
        return maxMin (elements, 1, elements [0], elements [0])

'''O algoritmo é O(N), pois lê todos os valores com a função readList
análisa o número de termos imputados na lista, e no retorno chama a função maxMin,
que percorre a lista sem ordená-la e retorna e o valor máximo e mínimo.'''
