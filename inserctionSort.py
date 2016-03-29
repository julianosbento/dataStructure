import unittest

''' O(1) para memória pois só utiliza variáveis
    O(N²) para tempo porque utiliza dois whiles aninhados para percorrer a lista'''

def insertion_sort(seq):

    if len(seq) <= 1:
        return seq
    else:
        i_desordenada = 1
        limite_ordenada = 0
        while i_desordenada < len(seq):
            i_ordenada = limite_ordenada
            if seq[limite_ordenada] < seq[i_desordenada]:
                limite_ordenada += 1
                i_desordenada += 1
            else:
                i_ordenada += 1
                i_desordenada += 1
                while i_ordenada > 0:
                    if seq[i_ordenada] < seq[i_ordenada - 1]:
                        seq[i_ordenada], seq[i_ordenada - 1] = seq[i_ordenada - 1], seq[i_ordenada]
                    i_ordenada -= 1
                limite_ordenada += 1
    return seq


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], insertion_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], insertion_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], insertion_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertion_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
