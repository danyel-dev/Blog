from autor import Autor
from leitor import Leitor
from post import Post
import os

leitores = {}
autores = {}
posts = {}

cont_leitor = 0
cont_autor = 0
cont_post = 0

while True:
    print("1 - Cadastrar Autor")
    print("2 - Cadastrar Leitor")
    print("3 - Cadastrar Post")
    print("4 - Seguir Autor")
    print("5 - Listar autores")
    print("6 - Listar leitores")
    print("0 - Sair")

    op = int(input("\nDigite uma opção: "))

    print()

    if op == 1:
        nome = input("Qual o seu nome? ")
        sobrenome = input("E o seu sobrenome? ")
        idade = int(input("Informe sua idade: "))

        autor = Autor(nome, sobrenome, idade)
        autores[cont_autor] = autor
        cont_autor += 1
    elif op == 2:
        nome = input("Qual o seu nome? ")
        sobrenome = input("E o seu sobrenome? ")
        idade = int(input("Informe sua idade: "))

        leitor = Leitor(nome, sobrenome, idade)
        leitores[cont_leitor] = leitor
        cont_leitor += 1
    elif op == 3:
        ...
    elif op == 4:
        for key, value in autores.items():
            print(f"Id: {key}")
            print(f"Nome: {value.nome} {value.sobrenome}")

        op = int(input("Qual desses autores você quer seguir? "))

    elif op == 5:
        ...

    elif op == 0:
        break 

    os.system("clear")

