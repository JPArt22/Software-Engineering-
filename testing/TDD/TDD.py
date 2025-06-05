import unittest

# ----------------------------
# 🟥 RED: Test falla porque aún no existe la clase CarritoDeCompras
# ----------------------------
# En este test, asumimos que existe una clase CarritoDeCompras y que comienza vacía

class TestCarritoDeCompras(unittest.TestCase):

    def test_carrito_empieza_vacio(self):
        carrito = CarritoDeCompras()  # ❌ Esto fallará si la clase aún no está definida
        self.assertEqual(len(carrito.productos), 0)


# ----------------------------
# 🟩 GREEN: Implementamos lo mínimo para que el test pase
# ----------------------------
# Creamos la clase CarritoDeCompras y definimos una lista vacía de productos

class CarritoDeCompras:
    def __init__(self):
        self.productos = []  # Ahora el test test_carrito_empieza_vacio pasa ✅


# ----------------------------
# 🟥 RED: Siguiente test, agregar un producto (aún no implementado)
# ----------------------------

    def test_agregar_producto(self):
        carrito = CarritoDeCompras()
        carrito.agregar_producto("Laptop", 1500)  # ❌ Este método no existe todavía
        self.assertEqual(len(carrito.productos), 1)
        self.assertEqual(carrito.productos[0]["nombre"], "Laptop")
        self.assertEqual(carrito.productos[0]["precio"], 1500)

# ----------------------------
# 🟩 GREEN: Implementamos agregar_producto
# ----------------------------

# Añadimos un método que agregue un diccionario {"nombre": ..., "precio": ...} a la lista

class CarritoDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append({"nombre": nombre, "precio": precio})


# ----------------------------
# 🟥 RED: Queremos ahora calcular el total del carrito
# ----------------------------

    def test_total_carrito(self):
        carrito = CarritoDeCompras()
        carrito.agregar_producto("Laptop", 1500)
        carrito.agregar_producto("Mouse", 50)
        self.assertEqual(carrito.total(), 1550)  # ❌ total() aún no existe


# ----------------------------
# 🟩 GREEN: Creamos el método total
# ----------------------------

# La función recorre los productos y suma sus precios

class CarritoDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append({"nombre": nombre, "precio": precio})

    def total(self):
        return sum(p["precio"] for p in self.productos)


# ----------------------------
# 🟥 RED: Añadir descuento (funcionalidad nueva)
# ----------------------------

    def test_descuento(self):
        carrito = CarritoDeCompras()
        carrito.agregar_producto("TV", 1000)
        carrito.aplicar_descuento(10)  # ❌ aplicar_descuento aún no existe
        self.assertEqual(carrito.total(), 900)  # 1000 - 10%


# ----------------------------
# 🟩 GREEN: Implementamos aplicar_descuento
# ----------------------------

# Guardamos el descuento en un atributo y lo aplicamos al calcular el total

class CarritoDeCompras:
    def __init__(self):
        self.productos = []
        self.descuento = 0  # Nuevo atributo para guardar el descuento

    def agregar_producto(self, nombre, precio):
        self.productos.append({"nombre": nombre, "precio": precio})

    def aplicar_descuento(self, porcentaje):
        self.descuento = porcentaje

    def total(self):
        total_bruto = sum(p["precio"] for p in self.productos)
        return total_bruto * (1 - self.descuento / 100)


# ----------------------------
# ♻️ REFACTOR: Código limpio y organizado, no rompemos ningún test
# ----------------------------
# En este punto ya podemos considerar reorganizar o mejorar código interno
# sin modificar lo que los tests validan. Por ejemplo: validar tipos, usar clases Producto, etc.

# ----------------------------
# Ejecutar todos los tests
# ----------------------------

if __name__ == '__main__':
    unittest.main()
