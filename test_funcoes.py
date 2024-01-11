import unittest
from funcoes import *

class TesteCalculadora(unittest.TestCase):

    def test_adicao(self):
        self.assertEqual(adicao(3, 5), 8)
        self.assertEqual(adicao(-1, 1), 0)
        self.assertEqual(adicao(0, 0), 0)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)
        self.assertEqual(subtracao(-1, 1), -2)
        self.assertEqual(subtracao(0, 0), 0)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(3, 5), 15)
        self.assertEqual(multiplicacao(-1, 1), -1)
        self.assertEqual(multiplicacao(0, 5), 0)

    def test_divisao(self):
        self.assertEqual(divisao(6, 2), 3)
        self.assertEqual(divisao(5, 0), "Erro: Impossível dividir por 0!")
        self.assertEqual(divisao(0, 5), 0.0)

if __name__ == '__main__':
    unittest.main()
