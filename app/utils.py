from django.db import connection

def obtener_productos_bajo_stock():
    with connection.cursor() as cursor:
        # Llama al procedimiento almacenado
        cursor.callproc('ObtenerProductosBajoStock')
        # Si el procedimiento devuelve resultados, puedes acceder a ellos
        resultados = cursor.fetchall()

    return resultados

def obtener_suma_totales_por_tipo_pago():
    with connection.cursor() as cursor:
        # Llama al procedimiento almacenado
        cursor.callproc('ObtenerSumaTotalesPorTipoPago')
        # Si el procedimiento devuelve resultados, puedes acceder a ellos
        resultados = cursor.fetchall()

    return resultados