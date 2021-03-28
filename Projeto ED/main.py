from banco import Banco
from listaen import ListaEncadeada
from pilhaen import PilhaEncadeada
from filaen import FilaEncadeada
from conta import Conta

b = Banco("Santander")

print(b)


resposta =int(0)
lista_resposta = [1,2,3,4]

while (resposta != 4):
    resposta = int(input("\nPara acessar as contas de PILHA digite 1\nPara acessar as contas de FILA digite 2\nPara acessar as contas de LISTA digite 3\nPara SAIR digite 4 "))
#CONTAS PILHA

    if(resposta == 1):
        print(b.contasP)
        
        resposta2 =int(0)
        lista_resposta2 = [1,2,3,4,5,6]
        while resposta2 != 6:
            resposta2 = int(input("1 - Creditar\n2 - Debitar\n3 - Adicionar Conta\n4 - Remover Conta\n5 - Tamanho Lista\n6 - Voltar\n"))
            
            if resposta2 == 1:
                valor = float(input("Digite o valor a ser creditado."))
                b.contasP.inicio.creditar(valor)
                print(f"Foi creditado R$ {valor} na sua conta, seu saldo atual é de R$ {b.contasP.inicio.saldo}.")

            elif resposta2 == 2:
                valor = float(input("Digite o valor a ser debitado."))
                if b.contasP.inicio.debitar(valor):
                    print(f"Foi debitado R$ {valor} da sua conta, seu saldo atual é de R$ {b.contasP.inicio.saldo}.")
                else:
                    print("Saldo Insuficiente.")
            
            elif resposta2 == 3:
                id=int(input("Digite o ID da nova conta."))
                cpf=str(input("Digite o CPF da conta."))
                saldo=float(input("Digite o saldo da conta."))
                no_conta = Conta(id,cpf,saldo)
                b.adiciona_conta_P(no_conta)
                print(f"A conta {b.contasP.inicio} foi adicionada.")

            elif resposta2 == 4:
                print(f"A conta {b.contasP.inicio} foi removida.")
                b.remove_conta_P()

            elif resposta2 == 5:
                print(f"A pilha tem {b.tamanho_conta_P()} conta(s).")
            else:
                print("Resposta Inválida.")

#CONTAS FILA    
    elif(resposta == 2):
        print(b.contasF)
        
        resposta2 =int(0)
        lista_resposta2 = [1,2,3,4,5,6]
        while resposta2 != 6:
            resposta2 = int(input("1 - Creditar\n2 - Debitar\n3 - Adicionar Conta\n4 - Remover Conta\n5 - Tamanho Lista\n6 - Voltar\n"))
            
            if resposta2 == 1:
                valor = float(input("Digite o valor a ser creditado."))
                b.contasF.inicio.creditar(valor)
                print(f"Foi creditado R$ {valor} na sua conta, seu saldo atual é de R$ {b.contasF.inicio.saldo}.")

            elif resposta2 == 2:
                valor = float(input("Digite o valor a ser debitado."))
                if b.contasF.inicio.debitar(valor):
                    print(f"Foi debitado R$ {valor} da sua conta, seu saldo atual é de R$ {b.contasF.inicio.saldo}.")
                else:
                    print("Saldo Insuficiente.")
            
            elif resposta2 == 3:
                id=int(input("Digite o ID da nova conta."))
                cpf=str(input("Digite o CPF da conta."))
                saldo=float(input("Digite o saldo da conta."))
                no_conta = Conta(id,cpf,saldo)
                b.adiciona_conta_F(no_conta)
                print(f"A conta {no_conta} foi adicionada.")

            elif resposta2 == 4:
                print(f"A conta {b.contasF.inicio} foi removida.")
                b.remove_conta_F()

            elif resposta2 == 5:
                print(f"A fila tem {b.tamanho_conta_F()} conta(s).")

            else:
                print("Resposta Inválida.")

#CONTAS LISTA
    elif(resposta == 3):
        print(b.contasL)
        
        resposta2 =int(0)
        lista_resposta2 = [1,2,3,4,5,6,7,8,9,10]
        while resposta2 != 10:
            resposta2 = int(input("1 - Creditar\n2 - Debitar\n3 - Adicionar Conta\n4 - Remover Conta\n5 - Tamanho Lista\n6 - Valor Total Lista\n7 - Buscar Conta ID\n8 - Ordenar Contas ID\n9 - Imprimir Lista\n10 - Voltar\n"))
            
            if resposta2 == 1:
                valor = float(input("Digite o valor a ser creditado."))
                id = int(input("Digite o ID da conta que será creditada."))
                b.adiciona_valor_conta(valor,id)
                print(f"Foi creditado R$ {valor} na sua conta, seu saldo atual é de R$ {b.contasL.mostrarL(id).saldo}.")

            elif resposta2 == 2:
                valor = float(input("Digite o valor a ser debitado."))
                id = int(input("Digite o ID da conta que será debitada."))
                b.debita_valor_conta(valor,id)
                if valor > b.contasL.mostrarL(id).saldo:
                    print("Saldo Insuficiente.")                
                else:
                    print(f"Foi debitado R$ {valor} da sua conta, seu saldo atual é de R$ {b.contasL.mostrarL(id).saldo}.")
                

            
            elif resposta2 == 3:
                id=int(input("Digite o ID da nova conta."))
                cpf=str(input("Digite o CPF da conta."))
                saldo=float(input("Digite o saldo da conta."))
                pos=int(input("Digite em qual posição da lista a conta será adicionada."))
                no_conta = Conta(id,cpf,saldo)
                b.adiciona_conta_L(no_conta, pos)
                print(f"A conta {no_conta} foi adicionada, na {pos}º posição.")

            elif resposta2 == 4:
                pos = int(input("Digite a posição que será removida."))
                print(f"A conta {b.contasL.mostrarL(pos)} foi removida.")
                b.remove_conta_L(pos)

            elif resposta2 == 5:
                print(f"A fila tem {b.tamanho_conta_L()} conta(s).")
            
            elif resposta2 == 6:
                print(f"O valor da lista de contas é {b.total_valor_contas()}.")

            elif resposta2 == 7:
                id = int(input("Digite o ID da conta que deseja buscar. "))
                print(b.busca_conta(id))

            elif resposta2 == 8:
                print("As contas estão ordenadas.")
                b.ordenar()

            elif resposta2 == 9:
                b.imprimirL()

            else:
                print("Resposta Inválida.")

#END   
    elif resposta == 4:
        pass 
    else:
        print("Resposta Inválida.")