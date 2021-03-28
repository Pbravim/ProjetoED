from conta import Conta

class FilaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)

class FilaEncadeada:
    def __init__(self):
        self._inicio = None
        self._tamanho = 0

    @property
    def inicio(self):
        if self.vaziaF():
                raise FilaException('A fila está vazia')

        return self._inicio

#Métodos Tamanho
    def tamanhoF(self):
        return self._tamanho

    def vaziaF(self):
        return self._tamanho == 0 
        
#Add e Remove
    def addF(self, id, cpf, saldo):
        no = Conta(id, cpf, saldo)
        aux = self._inicio

        if self.vaziaF() == True:
            self._inicio = no

        else:
            while aux.prox != None:
                aux = aux.prox
        
            aux.prox = no

        self._tamanho += 1 

    def removeF(self):
        if self.vaziaF():
            raise FilaException('A fila está vazia')

        self._inicio = self._inicio.prox
        self._tamanho -= 1  

#Mostrar e STR
    def mostrarF(self):
        if self.vaziaF():
            raise FilaException('A fila está vazia')

        return print(self._inicio)
    
    def __str__(self):
        saida = 'Fila:\n '
        p = self._inicio

        while p != None:
            saida += f'ID: {p.id}, CPF: {p.cpf}, Saldo Atual: R$ {p.saldo}'
            p = p.prox

            if p != None:
             saida += '\n '
        
        saida += '\n------------'
        return saida

    def imprimirF(self):
        print(self.__str__())

