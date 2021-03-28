class ContaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)

class Conta:
    def __init__(self, id, cpf, saldo):
        self._id = int(id)
        self._cpf = str(cpf)
        self._saldo = float(saldo)
        self._prox = None

#Property
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, novo):
        self._id = novo
      
    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, novo):
        self._cpf = novo

    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, novo):
        self._saldo = novo
        
    @property
    def prox (self):
        return self._prox
    @prox.setter
    def prox(self, novo):
        self._prox = novo
    
#Métodos Creditar e Debitar
    def creditar(self, valor):
      if valor <=0:
        raise ContaException('O valor é inválido')
        
      self._saldo += valor
      return True
    
    def debitar(self, valor):
      if valor <=0:
        raise ContaException('O valor é inválido')
        
      if valor > self._saldo:
        return False
      else:
        self._saldo-= valor
        return True
      
#STR
    def __str__(self):
       return f'------------\nID da conta: {self._id}\nCPF:{self._cpf}\nSaldo Atual:{self._saldo}\n------------'


       