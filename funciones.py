"""
Módulo: funciones.py
Descripción: Contiene el desarrollo lógico del sistema de monitoreo de
             consumo energético para pequeños comercios.
Restricciones respetadas:
- No usa librerías externas ni módulos estadísticos.
- Promedios y máximos se calculan manualmente mediante ciclos y acumuladores.
- No utiliza sum(), max(), min() ni sorted().
"""

def registrar_comercios():
    """
    1. registrar_comercios():
    Solicita la cantidad de comercios a registrar.
    Itera con un ciclo for para capturar la información de cada uno:
    - NIT, nombre, tipo, empleado, meta_semanal y consumos (inicializado como lista vacía).
    Almacena los diccionarios en una lista y la retorna.
    """
    comercios = []  # Lista creada fuera del ciclo para almacenar todos los comercios
    
    print("\n--- REGISTRO DE COMERCIOS ---")
    # Validación para asegurar que la cantidad ingresada sea un número entero positivo
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de comercios a registrar: "))
            if cantidad > 0:
                break
            else:
                print("[Error] Ingrese un número mayor a 0.")
        except ValueError:
            print("[Error] Debe ingresar un número entero válido.")

    # Ciclo for según el número de iteraciones solicitado
    for i in range(cantidad):
        print(f"\n>> Ingrese los datos del comercio #{i + 1}:")
        nit = input("  NIT: ").strip()
        nombre = input("  Nombre comercial: ").strip()
        tipo = input("  Tipo (ej. Tienda, Restaurante, Peluquería): ").strip()
        
        # Validación de cantidad de empleados (entero >= 0)
        while True:
            try:
                empleado = int(input("  Cantidad de empleados: "))
                if empleado >= 0:
                    break
                else:
                    print("  [Error] Los empleados no pueden ser un valor negativo.")
            except ValueError:
                print("  [Error] Ingrese un número entero válido.")

        # Validación de la meta semanal en kWh (> 0)
        while True:
            try:
                meta_semanal = float(input("  Meta semanal de consumo (kWh): "))
                if meta_semanal > 0:
                    break
                else:
                    print("  [Error] La meta debe ser mayor a 0 kWh.")
            except ValueError:
                print("  [Error] Ingrese un valor numérico válido.")

        # Diccionario con las claves requeridas
        comercio = {
            "NIT": nit,
            "nombre": nombre,
            "tipo": tipo,
            "empleado": empleado,
            "meta_semanal": meta_semanal,
            "consumos": []  # Inicializado como lista vacía para almacenar las mediciones
        }
        
        # Agregar el diccionario a la lista de comercios
        comercios.append(comercio)

    return comercios


def registrar_consumo(comercios):
    """
    2. registrar_consumo(comercios):
    Recorre la lista de comercios con un ciclo for.
    Por cada comercio, solicita exactamente 4 consumos semanales (validando que sean > 0 kWh).
    Actualiza la clave 'consumos' en el diccionario de cada comercio.
    Retorna la lista de comercios actualizada.
    """
    print("\n--- REGISTRO DE CONSUMOS SEMANALES (4 SEMANAS) ---")
    
    # Recorrer cada comercio registrado
    for comercio in comercios:
        print(f"\n>> Registrando consumos para '{comercio['nombre']}' (NIT: {comercio['NIT']}):")
        consumos_comercio = []
        
        # Se solicitan exactamente 4 datos semanales
        for semana in range(1, 5):
            while True:
                try:
                    consumo = float(input(f"  - Ingrese consumo de la Semana {semana} (kWh): "))
                    if consumo > 0:
                        consumos_comercio.append(consumo)
                        break
                    else:
                        print("    [Error] El consumo debe ser mayor a 0 kWh.")
                except ValueError:
                    print("    [Error] Ingrese un número válido.")
        
        # Actualización de la clave 'consumos' del diccionario respectivo
        comercio["consumos"] = consumos_comercio

    return comercios

# Alias por compatibilidad con el enunciado del README (registrar_consumos)
registrar_consumos = registrar_consumo


def calcular_promedio(consumo):
    """
    3. calcular_promedio(consumo):
    Recibe la lista de 4 consumos de un comercio.
    Usa una variable acumuladora suma = 0 y un ciclo for para recorrer los consumos.
    Divide la suma entre 4 para calcular y retornar el promedio (sin usar sum()).
    """
    suma = 0.0  # Variable acumuladora
    
    # Ciclo for sumando cada valor a la variable acumuladora
    for valor in consumo:
        suma += valor
        
    # División de la suma acumulada entre las 4 mediciones
    promedio = suma / 4.0
    return promedio


def calcular_variacion(consumo):
    """
    4. calcular_variacion(consumo):
    Recibe la lista de 4 consumos.
    Calcula la diferencia restando el último consumo (posición 3) menos el primero (posición 0).
    Divide esa sustracción entre el primer consumo (posición 0) y multiplica por 100.
    Retorna el porcentaje de variación.
    Fórmula: ((semana4 - semana1) / semana1) * 100
    """
    # Sustracción entre el último consumo (índice 3) y el primer consumo (índice 0)
    diferencia = consumo[3] - consumo[0]
    primer_consumo = consumo[0]
    
    # Cálculo porcentual de la variación
    if primer_consumo != 0:
        variacion_porcentual = (diferencia / primer_consumo) * 100.0
    else:
        variacion_porcentual = 0.0
        
    return variacion_porcentual


def clasificar_consumo(promedio, meta, variacion):
    """
    5. clasificar_consumo(promedio, meta, variacion):
    Recibe el promedio, la meta semanal y la variación porcentual.
    Evalúa múltiples condiciones y retorna un string con la clasificación:
    - "Eficiente": si el promedio <= meta y la variación es favorable (<= 5%).
    - "En Observación": si el promedio <= meta pero la variación es de alerta (> 5%).
    - "Alto": si el promedio > meta hasta por un 20% (promedio <= meta * 1.20).
    - "Crítico": si el promedio supera la meta en más del 20% (promedio > meta * 1.20).
    """
    if promedio <= meta:
        if variacion <= 5.0:
            return "Eficiente"
        else:
            return "En Observación"
    else:
        # El promedio supera la meta
        if promedio <= meta * 1.20:
            return "Alto"
        else:
            return "Crítico"


def generar_informe(comercios):
    """
    6. generar_informe(comercios):
    Recibe la lista de comercios.
    Usa un ciclo for para recorrerla.
    Dentro del ciclo llama a:
      - calcular_promedio()
      - calcular_variacion()
      - clasificar_consumo()
    Compara y encuentra manualmente el comercio con mayor promedio (sin usar max()).
    Contabiliza comercios por clasificación.
    Fuera del ciclo, imprime un informe detallado con:
      - Nombre, promedio, variación y clasificación de cada comercio.
      - Cantidad de comercios en cada categoría.
      - Datos completos del comercio que tuvo el mayor promedio.
    """
    print("\n" + "=" * 80)
    print("                 INFORME DE CONSUMO ENERGÉTICO EN COMERCIOS                 ")
    print("=" * 80)

    # Variables para encontrar manualmente el comercio con mayor promedio
    mayor_promedio = None
    comercio_con_mayor_promedio = None
    datos_comercio_mayor = {}

    # Contadores manuales por clasificación
    conteo_eficiente = 0
    conteo_observacion = 0
    conteo_alto = 0
    conteo_critico = 0

    # Lista para almacenar los resultados procesados de cada comercio
    resultados = []

    # Recorrido con ciclo for para procesar cada comercio
    for comercio in comercios:
        promedio = calcular_promedio(comercio["consumos"])
        variacion = calcular_variacion(comercio["consumos"])
        clasificacion = clasificar_consumo(promedio, comercio["meta_semanal"], variacion)

        # Actualización de contadores según la clasificación
        if clasificacion == "Eficiente":
            conteo_eficiente += 1
        elif clasificacion == "En Observación":
            conteo_observacion += 1
        elif clasificacion == "Alto":
            conteo_alto += 1
        elif clasificacion == "Crítico":
            conteo_critico += 1

        # Comparación manual para determinar el mayor promedio de consumo (sin usar max())
        if mayor_promedio is None or promedio > mayor_promedio:
            mayor_promedio = promedio
            comercio_con_mayor_promedio = comercio
            datos_comercio_mayor = {
                "nombre": comercio["nombre"],
                "nit": comercio["NIT"],
                "tipo": comercio["tipo"],
                "meta": comercio["meta_semanal"],
                "promedio": promedio,
                "variacion": variacion,
                "clasificacion": clasificacion
            }

        # Guardamos la fila calculada para la impresión
        resultados.append({
            "nombre": comercio["nombre"],
            "promedio": promedio,
            "variacion": variacion,
            "clasificacion": clasificacion
        })

    # Imprimir en consola el informe detallado por cada comercio
    print(f"{'Nombre del Comercio':<25} | {'Promedio (kWh)':<15} | {'Variación (%)':<15} | {'Clasificación':<15}")
    print("-" * 80)
    for res in resultados:
        print(f"{res['nombre']:<25} | {res['promedio']:<15.2f} | {res['variacion']:>12.2f}% | {res['clasificacion']:<15}")

    print("=" * 80)

    # Imprimir el conteo por clasificación
    print("\n--- RESUMEN POR CATEGORÍAS ---")
    print(f"  * Eficiente:      {conteo_eficiente} comercio(s)")
    print(f"  * En Observación: {conteo_observacion} comercio(s)")
    print(f"  * Alto:           {conteo_alto} comercio(s)")
    print(f"  * Crítico:        {conteo_critico} comercio(s)")

    # Imprimir los datos del comercio que tuvo el mayor promedio
    print("\n--- COMERCIO CON MAYOR PROMEDIO DE CONSUMO ---")
    if comercio_con_mayor_promedio is not None:
        print(f"  Nombre:        {datos_comercio_mayor['nombre']}")
        print(f"  NIT:           {datos_comercio_mayor['nit']}")
        print(f"  Tipo:          {datos_comercio_mayor['tipo']}")
        print(f"  Meta Semanal:  {datos_comercio_mayor['meta']:.2f} kWh")
        print(f"  Promedio:      {datos_comercio_mayor['promedio']:.2f} kWh")
        print(f"  Variación:     {datos_comercio_mayor['variacion']:.2f}%")
        print(f"  Clasificación: {datos_comercio_mayor['clasificacion']}")
    else:
        print("  No hay comercios registrados.")
    print("=" * 80 + "\n")
