import simpy
import random
import statistics
import matplotlib.pyplot as plt
import os

RANDOM_SEED = 42
PROCESOS = [25, 50, 100, 150, 200]
INTERVALOS = [10, 5, 1]

def proceso(env, name, ram, cpu, tiempos, instrucciones_por_ciclo):
    llegada = env.now
    
    memoria_necesaria = random.randint(1, 10)
    instrucciones = random.randint(1, 10)
    
    # Solicitar RAM
    yield ram.get(memoria_necesaria)
    
    while instrucciones > 0:
        with cpu.request() as req:
            yield req
            yield env.timeout(1)
            
            instrucciones -= instrucciones_por_ciclo
            
            if instrucciones <= 0:
                break
            
            decision = random.randint(1, 21)
            if decision == 1:
                yield env.timeout(1)  # Tiempo de I/O
    
    # Liberar RAM
    yield ram.put(memoria_necesaria)
    
    salida = env.now
    tiempos.append(salida - llegada)

def generador_procesos(env, num_procesos, ram, cpu, tiempos, intervalo, instrucciones_por_ciclo):
    for i in range(num_procesos):
        yield env.timeout(random.expovariate(1.0 / intervalo))
        env.process(proceso(env, f"P{i}", ram, cpu, tiempos, instrucciones_por_ciclo))

def correr_simulacion(num_procesos, intervalo, ram_capacidad, cpu_capacidad, instrucciones_por_ciclo):
    random.seed(RANDOM_SEED)
    env = simpy.Environment()
    
    ram = simpy.Container(env, init=ram_capacidad, capacity=ram_capacidad)
    cpu = simpy.Resource(env, capacity=cpu_capacidad)
    
    tiempos = []
    
    env.process(generador_procesos(env, num_procesos, ram, cpu, tiempos, intervalo, instrucciones_por_ciclo))
    env.run()
    
    promedio = statistics.mean(tiempos)
    desviacion = statistics.stdev(tiempos) if len(tiempos) > 1 else 0
    
    return promedio, desviacion

def experimento(nombre_archivo, titulo, ram_capacidad, cpu_capacidad, instrucciones_por_ciclo):
    print(f"\n===== {titulo} =====")
    
    plt.figure()
    
    for intervalo in INTERVALOS:
        promedios = []
        
        for n in PROCESOS:
            promedio, desviacion = correr_simulacion(
                num_procesos=n,
                intervalo=intervalo,
                ram_capacidad=ram_capacidad,
                cpu_capacidad=cpu_capacidad,
                instrucciones_por_ciclo=instrucciones_por_ciclo
            )
            
            print(f"Procesos: {n}, Intervalo: {intervalo}")
            print(f"Promedio: {promedio:.2f}, Desviación: {desviacion:.2f}")
            print("----------------------------------")
            
            promedios.append(promedio)
        
        plt.plot(PROCESOS, promedios, marker='o', label=f"Intervalo {intervalo}")
    
    plt.xlabel("Número de procesos")
    plt.ylabel("Tiempo promedio en el sistema")
    plt.title(titulo)
    plt.legend()
    plt.grid()
    
    # Guardar gráfica
    plt.savefig(f"graficas/{nombre_archivo}.png")
    plt.close()

# ----------------------------
# Crear carpeta de gráficas
# ----------------------------
if not os.path.exists("graficas"):
    os.makedirs("graficas")

# ----------------------------
# Ejecutar experimentos
# ----------------------------

# Caso base
experimento(
    nombre_archivo="caso_base",
    titulo="Caso Base (RAM=100, 1 CPU, 3 instrucciones)",
    ram_capacidad=100,
    cpu_capacidad=1,
    instrucciones_por_ciclo=3
)

# RAM = 200
experimento(
    nombre_archivo="ram_200",
    titulo="RAM = 200",
    ram_capacidad=200,
    cpu_capacidad=1,
    instrucciones_por_ciclo=3
)

# CPU más rápido
experimento(
    nombre_archivo="cpu_rapido",
    titulo="CPU más rápido (6 instrucciones)",
    ram_capacidad=100,
    cpu_capacidad=1,
    instrucciones_por_ciclo=6
)

# Dos CPUs
experimento(
    nombre_archivo="dos_cpus",
    titulo="2 CPUs",
    ram_capacidad=100,
    cpu_capacidad=2,
    instrucciones_por_ciclo=3
)

print("\nSimulación finalizada. Las gráficas fueron guardadas en la carpeta 'graficas'.")