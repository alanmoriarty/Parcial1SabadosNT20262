# Integrantes

* Yety Sanz
* Andres Piña

# ACDA 1 - Evaluación de Python Básico

## Envio:
https://forms.gle/wvZSoQ8hugCWPcXe8

## Caso 3: Sistema de monitoreo de consumo energético en pequeños comercios

## Contexto
Una empresa de asesoría energética acompaña pequeños comercios de barrio para identificar consumos elevados de electricidad. Durante una visita se registra información básica de cada negocio y cuatro mediciones semanales de consumo. Se necesita un prototipo que permita organizar los datos, calcular indicadores sencillos y detectar comercios que deberían recibir una recomendación de ahorro.

## Reto
Desarrolle un programa en Python que resuelva el caso planteado. La solución debe estar dividida en **exactamente 6 funciones principales**, descritas a continuación.

## Estructura de los datos
Cada registro principal debe representarse mediante un **diccionario** y almacenarse en una **lista**.

- **nit**: Identificador del comercio.
- **nombre**: Nombre comercial.
- **tipo**: Tienda, Restaurante o Peluquería.
- **empleados**: Cantidad de empleados.
- **meta_semanal**: Meta máxima de consumo en kWh.
- **consumos**: Lista con 4 mediciones semanales de kWh.

## Funciones obligatorias

### 1. registrar_comercios()
Registrar 10 comercios. Cada comercio será un diccionario y deberá incluir una lista inicialmente vacía para sus consumos. Retorna la lista de comercios.

### 2. registrar_consumos(comercios)
Para cada comercio solicitar exactamente 4 consumos semanales mayores que 0 y almacenarlos en la lista consumos de su diccionario. Retorna la lista actualizada.

### 3. calcular_promedio(consumos)
Calcular manualmente el promedio de las cuatro mediciones usando un ciclo y acumulador. Retorna el promedio.

### 4. calcular_variacion(consumos)
Calcular la diferencia porcentual entre la primera y la cuarta semana: ((semana4 - semana1) / semana1) * 100. Retorna la variación porcentual.

### 5. clasificar_consumo(promedio, meta, variacion)
Clasificar: Eficiente si promedio <= meta y variación <= 5%; En observación si promedio <= meta pero variación > 5%; Alto si promedio > meta hasta un 20%; Crítico si supera la meta en más del 20%. Retorna la clasificación.

### 6. generar_informe(comercios)
Mostrar por comercio: nombre, promedio, variación y clasificación. Al final indicar cuántos comercios están en cada clasificación y cuál tuvo el mayor promedio, hallándolo con un ciclo y comparaciones.

## Restricciones técnicas
- No utilizar clases, archivos, bases de datos, librerías externas ni módulos estadísticos.
- Usar solamente funciones, ciclos, condicionales, listas, diccionarios, variables y operadores básicos.
- El promedio y la búsqueda del mayor consumo deben resolverse manualmente con ciclos.
- No utilizar sum(), max(), min(), sorted() ni funciones equivalentes para resolver los cálculos centrales.
- Cada una de las seis funciones debe ser llamada en la ejecución principal.

## Entrega esperada
- Código fuente ejecutable en Python.
- Las 6 funciones solicitadas claramente identificadas.
- Programa principal que invoque las funciones y permita comprobar el funcionamiento completo.
- Nombres de variables y funciones comprensibles.
- Salidas en consola suficientemente claras para interpretar el resultado.

> **Importante:** se evaluará tanto que el programa funcione como la forma en que el problema fue dividido y resuelto mediante funciones.
