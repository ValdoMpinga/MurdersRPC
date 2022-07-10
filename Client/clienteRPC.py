import xmlrpc.client

print('\tCLIENTE')

IP = input('- Digite o IP do servidor: ')
PORTA = int(input('- Digite a PORTA: '))

servidor = xmlrpc.client.ServerProxy("http://{0}:{1}/".format(IP, PORTA))

opcao = 100
idade1= True
idade2 = True
sexo =" "
raca =" "
arma =" "
armas=100

while (opcao !=0) :
    print("""
    1.Selecionar crimes resolvidos
    2.Selecionar crimes entre duas idades
    3.Selecionar crimes por sexo e raça
    4.Selecionar crimes pelo mês 
    5.Listar assassinatos por armas
    6.Inserir ficheiro xml convertido na base de dados
    7.Inserir soft-Delete
    8.Apagar o soft-Delete
    9.Selecionar o dado apagado
    """ )
    
    opcao = int(input("- Introduza uma opcao: "))
    if opcao==1: 
        opcaoEscolhida = servidor.menu(opcao)
        print(opcao)
        print(opcaoEscolhida)
    elif opcao==2:
        print("Introduza a primeira idade: ")
        if idade1<0 and idade >100 :
            print("A idade deve ser  entre 0 e 100 anos de idade")
        else :
            idade1=int(input())
        print("Introduza a segunda idade: ")
        if idade2<idade1 and idade2>100:
            print("A segunda idade deve ser maior que a primeira e menor que 100")
        else:
            idade2=int(input())
        opcaoEscolhida = servidor.menu(opcao,idade1,idade2)
        print(opcaoEscolhida)
            
    elif opcao==3:
        print("Introduza o sexo: ")
        sexo=str(input())
        print("Introduza a raça")
        raca=str(input())
        opcaoEscolhida = servidor.menu(opcao,sexo,raca)
        print(opcaoEscolhida)

        
    elif opcao==4:
        print("Introduza o mês da ocorrência do crime:")
        mes=str(input())
        print("Introduza o ano da ocorrência do crime:")
        ano=str(input())
        opcaoEscolhida = servidor.menu(opcao,mes,ano)
        print(opcaoEscolhida)

    elif opcao==5:
        while (armas!=0 ):
            print("""Escolha o tipo de arma:
                  1-Handgun
                  2-Knife
                  3-Rifle
                  4-Blunt Object
                  5-Fire
                  6-Shotgun
                  0-Voltar""")
            armas=int(input())
            if armas==1:
                opcaoEscolhida = servidor.menu(5,"Handgun")
                print(opcaoEscolhida)
            elif armas==2:
                opcaoEscolhida = servidor.menu(5,"Knife")
                print(opcaoEscolhida)
            elif armas==3:
                opcaoEscolhida = servidor.menu(5,"Rifle")
                print(opcaoEscolhida)
            elif armas==4:
                opcaoEscolhida = servidor.menu(5,"Blunt Object")
                print(opcaoEscolhida)
            elif armas==5:
                opcaoEscolhida = servidor.menu(5,"Fire")
                print(opcaoEscolhida)
                
            elif armas==6:
                opcaoEscolhida = servidor.menu(5,"Shotgun")
                print(opcaoEscolhida)
    elif opcao==6: 
        opcaoEscolhida = servidor.menu(opcao)
        print(opcaoEscolhida)            
    elif opcao==7: 
        opcaoEscolhida = servidor.menu(opcao)
        print(opcaoEscolhida)       
    elif opcao==8: 
        opcaoEscolhida = servidor.menu(opcao)
        print(opcaoEscolhida)
    elif opcao==9: 
        opcaoEscolhida = servidor.menu(opcao)
        print(opcaoEscolhida)
                
    
    
    
    

    
    
    
