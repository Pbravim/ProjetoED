from listaen import ListaEncadeada
from pilhaen import PilhaEncadeada
from filaen import FilaEncadeada
from conta import Conta

class Banco:
    def __init__(self, nome):
        self._nome = str(nome)
        self._contasL = ListaEncadeada()
        self._contasP = PilhaEncadeada()
        self._contasF = FilaEncadeada()

#Property e Setter
    @property  
    def nome (self):
        return self._nome
    @nome.setter
    def nome (self, novo):
        self._nome = novo

    @property
    def contasL (self):
        return self._contasL
    @contasL.setter
    def contasL (self, novo):
        self._contasL = novo

    @property
    def contasP (self):
        return self._contasP
    @contasP.setter
    def contasP (self, novo):
        self._contasP = novo

    @property
    def contasF (self):
        return self._contasF
    @contasF.setter
    def contasF (self, novo):
        self._contasF = novo

#Métodos Total Valor, Creditar e Debitar
    def total_valor_contas(self):
        soma = 0
        for i in range(1,self.contasL.tamanhoL()+1):
            soma+= self.contasL.mostrarL(i).saldo
        return soma

    def adiciona_valor_conta(self, valor, id):
        self.contasL.buscar(id).creditar(valor)

    def debita_valor_conta(self, valor, id):
        self.contasL.buscar(id).debitar(valor)

#Métodos Adicionar Conta
    def adiciona_conta_P(self, nova_conta):
        self.contasP.addP(nova_conta.id,nova_conta.cpf,nova_conta.saldo)

    def adiciona_conta_L(self, nova_conta, pos):
        if pos == 1:
            self.contasL.addLS(nova_conta.id,nova_conta.cpf,nova_conta.saldo)
        elif pos >= self._contasL.tamanhoL():
            self.contasL.addLE(nova_conta.id,nova_conta.cpf,nova_conta.saldo)    
        else:
            self.contasL.addLM(nova_conta.id,nova_conta.cpf,nova_conta.saldo,pos)
    
    def adiciona_conta_F(self, nova_conta):
        
        self.contasF.addF(nova_conta.id,nova_conta.cpf,nova_conta.saldo)
        
#Métodos Remover Conta
    def remove_conta_P(self):
        self.contasP.removeP()

    def remove_conta_L(self,pos):
        if pos == 1:
            self.contasL.removeLS()
        elif pos >= self._contasL.tamanhoL():
            self.contasL.removeLE()
        else:
            self.contasL.removeLM(pos)

    def remove_conta_F(self):
        self.contasF.removeF()

#Métodos Busca Contas, Ordena Contas e Imprime Contas 
    def busca_conta (self, id):
        return self._contasL.buscar(id)
    
    def ordenar (self):
        self.contasL.ordenarL()       
    
    def imprimirL(self):
        return self.contasL.imprimirL()

#Métodos Tamanho Contas
    def tamanho_conta_L(self):
        return self.contasL.tamanhoL()

    def tamanho_conta_F(self):
        return self.contasF.tamanhoF()
    
    def tamanho_conta_P(self):
        return self.contasP.tamanhoP()

#Str
    def __str__(self):
        return f'----------{self.nome}----------\nContas {self._contasP}\nContas {self._contasF}\nContas {self._contasL}'

