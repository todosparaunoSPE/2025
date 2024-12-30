# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 13:23:50 2024

@author: jperezr
"""



import streamlit as st
import time
import random
import pandas as pd
import datetime
import pytz
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(page_title="Feliz Año 2025", page_icon="🎉")

# Estilo de fondo
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background:
radial-gradient(black 15%, transparent 16%) 0 0,
radial-gradient(black 15%, transparent 16%) 8px 8px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 0 1px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 8px 9px;
background-color:#282828;
background-size:16px 16px;
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Título inicial
st.title("🎉 ¡Bienvenidos! 🎉")

# Texto que se mostrará letra por letra
mensaje = "🎉 Feliz Año 2025 🎉"

# Contenedor para las letras
espacio = st.empty()

# Mostrar las letras una por una
texto_mostrado = ""
for letra in mensaje:
    texto_mostrado += letra
    espacio.markdown(f"<h1 style='text-align: center; color: #ff4500;'>{texto_mostrado}</h1>", unsafe_allow_html=True)
    time.sleep(0.3)  # Tiempo de retraso en segundos

# Mensaje con efecto de parpadeo para tus compañeros de AFORE PENSIONISSSTE
st.write("---")  # Separador
st.markdown(
    """
    <style>
    .blink {
        text-align: center;
        color: #007bff;
        font-size: 24px;
        animation: blink-animation 1s steps(2, start) infinite;
    }
    @keyframes blink-animation {
        to {
            visibility: hidden;
        }
    }
    </style>
    <div class="blink">🎊 Un cordial saludo a todo el equipo de AFORE PENSIONISSSTE. ¡Gracias por su compromiso y excelente trabajo! 🎊</div>
    """,
    unsafe_allow_html=True
)

# Confeti animado
confetti_html = """
<script>
(function() {
    const confetti = document.createElement('script');
    confetti.src = 'https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js';
    confetti.onload = () => {
        const duration = 5 * 1000;
        const end = Date.now() + duration;
        (function frame() {
            confetti({
                particleCount: 5,
                angle: 60,
                spread: 55,
                origin: { x: 0 }
            });
            confetti({
                particleCount: 5,
                angle: 120,
                spread: 55,
                origin: { x: 1 }
            });
            if (Date.now() < end) {
                requestAnimationFrame(frame);
            }
        })();
    };
    document.head.appendChild(confetti);
})();
</script>
"""
components.html(confetti_html)

# Funcionalidad para guardar deseos en un archivo CSV
def guardar_deseo(nuevo_deseo):
    archivo = "deseos.csv"
    try:
        # Cargar el archivo CSV si existe
        df = pd.read_csv(archivo)
    except FileNotFoundError:
        # Crear un DataFrame vacío si no existe
        df = pd.DataFrame(columns=["Deseo"])

    # Agregar el nuevo deseo al DataFrame
    nuevo_registro = pd.DataFrame({"Deseo": [nuevo_deseo]})
    df = pd.concat([df, nuevo_registro], ignore_index=True)

    # Guardar los cambios en el archivo CSV
    df.to_csv(archivo, index=False)
    return df

# Mostrar video y deseos de los usuarios en la página principal
st.write("---")
st.header("🎶 Escucha un mensaje especial 🎶")
st.audio("buenos_deseos.mp3", format="audio/mp3")

st.write("---")
st.header("🎉 ¡Haz tu deseo para el 2025! 🎉")

# Formulario para enviar buenos deseos
deseo = st.text_input("Escribe tus buenos deseos para el equipo", key="deseos")
if st.button("Enviar deseo"):
    if deseo.strip():
        deseos_actualizados = guardar_deseo(deseo.strip())
        st.success(f"🎉 ¡Gracias por compartir tu deseo: {deseo}! ")
    else:
        st.warning("Por favor, escribe un deseo antes de enviarlo.")

# Mostrar deseos enviados previamente
try:
    deseos_previos = pd.read_csv("deseos.csv")
    if not deseos_previos.empty:
        st.write("### Deseos enviados por el equipo:")
        st.table(deseos_previos)
except FileNotFoundError:
    st.write("Aún no se han enviado deseos.")

# Mensajes aleatorios de buenos deseos
mensajes = [
    "¡Que este año te traiga mucha felicidad y éxito! 🎉",
    "¡Que todos tus sueños se hagan realidad en 2025! 🌟",
    "¡A trabajar juntos para un gran 2025! 💪",
    "¡Disfruta cada momento de este nuevo año! 🌈",
]

mensaje_random = random.choice(mensajes)
st.info(f"💬 {mensaje_random}")

# Barra lateral con cuenta regresiva
with st.sidebar:
    st.header("⏳ Cuenta Regresiva para el Año Nuevo 2025 ⏳")
    
    # Zona horaria de Ciudad de México
    tz = pytz.timezone('America/Mexico_City')
    
    # Reloj de cuenta regresiva dinámica con segundos
    año_nuevo = datetime.datetime(2025, 1, 1, 0, 0, 0, tzinfo=tz)  # Ajustamos la hora a la zona horaria correcta
    espacio_contador = st.empty()  # Contenedor para la cuenta regresiva

    # Actualizar la cuenta regresiva cada segundo
    while True:
        ahora = datetime.datetime.now(tz)  # Usamos la hora actual ajustada a la zona horaria de Ciudad de México
        tiempo_restante = año_nuevo - ahora

        # Mostrar la cuenta regresiva con días, horas, minutos y segundos
        espacio_contador.markdown(f"""
        <h2 style="text-align:center; color: #ff4500;">
        ⏳ Tiempo restante para 2025: {tiempo_restante.days} días, {tiempo_restante.seconds // 3600} horas, 
        {(tiempo_restante.seconds // 60) % 60} minutos, {tiempo_restante.seconds % 60} segundos.
        </h2>
        """, unsafe_allow_html=True)

        # Actualizar cada segundo
        time.sleep(1)
        if tiempo_restante.total_seconds() <= 0:
            break  # Detener el bucle cuando llegue el año nuevo
