import unittest
from EmprestimoDeBike import Loja, Cliente

class Testes(unittest.TestCase):
    def setUp(self):
        self.bike = Loja(50, 150)
        self.cliente = Cliente("Pedro", 500)
    
    def testeReceberPedido1(self):
        print('\nTeste Loja recebe pedido de quantidade negativa')
        self.assertEqual(self.bike.receber_pedidos(-10, 'horas', 2), 0)
    
    def testeReceberPedido2(self):
        print('\nTeste Loja recebe pedido maior que o estoque')
        self.assertEqual(self.bike.receber_pedidos(70, 'horas', 2), 0)

    def testeReceberPedido3(self):
        print('\nTeste Loja receber pedido Família em horas')
        self.assertEqual(self.bike.receber_pedidos(3, 'horas', 2), 21)

    def testeReceberPedido4(self):
        print('\nTeste Loja receber pedido Família em dias')
        self.assertEqual(self.bike.receber_pedidos(3, 'dias', 2), 105)
    
    def testeReceberPedido5(self):
        print('\nTeste Loja receber pedido Família em semanas')
        self.assertEqual(self.bike.receber_pedidos(3, 'semanas', 2), 420)
    
    def testeReceberPedido6(self):
        print('\nTeste Loja receber pedidos em horas')
        self.assertEqual(self.bike.receber_pedidos(2, 'horas', 2), 20)

    def testeReceberPedido7(self):
        print('\nTeste Loja receber pedidos em dias')
        self.assertEqual(self.bike.receber_pedidos(2, 'dias', 2), 100)

    def testeReceberPedido8(self):
        print('\nTeste Loja receber pedidos em semanas')
        self.assertEqual(self.bike.receber_pedidos(2, 'semanas', 2), 400)

    def testeReceberPagamento1(self):
        print('\nTeste Valor pagamento negativo')
        self.assertEqual(self.bike.receber_pagamento(20, -10), 20)
    
    def testeReceberPagamento2(self):
        print('\nTeste Valor pagamento correto')
        self.assertEqual(self.bike.receber_pagamento(20, 20), 0)
    
    def testeReceberPagamento3(self):
        print('\nTeste Valor pagamento com troco')
        self.assertEqual(self.bike.receber_pagamento(20, 30), -10)

if __name__ == "__main__":
    unittest.main()