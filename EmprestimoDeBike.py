class Loja():
    
    def __init__(self, estoque, caixa):
        self.estoque = estoque
        self.caixa = caixa
        
        
    def mostrar_estoque(self):
        return f'Loja - Temos um total de {self.estoque} bicicletas disponiveis'

    def receber_pedidos(self, quantidade, tipo, tempo):

        '''
        Parametros: 
        - Quantidade = numero de bicicletas alugadas.
        - Tipo = hora / dia / semana. (String)
        - Tempo = quanto tempo ficará com a bicicleta.
        '''

        try:
            if quantidade <= 0:
                raise ValueError('Quantidade invalida')
            if quantidade > self.estoque:
                raise SystemError('Estoque indisponivel')

            print(f'Loja - Estoque disponivel: {self.estoque}.')
            self.estoque -= quantidade
            

            if 3 <= quantidade <= 5:
                if tipo == 'horas':
                    print(f'Loja - Pedido de {quantidade} bicicletas efetuados. Valor do Pedido: R${quantidade * 5 * tempo * 0.7}. * Alugado por hora e com desconto de familia de 30%. *')
                    return quantidade * 5 * tempo * 0.7
                elif tipo == 'dias':
                    print(f'Loja - Pedido de {quantidade} bicicletas efetuados. Valor do Pedido: R${quantidade * 25 * tempo * 0.7}. * Alugado por dia e com desconto de familia de 30%. *')
                    return quantidade * 25 * tempo * 0.7
                else:
                    print(f'Loja - Pedido de {quantidade} bicicletas efetuados. Valor do Pedido: R${quantidade * 100 * tempo * 0.7}. * Alugado por semana e com desconto de familia de 30%. *')
                    return quantidade * 100 * tempo * 0.7

            elif tipo == 'horas':
                print(f'Loja - Pedido de {quantidade} bicicleta(s) efetuados. Valor do Pedido: R${quantidade * 5 * tempo}. * Alugado por hora *.')
                return quantidade * 5 * tempo

            elif tipo == 'dias':
                print(f'Loja - Pedido de {quantidade} bicicleta(s) efetuados. Valor do Pedido: R${quantidade * 25 * tempo}. * Alugado por dia *.')
                return quantidade * 25 * tempo

            else:
                print(f'Loja - Pedido de {quantidade} bicicleta(s) efetuados. Valor do Pedido: R${quantidade * 100 * tempo}. * Alugado por semana *.')
                return quantidade * 100 * tempo
            
        except ValueError:
            print(f'Loja - Pedido de {quantidade} bicicleta(s) não efetuado, quantidade invalida. Estoque: {self.estoque}')
            return 0
        except SystemError:
            print(f'Loja - Pedido de {quantidade} bicicleta(s) não efetuado por falta de estoque. Estoque: {self.estoque}')
            return 0
        except:
            print(f'Loja - Pedido de {quantidade} bicicleta(s) não efetudo. Estoque: {self.estoque}')
            return 0

    def finalizar_pedido(self, quantidade):
        self.estoque += quantidade

    def receber_pagamento(self, valor_conta, valor_pgmto):
        try:
            if valor_conta < 0 or valor_pgmto <= 0:
                raise ValueError('Valor(es) invalidos(s)')

            if valor_conta == valor_pgmto:
                self.caixa += valor_pgmto
                print(f'Loja - Conta paga totalmente. Recebido: R${valor_pgmto}. Conta: R${valor_conta}. Caixa: R${self.caixa}')
                return 0

            elif valor_conta <  valor_pgmto:
                self.caixa += valor_conta
                print(f'Loja - Conta paga com troco de R${valor_pgmto - valor_conta}. Recebido: R${valor_pgmto}. Conta: R${valor_conta}. Caixa: R${self.caixa}')
                return -(valor_pgmto - valor_conta)

            else:
                self.caixa += valor_pgmto
                print(f'Loja - Conta paga parcialmente, restam R${valor_conta - valor_pgmto}. Recebido: R${valor_pgmto}. Conta: R${valor_conta}. Caixa: R${self.caixa}')

        except ValueError:
            print(f'Loja - Erro ao pagar conta, valor invalido. Recebido: R${valor_pgmto}. Caixa: R${self.caixa}')
            return valor_conta

        except:
            print(f'Loja - Erro ao pagar conta. Recebido: R${valor_pgmto}. Caixa: R${self.caixa}')
            return valor_conta
    
    
class Cliente():
    def __init__(self, nome, carteira):
        self.nome = nome
        self.carteira = carteira
        self.conta = 0.0

    def mostrar_bike(self, obj_loja):
        print(obj_loja.mostrar_estoque())

    def fazer_pedido(self, obj_loja, quantidade, tipo, tempo):
        '''
        Paramentros: 
        - obj_loja = instancia criada a partir da Classe loja.
        - Quantidade = numero de bicicletas alugadas.
        - Tipo = hora / dia / semana. (String)
        - Tempo = quanto tempo ficará com a biciclieta.

        '''

        try:
            if quantidade <= 0:
                raise ValueError('Quantidade invalida.')

            if not isinstance(obj_loja, Loja):
                raise SystemError('Não recebeu uma Loja de bicicletas')
        
            self.conta += obj_loja.receber_pedidos(quantidade, tipo, tempo)
            print(f'Cliente {self.nome} - Pedido de {quantidade} bicicleta(s). Tipo de alguel por: {tipo}. Tempo Creditado: {tempo}')
            return self.conta

        except ValueError:
            print(f'Cliente {self.nome} - Pedido de {quantidade} bicicleta(s) não efetuado, quantidade invalida. Conta: {self.conta}')
            return 0
        except SystemError:
            print(f'Cliente {self.nome} - Pedido de {quantidade} bicicleta(s) não efetuado, tipo de loja invalida. Conta: {self.conta}')
            return 0
        except:
            print(f'Cliente {self.nome} - Pedido de {quantidade} bicicleta(s) não efetuado. Conta: {self.conta}')
            return 0

    def pagar_conta(self, valor_pgmto, obj_loja):
        try:
            if valor_pgmto <= 0:
                raise ValueError('Valor invalido')
            if valor_pgmto > self.carteira:
                raise ArithmeticError('Conta maior que dinheiro disponivel')
            if not isinstance(obj_loja, Loja):
                raise SystemError('Não recebeu uma Loja de bicicletas')

            self.carteira -= valor_pgmto
            
            divida = obj_loja.receber_pagamento(self.conta, valor_pgmto)
            print(f'Cliente {self.nome} - Pagamento de R${valor_pgmto} da conta de R${self.conta} realizado. Conta: R${self.conta}. Carteira: R${self.carteira}')
            
            if divida == 0: #Pagamento total
                self.conta = 0
            elif divida > 0: #Pagamento parcial
                self.conta = divida
            else: #Pagamento com troco
                self.carteira -= divida
                self.conta = 0
            return self.carteira


        except ValueError:
            print(f'Cliente {self.nome} - Pagamento de R${valor_pgmto} da conta de R${self.conta} não foi efetuado, pois o valor de pagamento é invalido. Conta: R${self.conta}. Carteira: R${self.carteira}')
            return 0
        except ArithmeticError:
            print(f'Cliente {self.nome} - Pagamento de R${valor_pgmto} da conta de R${self.conta} não foi efetuado, pois o valor da conta é superior ao disponivel na carteira. Conta: R${self.conta}. Carteira: R${self.carteira}')
            return 0
        except SystemError:
            print(f'Cliente {self.nome} - Pagamento de R${valor_pgmto} da conta de R${self.conta} não foi efetuado, pois a loja não é uma bicicletaria. Conta: R${self.conta}. Carteira: R${self.carteira}')
            return 0
        except:
            print(f'Cliente {self.nome} - Pagamento de R${valor_pgmto} da conta de R${self.conta} não foi efetuado. Conta: R${self.conta}. Carteira: R${self.carteira}')
            return 0

    def devolver_bike(self, quantidade, obj_loja):
        devolucao = obj_loja.finalizarPedido(quantidade)