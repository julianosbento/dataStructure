import unittest

''' O(1) para memória pois só possui uma lista
    O(n²) pois foi implementado um for aninhado a outro para fazer a iteração
    Não encontrei maneira de melhorar o algoritmo
    O melhor caso seria se a lista estivesse ordenada, pois só percorreria uma vez'''

def bubble_sort(seq):
    n = (len (seq) - 1)
    for i in range (n):
        for i_corrente in range(n):
            if seq[i_corrente] > seq[(i_corrente+1)]:
                seq[i_corrente],seq[i_corrente + 1] = seq[i_corrente + 1], seq[i_corrente]
    return seq

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], bubble_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], bubble_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], bubble_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
