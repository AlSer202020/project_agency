"""
Módulo de datos: DESTINOS
-------------------------
Campos:
    id_destino  (int)          Identificador único.
    nombre      (str)          Nombre del destino.
    entorno     (str)          "playa", "montana" o "ciudad" (ver ENTORNOS).
    consejo     (str | None)   Consejo adicional para el viajero (opcional).
    temporada   (str)          Temporada alta / mejor época para visitarlo.
"""

ENTORNOS = {
    "playa": "Playa",
    "montana": "Montaña",
    "ciudad": "Ciudad",
}

DESTINOS = [
    {
        "id_destino": 1,
        "nombre": "Kioto",
        "entorno": "ciudad",
        "consejo": (
            "La moneda local es el yen y recomendamos llevar siempre efectivo "
            "para el acceso a los templos tradicionales."
        ),
        "temporada": "Primavera",
    },
    {
        "id_destino": 2,
        "nombre": "Islas Lofoten",
        "entorno": "montana",
        "consejo": "Es imprescindible viajar con ropa térmica extrema y calzado impermeable.",
        "temporada": "Invierno",
    },
    {
        "id_destino": 3,
        "nombre": "Zanzíbar",
        "entorno": "playa",
        "consejo": None,
        "temporada": "Verano",
    },
    {
        "id_destino": 4,
        "nombre": "Playa del Carmen",
        "entorno": "playa",
        "consejo": (
            "La moneda es el peso mexicano, aunque aceptan dólares en casi "
            "todas las zonas turísticas."
        ),
        "temporada": "Verano",
    },
]


# --- Funciones de acceso ---------------------------------------------------

def obtener_destinos():
    """Todos los destinos ordenados por nombre."""
    return sorted(DESTINOS, key=lambda d: d["nombre"])


def contar_destinos():
    """Número total de destinos (portada)."""
    return len(DESTINOS)


def obtener_destino_por_id(id_destino):
    """Destino con ese id, o None si no existe (el controlador hará abort(404))."""
    return next((d for d in DESTINOS if d["id_destino"] == id_destino), None)


def nombre_entorno(clave):
    """Texto visible de un entorno."""
    return ENTORNOS.get(clave, clave)


# --- Funciones de filtrado -------------------------------------------------

def filtrar_destinos(entorno=None):
    """Explorador de Destinos: filtra por entorno (None/"" = todos)."""
    resultado = DESTINOS
    if entorno:
        resultado = [d for d in resultado if d["entorno"] == entorno]
    return sorted(resultado, key=lambda d: d["nombre"])
