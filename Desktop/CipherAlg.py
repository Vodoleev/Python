import sys


def read(path):
    with open(path, 'rb') as file:
        return bytearray(file.read())
def write(path, data):
    with open(path, 'wb') as file:
        file.write(bytes(data))
        
def CaesarEncryption(data, key):
    for i in range(len(data)):
        data[i] = (data[i] + key) % 256
    return data
def CaesarDecryption(data, key):
    return CaesarEncryption(data, -key)

def VigenerEncryption(data, keyWord):
    keyWord = bytearray(keyWord.encode("utf-8"))
    for i in range(len(data)):
        data[i] = (data[i] + keyWord[i % len(keyWord)]) % 256
    return data
def VigenerDecryption(data, keyWord):
    keyWord = bytearray(keyWord.encode("utf-8"))
    for i in range(len(data)):
        data[i] = (data[i] - keyWord[i % len(keyWord)]) % 256
    return data

def VernamEncryption(data, keyWord):
    keyWord = bytearray(keyWord.encode("utf-8"))
    for i in range(len(data)):
        data[i] = (data[i] ^ keyWord[i % len(keyWord)]) % 256
    return data
def VernamDecryption(data, keyWord):
    keyWord = bytearray(keyWord.encode("utf-8"))
    for i in range(len(data)):
        data[i] = (data[i] ^ keyWord[i % len(keyWord)]) % 256
    return data

