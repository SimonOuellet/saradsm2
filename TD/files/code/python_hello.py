import sys
prenom = input("Quel est ton prénom? ")
print(f"Bonjour {prenom}")
print(len(sys.argv), sys.argv[0])
if len(sys.argv) > 1:
    print(f"Argument passer en premiere position : {sys.argv[1]}")
if len(sys.argv) > 2:
    print(f"Argument passer en seconde position : {sys.argv[2]}")

