"""
Módulo de datos: ALOJAMIENTOS
-----------------------------
Campos (según el esquema del cuaderno):
    id_alojamiento  (int)          Identificador único.
    id_destino      (int)          Relación con DESTINOS["id_destino"].
    nombre          (str)          Nombre comercial.
    precio          (int)          Precio por noche en euros.
    desayuno        (bool)         True si incluye desayuno.
    mascota         (bool)         True si admite mascotas.
    estrellas       (int | None)   Categoría oficial (opcional).
    descripcion     (str | None)   Servicios o extras destacados (opcional).
"""

ALOJAMIENTOS = [
    # --- Kioto (id_destino 1) ---
    {
        "id_alojamiento": 1, "id_destino": 1,
        "nombre": "Ryokan Tradicional Gion",
        "precio": 140, "desayuno": True, "mascota": False,
        "estrellas": 4,
        "descripcion": "Baño termal privado en la habitación.",
    },
    {
        "id_alojamiento": 2, "id_destino": 1,
        "nombre": "Capsule Hostel Urban",
        "precio": 35, "desayuno": False, "mascota": False,
        "estrellas": 2,
        "descripcion": None,
    },
    {
        "id_alojamiento": 3, "id_destino": 1,
        "nombre": "Apartamento Bambú Arashiyama",
        "precio": 95, "desayuno": False, "mascota": True,
        "estrellas": None,
        "descripcion": "Terraza con vistas al río.",
    },
    # --- Islas Lofoten (id_destino 2) ---
    {
        "id_alojamiento": 4, "id_destino": 2,
        "nombre": "Rorbu Fjord Cabins",
        "precio": 160, "desayuno": True, "mascota": True,
        "estrellas": 4,
        "descripcion": "Acceso directo al muelle del fiordo.",
    },
    {
        "id_alojamiento": 5, "id_destino": 2,
        "nombre": "Arctic Light Hotel",
        "precio": 210, "desayuno": True, "mascota": False,
        "estrellas": 5,
        "descripcion": "Mirador acristalado en la azotea.",
    },
    {
        "id_alojamiento": 6, "id_destino": 2,
        "nombre": "Refugio de Pescadores Svolvær",
        "precio": 55, "desayuno": False, "mascota": True,
        "estrellas": None,
        "descripcion": None,
    },
    # --- Zanzíbar (id_destino 3): sin alojamientos ---
    # --- Playa del Carmen (id_destino 4) ---
    {
        "id_alojamiento": 7, "id_destino": 4,
        "nombre": "Hostal Caribe Maya",
        "precio": 25, "desayuno": True, "mascota": True,
        "estrellas": 2,
        "descripcion": None,
    },
    {
        "id_alojamiento": 8, "id_destino": 4,
        "nombre": "Eco-Villas Tulum Road",
        "precio": 110, "desayuno": False, "mascota": True,
        "estrellas": 3,
        "descripcion": "Funciona al 100% con energía solar.",
    },
    {
        "id_alojamiento": 9, "id_destino": 4,
        "nombre": "Grand Resort Riviera",
        "precio": 190, "desayuno": True, "mascota": False,
        "estrellas": 5,
        "descripcion": "Club de playa privado.",
    },
    {
        "id_alojamiento": 10, "id_destino": 4,
        "nombre": "Loft Quinta Avenida",
        "precio": 80, "desayuno": False, "mascota": False,
        "estrellas": None,
        "descripcion": None,
    },
]


# --- Funciones de acceso ---------------------------------------------------

def obtener_alojamientos():
    """Todos los alojamientos ordenados por nombre."""
    return sorted(ALOJAMIENTOS, key=lambda a: a["nombre"])


def contar_alojamientos():
    """Número total de alojamientos (portada)."""
    return len(ALOJAMIENTOS)


def obtener_alojamiento_por_id(id_alojamiento):
    """Alojamiento con ese id, o None si no existe."""
    return next((a for a in ALOJAMIENTOS if a["id_alojamiento"] == id_alojamiento), None)


def obtener_alojamientos_por_destino(id_destino):
    """Alojamientos de un destino (lista vacía si no hay), por precio."""
    return sorted(
        (a for a in ALOJAMIENTOS if a["id_destino"] == id_destino),
        key=lambda a: a["precio"],
    )



# --- Funciones de filtrado -------------------------------------------------

def filtrar_alojamientos(precio_max=None, desayuno=False, mascota=False,
                         ids_destino=None):
    """
    Comparador de Alojamientos (y base del Asistente de Viaje a Medida).
    Los criterios vacíos (None / False / "") no filtran.
    """
    resultado = ALOJAMIENTOS
    if precio_max is not None:
        resultado = [a for a in resultado if a["precio"] <= precio_max]
    if desayuno:
        resultado = [a for a in resultado if a["desayuno"]]
    if mascota:
        resultado = [a for a in resultado if a["mascota"]]
    if ids_destino is not None:
        ids = set(ids_destino)
        resultado = [a for a in resultado if a["id_destino"] in ids]
    return sorted(resultado, key=lambda a: a["precio"])
