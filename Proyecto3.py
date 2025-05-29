import networkx as nx
import matplotlib.pyplot as plt
import json

class Grafo:
    def __init__(self):
        """Inicializa el grafo cargando datos desde un archivo JSON si existe."""
        self.grafo = {}
        self.pesos = {}
        self.archivo = "grafo.json"
        self.cargar_grafo()

    def guardar_grafo(self):
        """Guarda el estado actual del grafo en un archivo JSON."""
        datos = {
            "grafo": self.grafo,
            "pesos": {f"{k[0]}-{k[1]}": v for k, v in self.pesos.items()}
        }
        with open(self.archivo, "w") as f:
            json.dump(datos, f, indent=4)

    def cargar_grafo(self):
        """Carga el grafo desde un archivo JSON si existe, sino lo inicializa."""
        try:
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                self.grafo = datos.get("grafo", {})
                self.pesos = {tuple(k.split("-")): v for k, v in datos.get("pesos", {}).items()}
        except (FileNotFoundError, json.JSONDecodeError):
            
            self.inicializar_paradas()
            self.guardar_grafo()

    def inicializar_paradas(self):
        """Carga las paradas por defecto y establece conexiones con pesos."""
        paradas = ["Uis", "Cra 33", "Cra 27", "Real de minas", "Terminal", 
                   "Rocio", "Provenza", "Paralela", "Parque Florida", "Limoncito"]
        
        # Conexiones iniciales con sus pesos específicos
        conexiones_iniciales = [
            ("Uis", "Cra 33", 7),
            ("Cra 33", "Cra 27", 5),
            ("Cra 27", "Real de minas", 4),
            ("Real de minas", "Terminal", 7),
            ("Terminal", "Rocio", 6),
            ("Rocio", "Provenza", 4),
            ("Provenza", "Paralela", 5),
            ("Paralela", "Parque Florida", 8),
            ("Parque Florida", "Limoncito", 6)
        ]
        
        # Primero agregamos todas las paradas
        for parada in paradas:
            self.agregar_parada(parada)
        
        # Establecemos las conexiones iniciales
        for origen, destino, peso in conexiones_iniciales:
            self.agregar_conexion(origen, destino, peso)
        
        # Conectamos las paradas restantes entre sí
        for i in range(len(paradas)):
            for j in range(i + 1, len(paradas)):
                origen = paradas[i]
                destino = paradas[j]
                # Si no existe una conexión, la creamos
                if destino not in self.grafo[origen]:
                    peso = abs(i - j) * 3  # Peso basado en la distancia
                    self.agregar_conexion(origen, destino, peso)

    def agregar_parada(self, parada):
        """Agrega una parada y la conecta con todas las existentes."""
        if parada not in self.grafo:
            self.grafo[parada] = []
            self.guardar_grafo()
            return True
        return False

    def agregar_conexion(self, origen, destino, peso=1):
        """Agrega una conexión con peso y guarda los cambios."""
        self.agregar_parada(origen)
        self.agregar_parada(destino)
        if destino not in self.grafo[origen]:
            self.grafo[origen].append(destino)
            self.grafo[destino].append(origen)
            self.pesos[(origen, destino)] = peso
            self.pesos[(destino, origen)] = peso
            self.guardar_grafo()

    def eliminar_parada(self, parada):
        """Elimina una parada y guarda los cambios."""
        if parada in self.grafo:
            del self.grafo[parada]
            for conexiones in self.grafo.values():
                if parada in conexiones:
                    conexiones.remove(parada)
            self.pesos = {k: v for k, v in self.pesos.items() if parada not in k}
            self.guardar_grafo()

    def buscar_parada(self, parada):
        """Verifica si una parada existe en el grafo."""
        return parada in self.grafo

    def mostrar_ruta(self):
        """Muestra todas las paradas y sus conexiones."""
        for parada, conexiones in self.grafo.items():
            print(f"{parada}: {', '.join(conexiones)}")

    def obtener_proxima_parada(self, parada):
        """Muestra las conexiones de una parada específica."""
        return self.grafo.get(parada, [])

    def visualizar_grafo(self):
        """Genera una representación visual del grafo con pesos."""
        G = nx.Graph()
        G.add_nodes_from(self.grafo.keys())
        
        for (origen, destino), peso in self.pesos.items():
            G.add_edge(origen, destino, weight=peso)

        # Aumentamos el tamaño de la figura
        plt.figure(figsize=(12, 8))
        
        # Usamos diferentes layouts para mejor organización
        # pos = nx.spring_layout(G, k=1, iterations=50)  # Distribución en resorte
        # pos = nx.circular_layout(G)  # Distribución circular
        pos = nx.shell_layout(G)      # Distribución en capas
        
        # Dibujamos los nodos
        nx.draw_networkx_nodes(G, pos,
                              node_color='lightblue',
                              node_size=2500,
                              alpha=0.7)
        
        # Dibujamos las aristas
        nx.draw_networkx_edges(G, pos,
                              edge_color='gray',
                              width=2,
                              alpha=0.6)
        
        # Dibujamos las etiquetas de los nodos
        nx.draw_networkx_labels(G, pos,
                              font_size=10,
                              font_weight='bold')
        
        # Dibujamos los pesos de las aristas
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos,
                                   edge_labels=labels,
                                   font_size=8)
        
        plt.title("Sistema De Optimizacion de Rutas Area metropolitana", pad=20, size=16)
        plt.axis('off')  # Ocultamos los ejes
        
        # Ajustamos los márgenes
        plt.tight_layout()
        plt.show()

    def encontrar_ruta_optima(self, origen, destino, tipo_ruta="corta"):
        """Encuentra la ruta más corta o más larga entre dos paradas."""
        if not self.buscar_parada(origen) or not self.buscar_parada(destino):
            print(f"⚠️ Error: {origen if not self.buscar_parada(origen) else destino} no existe en el grafo.")
            return

        G = nx.Graph()
        for (orig, dest), peso in self.pesos.items():
            # Para ruta más larga, invertimos los pesos
            peso_usado = 1/peso if tipo_ruta == "larga" else peso
            G.add_edge(orig, dest, weight=peso_usado)

        try:
            ruta = nx.shortest_path(G, source=origen, target=destino, weight="weight")
            distancia = sum(self.pesos[(ruta[i], ruta[i+1])] for i in range(len(ruta)-1))
            
            tipo_texto = "más corta" if tipo_ruta == "corta" else "más larga"
            print(f"\nRuta {tipo_texto} de {origen} a {destino}:")
            print(f"{'→'.join(ruta)}")
            print(f"Tiempo total: {distancia} minutos")
        except nx.NetworkXNoPath:
            print(f"⚠️ No existe ruta entre {origen} y {destino}.")

def menu():
    ruta = Grafo()
    while True:
        print("\nMenú de Gestión de Rutas:")
        print("1. Agregar parada")
        print("2. Agregar conexión")
        print("3. Eliminar parada")
        print("4. Buscar parada")
        print("5. Mostrar rutas")
        print("6. Obtener próxima parada")
        print("7. Visualizar grafo")
        print("8. Encontrar ruta óptima")
        print("9. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            parada = input("Ingrese el nombre de la nueva parada: ")
            if ruta.agregar_parada(parada):
                print(f"\nParada '{parada}' agregada.")
                print("\nAhora conectaremos esta parada con las existentes.")
                for parada_existente in ruta.grafo:
                    if parada_existente != parada:
                        print(f"\nConectando '{parada}' con '{parada_existente}'")
                        while True:
                            try:
                                peso = int(input(f"Ingrese el tiempo en minutos entre {parada} y {parada_existente}: "))
                                ruta.agregar_conexion(parada, parada_existente, peso)
                                break
                            except ValueError:
                                print("Por favor, ingrese un número válido.")
                print("\n Todas las conexiones han sido establecidas.")
            else:
                print(f"⚠️ La parada '{parada}' ya existe.")
        
        elif opcion == "2":
            origen = input("Ingrese la parada de origen: ")
            destino = input("Ingrese la parada de destino: ")
            while True:
                try:
                    peso = int(input("Ingrese el peso de la conexión (tiempo en minutos): "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            ruta.agregar_conexion(origen, destino, peso)
            print(f"Conexión establecida de '{origen}' a '{destino}' con peso {peso}.")
        elif opcion == "3":
            parada = input("Ingrese la parada a eliminar: ")
            ruta.eliminar_parada(parada)
            print(f"Parada '{parada}' eliminada.")
        elif opcion == "4":
            parada = input("Ingrese la parada a buscar: ")
            print(f"Parada {'encontrada' if ruta.buscar_parada(parada) else 'no encontrada'}.")
        elif opcion == "5":
            print("\nRecorrido actual:")
            ruta.mostrar_ruta()
        elif opcion == "6":
            parada = input("Ingrese la parada para ver conexiones: ")
            print(f"Próximas paradas: {', '.join(ruta.obtener_proxima_parada(parada))}")
        elif opcion == "7":
            ruta.visualizar_grafo()
        elif opcion == "8":
            origen = input("Ingrese la parada de origen: ")
            destino = input("Ingrese la parada de destino: ")
            print("\nTipo de ruta:")
            print("1. Ruta más corta")
            print("2. Ruta más larga")
            while True:
                tipo = input("Seleccione el tipo de ruta (1/2): ")
                if tipo in ["1", "2"]:
                    tipo_ruta = "corta" if tipo == "1" else "larga"
                    ruta.encontrar_ruta_optima(origen, destino, tipo_ruta)
                    break
                else:
                    print(" Opción inválida. Ingrese 1 o 2.")
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()