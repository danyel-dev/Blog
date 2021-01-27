autor1 = Autor("Carlos daniel", "Pinheiro", 20)

leitor1 = Leitor("Matheus", "Silva", 22)
leitor2 = Leitor("Diego", "Perreira", 30)

autor1.add_leitor(leitor1)
autor1.add_leitor(leitor2)

post1 = Post("A razão das coisas", "20/01/2021")

autor1.add_post(post1)
