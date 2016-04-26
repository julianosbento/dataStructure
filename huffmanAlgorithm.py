def calcular_frequencias(s):
    letters = {}
    for letter in s:
        if (letter in letters.keys()):
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def gerar_arvore_de_huffman(s):
    letters = calcular_frequencias(s)
    for i, k in letters.items():
        char = i
        small = k
        break
    for i, k in letters.items():
        if k <= small:
            small = k
            char = i
    letters.__delitem__(char)
    tree = Arvore(char,small)
    while len(letters.keys()) > 0:
        for i, k in letters.items():
            char = i
            small = k
            break
        for i, k in letters.items():
            if k <= small:
                char = i
                small = k
        tree = tree.fundir(Arvore(char, small))
        letters.__delitem__(char)
    return tree

def codificar(cod_dict, s):
    full = ''
    for k in s:
        full = full + cod_dict.get(k)
    return full

class Noh:
    def __hash__(self):
        return hash(self.peso)

    def __eq__(self, other):
        if other is None or not isinstance(other, Noh):
            return False
        return self.peso == other.peso and self.esquerdo == other.esquerdo and self.direito == other.direito

    def __init__(self,peso):
        self.peso = peso
        self.caminho = None
        self.esquerdo = None
        self.direito = None

    def I (self):
        return "noh"

class Folha():
    def __hash__(self):
        return hash(self.__dict__)

    def __eq__(self, other):
        if other is None or not isinstance(other, Folha):
            return False
        return self.__dict__ == other.__dict__

    def __init__(self, char, peso):
        self.peso = peso
        self.char = char

    def I(self):
        return "folha"

class Arvore(object):
    def __hash__(self):
        return hash(self.raiz)

    def __eq__(self, other):
        if other is None:
            return False
        return self.raiz == other.raiz

    def __init__(self, char = None, peso = None):
        self.letters = {}
        if char == None:
            self.raiz = None
        else:
            self.raiz = Folha(char, peso)

    def decodificar(self, s):
        self.cod_dict()
        full = ''
        time = ''
        for k in s:
            time += k
            for i, k in self.letters.items():
                if k == time:
                    full = full + i
                    time = ''
        return full

    def fundir(self,arvore):
        newTree = Arvore()
        newTree.raiz = Noh(self.raiz.peso + arvore.raiz.peso)
        if self.raiz.peso > arvore.raiz.peso:
            newTree.raiz.esquerdo = self.raiz
            newTree.raiz.direito = arvore.raiz
        else:
            newTree.raiz.direito = self.raiz
            newTree.raiz.esquerdo = arvore.raiz
        return newTree

    def cod_dict(self):
        way = ''

        cod_dict_rec('', self.letters, self.raiz)

        return self.letters

def cod_dict_rec(way, letters, time):

    if time.I() == "folha":
        letters[time.char] = way
    else:
        cod_dict_rec(way + '1', letters, time.direito)
        cod_dict_rec(way + '0', letters, time.esquerdo)

from unittest import TestCase


class CalcularFrequenciaCarecteresTestes(TestCase):
    def teste_string_vazia(self):
        self.assertDictEqual({}, calcular_frequencias(''))

    def teste_string_nao_vazia(self):
        self.assertDictEqual({'a': 3, 'b': 2, 'c': 1}, calcular_frequencias('aaabbc'))


class NohTestes(TestCase):
    def teste_folha_init(self):
        folha = Folha('a', 3)
        self.assertEqual('a', folha.char)
        self.assertEqual(3, folha.peso)

    def teste_folha_eq(self):
        self.assertEqual(Folha('a', 3), Folha('a', 3))
        self.assertNotEqual(Folha('a', 3), Folha('b', 3))
        self.assertNotEqual(Folha('a', 3), Folha('a', 2))
        self.assertNotEqual(Folha('a', 3), Folha('b', 2))

    def testes_eq_sem_filhos(self):
        self.assertEqual(Noh(2), Noh(2))
        self.assertNotEqual(Noh(2), Noh(3))

    def testes_eq_com_filhos(self):
        noh_com_filho = Noh(2)
        noh_com_filho.esquerdo = Noh(3)
        self.assertNotEqual(Noh(2), noh_com_filho)

    def teste_noh_init(self):
        noh = Noh(3)
        self.assertEqual(3, noh.peso)
        self.assertIsNone(noh.esquerdo)
        self.assertIsNone(noh.direito)


def _gerar_arvore_aaaa_bb_c():
    raiz = Noh(7)
    raiz.esquerdo = Folha('a', 4)
    noh = Noh(3)
    raiz.direito = noh
    noh.esquerdo = Folha('b', 2)
    noh.direito = Folha('c', 1)
    arvore_esperada = Arvore()
    arvore_esperada.raiz = raiz
    return arvore_esperada


class ArvoreTestes(TestCase):
    def teste_init_com_defaults(self):
        arvore = Arvore()
        self.assertIsNone(arvore.raiz)

    def teste_init_sem_defaults(self):
        arvore = Arvore('a', 3)
        self.assertEqual(Folha('a', 3), arvore.raiz)

    def teste_fundir_arvores_iniciais(self):
        raiz = Noh(3)
        raiz.esquerdo = Folha('b', 2)
        raiz.direito = Folha('c', 1)
        arvore_esperada = Arvore()
        arvore_esperada.raiz = raiz

        arvore = Arvore('b', 2)
        arvore2 = Arvore('c', 1)
        arvore_fundida = arvore.fundir(arvore2)
        self.assertEqual(arvore_esperada, arvore_fundida)

    def teste_fundir_arvores_nao_iniciais(self):
        arvore_esperada = _gerar_arvore_aaaa_bb_c()

        arvore = Arvore('b', 2)
        arvore2 = Arvore('c', 1)
        arvore3 = Arvore('a', 4)
        arvore_fundida = arvore.fundir(arvore2)
        arvore_fundida = arvore3.fundir(arvore_fundida)

        self.assertEqual(arvore_esperada, arvore_fundida)

    def teste_gerar_dicionario_de_codificacao(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertDictEqual({'a': '0', 'b': '10', 'c': '11'}, arvore.cod_dict())

    def teste_decodificar(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertEqual('aaaabbc', arvore.decodificar('0000101011'))


class TestesDeIntegracao(TestCase):
    def teste_gerar_arvore_de_huffman(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertEqual(arvore, gerar_arvore_de_huffman('aaaabbc'))

    def teste_codificar(self):
        arvore = gerar_arvore_de_huffman('aaaabbc')
        self.assertEqual('0000101011', codificar(arvore.cod_dict(), 'aaaabbc'))
        self.assertEqual('aaaabbc', arvore.decodificar('0000101011'))
