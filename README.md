Simulación de Eventos Discretos – Hoja de Trabajo No. 5
Descripción del Proyecto

Este proyecto consiste en la implementación de una Simulación de Eventos Discretos (DES) utilizando la biblioteca SimPy en Python.

La simulación modela la ejecución de procesos en un sistema operativo de tiempo compartido, donde múltiples procesos compiten por recursos limitados como la memoria RAM y el CPU.

El objetivo principal del trabajo es analizar el comportamiento del sistema bajo diferentes niveles de carga y evaluar estrategias que permitan reducir el tiempo promedio que los procesos permanecen en el sistema.

Modelo del Sistema

El sistema simulado representa el ciclo de vida de un proceso dentro de un sistema operativo, el cual incluye los siguientes estados:

New: El proceso llega al sistema y solicita memoria RAM.

Ready: El proceso espera turno para utilizar el CPU.

Running: El proceso ejecuta instrucciones en el CPU durante un tiempo limitado.

Waiting: El proceso realiza operaciones de entrada/salida.

Terminated: El proceso finaliza su ejecución y libera los recursos utilizados.

Cada proceso solicita una cantidad aleatoria de memoria entre 1 y 10 unidades y tiene un número aleatorio de instrucciones entre 1 y 10. La memoria se modela como un recurso limitado y el CPU como un recurso compartido entre los procesos.

Las llegadas de los procesos siguen una distribución exponencial, lo que permite simular diferentes niveles de carga en el sistema.

Parámetros Evaluados

Durante la simulación se analizaron diferentes configuraciones del sistema:

Cantidades de procesos: 25, 50, 100, 150 y 200.

Intervalos de llegada: 10, 5 y 1.

Capacidad de memoria RAM: 100 y 200 unidades.

Velocidad del CPU: 3 y 6 instrucciones por unidad de tiempo.

Número de procesadores: 1 y 2.

Para cada configuración se calcularon el tiempo promedio que los procesos permanecen en el sistema y la desviación estándar correspondiente.

Experimentos Realizados

Se evaluaron cuatro escenarios principales:

Caso base: RAM de 100 unidades, un procesador y 3 instrucciones por unidad de tiempo.

Incremento de memoria RAM a 200 unidades.

Incremento de la velocidad del procesador a 6 instrucciones por unidad de tiempo.

Uso de dos procesadores manteniendo la configuración original de memoria y velocidad.

Los resultados fueron representados mediante gráficas que muestran la relación entre el número de procesos y el tiempo promedio en el sistema.

Resultados Principales

Bajo condiciones de alta carga (intervalo de llegada igual a 1), se observó que:

Incrementar la memoria RAM no produjo mejoras significativas en el tiempo promedio.

Aumentar la velocidad del procesador redujo considerablemente el tiempo promedio.

Incorporar un segundo procesador fue la estrategia que generó la mayor reducción en el tiempo promedio de permanencia de los procesos.

Estos resultados indican que el principal cuello de botella del sistema es el CPU y no la memoria.

Conclusión

El análisis realizado demuestra que, bajo condiciones de alta carga, la capacidad de procesamiento es el factor determinante en el desempeño del sistema. Aumentar la memoria no mejora significativamente el rendimiento cuando el CPU es el recurso más demandado.

La estrategia más efectiva para reducir el tiempo promedio de ejecución de los procesos es incrementar la cantidad de procesadores, ya que esto reduce la congestión en la cola del CPU y permite una mayor atención simultánea de procesos.

Autor

Kenett Alexander Ortega Cerón
25777