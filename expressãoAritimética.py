# Exercício de avaliação de expressão aritmética.
# Só podem ser usadas as estruturas Pilha e Fila implementadas em aulas anteriores.
# Deve ter análise de tempo e espaço para função avaliação

'''Tempo O(N) pois percorre a fila para adicionar os elementos e depois para desenfilar e avaliar com pilha
Memória O(N) pois aumenta a conforme são adicionados os elementos e retirados'''

#from aula5.fila import Fila
#from aula4.pilha import Pilha

from collections import deque

class Pilha ():
    def __init__(self):
        self.lista = []

    def __len__(self):
        return len (self.lista)

    def vazia (self):
        return len(self.lista) == 0

    def topo (self):
        if self.lista:
            return self.lista [-1]
        raise IndexError

    def empilhar(self, valor):
        return self.lista.append(valor)

    def desempilhar (self):
        if len (self.lista) == 0:
            raise IndexError
        else:
            self.lista.pop()

class Fila():
    def __init__(self):
        self._deque = deque()

    def __len__(self):
        return len(self._deque)

    def __iter__(self):
        try:
            while True:
                yield self.desenfileirar()
        except FilaVaziaErro:
            pass

    def enfileirar(self, valor):
        return self._deque.append(valor)

    def vazia(self):
        return len(self) == 0

    def primeiro(self):
        try:
            return self._deque[0]
        except IndexError:
            raise FilaVaziaErro('Não é possível obter primeiro de lista vazia')

    def desenfileirar(self):
        try:
            return self._deque.popleft()
        except IndexError:
            raise FilaVaziaErro('Não é possível desenfileirar lista vazia')

class FilaVaziaErro(Exception):
    pass

class ErroLexico(Exception):
    pass

class ErroSintatico(Exception):
    pass

def analise_lexica(expressao):
    letras = 'abcdefghijklmnopqrstuvwxyz'
    operadores = '+-*/'
    fila = Fila()
    num = '0123456789'
    numVar = ''
    for letra in expressao:
        if letra == '':
            raise ErroLexico ('')
        if letra in set(letras):
            raise ErroLexico ('')
        if letra in '{[()]}+-*/.':
            if len(numVar) > 0:
                fila.enfileirar(numVar)
                numVar = ''
            fila.enfileirar(letra)
        if letra in set(num):
            numVar += letra

    if len(numVar) > 0:
        fila.enfileirar(numVar)

    return fila


def analise_sintatica(fila):

    tokens = Fila ()
    numValor = 0
    point = False
    if len(fila) > 0:
        for elemento in fila:
            if elemento in set('{[()]}+-*/'):
                if not numValor == 0:
                    tokens.enfileirar(numValor)
                numValor = 0
                tokens.enfileirar(elemento)
                point = False
            else:
                if elemento == '.':
                    point = True
                else:
                    valor = float(elemento)
                    if point:
                        numValor += (valor / 10 ** len (elemento))
                    else:
                        numValor += valor
        if not numValor == 0:
            tokens.enfileirar(numValor)
        return tokens
    else:
         raise ErroSintatico ('')

def avaliar(expressao):

    avalia = analise_sintatica(analise_lexica(expressao))
    resposta = Pilha ()
    a, b, c = None, None, None
    aux = 0
    for elemento in avalia:
        resposta.empilhar(elemento)

        if len(resposta) >= 3:
            a = resposta.desempilhar()
            b = resposta.desempilhar()
            c = resposta.desempilhar()
            if str(b) in '+-*/' and str(a) not in '{[()]}' and str(c) not in '{[()]}':
                if b == '+':
                    aux = c + a
                elif b == '-':
                    aux = c - a
                elif b == '*':
                    aux = c * a
                elif b == '/':
                    aux = c / a
                resposta.empilhar (aux)
            else:
                resposta.empilhar(c)
                resposta.empilhar(b)
                resposta.empilhar(a)
        if str (elemento) in ')]}':
            resposta.desempilhar()
            aux = resposta.desempilhar()
            resposta.desempilhar()
            resposta.empilhar(aux)
            if len(resposta) >= 3:
                a = resposta.desempilhar()
                b = resposta.desempilhar()
                c = resposta.desempilhar()
                if str(b) in '+-*/' and str(a) not in '{[()]}' and str(c) not in '{[()]}':
                    if b == '+':
                        aux = c + a
                    elif b == '-':
                        aux = c - a
                    elif b == '*':
                        aux = c * a
                    elif b == '/':
                        aux = c / a
                    resposta.empilhar (aux)
                else:
                    resposta.empilhar(c)
                    resposta.empilhar(b)
                    resposta.empilhar(a)

    return resposta.desempilhar()

import unittest


class AnaliseLexicaTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        fila = analise_lexica('')
        self.assertTrue(fila.vazia())

    def test_caracter_estranho(self):
        self.assertRaises(ErroLexico, analise_lexica, 'a')
        self.assertRaises(ErroLexico, analise_lexica, 'ab')

    def test_inteiro_com_um_algarismo(self):
        fila = analise_lexica('1')
        self.assertEqual('1', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_inteiro_com_vários_algarismos(self):
        fila = analise_lexica('1234567890')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_float(self):
        fila = analise_lexica('1234567890.34')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('34', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_parenteses(self):
        fila = analise_lexica('(1)')
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_chaves(self):
        fila = analise_lexica('{(1)}')
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_colchetes(self):
        fila = analise_lexica('[{(1.0)}]')
        self.assertEqual('[', fila.desenfileirar())
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertEqual(']', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_adicao(self):
        fila = analise_lexica('1+2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('+', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_subtracao(self):
        fila = analise_lexica('1-2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('-', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_multiplicacao(self):
        fila = analise_lexica('1*2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('*', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_divisao(self):
        fila = analise_lexica('1/2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('/', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_expresao_com_todos_simbolos(self):
        expressao = '1/{2.0+3*[7-(5-3)]}'
        fila = analise_lexica(expressao)
        self.assertListEqual(list(expressao), [e for e in fila])
        self.assertTrue(fila.vazia())


class AnaliseSintaticaTestes(unittest.TestCase):
    def test_fila_vazia(self):
        fila = Fila()
        self.assertRaises(ErroSintatico, analise_sintatica, fila)

    def test_int(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_float(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila.enfileirar('.')
        fila.enfileirar('4')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890.4, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_expressao_com_todos_elementos(self):
        fila = analise_lexica('1000/{222.125+3*[7-(5-3)]}')
        fila_sintatica = analise_sintatica(fila)
        self.assertListEqual([1000, '/', '{', 222.125, '+', 3, '*', '[', 7, '-', '(', 5, '-', 3, ')', ']', '}'],
                             [e for e in fila_sintatica])


class AvaliacaoTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertRaises(ErroSintatico, avaliar, '')

    def test_inteiro(self):
        self.assert_avaliacao('1')

    def test_float(self):
        self.assert_avaliacao('2.1')

    def test_soma(self):
        self.assert_avaliacao('2+1')

    def test_subtracao_e_parenteses(self):
        self.assert_avaliacao('(2-1)')

    def test_expressao_com_todos_elementos(self):
        self.assertEqual(1.0, avaliar('2.0/[4*3+1-{15-(1+3)}]'))

    def assert_avaliacao(self, expressao):
        self.assertEqual(eval(expressao), avaliar(expressao))


if __name__ == '__main__':
    unittest.main()
