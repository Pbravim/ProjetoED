from conta import Conta

class PilhaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)

class PilhaEncadeada:
    def __init__ (self):
        self._topo = None
        self._tamanho = 0
    
    @property
    def inicio(self):
        if self.vaziaP():
                raise PilhaException('A fila está vazia')

        return self._topo
        
#Métodos Tamanho
    def tamanhoP(self):
        return self._tamanho

    def vaziaP(self):
        return self._tamanho == 0

#ADD e Remove   
    def addP (self, id, cpf, saldo):
        no = Conta (id, cpf, saldo)
        no.prox = self._topo
        self._topo = no

        self._tamanho += 1

    def removeP (self):
        if self.vaziaP():
            raise PilhaException('A pilha está vazia')
       
        self._topo = self._topo.prox
        self._tamanho -= 1

#Mostrar e STR    
    def mostrarP(self):
        if self.vaziaP():
            raise PilhaException('A lista está vazia')
        
        return print(self._topo)

    def __str__(self):
        saida = 'Pilha:\n '
        p = self._topo

        while p != None:
            saida += f'ID: {p.id}, CPF: {p.cpf}, Saldo Atual: R$ {p.saldo}'
            p = p.prox

            if p != None:
                saida +='\n '
        
        saida += '\n------------'
        return saida

    def imprimirP(self):
        print(self.__str__())


