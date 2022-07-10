import unittest
from xmlrpc.server import SimpleXMLRPCServer

class TestesRPC(unittest.TestCase):

    def test_serverCriation(self):
        ip = '127.0.0.1'
        porta = 8080
        servidor = SimpleXMLRPCServer((ip, porta))
        print(servidor)
        self.assertTrue(servidor,'Erro ao criar o servidor')

    if __name__ == '__main__':
        unittest.main()
