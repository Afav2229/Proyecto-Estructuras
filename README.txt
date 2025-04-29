Contexto del Problema: Incentivar el Turismo en Santander
El turismo es una de las actividades económicas y culturales más importantes en cualquier región.
En el caso de Santander, Colombia, se busca promover la riqueza natural, histórica y cultural que ofrece el departamento, para atraer más visitantes y fortalecer la economía local. Sin embargo, uno de los desafíos actuales es la organización de la información turística y la facilidad con la que los turistas pueden acceder a rutas, destinos y sitios de interés.
¿Cuál es el problema que enfrentan los turistas?
- Falta de información centralizada. Muchos turistas no saben qué sitios visitar, cómo llegar a ellos, o cuál es la mejor ruta desde su ubicación actual.
- Dificultad para planificar recorridos. Sin una estructura clara, los visitantes pueden perder tiempo en la planificación, generando frustración y afectando su experiencia.
- Conectividad entre destinos turísticos. Santander cuenta con zonas urbanas y naturales que requieren desplazamientos organizados, pero la información sobre estos trayectos no siempre es accesible.
- Fomento del turismo sostenible. Se busca que los viajeros puedan explorar diversos destinos sin afectar la riqueza ambiental y cultural del departamento.

Objetivo del Proyecto
Este sistema turístico digital está diseñado para organizar rutas turísticas de Santander en un modelo de árbol, permitiendo:
- Explorar municipios y rutas de manera interactiva.
- Facilitar la navegación hacia sitios turísticos según categorías.
- Agilizar la búsqueda de destinos mediante herramientas automatizadas.
- Permitir agregar y actualizar sitios turísticos, adaptando la información según necesidades.

Al utilizar estructuras de datos avanzadas, como un árbol jerárquico, el sistema proporciona una representación clara de los diferentes municipios, rutas y sitios turísticos. Esto hace que la información sea más accesible y eficiente para los turistas, incentivando la visita y promoviendo el turismo interno y externo.
Beneficios del Sistema
- Turismo guiado. Los visitantes pueden acceder a información organizada sobre cada destino sin necesidad de depender de múltiples fuentes.
- Desarrollo económico. Promueve la inversión en el turismo local, aumentando la afluencia de visitantes.
- Mayor conectividad entre sitios. Se facilita la planificación de recorridos, haciendo que los turistas puedan optimizar su tiempo y disfrutar más lugares en una sola visita.
- Adaptabilidad y expansión. Se pueden agregar nuevos lugares turísticos, permitiendo la actualización constante del sistema.

Tecnologías y herramientas utilizadas
Para construir este sistema digital, se hace uso de herramientas especializadas:
- Librería bigtree. Permite estructurar información en forma de árbol, facilitando la organización de destinos turísticos y rutas.
- Librería unicodedata. Se encarga de procesar nombres de sitios sin importar mayúsculas, minúsculas o tildes, asegurando búsquedas más flexibles.
- Menú interactivo. Los usuarios pueden explorar, agregar o eliminar sitios, mejorando la personalización de la experiencia turística.

Manual de Uso - Sistema de Rutas Turísticas de Santander
Este sistema permite explorar rutas turísticas en Santander, organizar sitios turísticos y facilitar la planificación de recorridos. Se maneja a través de un menú interactivo, donde el usuario puede navegar por el árbol de rutas, buscar destinos y modificar la estructura agregando o eliminando sitios.
Cómo Usarlo
- Abrir el programa- Ejecuta el script en Python.
- Aparecerá el menú interactivo con opciones para gestionar las rutas.

- Opciones del menú. Mostrar rutas turísticas de Santander- Muestra la estructura completa del árbol, incluyendo municipios, rutas y sitios turísticos.
2. Imprimir ruta desde un sitio turístico- Introduce el nombre de un sitio turístico y el programa imprimirá la ruta desde la raíz hasta el destino.
- También se mostrará cuántas paradas o nodos son necesarios para llegar.
3. Agregar un sitio turístico- Permite agregar un nuevo sitio bajo un nodo existente.
- Ingresa el nombre del nuevo sitio y el nombre del nodo padre donde debe agregarse.
4. Eliminar un sitio turístico- Elimina un nodo específico pero sus hijos no desaparecen. En su lugar, se transfieren al nodo padre del nodo eliminado.
- Ingresa el nombre del nodo a eliminar.
5. Salir- Cierra el programa.


Características Adicionales
✅ Búsqueda flexible: No importa si el usuario ingresa el nombre con mayúsculas, minúsculas o sin tildes.
✅ Gestión de rutas: Se pueden modificar los sitios turísticos para actualizar la información.
✅ Interfaz simple e interactiva: Fácil de usar sin necesidad de conocimientos avanzados.


Una funcionalidad que podría mejorar el software anterior es la optimización y planificación de rutas utilizando árboles de búsqueda. Esto permitiría al usuario encontrar la ruta más corta entre dos paradas o destinos, teniendo en cuenta las conexiones dentro del sistema de transporte.
Mejora con Árboles de Búsqueda
La implementación de un árbol de búsqueda en el sistema de rutas turísticas de Santander podría mejorar significativamente la experiencia del usuario. Actualmente, el software utiliza listas enlazadas, lo que permite recorrer las rutas de manera secuencial. Sin embargo, si se implementara un árbol de búsqueda (como un Árbol Binario de Búsqueda o un Árbol Trie), se podrían lograr varias mejoras:

Actualmente, el software usa listas enlazadas, lo que permite recorrer las rutas de manera secuencial. Sin embargo, si se usa un árbol de búsqueda (como un Árbol Binario de Búsqueda o un Árbol Trie), se podría:
✅ Buscar rutas más rápido: En lugar de recorrer toda la lista, el usuario podría ingresar una parada y obtener directamente el camino óptimo.
✅ Optimizar recorridos: El sistema podría calcular cuál es la mejor combinación de paradas para llegar a un destino específico con menos transbordos.
✅ Facilitar cambios en la estructura de la ru  ta: Se podrían agregar rutas alternativas sin afectar la estructura global del sistema.
