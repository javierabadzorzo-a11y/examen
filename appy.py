
import streamlit as st

preguntas = [
    {
        "texto": "¿Cuál es más rápido?",
        "opciones": ["Sonic", "Flash", "Usain Bolt", "IShowSpeed"],
        "correcta": "Flash"
    },
    {
        "texto": "¿Tutor de 3B?",
        "opciones": ["JCREYES", "CHUPI", "DIEGO VILAR", "MELLE"],
        "correcta": "JCREYES"
    },
    {
        "texto": "¿Mejor futbolista del Atlético de Madrid?",
        "opciones": ["Griezman", "Oblak", "Koke"],
        "correcta": "Koke"
    },
    {
        "texto": "¿Mejor emoji?",
        "opciones": ["😎", "🤣", "🙉", "🌯"],
        "correcta": "😎"
    },
    {
        "texto": "¿Color del cielo?",
        "opciones": ["Amarillo", "Rosa", "Azul"],
        "correcta": "Azul"
    },
    {
        "texto": "¿Color de la hierba?",
        "opciones": ["Verde", "Violeta", "Fuxia"],
        "correcta": "Verde"
    },
    {
        "texto": "¿Apellido de Koke?",
        "opciones": ["Sánchez", "Resurrección", "Gómez"],
        "correcta": "Resurrección"
    },
    {
        "texto": "¿Marca con una pantera en su logo?",
        "opciones": ["Adidas", "Puma", "Nike"],
        "correcta": "Puma"
    },
    {
        "texto": "¿Dónde muere Jesús?",
        "opciones": ["En su cama", "En el sepulcro", "En la cruz"],
        "correcta": "En la cruz"
    },
]

# Configuración visual de la página
st.title("🎓 Examen De Un Poco de Todo")
st.write("Responde a las preguntas y pulsa el botón al final para saber tu nota.")

# 2. EL FORMULARIO (Agrupamos todo para que no se recargue la web a cada clic)
# Eso se consigue con el comando with

with st.form("quiz_form"):

    # Aquí guardaremos las respuestas que elija el alumno. Será una lista.
    respuestas_usuario = []
   
    # Recorremos el archivador usando un bucle 'for' para crear las preguntas
    for pregunta in preguntas:
        st.subheader(pregunta["texto"]) # Ponemos el texto de la pregunta

        # Creamos los botones de opción (radio)
        eleccion = st.radio("Elige una opción:", pregunta["opciones"], key=pregunta["texto"])

        # Guardamos la elección en nuestra lista usando append ()
        respuestas_usuario.append(eleccion)
        st.write("---") # Una línea para separar preguntas

    # Botón obligatorio para cerrar el formulario
    boton_enviar = st.form_submit_button("Entregar Examen")

# 3. LA CORRECCIÓN (Solo ocurre cuando pulsamos el botón)
if boton_enviar:
    aciertos = 0
    # Total es número de preguntas (usa el método len)
    total = len(preguntas)

    # Comparamos las respuestas del usuario con las 'correctas' del archivador
    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos = aciertos + 1

    # Calculamos la nota sobre 10
    nota = round((aciertos / total) * 10,2)

    # Mostramos el resultado con colores
    st.divider()
    st.header(f"Resultado final: {nota} / 10")

    if 5<nota<7:
    st.text(f"Has puesto {aciertos} preguntas bien. A ver que tal la próxima...")
    st.balloons()
elif 1>nota<5:
    st.text(f"¡Estudia un poco MÁS!")
elif 7<nota<=10:
    st.text(f"Grandee, se nota el empollo")
