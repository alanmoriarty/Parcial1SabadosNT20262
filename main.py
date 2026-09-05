"""
Módulo: main.py
Descripción: Archivo principal de ejecución del Sistema de Monitoreo de Consumo Energético.
             Importa el módulo funciones y orquesta el flujo de ejecución secuencial.
"""

import funciones

def main():
    """
    Función principal que orquesta el flujo de la aplicación:
    1. Registra los comercios iniciales con registrar_comercios().
    2. Registra las 4 mediciones semanales de consumo con registrar_consumo().
    3. Procesa y genera el informe consolidado con generar_informe().
    """
    print("*" * 65)
    print(" SISTEMA DE MONITOREO DE CONSUMO ENERGÉTICO EN PEQUEÑOS COMERCIOS ")
    print("*" * 65)

    # 1. Llamar a registrar_comercios() para capturar los datos básicos
    comercios = funciones.registrar_comercios()

    # 2. Pasar el resultado a registrar_consumo() para capturar las 4 semanas de consumo
    comercios_actualizados = funciones.registrar_consumo(comercios)

    # 3. Pasar los comercios actualizados a generar_informe() para procesar y mostrar resultados
    funciones.generar_informe(comercios_actualizados)

# Bloque de ejecución principal
if __name__ == "__main__":
    main()
