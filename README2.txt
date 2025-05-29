# Sistema de Optimización de Rutas del Área Metropolitana de Bucaramanga

## Descripción del Problema
El área metropolitana de Bucaramanga necesita un sistema eficiente para gestionar y optimizar las rutas de transporte público ya que hoy en dia no es posible poder encontrar un sistema publico el cual permita a los usuarios llegar de manera mas rapida a sus destinos. Este proyecto implementa una solución que permite:
- Visualizar las rutas existentes
- Encontrar caminos óptimos entre paradas
- Gestionar dinámicamente la red de transporte

## Etapas Desarrolladas

### 1. Sistema Base con Listas Enlazadas
- Implementación de una estructura básica para almacenar paradas
- Gestión de recorridos usando listas enlazadas simples
- Funcionalidades básicas de agregar/eliminar paradas
[`avanceProyecto_eYa.py`](Proyecto-Estructuras/avanceProyecto_eYa.py)

### 2. Implementación con Árboles
- Organización jerárquica de rutas turísticas
- Búsqueda eficiente de destinos
- Gestión de rutas alternativas
[`Parte2_proyecto_arboles.py`](Proyecto-Estructuras/Parte2_proyecto_arboles.py)

### 3. Optimización con Grafos
- Representación de la red mediante grafos
- Algoritmos de búsqueda de rutas óptimas
- Visualización interactiva del sistema
[`Proyecto3.py`](Proyecto-Estructuras/Proyecto3.py)

## Características Principales
-  Gestión dinámica de paradas y conexiones
-  Visualización gráfica de la red de transporte
-  Búsqueda de rutas óptimas (más cortas/más largas)
-  Persistencia de datos en formato JSON
- Actualizaciones en tiempo real

## Tecnologías Utilizadas
- Python 3.x
- NetworkX para manejo de grafos
- Matplotlib para visualización
- JSON para almacenamiento persistente

## Estructura del Proyecto
```
Proyecto-Estructuras/
├── avanceProyecto_eYa.py    # Implementación con listas enlazadas
├── Parte2_proyecto_arboles.py # Implementación con árboles
├── Proyecto3.py              # Implementación final con grafos
├── grafo.json               # Almacenamiento de datos
└── README.txt               # Documentación del proyecto
```

## Equipo de Desarrollo
- **Autor**: Andres Felipe Alfonso Viviescas
- **Código**: 2162063
- **Universidad**: Universidad Industrial de Santander
- **Facultad**: Ingenierías Fisicomecánicas
- **Escuela**: Ingeniería de Sistemas
- **Asignatura**: Estructuras de datos y análisis de algoritmos

## Cómo Ejecutar
1. Asegúrese de tener Python 3.x instalado
2. Instale las dependencias:
```bash
pip install networkx matplotlib
```
3. Ejecute el programa principal:
```bash
python Proyecto3.py
```

## Manual de Usuario
El sistema ofrece un menú interactivo con las siguientes opciones:
1. Agregar parada
2. Agregar conexión
3. Eliminar parada
4. Buscar parada
5. Mostrar rutas
6. Obtener próxima parada
7. Visualizar grafo
8. Encontrar ruta óptima
9. Salir

## Funcionalidades Adicionales
- Agregar/Eliminar paradas
- Conectar paradas secuencialmente 
- Buscar paradas en la ruta
- Validación de datos básica

Mejoras Implementadas en Cada Etapa
Etapa 1 → Etapa 2
De estructura lineal a jerárquica
Mejora en eficiencia de búsqueda
Implementación de recorridos alternativos
Etapa 2 → Etapa 3
De árbol a grafo completo
Implementación de pesos en conexiones
Visualización interactiva
Sistema de rutas óptimas
Resultados Finales
Sistema robusto y escalable
Interfaz de usuario intuitiva
Optimización efectiva de rutas
Visualización clara de la red
Manejo eficiente de datos
Este desarrollo iterativo permitió mejorar progresivamente el sistema, incorporando nuevas funcionalidades y optimizando el rendimiento en cada etapa.