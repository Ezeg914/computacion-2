# Funcionamiento general

El programa lanza tres rutinas diferentes, las cuales encadena para inicializar una por una. Cada rutina va a ser asignada una 2 tareas, cada rutina demorará X tiempo en cada tarea. Cada rutina hará sus tarea paralelamente usando asincronismo.

# Explicacion

El programa crea una lista, luego empieza a contar el tiempo con un contador y lanza la funcion main de manera asincrona.

El main se crea un 'event loop' y frabrica un generador de llamadas ecorrutinas las cual mete dentro del even loop, se lanza la funcion chain con la primer rutina. Esta queda durmiendo y corre la funcion 'primera'.

en la funcion primera se establece una variable con un random
y imprime el numero de la ecorrutina y el tiempo de la variable random
esta duerme la tarea en segundo hasta que pasen los segundos y en ese tiempo el event loop toma el control volviendo a la funcion main y se fija cual es la siguiente tarea disponible para ejecutar en el chain.

cuando el tiempo de la funcion primera termina devolvera un resultado y seguira con la segunda tarea, en la cual espera a que termine la 'segunda'

dentro de la segunda tambien se establese una variable con un numero random, imprime el numero de la rutina y el tiempo del la variable random
esta tarea queda dormida en segundo plano hasta que se termine el tiempo. mientras eso sucede el elvet loop vuelve a tomar el control.

al terminar el tiempo la funcion segunda devolvera un resulado a la funcion 'chain' y esta restara el tiempo de inicio con el tiempo final y mostrara los resultados encadenados con el tiempo total de la ejecucion.