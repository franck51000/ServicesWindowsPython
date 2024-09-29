# -*- coding: utf-8 -*-
import time

def write_hello_world():
    # Fonction qui écrit "Hello World" dans un fichier
    with open("C:\\python\\output.txt", "a") as file:
        file.write("Hello World\n")

def main():
    # Fonction principale qui écrit un log et appelle write_hello_world toutes les minutes
    with open("C:\\python\\test_log.txt", "a") as log:
        log.write("Le script a démarré à : {}\n".format(time.ctime()))
    while True:
        write_hello_world()
        time.sleep(60)  # Attendre 1 minute

if __name__ == "__main__":
    main()
