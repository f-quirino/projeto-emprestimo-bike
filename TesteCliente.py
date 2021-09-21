import unittest
from EmprestimoDeBike import Loja, Cliente

class Testes(unittest.TestCase):
    def setUp(self):
        self.bike = Loja(50, 150)
        self.cliente = Cliente("Pedro", 500)

    def testeFazerPedido1(self):
        print('\nTeste Cliente fazer pedido de números de bike negativo')
        self.assertEqual(self.cliente.fazer_pedido(self.bike, -10, 'horas', 2), 0)

    def testeFazerPedido2(self):
        print('\nTeste Cliente fazer pedido em loja diferente da loja de bicicleta')
        self.assertEqual(self.cliente.fazer_pedido(self.cliente, 10, 'horas', 2), 0)
    
    def testeFazerPedido3(self):
        print('\nTeste Cliente fazer pedido caso ideal')
        self.assertEqual(self.cliente.fazer_pedido(self.bike, 10, 'horas', 2), 100)
    
    def testePagarConta1(self):
        print('\nTeste Cliente pagar com valor de pagamento negativo')
        self.assertEqual(self.cliente.pagar_conta(-10, self.bike), 0)
    
    def testePagarConta2(self):
        print('\nTeste Cliente valor da conta maior que valor da carteira')
        self.assertEqual(self.cliente.pagar_conta(550, self.bike), 0)
    
    def testePagarConta3(self):
        print('\nTeste Cliente pagamento de conta ideal')
        self.cliente.fazer_pedido(self.bike, 2, 'horas', 2)
        self.assertEqual(self.cliente.pagar_conta(20, self.bike), 480)
    
    def testePagarConta4(self):
        print('\nTeste Cliente pagamento de conta com troco')
        self.cliente.fazer_pedido(self.bike, 2, 'horas', 2)
        self.assertEqual(self.cliente.pagar_conta(30, self.bike), 480)


    


if __name__ == "__main__":
    unittest.main()