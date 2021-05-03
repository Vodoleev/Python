import sys
import requests
from urllib.parse import urlparse


def file_name(path):
    prename = urlparse(path).path
    return prename[prename.rfind('/') + 1::]
def isURL(path):
    return (urlparse(path).scheme != '' and urlparse(path).netloc != '')
def download(path):
    return bytearray(requests.get(path).content)
def read(path):
    if isURL(path):
        return bytearray(download(path))
    else:
        with open(path, 'rb') as file:
            return bytearray(file.read())
def write(path, data):
    if isURL(path):
    	path = file_name(path)
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
