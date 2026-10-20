"""
Módulo de datos: DESTINOS
-------------------------
Campos:
    id_destino  (int)          Identificador único.
    nombre      (str)          Nombre del destino.
    pais        (str)          País al que pertenece.
    entorno     (str)          "playa", "montana" o "ciudad" (ver ENTORNOS).
    visado      (bool)         True si exige visado previo para entrar.
    consejo     (str | None)   Consejo adicional para el viajero (opcional).
    temporada   (str)          Temporada alta / mejor época para visitarlo.
    imagen      (str | None)   Nombre del archivo en static/img (opcional).
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
        "pais": "Japón",
        "entorno": "ciudad",
        "visado": False,
        "consejo": (
            "La moneda local es el yen y recomendamos llevar siempre efectivo "
            "para el acceso a los templos tradicionales."
        ),
        "temporada": "Primavera",
        "imagen": None,
    },
    {
        "id_destino": 2,
        "nombre": "Islas Lofoten",
        "pais": "Noruega",
        "entorno": "montana",
        "visado": False,
        "consejo": "Es imprescindible viajar con ropa térmica extrema y calzado impermeable.",
        "temporada": "Invierno",
        "imagen": None,
    },
    {
        "id_destino": 3,
        "nombre": "Zanzíbar",
        "pais": "Tanzania",
        "entorno": "playa",
        "visado": True,
        "consejo": None,
        "temporada": "Verano",
        "imagen": None,
    },
    {
        "id_destino": 4,
        "nombre": "Playa del Carmen",
        "pais": "México",
        "entorno": "playa",
        "visado": False,
        "consejo": (
            "La moneda es el peso mexicano, aunque aceptan dólares en casi "
            "todas las zonas turísticas."
        ),
        "temporada": "Verano",
        "imagen": None,
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

def filtrar_destinos(entorno=None, sin_visado=False):
    """Explorador de Destinos: filtra por entorno (None/"" = todos) y visado."""
    resultado = DESTINOS
    if entorno:
        resultado = [d for d in resultado if d["entorno"] == entorno]
    if sin_visado:
        resultado = [d for d in resultado if not d["visado"]]
    return sorted(resultado, key=lambda d: d["nombre"])