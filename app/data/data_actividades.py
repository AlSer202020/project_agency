"""
Módulo de datos: ACTIVIDADES
----------------------------
Campos (según el esquema del cuaderno):
    id_actividad  (int)          Identificador único.
    id_destino    (int)          Relación con DESTINOS["id_destino"].
    nombre        (str)          Nombre de la experiencia o excursión.
    duracion      (int)          Duración aproximada en horas.
    precio        (int)          Precio por persona en euros.
    edad          (int | None)   Edad mínima (opcional).
    descripcion   (str | None)   En qué consiste / qué incluye / dificultad (opcional).
"""

ACTIVIDADES = [
    # --- Kioto (id_destino 1) ---
    {
        "id_actividad": 1, "id_destino": 1,
        "nombre": "Ceremonia del Té en Gion",
        "duracion": 2, "precio": 30, "edad": None,
        "descripcion": "Incluye degustación de dulces tradicionales matcha.",
    },
    {
        "id_actividad": 2, "id_destino": 1,
        "nombre": "Tour Nocturno por Fushimi Inari",
        "duracion": 3, "precio": 40, "edad": 10,
        "descripcion": "Caminata nocturna de dificultad media.",
    },
    {
        "id_actividad": 3, "id_destino": 1,
        "nombre": "Clase de Cocina Ramen y Gyozas",
        "duracion": 3, "precio": 65, "edad": 12,
        "descripcion": (
            "Incluye todos los ingredientes, delantal y recetario impreso. "
            "Edad mínima por el uso de fuegos y cuchillos."
        ),
    },
    {
        "id_actividad": 4, "id_destino": 1,
        "nombre": "Ruta en Bicicleta por el Bosque de Bambú",
        "duracion": 4, "precio": 50, "edad": None,
        "descripcion": "Dificultad baja. Incluye alquiler de bicicleta eléctrica y casco.",
    },
    # --- Islas Lofoten (id_destino 2): sin actividades ---
    # --- Zanzíbar (id_destino 3) ---
    {
        "id_actividad": 5, "id_destino": 3,
        "nombre": "Ruta de las Especias y Paseo en Dhow",
        "duracion": 5, "precio": 45, "edad": None,
        "descripcion": "Dificultad baja. Incluye almuerzo tradicional especiado.",
    },
    {
        "id_actividad": 6, "id_destino": 3,
        "nombre": "Snorkel en el Atolón Mnemba",
        "duracion": 4, "precio": 60, "edad": 8,
        "descripcion": "Dificultad media. Incluye todo el equipo de tubo, gafas y aletas.",
    },
    {
        "id_actividad": 7, "id_destino": 3,
        "nombre": "Visita Guiada por Stone Town",
        "duracion": 2, "precio": 20, "edad": None,
        "descripcion": None,
    },
    # --- Playa del Carmen (id_destino 4) ---
    {
        "id_actividad": 8, "id_destino": 4,
        "nombre": "Buceo en Cenotes Sagrados",
        "duracion": 4, "precio": 75, "edad": 16,
        "descripcion": (
            "Dificultad alta. Incluye bombona de oxígeno, linterna subacuática "
            "y traje de neopreno."
        ),
    },
    {
        "id_actividad": 9, "id_destino": 4,
        "nombre": "Excursión a las Ruinas de Tulum",
        "duracion": 6, "precio": 55, "edad": None,
        "descripcion": (
            "Dificultad baja. Incluye entradas al recinto arqueológico "
            "y transporte en autobús."
        ),
    },
    {
        "id_actividad": 10, "id_destino": 4,
        "nombre": "Paseo en Catamarán al Atardecer",
        "duracion": 3, "precio": 65, "edad": 18,
        "descripcion": "Incluye barra libre de bebidas y aperitivos a bordo.",
    },
]


# --- Funciones de acceso ---------------------------------------------------

def obtener_actividades():
    """Todas las actividades ordenadas por nombre."""
    return sorted(ACTIVIDADES, key=lambda a: a["nombre"])


def contar_actividades():
    """Número total de actividades (portada)."""
    return len(ACTIVIDADES)


def obtener_actividad_por_id(id_actividad):
    """Actividad con ese id, o None si no existe."""
    return next((a for a in ACTIVIDADES if a["id_actividad"] == id_actividad), None)


def obtener_actividades_por_destino(id_destino):
    """Actividades de un destino (lista vacía si no hay)."""
    return sorted(
        (a for a in ACTIVIDADES if a["id_destino"] == id_destino),
        key=lambda a: a["nombre"],
    )


# --- Funciones de filtrado (para requerimientos futuros) -------------------

def filtrar_actividades(precio_max=None, edad=None, duracion_max=None, ids_destino=None):
    """Filtra por precio máximo, edad del viajero, duración máxima y destinos."""
    resultado = ACTIVIDADES
    if precio_max is not None:
        resultado = [a for a in resultado if a["precio"] <= precio_max]
    if edad is not None:
        resultado = [a for a in resultado if a["edad"] is None or a["edad"] <= edad]
    if duracion_max is not None:
        resultado = [a for a in resultado if a["duracion"] <= duracion_max]
    if ids_destino is not None:
        ids = set(ids_destino)
        resultado = [a for a in resultado if a["id_destino"] in ids]
    return sorted(resultado, key=lambda a: a["nombre"])
