import unittest

class Pilha ():
    def __init__(self):
        self.lista = []

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

def esta_balanceada (word):

    parentese = Pilha ()
    colchete = Pilha ()
    key = Pilha ()

    for letters in word:
        if letters == '(':
            parentese.empilhar(0)
        if letters == '[':
            colchete.empilhar(0)
        if letters == '{':
            key.empilhar(0)
        if letters == ')':
            try:
                parentese.desempilhar()
            except IndexError:
                return False
        if letters == ']':
            try:
                colchete.desempilhar()
            except IndexError:
                return False
        if letters == '}':
            try:
                key.desempilhar()
            except IndexError:
                return False
    if parentese.vazia() and colchete.vazia() and key.vazia():
        return True
    else:
        return False
    """
    Tempo de execução O(N) porque vai percorrer uma lista com o for.
    O(N) para memória porque as pilhas crescem conforme são inputados elementos na lista
    """

class BalancearTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertTrue(esta_balanceada(''))

    def test_parenteses(self):
        self.assertTrue(esta_balanceada('()'))

    def test_chaves(self):
        self.assertTrue(esta_balanceada('{}'))

    def test_colchetes(self):
        self.assertTrue(esta_balanceada('[]'))

    def test_todos_caracteres(self):
        self.assertTrue(esta_balanceada('({[]})'))
        self.assertTrue(esta_balanceada('[({})]'))
        self.assertTrue(esta_balanceada('{[()]}'))

    def test_chave_nao_fechada(self):
        self.assertFalse(esta_balanceada('{'))

    def test_colchete_nao_fechado(self):
        self.assertFalse(esta_balanceada('['))

    def test_parentese_nao_fechado(self):
        self.assertFalse(esta_balanceada('('))

    def test_chave_nao_aberta(self):
        self.assertFalse(esta_balanceada('}{'))

    def test_colchete_nao_aberto(self):
        self.assertFalse(esta_balanceada(']['))

    def test_parentese_nao_aberto(self):
        self.assertFalse(esta_balanceada(')('))

    def test_falta_de_caracter_de_fechamento(self):
        self.assertFalse(esta_balanceada('({[]}'))

    def test_falta_de_caracter_de_abertura(self):
        self.assertFalse(esta_balanceada('({]})'))

    def test_expressao_matematica_valida(self):
        self.assertTrue(esta_balanceada('({[1+3]*5}/7)+9'))

    def test_char_errado_fechando(self):
        self.assertFalse(esta_balanceada('[)'))
