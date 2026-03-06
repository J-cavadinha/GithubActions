import unittest

# A sua função de teste 
def sum2(a, b):
    return a - b

# Classe de testes estruturada para o unittest
class TestSoma(unittest.TestCase):
    
    def test_soma_numeros_positivos(self):
        # Verifica se 2 + 3 é exatamente igual a 5
        self.assertEqual(sum2(2, 3), 5)
        
    def test_soma_numeros_negativos(self):
        # Verifica se -1 + (-2) é exatamente igual a -3.
        self.assertEqual(sum2(-1, -2), -3)

if __name__ == '__main__':
    unittest.main()