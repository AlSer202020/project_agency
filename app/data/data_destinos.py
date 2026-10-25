

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
        "imagen": "kioto.jpg",
    },
    {
        "id_destino": 2,
        "nombre": "Islas Lofoten",
        "pais": "Noruega",
        "entorno": "montana",
        "visado": False,
        "consejo": "Es imprescindible viajar con ropa térmica extrema y calzado impermeable.",
        "temporada": "Invierno",
        "imagen": "lofoten.jpg",
    },
    {
        "id_destino": 3,
        "nombre": "Zanzíbar",
        "pais": "Tanzania",
        "entorno": "playa",
        "visado": True,
        "consejo": None,
        "temporada": "Verano",
        "imagen": "zanzibar.jpg",
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
        "imagen": "playa_del_carmen.jpg",
    },
]

def obtener_destinos():
    return sorted(DESTINOS, key=lambda d: d["nombre"])


def contar_destinos():
    return len(DESTINOS)


def obtener_destino_por_id(id_destino):
    return next((d for d in DESTINOS if d["id_destino"] == id_destino), None)


def nombre_entorno(clave):
    return ENTORNOS.get(clave, clave)

def filtrar_destinos(entorno=None, sin_visado=False):
    resultado = DESTINOS
    if entorno:
        resultado = [d for d in resultado if d["entorno"] == entorno]
    if sin_visado:
        resultado = [d for d in resultado if not d["visado"]]
    return sorted(resultado, key=lambda d: d["nombre"])