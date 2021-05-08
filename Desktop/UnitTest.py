import random, string, unittest
from CipherAlg import *


class TestCipherMethods(unittest.TestCase):
    def randomword(self):
        length = random.randint(1, 10**5)
        letters = [chr(i) for i in range(255)]
        return ''.join(random.choice(letters) for i in range(length))
    def make_data(self):
        return bytearray(self.randomword().encode('utf-8'))
    def test_caesar(self):
        data = self.make_data()
        key = random.randint(0, 10**5)
        self.assertEqual(data, CaesarDecryption(CaesarEncryption(data, key), key))
    def test_vigener(self):
        data = self.make_data()
        key = self.randomword()
        self.assertEqual(data, VigenerDecryption(VigenerEncryption(data, key), key))
    def test_vernam(self):
        data = self.make_data()
        key = self.randomword()
        self.assertEqual(data, VernamDecryption(VernamEncryption(data, key), key))

if __name__ == '__main__':

    unittest.main(argv=['first-arg-is-ignored'], exit=False)

