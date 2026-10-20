from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, BooleanField, SubmitField
from wtforms.validators import Optional, NumberRange

from data.data_destinos import ENTORNOS
from data.data_alojamientos import TIPOS

# Las opciones salen de los diccionarios de los módulos de datos
OPCIONES_ENTORNO = [("", "Cualquiera")] + list(ENTORNOS.items())
OPCIONES_TIPO = [("", "Cualquiera")] + list(TIPOS.items())

MENSAJE_PRECIO = "Introduce un precio entre 0 y 5000 €."


class ExploradorForm(FlaskForm):
    class Meta:
        csrf = False  # Formulario de solo consulta: sin CSRF

    entorno = SelectField("Tipo de entorno", choices=OPCIONES_ENTORNO)
    sin_visado = BooleanField("Solo destinos sin visado")
    submit = SubmitField("Buscar destinos")


class ComparadorForm(FlaskForm):
    class Meta:
        csrf = False

    presupuesto_max = IntegerField(
        "Presupuesto máximo por noche (€)",
        validators=[Optional(), NumberRange(min=0, max=5000, message=MENSAJE_PRECIO)],
    )
    tipo = SelectField("Tipo de alojamiento", choices=OPCIONES_TIPO)
    desayuno = BooleanField("Desayuno incluido")
    mascotas = BooleanField("Admite mascotas")
    submit = SubmitField("Buscar alojamientos")


class AsistenteForm(FlaskForm):
    class Meta:
        csrf = False

    entorno = SelectField("Tipo de entorno", choices=OPCIONES_ENTORNO)
    sin_visado = BooleanField("Prefiero viajar sin visado")
    tipo = SelectField("Tipo de alojamiento", choices=OPCIONES_TIPO)
    presupuesto_max = IntegerField(
        "Gasto máximo por noche (€)",
        validators=[Optional(), NumberRange(min=0, max=5000, message=MENSAJE_PRECIO)],
    )
    desayuno = BooleanField("Desayuno incluido")
    submit = SubmitField("Buscar mi viaje")