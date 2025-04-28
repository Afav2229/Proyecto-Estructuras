
# ===========================================
# ===========================================
#Universidad Industrial de Santander
#Facultad de Ingenierías Fisicomecánicas
#Escuela de Ingeniería de Sistemas
#Asignatura: Estructuras de datos y  analisis de algoritmos.
#Autor:Andres Felipe Alfonso Viviescas
#Codigo: 2162063
#===========================================
# ==========================================
# Título: Sistema de Transporte Público en el area metropolitana de Bucaramanga basado en listas enlazadas.
#
# Descripción: Este programa simula el recorrido de la ruta de transporte público "Igsabelar" y permite al usuario modificar la ruta si lo desea.
# Funcionamiento del codigo:
# 1. Se crea una lista enlazada simple con las paradas iniciales de la ruta.
# 2. Se simula el recorrido de la ruta eliminando las paradas de la lista enlazada. 
# 3. Se le pregunta al usuario si desea modificar la ruta o continuar con la ruta actual.
# 4. Si el usuario desea modificar la ruta, se le pide que ingrese el número de paradas que desea agregar y el nombre de cada parada.
# 5. Al ingresar el nombre  se debe escribir igual que en la lista de paradas iniciales.
# paradas = ["Uis", "Cra 33", "Cra 27 ", "Real de minas", "Terminal", "Rocio", "Provenza", "Paralela", "Parque Florida", "Limoncito"]
# 6. El usuario puede elegir si desea agregar la parada al inicio, en una posición específica o al final de la lista.
# 7. Se crea una nueva lista enlazada con las paradas completas.
# 8. Se le pregunta al usuario en qué parada está y se le dice cuántas paradas faltan para llegar a la estación final.
# 9. Se imprime la parada actual y las paradas restantes.
# 10. Si la parada ingresada no está en la lista de paradas, se imprime un mensaje de error.
# si el usuario desea devolverse al punto de origen puede elegir la opcion de recorrido de vuelta
#si desea saber en que parada esta en el recorrido de vuelta y cuantas paradas faltan para llegar al punto de origen lo puede hacer
 # usando el metedo de busqueda binaria podemos verificar si el bus realiza paradas en una parada especifica
# ===========================================
# Clase Nodo
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

# Clase Lista Enlazada Simple
class ListaSE:
    def __init__(self):
        self.cabeza = None

    # Lista Vacía
    def vacio(self):
        return self.cabeza is None

    # Agregar al inicio
    def agregarInicio(self, nombre):
        nuevo_nodo = Nodo(nombre)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    # Eliminar al inicio
    def eliminarInicio(self):
        if not self.vacio():
            self.cabeza = self.cabeza.siguiente

    # Mostrar la parada actual y cuántas faltan
    def mostrarRuta(self):
        if self.vacio():
            print("La ruta ha terminado.")
        else:
            actual = self.cabeza
            contador = 0
            while actual is not None:
                contador += 1
                actual = actual.siguiente
            print(f"Parada actual: {self.cabeza.nombre}")
            print(f"Faltan {contador - 1} para llegar a la estación final")

    # Imprimir toda la ruta
    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.nombre, end=" -> ")
            actual = actual.siguiente
        print("Fin")

    # Guardar la ruta en una lista para recorrerla en sentido inverso
    def guardarRuta(self):
        ruta_invertida = []
        actual = self.cabeza
        while actual is not None:
            ruta_invertida.append(actual.nombre)
            actual = actual.siguiente
        return ruta_invertida


# Crear la lista con las  paradas iniciales
ruta = ListaSE()
paradas = ["Uis", "Cra 33", "Cra 27 ", "Real de minas", "Terminal", "Rocio", "Provenza", "Paralela", "Parque Florida", "Limoncito"]
print("\n Este es su recorrido inicial: \n")
for parada in reversed(paradas):
    ruta.agregarInicio(parada)
    print("-", parada)

# Función para simular el recorrido
def recorrerRuta(ruta):
    
    while not ruta.vacio():
    #   ruta.mostrarRuta()
        ruta.eliminarInicio()

def recorrerRutaVuelta(ruta):
    print("\nRecorrido de vuelta:\n")
    ruta_original = ruta.guardarRuta()  # Obtener la lista original de paradas
    ruta_invertida = list(reversed(ruta_original))  # Invertir para representar el recorrido de vuelta

    # Mostrar las paradas desde "Uis" hasta "Limoncito"
    for nombre in ruta_original:
        print(f"- {nombre}")  # Aquí mostramos el orden de ida, que también se usa para el recorrido de vuelta.

    # Pedir al usuario la parada actual
    parada_actual_vuelta = input("\nIngrese la parada en la que se encuentra durante el recorrido de vuelta: ").strip()

    if parada_actual_vuelta in ruta_original:  # Siempre usamos el orden original
        indice_actual_vuelta = ruta_original.index(parada_actual_vuelta)
        
        # Verificar si es la última parada ("Limoncito")
        if indice_actual_vuelta == len(ruta_original) - 1:  # Última parada
            print(f"Usted está en la parada '{parada_actual_vuelta}'.")
            print("No le faltan más paradas, ha llegado a su destino final.\n")
        else:
            # Calcular las paradas restantes desde la parada actual hasta el final
            paradas_restantes_vuelta = ruta_original[indice_actual_vuelta + 1:]
            print(f"\nUsted está en la parada '{parada_actual_vuelta}'.")
            if len(paradas_restantes_vuelta) > 0:
                print(f"Le faltan {len(paradas_restantes_vuelta)} paradas para llegar a la estación final (Limoncito).\n")
                print("Las paradas restantes son:")
                for parada in paradas_restantes_vuelta:
                    print("  -", parada)
    else:
        print("La parada ingresada no se encuentra en la lista de paradas.")


2

# El usuario decide si desea modificar la ruta o continuar con la ruta actual
opcion = int(input("\n Si desea modificar la ruta presione 1, si desea continuar con la ruta actual presione 2: "))  

if opcion == 1:
    recorrerRuta(ruta)
    n = int(input("\n Ingrese el número de paradas que desea añadir: ")) #Pide la usuario el número de paradas que desea añadir
   
    for i in range(n):
        parada = input(f"Ingrese el nombre de la parada que desea agregar: ")
        ubicacion = input("Si desea agregar la parada al inicio presione 1, si desea agregar parada en una posición específica presione 2, si desea agregar parada al final presione 3:\n")
        if ubicacion.lower() == "3":
            paradas.insert(1, parada)  # Insertar cada nueva parada al inicio de la lista
        elif ubicacion == "2":
            posicion = int(input(f"Ingrese la posición (0 a {len(paradas)}): "))
            if 0 <= posicion <= len(paradas):
                paradas.insert(posicion, parada)  # Insertar en la posición específica
        else:
             paradas.append(parada)  # Insertar cada nueva parada al final de la lista

# Imprimir el vector de paradas completo después de añadir las nuevas paradas
    print("Este será su nuevo recorrido : \n")
    for parada in reversed(paradas):
        print("-", parada)

# Crear una nueva lista enlazada con las paradas completas
    nueva_ruta = ListaSE()
    for nueva_parada in paradas:
        nueva_ruta.agregarInicio(nueva_parada)  # Agregar cada nueva parada a la lista enlazada
else:
    print("Se ha continuado con la ruta actual")
    nueva_ruta = ruta


# Preguntar al usuario en qué parada está y cuántas paradas faltan para llegar a la estación final
paradas_invertidas = list(reversed(paradas))
parada_actual = input("\nIngrese la parada en la que se encuentra: ")

if parada_actual in paradas_invertidas:
    indice_actual = paradas_invertidas.index(parada_actual)
    if paradas_invertidas[indice_actual] == "Uis":  # Corrección aquí
        print(f" Usted está en la parada \n '{parada_actual}'.")
        print("No le faltan más paradas, ha llegado a su destino final.\n")
    else:
        paradas_restantes = paradas_invertidas[indice_actual + 1:]
        
        print(f"\nUsted está en la parada '{parada_actual}'.")
        print(f"Le faltan {len(paradas_restantes)} paradas para llegar a la estación (Uis).\n")
        print("Las paradas restantes son:")
        for parada in paradas_restantes:
            print("  -", parada)
else:
    print("La parada ingresada no se encuentra en la lista de paradas.")





# Preguntar al usuario si desea hacer el recorrido de vuelta
opcion_vuelta = int(input("\n¿Desea hacer el recorrido de vuelta? Presione 1 para sí, 2 para no: "))  
if opcion_vuelta == 1:
    recorrerRutaVuelta(nueva_ruta)
else:
    print("Fin del recorrido.")

def buscar_en_lista_ordenada(lista_enlazada, objetivo):
    # Obtener los elementos en la lista enlazada
    elementos = lista_enlazada.guardarRuta()
    
    # Ordenar la lista de elementos
    elementos.sort()  # Esto organiza la lista alfabéticamente
    
    # Realizar búsqueda binaria
    inicio = 0
    fin = len(elementos) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if elementos[medio] == objetivo:
            return f"El elemento '{objetivo}' está en la lista ordenada."
        elif elementos[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    return f"El elemento '{objetivo}' no está en la lista."

# Ejemplo de uso con tu clase ListaSE
print("\nBuscando elemento en la ruta ordenada:\n")
elemento_a_buscar = input("Ingrese el nombre de la parada que desea buscar: ")
resultado = buscar_en_lista_ordenada(ruta, elemento_a_buscar)
print(resultado)