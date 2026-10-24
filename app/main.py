from flask import abort, Flask, render_template

from data.catalogo import (
    actividad_con_destino,
    alojamiento_con_destino,
    buscar_alojamientos,
    listado_actividades_con_destino,
    listado_alojamientos_con_destino,
    resumen_catalogo,
    viaje_a_medida,
)
from data.data_actividades import obtener_actividades_por_destino
from data.data_alojamientos import nombre_tipo, obtener_alojamientos_por_destino
from data.data_destinos import (
    filtrar_destinos,
    nombre_entorno,
    obtener_destino_por_id,
    obtener_destinos,
    
)
from form import ExploradorForm, ComparadorForm, AsistenteForm


app = Flask(__name__)

app.config["SECRET_KEY"] = "mi_clave_secreta_super_segura"


app.jinja_env.filters["entorno_texto"] = nombre_entorno
app.jinja_env.filters["tipo_texto"] = nombre_tipo


@app.route("/")
def inicio():
    return render_template("index.html", resumen=resumen_catalogo())


@app.route("/acerca")
def acerca():
    return render_template("about.html")


@app.route("/destinos")
def lista_destinos():
    return render_template("destinos.html", destinos=obtener_destinos())


@app.route("/alojamientos")
def lista_alojamientos():
    return render_template(
        "alojamientos.html", alojamientos=listado_alojamientos_con_destino()
    )


@app.route("/actividades")
def lista_actividades():
    return render_template(
        "actividades.html", actividades=listado_actividades_con_destino()
    )


@app.route("/explorador", methods=["GET", "POST"])
def explorador_destinos():
    form = ExploradorForm()
    resultados = None  
    if form.validate_on_submit():
        resultados = filtrar_destinos(
            entorno=form.entorno.data,
            sin_visado=form.sin_visado.data,
        )

    return render_template("explorador.html", form=form, resultados=resultados)


@app.route("/comparador", methods=["GET", "POST"])
def comparador_alojamientos():
    form = ComparadorForm()
    resultados = None

    if form.validate_on_submit():
        resultados = buscar_alojamientos(
            precio_max=form.presupuesto_max.data,
            tipo=form.tipo.data,
            desayuno=form.desayuno.data,
            mascota=form.mascotas.data,
        )

    return render_template("comparador.html", form=form, resultados=resultados)


@app.route("/asistente", methods=["GET", "POST"])
def asistente_viaje():
    form = AsistenteForm()
    resultados = None

    if form.validate_on_submit():
        resultados = viaje_a_medida(
            entorno=form.entorno.data,
            sin_visado=form.sin_visado.data,
            tipo=form.tipo.data,
            precio_max=form.presupuesto_max.data,
            desayuno=form.desayuno.data,
        )

    return render_template("asistente.html", form=form, resultados=resultados)


@app.route("/destino/<int:id_destino>")
def detalle_destino(id_destino):
    lista_destinos=obtener_destinos()
    destino = obtener_destino_por_id(id_destino)
    if destino is None:
        abort(404)
    if destino not in lista_destinos:
        abort(404)
    return render_template(
        "destino_detalle.html",
        destino=destino,
        alojamientos=obtener_alojamientos_por_destino(id_destino),
        actividades=obtener_actividades_por_destino(id_destino),
    )


@app.route("/alojamiento/<int:id_alojamiento>")
def detalle_alojamiento(id_alojamiento):
    alojamiento = alojamiento_con_destino(id_alojamiento)
    if alojamiento is None:
        abort(404)

    return render_template("alojamiento_detalle.html", alojamiento=alojamiento)


@app.route("/actividad/<int:id_actividad>")
def detalle_actividad(id_actividad):
    actividad = actividad_con_destino(id_actividad)
    #destino = obtener_destino_por_id(actividad["id_destino"]) if actividad else None
    if actividad is None:
        abort(404)

    return render_template("actividad_detalle.html", actividad=actividad)


@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
