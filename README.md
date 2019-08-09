# Prueba tecnica Frubana - Steven Bustos

## Problemas
Para el desarrollo de los problemas se uso Python 2.7

### Problema 1:
Mi propuesta para solucionar este problema es tener dos listas ordenadas, partiendo por mitad la lista de numeros del input, la lista *limin* contiene los numeros abajo de la mitad *n/2* y la lista *limax* contiene los numeros arriba de *n/2*.

Como no se puede asegurar que al añadir o quitar un numero se mantenga la regla de las listas, agregue un *fix* a este problema en el que:
* Si el tamaño de *limax* es mayor a *limin* se saque el primer item de *limax* y se inserte en *limin*
* Si el tamaño de *limin* es mayor al de *limax + 1*, se extrae de *limin* el ultimo numero y se inserta a *limax*.

Al tener dos listas de esta forma, solo hay que mirar el primer numero de *limax* y el ultimo numero de *limin* para calcular la media:
* Si el tamaño de *limin* es mayor a *limax*, la **media** es el ultimo numero de *limin*
* Si el tamaño de *limax* es mayor al de *limin*, la **media** es el primer numero de *limax*
* Si los tamaños de *limin* y *limax* son iguales, y son 1 (solo existe un elemento en cada lista), la **media** es la suma de los dos elementos de la lista divida por 2.
* Si los tamaños de *limin* y *limax* son iguales y mayores que 1, la **media** es la suma del __ultimo numero de *limin*__ y del __primer numero de *limax*__

### Problema 2:
Para este problema use dos métodos que aprendi en la materia de [algoritmos de la universidad](https://nbviewer.jupyter.org/gist/fabgoos/10306113).

Primero se construye el grafo usando el metodo *make_link*, tengo ademas un diccionario con los "colores" de cada nodo del grafo, este se usa despues para calcular el numero de colores que hay de un nodo a otro.

Despues con este grafo uso el metodo *path* para calcular el camino de un nodo a otro, este a su vez usa el metodo *DFS_Visit_p*; El metodo *path* devuelte en una lista el camino del nodo *v1* al nodo *v2*, con un cambio al codigo y pasando el diccionario de los colores de los nodos la lista retorna en vez de los nodos del camino los colores de cada uno de esos nodos.

En otro metodo calculo el resultado de la sumatoria de los colores diferentes del camino del nodo v1 al v2, iterando sobre todos los nodos del grafo.

## Preguntas adicionales:
* Cuales serian las cualidades para un código limpio?
  - Facilidad para ser leido: Esto facilita el trabajo en equipo y si alguien mas va a mantener el codigo no sea tedioso.
  - Eficiente: Debe hacer lo que debe de manera rapida.
  - Simple: Debe ser minimo, escrito en pocas lineas y que haga lo que se necesita y no mas.
  - Robusto: Debe estar escrito siguiendo buenas practicas de desarrollo.
  - Documentado: Para facilitar la mantenibilidad del codigo.
  - No ser redundante

* Cuales serian los estándares según tú para un buen proyecto?
  - Estar bien planeado: El levantamiento de requerimientos debe ser minucioso, la decision de que herramientas se deben usar dependiendo los requerimientos tambien es importante.
  - Documentacion: Debe estar bien documentado para que sea facil de mantener.
  - Pruebas: Cada funcion y nueva funcionalidad debe ser probada antes de ser desplegada.
  -Escalable: Se debe poder escalar el proyecto dependiendo nuevos requerimientos o implementacion de nuevas tecnologias.

* Qué patrones conoce? y utiliza?
  * Conozco los patrones de diseño:
     - Singleton
     - Prototype
     - Decorator
     - Observer
  * No uso ninguno.


