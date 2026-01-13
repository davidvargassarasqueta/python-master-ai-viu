def calcular_retorno_diario(precio_actual, precio_anterior):
    # Calculamos el porcentaje de cambio segun la formula
    return ((precio_actual - precio_anterior) / precio_anterior) * 100

def categorizar_volatilidad(desviacion_estandar):
    if desviacion_estandar < 2:
        return "Baja"
    elif 2 <= desviacion_estandar < 5:
        return "Media"
    else:
        return "Alta"