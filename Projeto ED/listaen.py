from conta import Conta

class ListaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)

class ListaEncadeada:
    def __init__(self):
        self._inicio = None
        self._tamanho = 0

    @property
    def inicio (self):
        if self.vaziaL():
            raise ListaException('A lista está vazia')
        
        return self._inicio 

#Tamanho
    def tamanhoL (self):
        return self._tamanho

    def vaziaL (self):
        return self._tamanho == 0

#ADD
    def addLS (self, id, cpf, saldo):   
        no = Conta(id, cpf, saldo)
        no.prox= self._inicio
        self._inicio = no
        self._tamanho+= 1
    
    def addLM (self, id, cpf, saldo, pos): 
        p = self._inicio
        q = None
        cont = 1
        while cont < pos and p != None:
            q = p
            p = p.prox
            cont +=1
        no = Conta(id, cpf, saldo)
        no.prox = p
        q.prox = no
        self._tamanho+=1
    
    def addLE (self, id, cpf, saldo): 
        p = self._inicio
        if self.vaziaL():
            return self.addLS(id,cpf,saldo)
        else:
            while p.prox != None:
                p= p.prox    
            
            no = Conta(id, cpf, saldo)
            p.prox = no
        self._tamanho+=1

#REMOVE    
    def removeLS (self):
        self._inicio = self._inicio.prox
    
    def removeLM(self, pos):
        p = self._inicio
        q = None
        cont = 1
        while cont < pos and p != None:
            q = p
            p = p.prox
            cont +=1
        q.prox = p.prox

    def removeLE (self):        
        p = self._inicio
        if self._tamanho == 1:
            self.removeLS()

        else:
            while p.prox.prox != None:
                p = p.prox 
            p.prox = None

#Mostrar , Ordenar e Buscar
    def mostrarL(self, pos):
        p = self._inicio
        q = None
        cont = 1

        if pos == 1:
            return self._inicio

        elif pos == self._tamanho:
            while p.prox != None:
                p= p.prox
            return p

        else:
            p2 = self._inicio.prox
            while cont < pos and p.prox != None:
                if pos > self._tamanho:
                    raise ListaException('Selecione uma posição dentro da lista')
                q = p2
                p2 = p2.prox
                cont +=1
            return q

    def ordenarL(self):
        ordenado = False

        while ordenado == False:
            ordenado = True
            p = self._inicio
            p2 = self._inicio.prox
            
            while p2 != None:
                if p.id > p2.id:
                    ordenado = False
                    p.id, p2.id = p2.id, p.id
                    p.cpf, p2.cpf = p2.cpf, p.cpf
                    p.saldo, p2.saldo = p2.saldo, p.saldo
                p = p2
                p2 = p2.prox
    
    def buscar(self, id):
        if self.vaziaL():
            raise ListaException('A lista está vazia.')
        p = self._inicio
        p2 = self._inicio.prox
        cont = 1
        while p != None:
            if p.id == id:
                return p
            cont+= 1
            if cont > self.tamanhoL():
                raise ListaException('O ID não foi encontrado.')        
            p = p2
            p2 = p2.prox
            
#STR
    def __str__(self):
            saida = 'Lista:\n '
            p = self._inicio

            while p != None:
                saida += f'ID: {p.id}, CPF: {p.cpf}, Saldo Atual: R$ {p.saldo}'
                p = p.prox

                if p != None:
                    saida +='\n '
            
            saida += '\n------------'
            return saida

    def imprimirL(self):
        print(self.__str__())

