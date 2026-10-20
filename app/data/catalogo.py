"""
Módulo auxiliar: CATÁLOGO
-------------------------
Funciones que cruzan datos de varios módulos, para que app.py y las
plantillas reciban la información ya preparada.
"""

from data_destinos import contar_destinos, filtrar_destinos, obtener_destino_por_id
from data_alojamientos import contar_alojamientos, filtrar_alojamientos
from data_actividades import contar_actividades, obtener_actividades


def resumen_catalogo():
    """Totales para la portada."""
    return {
        "destinos": contar_destinos(),
        "alojamientos": contar_alojamientos(),
        "actividades": contar_actividades(),
    }


def listado_actividades_con_destino():
    """Listado general de actividades con el nombre de su destino añadido."""
    listado = []
    for actividad in obtener_actividades():
        destino = obtener_destino_por_id(actividad["id_destino"])
        listado.append({
            **actividad,
            "nombre_destino": destino["nombre"] if destino else None,
        })
    return listado


def viaje_a_medida(entorno=None, precio_max=None, desayuno=False):
    """
    Asistente de "Viaje a Medida".
    Devuelve [{"destino": {...}, "alojamiento": {...}}, ...] solo con los
    pares que cumplen todos los requisitos a la vez.
    """
    destinos = {d["id_destino"]: d for d in filtrar_destinos(entorno)}
    alojamientos = filtrar_alojamientos(
        precio_max=precio_max,
        desayuno=desayuno,
        ids_destino=destinos.keys(),
    )
    return [{"destino": destinos[a["id_destino"]], "alojamiento": a} for a in alojamientos]
