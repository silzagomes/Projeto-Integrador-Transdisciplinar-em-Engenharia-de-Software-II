# loja-cupcakes/models.py
class Produto:
  def __init__(self, id_produto, nome, descricao, preco, categoria, imagemUrl):
    self.id_produto = id_produto
    self.nome = nome
    self.descricao = descricao
    self.preco = preco
    self.categoria = categoria
    self.imagemUrl = imagemUrl
    
  @staticmethod
  def get_todos():
    return [
      # Nota: O caminho das imagens é ajustado para a pasta 'static' do Flask
      Produto(1, "Cupcake Red Velvet", "Clássico com cobertura de cream cheese.", 8.50, "Clássicos", "images/red-velvet.jpg"),
      Produto(2, "Cupcake de Chocolate", "Massa fofinha e cobertura de brigadeiro.", 7.00, "Chocolate", "images/chocolate.jpg"),
      Produto(3, "Cupcake de Baunilha", "Simples e delicioso, com baunilha de Madagascar.", 7.50, "Clássicos", "images/baunilha.jpg"),
      Produto(4, "Cupcake Vegano", "Feito com leite de amêndoas e cacau.", 9.00, "Veganos", "images/vegano.jpg")
    ]

  @staticmethod
  def buscar_por_id(id_produto):
    id_produto = int(id_produto)
    for p in Produto.get_todos():
        if p.id_produto == id_produto:
            return p
    return None