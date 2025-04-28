import unicodedata
from bigtree import Node, print_tree

class SantanderTour:
    def __init__(self):
        """Inicializa el árbol turístico con big-tree"""
        self.raiz = self._crear_estructura()

    def _crear_estructura(self):
        """Crea la estructura jerárquica inicial del árbol turístico"""
        raiz = Node("Aeropuerto Palonegro")

        # Nivel 2: Municipios
        bucaramanga = Node("Bucaramanga", parent=raiz)
        giron = Node("Giron", parent=raiz)
        floridablanca = Node("Floridablanca", parent=raiz)
        piedecuesta = Node("Piedecuesta", parent=raiz)

        # Nivel 3: Rutas principales
        parque_buca = Node("Ruta 1: Parque Principal", parent=bucaramanga)
        ruta_alternativa_buca = Node("Ruta 2: Sitios Alternativos", parent=bucaramanga)
        parque_giron = Node("Ruta 1: Parque Principal", parent=giron)
        ruta_alternativa_giron = Node("Ruta 2: Sitios Alternativos", parent=giron)
        parque_flori = Node("Ruta 1: Parque Principal", parent=floridablanca)
        ruta_alternativa_flori = Node("Ruta 2: Sitios Alternativos", parent=floridablanca)
        parque_piedecuesta = Node("Ruta 1: Parque Principal", parent=piedecuesta)
        ruta_alternativa_piedecuesta = Node("Ruta 2: Sitios Alternativos", parent=piedecuesta)

        # Nivel 4: Sitios turísticos en rutas principales
        Node("Casa del Libro Total", parent=parque_buca)
        Node("Museo de Arte Moderno", parent=parque_buca)
        Node("Parque del Agua", parent=ruta_alternativa_buca)
        Node("Mirador La Mesa", parent=ruta_alternativa_buca)

        Node("Basilica", parent=parque_giron)
        Node("Cañon de las Iguanas", parent=parque_giron)
        Node("Capilla de las Nieves", parent=ruta_alternativa_giron)
        Node("Cascada Juan Curi", parent=ruta_alternativa_giron)

        Node("Jardin Botanico", parent=parque_flori)
        Node("Parque de Parapentes", parent=parque_flori)
        Node("Parque El Santisimo", parent=ruta_alternativa_flori)

        Node("Gran Cañon del Chicamocha", parent=parque_piedecuesta)
        Node("Balneario la Maravilla", parent=parque_piedecuesta)
        Node("Iglesia San Francisco Javier", parent=ruta_alternativa_piedecuesta)
        Node("Casona El Tabacal", parent=ruta_alternativa_piedecuesta)

        return raiz

    def mostrar_estructura(self):
        """Muestra la estructura completa del árbol"""
        print("\nEstructura del Arbol Turístico de Santander")
        print_tree(self.raiz, style="ascii")

    def imprimir_ruta_y_paradas(self, palabra):
        """
        Busca un nodo basado en una palabra clave, imprime la ruta completa y cuenta las paradas necesarias.
        :param palabra: Palabra clave para buscar el nodo.
        """
        nodo = self._buscar_nodo(self.raiz, palabra)
        if nodo:
            ruta = self._construir_ruta(nodo)
            print(f"\nRuta hacia '{palabra}':\n{' → '.join(ruta)}")
            print(f"Paradas necesarias: {len(ruta)}")
        else:
            print(f"\nNo se encontró un nodo con la palabra '{palabra}'.")

    def agregar_nodo(self, nombre_nodo, nombre_padre):
        """
        Agrega un nodo al árbol bajo el nodo padre especificado.
        :param nombre_nodo: Nombre del nuevo nodo a agregar.
        :param nombre_padre: Nombre del nodo padre donde se agregará el nuevo nodo.
        """
        nodo_padre = self._buscar_nodo(self.raiz, nombre_padre)
        if nodo_padre:
            Node(nombre_nodo, parent=nodo_padre)
            print(f"\nNodo '{nombre_nodo}' agregado exitosamente bajo '{nombre_padre}'.")
        else:
            print(f"\nNodo padre '{nombre_padre}' no encontrado en el árbol.")

    def eliminar_nodo(self, nombre_nodo):
        """
        Elimina un nodo del árbol pero transfiere sus hijos al nodo padre.
        :param nombre_nodo: Nombre del nodo que se desea eliminar.
        """
        if self._normalizar_texto(nombre_nodo) == self._normalizar_texto(self.raiz.name):
            print("\nNo se puede eliminar la raíz del árbol.")
            return

        nodo_a_eliminar = self._buscar_nodo(self.raiz, nombre_nodo)
        if nodo_a_eliminar:
            # Transfiere los hijos al nodo padre
            padre = nodo_a_eliminar.parent
            if padre is not None:
                for hijo in nodo_a_eliminar.children:
                    hijo.parent = padre  # Reasigna el padre de los hijos
                nodo_a_eliminar.parent = None  # Desconecta el nodo eliminado
                print(f"\nNodo '{nombre_nodo}' eliminado, y sus hijos han sido transferidos a '{padre.name}'.")
            else:
                print(f"\nNo se puede transferir los hijos porque el nodo '{nombre_nodo}' no tiene padre.")
        else:
            print(f"\nNodo '{nombre_nodo}' no encontrado en el árbol.")

    def _buscar_nodo(self, nodo, nombre):
        """Busca un nodo por nombre en el árbol. Ignora mayúsculas, minúsculas y tildes."""
        if self._normalizar_texto(nodo.name) == self._normalizar_texto(nombre):
            return nodo
        for hijo in nodo.children:
            resultado = self._buscar_nodo(hijo, nombre)
            if resultado:
                return resultado
        return None

    def _construir_ruta(self, nodo):
        """
        Construye la ruta desde la raíz hasta el nodo indicado.
        :param nodo: Nodo actual.
        :return: Lista con la ruta completa desde la raíz hasta el nodo.
        """
        ruta = []
        actual = nodo
        while actual is not None:
            ruta.insert(0, actual.name)  # Insertamos al inicio para construir la ruta desde la raíz
            actual = actual.parent
        return ruta

    def _normalizar_texto(self, texto):
        """
        Normaliza texto para eliminar mayúsculas, minúsculas y tildes.
        :param texto: Texto a normalizar.
        :return: Texto normalizado.
        """
        return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII').lower()

# Uso del sistema turístico con menú interactivo
def main():
    sistema = SantanderTour()

    while True:
        print("\nMENU PRINCIPAL")
        print("1. Mostrar estructura completa")
        print("2. Imprimir ruta hacia un nodo")
        print("3. Agregar un nodo")
        print("4. Eliminar un nodo")
        print("5. Salir")

        opcion = input("\nSeleccione una opción (1-5): ")

        if opcion == "1":
            sistema.mostrar_estructura()
        elif opcion == "2":
            palabra = input("Ingrese la palabra clave del nodo: ")
            sistema.imprimir_ruta_y_paradas(palabra)
        elif opcion == "3":
            nombre_nodo = input("Ingrese el nombre del nuevo nodo: ")
            nombre_padre = input("Ingrese el nombre del nodo padre donde desea agregarlo: ")
            sistema.agregar_nodo(nombre_nodo, nombre_padre)
        elif opcion == "4":
            nombre_nodo = input("Ingrese el nombre del nodo que desea eliminar: ")
            sistema.eliminar_nodo(nombre_nodo)
        elif opcion == "5":
            print("\n¡Gracias por explorar Santander con nosotros!")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()