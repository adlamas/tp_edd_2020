class Producto:
    def __init__(self, titulo='', modelo='', categoria='', precio=0.00, link=''):
        self.titulo = titulo
        self.categoria = categoria
        self.modelo = modelo
        self.precio = precio
        self.link = link

    def __str__(self):
        return f'Titulo: {self.titulo}, Categoria: {self.categoria}, Precio: {self.precio}'

    def __repr__(self):
        return f'{self.titulo};{self.categoria};{self.precio};{self.link}'

    def __eq__(self, otro):
        return self.modelo == otro.modelo