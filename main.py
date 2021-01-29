from autor import Autor
from leitor import Leitor
from post import Post

autor = Autor("daniel", "Pinheiro", 20)

leitor1 = Leitor("Marcos", "Brito", 18)
leitor2 = Leitor("Bryan", "Bezerra", 28)

post1 = Post("A razão das coisas", "20/01/2021", "20/01/2021", "mknjknnj")
post2 = Post("Mundo ciência", "02/01/2021", "02/01/2021", "mweawaaknnj")

autor.add_leitor(leitor1)
autor.add_leitor(leitor2)

# autor.remove_leitor(leitor1)

autor.add_post(post1)

autor.atualizar_post("A razão das coisas")
