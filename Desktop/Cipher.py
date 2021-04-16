from CipherAlg import *

args = sys.argv
if args[1] == 'caesar':
	path = args[3]
	key = int(args[4])
	if args[2] == '-e':
		write(path, CaesarEncryption(read(path), key))
	elif args[2] == '-d':
		write(path, CaesarDecryption(read(path), key))
elif args[1] == 'vigener':
	path = args[3]
	keyWord = args[4]
	if args[2] == '-e':
		write(path, VigenerEncryption(read(path), keyWord))
	elif args[2] == '-d':
		write(path, VigenerDecryption(read(path), keyWord))
elif args[1] == 'vernam':
	path = args[3]
	keyWord = args[4]
	if args[2] == '-e':
		write(path, VernamEncryption(read(path), keyWord))
	elif args[2] == '-d':
		write(path, VernamDecryption(read(path), keyWord))
