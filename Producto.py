class Producto:

    def __init__(self, nombre, valor, stock):
        self.nombre = nombre
        self.valor = valor
        self.stock = stock

    def toDBCollection (self):
        return{
            "nombre":self.nombre,
            "valor":self.valor,
            "stock":self.stock
            }

    def __str__(self):
        return "nombre: %s - valor: %f - stock: %i" \
               %(self.nombre, self.valor, self.stock)
