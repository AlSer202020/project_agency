TIPOS = {
    "hotel": "Hotel",
    "hostal": "Hostal",
    "cabana": "Cabaña",
    "apartamento": "Apartamento",
}

ALOJAMIENTOS = [
    {
        "id_alojamiento": 1, "id_destino": 1,
        "nombre": "Ryokan Tradicional Gion", "tipo": "hotel",
        "precio": 140, "desayuno": True, "mascota": False,
        "estrellas": 4,
        "descripcion": "Baño termal privado en la habitación.",
    },
    {
        "id_alojamiento": 2, "id_destino": 1,
        "nombre": "Capsule Hostel Urban", "tipo": "hostal",
        "precio": 35, "desayuno": False, "mascota": False,
        "estrellas": 2,
        "descripcion": None,
    },
    {
        "id_alojamiento": 3, "id_destino": 1,
        "nombre": "Apartamento Bambú Arashiyama", "tipo": "apartamento",
        "precio": 95, "desayuno": False, "mascota": True,
        "estrellas": None,
        "descripcion": "Terraza con vistas al río.",
    },
    {
        "id_alojamiento": 4, "id_destino": 2,
        "nombre": "Rorbu Fjord Cabins", "tipo": "cabana",
        "precio": 160, "desayuno": True, "mascota": True,
        "estrellas": 4,
        "descripcion": "Acceso directo al muelle del fiordo.",
    },
    {
        "id_alojamiento": 5, "id_destino": 2,
        "nombre": "Arctic Light Hotel", "tipo": "hotel",
        "precio": 210, "desayuno": True, "mascota": False,
        "estrellas": 5,
        "descripcion": "Mirador acristalado en la azotea.",
    },
    {
        "id_alojamiento": 6, "id_destino": 2,
        "nombre": "Refugio de Pescadores Svolvær", "tipo": "hostal",
        "precio": 55, "desayuno": False, "mascota": True,
        "estrellas": None,
        "descripcion": None,
    },
    {
        "id_alojamiento": 7, "id_destino": 4,
        "nombre": "Hostal Caribe Maya", "tipo": "hostal",
        "precio": 25, "desayuno": True, "mascota": True,
        "estrellas": 2,
        "descripcion": None,
    },
    {
        "id_alojamiento": 8, "id_destino": 4,
        "nombre": "Eco-Villas Tulum Road", "tipo": "cabana",
        "precio": 110, "desayuno": False, "mascota": True,
        "estrellas": 3,
        "descripcion": "Funciona al 100% con energía solar.",
    },
    {
        "id_alojamiento": 9, "id_destino": 4,
        "nombre": "Grand Resort Riviera", "tipo": "hotel",
        "precio": 190, "desayuno": True, "mascota": False,
        "estrellas": 5,
        "descripcion": "Club de playa privado.",
    },
    {
        "id_alojamiento": 10, "id_destino": 4,
        "nombre": "Loft Quinta Avenida", "tipo": "apartamento",
        "precio": 80, "desayuno": False, "mascota": False,
        "estrellas": None,
        "descripcion": None,
    },
]

def obtener_alojamientos():
    return sorted(ALOJAMIENTOS, key=lambda a: a["nombre"])


def contar_alojamientos():
    return len(ALOJAMIENTOS)


def obtener_alojamiento_por_id(id_alojamiento):
    return next((a for a in ALOJAMIENTOS if a["id_alojamiento"] == id_alojamiento), None)


def obtener_alojamientos_por_destino(id_destino):
    return sorted(
        (a for a in ALOJAMIENTOS if a["id_destino"] == id_destino),
        key=lambda a: a["precio"],
    )


def nombre_tipo(clave):
    return TIPOS.get(clave, clave)



def filtrar_alojamientos(precio_max=None, tipo=None, desayuno=False, mascota=False,
                         ids_destino=None):
    
    resultado = ALOJAMIENTOS
    if precio_max is not None:
        resultado = [a for a in resultado if a["precio"] <= precio_max]
    if tipo:
        resultado = [a for a in resultado if a["tipo"] == tipo]
    if desayuno:
        resultado = [a for a in resultado if a["desayuno"]]
    if mascota:
        resultado = [a for a in resultado if a["mascota"]]
    if ids_destino is not None:
        ids = set(ids_destino)
        resultado = [a for a in resultado if a["id_destino"] in ids]
    return sorted(resultado, key=lambda a: a["precio"])