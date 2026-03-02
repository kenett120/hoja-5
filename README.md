# Simulación de Eventos Discretos – Hoja de Trabajo No. 5

## Descripción del Proyecto

Este proyecto implementa una **Simulación de Eventos Discretos (DES)** utilizando la biblioteca **SimPy** en Python.

La simulación modela la ejecución de procesos en un sistema operativo de tiempo compartido, donde múltiples procesos compiten por recursos limitados como la **memoria RAM** y el **CPU**.

El objetivo principal es analizar el comportamiento del sistema bajo distintos niveles de carga y evaluar estrategias que permitan reducir el **tiempo promedio** que los procesos permanecen en el sistema.


## Modelo del Sistema

El sistema simulado representa el ciclo de vida de un proceso dentro de un sistema operativo:

- **New:** El proceso llega al sistema y solicita memoria RAM.
- **Ready:** El proceso espera turno para utilizar el CPU.
- **Running:** El proceso ejecuta instrucciones durante un tiempo limitado.
- **Waiting:** El proceso realiza operaciones de entrada/salida (I/O).
- **Terminated:** El proceso finaliza y libera los recursos utilizados.

Cada proceso:

- Solicita entre **1 y 10 unidades de memoria**.
- Tiene entre **1 y 10 instrucciones**.
- Es atendido por el CPU que ejecuta **3 instrucciones por unidad de tiempo** (configurable).

Las llegadas de los procesos siguen una **distribución exponencial**, lo que permite simular diferentes niveles de carga en el sistema.


## Parámetros Evaluados

Durante la simulación se analizaron distintas configuraciones:

- **Cantidad de procesos:** 25, 50, 100, 150 y 200.
- **Intervalos de llegada:** 10, 5 y 1.
- **Memoria RAM:** 100 y 200 unidades.
- **Velocidad del CPU:** 3 y 6 instrucciones por unidad de tiempo.
- **Número de procesadores:** 1 y 2.

Para cada configuración se calcularon:

- **Tiempo promedio en el sistema**
- **Desviación estándar**


## Experimentos Realizados

### **1. Caso Base**
- RAM = 100  
- 1 CPU  
- 3 instrucciones por unidad de tiempo  

### **2. Incremento de Memoria**
- RAM = 200  
- 1 CPU  
- 3 instrucciones por unidad de tiempo  

### **3. CPU Más Rápido**
- RAM = 100  
- 1 CPU  
- 6 instrucciones por unidad de tiempo  

### **4. Dos Procesadores**
- RAM = 100  
- 2 CPUs  
- 3 instrucciones por unidad de tiempo  

Los resultados fueron representados mediante gráficas que muestran la relación entre el **número de procesos** y el **tiempo promedio en el sistema**.


## Resultados Principales

Bajo condiciones de **alta carga (intervalo = 1)** se observó que:

- Incrementar la **memoria RAM** no produjo mejoras significativas.
- Aumentar la **velocidad del CPU** redujo considerablemente el tiempo promedio.
- Incorporar **dos procesadores** fue la estrategia que generó la mayor reducción del tiempo promedio.

Esto indica que el principal **cuello de botella** del sistema es el **CPU** y no la memoria.


## Conclusión

El análisis demuestra que, bajo condiciones de alta carga, la capacidad de procesamiento es el factor determinante en el desempeño del sistema.

La estrategia más efectiva para reducir el tiempo promedio de ejecución de los procesos es **incrementar la cantidad de procesadores**, ya que esto reduce la congestión en la cola del CPU y permite mayor atención simultánea de procesos.


## Autor

Kenett Alexander Ortega Cerón
25777