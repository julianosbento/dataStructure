import unittest
from itertools import product

regra = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wzyz'}


def gerar_alfa(s):

    answer = [tuple()]
    for k in s:
        position = len (answer) -1
        while (position >= 0):
            now = ans.pop(position)
            time = regra.__getitem__(k)
            for i in time:
                answer.append(now + tuple (i,))
            position -= 1

    return answer
    """
    O(n^n) para espaço porque a lista cresce conforme são analisados os caracteres em relação ao número digitado
    O(n^3) para tempo, porque é usado um for que contém um while e outro for dentro da estrutura 
    """
    pass


class Testes(unittest.TestCase):
    def testes_string_vazia(self):
        self.assertListEqual([tuple()], list(gerar_alfa('')))

    def testes_string_2(self):
        self.assertListEqual([('a',), ('b',), ('c',)], list(gerar_alfa('2')))

    def testes_string_3(self):
        self.assertListEqual([('d',), ('e',), ('f',)], list(gerar_alfa('3')))

    def testes_string_com_2_numeros(self):
        self.assertSetEqual(set((('a', 'd'), ('a', 'e'), ('a', 'f'), ('b', 'd'), ('b', 'e'), ('b', 'f'), ('c', 'd'),
                                 ('c', 'e'), ('c', 'f'))), set(gerar_alfa('23')))

    def testes_com_5_numeros(self):
        resultado = set(gerar_alfa('73696'))
        self.assertIn(tuple('renzo'), resultado)
        self.assertSetEqual(set(product('pqrs', 'def', 'mno', 'wzyz', 'mno')), resultado)
