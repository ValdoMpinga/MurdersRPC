import unittest
import xmlrpc
import xmlrpc.client


class MyTestCase(unittest.TestCase):
    def test_clientCreation(self):
            ip = '127.0.0.1'
            porta = 8080
            servidor = xmlrpc.client.ServerProxy("http://{0}:{1}/".format(ip, porta))
            print(servidor)
            self.assertTrue(servidor,'Err ao criar o cliente')


if __name__ == '__main__':
    unittest.main()
