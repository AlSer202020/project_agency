"""
Módulo auxiliar: CATÁLOGO
-------------------------
Funciones que cruzan datos de varios módulos, para que main.py y las
plantillas reciban la información ya preparada.
"""

from data.data_destinos import (
    contar_destinos,
    filtrar_destinos,
    obtener_destino_por_id,
)
from data.data_alojamientos import (
    contar_alojamientos,
    filtrar_alojamientos,
    obtener_alojamientos,
    obtener_alojamiento_por_id,
)
from data.data_actividades import (
    contar_actividades,
    obtener_actividades,
    obtener_actividad_por_id,
)


def resumen_catalogo():
    """Totales para la portada."""
    return {
        "destinos": contar_destinos(),
        "alojamientos": contar_alojamientos(),
        "actividades": contar_actividades(),
    }


def _nombre_destino(id_destino):
    destino = obtener_destino_por_id(id_destino)
    return destino["nombre"] if destino else None


def con_nombre_destino(elementos):
    """Añade "nombre_destino" a una lista de alojamientos o actividades."""
    return [{**e, "nombre_destino": _nombre_destino(e["id_destino"])} for e in elementos]


def listado_alojamientos_con_destino():
    """Listado general de alojamientos con el nombre de su destino añadido."""
    return con_nombre_destino(obtener_alojamientos())


def listado_actividades_con_destino():
    """Listado general de actividades con el nombre de su destino añadido."""
    return con_nombre_destino(obtener_actividades())


def alojamiento_con_destino(id_alojamiento):
    """Alojamiento con su nombre_destino, o None si no existe."""
    alojamiento = obtener_alojamiento_por_id(id_alojamiento)
    if alojamiento is None:
        return None
    return con_nombre_destino([alojamiento])[0]


def actividad_con_destino(id_actividad):
    """Actividad con su nombre_destino, o None si no existe."""
    actividad = obtener_actividad_por_id(id_actividad)
    if actividad is None:
        return None
    return con_nombre_destino([actividad])[0]


def buscar_alojamientos(precio_max=None, tipo=None, desayuno=False, mascota=False):
    """Comparador de Alojamientos: resultados con el nombre del destino."""
    return con_nombre_destino(
        filtrar_alojamientos(precio_max=precio_max, tipo=tipo, desayuno=desayuno, mascota=mascota)
    )


def viaje_a_medida(entorno=None, sin_visado=False, tipo=None, precio_max=None, desayuno=False):
    """
    Asistente de "Viaje a Medida".
    Devuelve [{"destino": {...}, "alojamiento": {...}}, ...] solo con los
    pares que cumplen todos los requisitos a la vez.
    """
    destinos = {d["id_destino"]: d for d in filtrar_destinos(entorno, sin_visado)}
    alojamientos = filtrar_alojamientos(
        precio_max=precio_max,
        tipo=tipo,
        desayuno=desayuno,
        ids_destino=destinos.keys(),
    )
    return [{"destino": destinos[a["id_destino"]], "alojamiento": a} for a in alojamientos]