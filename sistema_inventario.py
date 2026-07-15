class Producto:
    def __init__(self, nombre, precio, cantidad):

        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.nombre = nombre

        self.validar_precio(precio)
        self.precio = float(precio)

        self.validar_cantidad(cantidad)
        self.cantidad = int(cantidad)

    @staticmethod
    def validar_precio(precio):
        if not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un número.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

    @staticmethod
    def validar_cantidad(cantidad):
        if not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un número entero.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

    def actualizar_precio(self, nuevo_precio):
        self.validar_precio(nuevo_precio)
        self.precio = float(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad):
        self.validar_cantidad(nueva_cantidad)
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return (
            f"Nombre: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Cantidad: {self.cantidad} | "
            f"Valor Total: ${self.calcular_valor_total():.2f}"
        )


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        existente = self.buscar_producto(producto.nombre)
        if existente:
            raise ValueError("Ya existe un producto con ese nombre.")

        self.productos.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def calcular_valor_inventario(self):
        valor_inventario = 0
        for producto in self.productos:
            valor_inventario += producto.calcular_valor_total()

        return valor_inventario

    def listar_productos(self):
        if not self.productos:
            print("\nEl inventario está vacío.\n")
            return

        print("\n===== INVENTARIO =====")
        for producto in self.productos:
            print(producto)
        print("======================\n")


def menu_principal():
    inventario = Inventario()

    while True:
        print("====== SISTEMA DE INVENTARIO ======")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Actualizar precio")
        print("6. Actualizar cantidad")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre del producto: ").strip()
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))

                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)

                print("Producto agregado correctamente.\n")

            elif opcion == "2":
                nombre = input("Ingrese el nombre del producto: ")

                producto = inventario.buscar_producto(nombre)

                if producto:
                    print("\nProducto encontrado:")
                    print(producto)
                    print()
                else:
                    raise LookupError("Producto no encontrado.")

            elif opcion == "3":
                inventario.listar_productos()

            elif opcion == "4":
                total = inventario.calcular_valor_inventario()
                print(f"\nValor total del inventario: ${total:.2f}\n")

            elif opcion == "5":
                nombre = input("Ingrese el nombre del producto a actualizar precio: ")

                producto = inventario.buscar_producto(nombre)

                if producto:
                    nuevo_precio = float(input(f"Ingrese el nuevo precio para {nombre.lower()}: "))
                    producto.actualizar_precio(nuevo_precio)
                    print("\nPrecio actualizado correctamente.\n")
                else:
                    raise LookupError("Producto no encontrado.")

            elif opcion == "6":
                nombre = input("Ingrese el nombre del producto a actualizar la cantidad: ")

                producto = inventario.buscar_producto(nombre)

                if producto:
                    nueva_cantidad = int(input(f"Ingrese la nueva cantidad para {nombre.lower()}: "))
                    producto.actualizar_cantidad(nueva_cantidad)
                    print("\nCantidad actualizada correctamente.\n")
                else:
                    raise LookupError("Producto no encontrado.")

            elif opcion == "7":
                print("\nGracias por utilizar el sistema.")
                break

            else:
                print("\nOpción inválida.\n")

        except ValueError as e:
            print(f"\nError: {e}\n")

        except TypeError as e:
            print(f"\nError de tipo de dato: {e}\n")

        except LookupError as e:
            print(f"\n{e}\n")

        except Exception as e:
            print(f"\nError inesperado: {e}\n")


if __name__ == "__main__":
    menu_principal()
