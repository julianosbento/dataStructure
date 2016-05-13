from collections import Counter

lru = {0:[0]}
def soma_quadrados(n):
    if n == 0:
        return [0]
    square = []
    m = 1
    while(m*m <= n):
        square.append(m*m)
        m += 1
    while len(square) > 0:
        k = n
        squareTwo = square.copy()
        i = squareTwo.pop()
        answer = []
        while(k > 0):
            if k in lru.keys() and k is not n:
                answer = answer + lru[k]
                k = 0
            else:
                if len(squareTwo) > 0:
                    if k - i < 0:
                       i = squareTwo.pop()
                    else:
                        k -= i
                        answer.append(i)
                        if(k < squareTwo[-1]):
                            i = squareTwo.pop()
                else:
                    k -= i
                    answer.append(i)
        if n not in lru.keys():
            lru[n] = answer.copy()
        elif len(answer) < len(lru[n]):
            lru[n] = answer.copy()
        square.pop()

    return lru[n]

import unittest


class SomaQuadradosPerfeitosTestes(unittest.TestCase):
    def teste_0(self):
        self.assert_possui_mesmo_elementos([0], soma_quadrados(0))

    def teste_01(self):
        self.assert_possui_mesmo_elementos([1], soma_quadrados(1))

    def teste_02(self):
        self.assert_possui_mesmo_elementos([1, 1], soma_quadrados(2))

    def teste_03(self):
        self.assert_possui_mesmo_elementos([1, 1, 1], soma_quadrados(3))

    def teste_04(self):
        self.assert_possui_mesmo_elementos([4], soma_quadrados(4))

    def teste_05(self):
        self.assert_possui_mesmo_elementos([4, 1], soma_quadrados(5))

    def teste_11(self):
        self.assert_possui_mesmo_elementos([9, 1, 1], soma_quadrados(11))

    def teste_12(self):
        self.assert_possui_mesmo_elementos([4, 4, 4], soma_quadrados(12))


    def assert_possui_mesmo_elementos(self, esperado, resultado):
        self.assertEqual(Counter(esperado), Counter(resultado))
if __name__ == '__main__':
    unittest.main()
