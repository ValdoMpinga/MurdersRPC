from xmlrpc.server import SimpleXMLRPCServer
from QueryExecutor import queries

IP = '172.16.186.178'
PORT = 8080

menuOptions = {
    1: 'Listar numero de assassinatos resolvidos',
    2: 'Listar assassinatos entre idades',
    3: 'Listagem de assassinos por sexo e raça',
    4: 'Listagem de crimes por mês',
    5: 'Listagem de assassinatos por armas',
    6: 'Inserção do ficheiro xml para a base de dados',
    7: 'soft insert',
    8: 'soft delete',
    9: 'backup check',
}

queryExecutorInstance = queries.QueriesExecutor()

# def option1():
#     return queryExecutorInstance.listNumberOfSolvedMurderers()
#
# def option2(ageOne,ageTwo):
#     queryExecutorInstance.listMurdersBetweenAges(ageOne,ageTwo)
#
# def option3(sex,race):
#     queryExecutorInstance.listMurderersThrowSexAndRace(sex,race)
#
# def option4(month):
#     queryExecutorInstance.listCrimeThrowMonths(month.year)
#
# def option5():
#     queryExecutorInstance.listCrimesThrowGuns()
#
# def option6():
#     queryExecutorInstance.sendParsedXMLToDB()

def printMenu():
    print("Bem vindo aos registros dos assassinatos!")
    for key in menuOptions.keys():
        print(key, '--', menuOptions[key])
    opcao = int(input('Introduz a opcao'))
    menu(opcao)

def menu(option,*args):
    if option == 1:
        return  queryExecutorInstance.listNumberOfSolvedMurderers()
    elif option == 2:
        return queryExecutorInstance.listMurdersBetweenAges(args[0], args[1])
    elif option == 3:
        return queryExecutorInstance.listMurderersThroughSexAndRace(args[0], args[1])
    elif option == 4:
        return queryExecutorInstance.listCrimeThroughMonths(args[0], args[1])
    elif option == 5:
        return queryExecutorInstance.listCrimesThroughGuns(args[0])
    elif option == 6:
        return queryExecutorInstance.sendParsedXMLToDB()
    elif option == 7:
        return queryExecutorInstance.softDeleteInsert()
    elif option == 8:
        return queryExecutorInstance.softDeleteDelete()
    elif option == 9:
        return queryExecutorInstance.deletedDataSelect()
    elif option == 0:
        print('Adeus!')
        exit()
    else:
        print('Opção invalida, por favor escolha uma opção entre 1 a 9')

if __name__ == "__main__":
     server= SimpleXMLRPCServer((IP, PORT))
     server.register_function(menu, "menu")
     server.serve_forever()
     #printMenu()

