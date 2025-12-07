import streamlit as st
import random
import folium
from streamlit_folium import st_folium

# -------------------------------
#         CONFIGURACIÓN
# -------------------------------
st.set_page_config(page_title="One Piece Explorer", page_icon="🏴‍☠️", layout="wide")

# Fondo rojo claro + texto negro
st.markdown("""
    <style>
        body {
            background-color: #ffcccc !important;
            color: black !important;
        }
        .stApp {
            background-color: #ffcccc !important;
        }
        h1, h2, h3, h4, h5, h6, p, div, span {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
#           DATOS
# -------------------------------

personajes = {
    "Monkey D. Luffy": {
        "descripcion": "Capitán de los Sombrero de Paja. Usuario del Gomu Gomu no Mi.",
        "rol": "Capitán",
        "imagen": "https://i.imgur.com/CKIuK8Y.png"
    },
    "Roronoa Zoro": {
        "descripcion": "Espadachín de la tripulación. Futuro mejor espadachín del mundo.",
        "rol": "Espadachín",
        "imagen": "https://i.imgur.com/cG1wq4Z.png"
    },
    "Nami": {
        "descripcion": "Navegante experta. Sueña con hacer un mapa del mundo.",
        "rol": "Navegante",
        "imagen": "https://i.imgur.com/Ew3pJ7I.png"
    },
    "Sanji": {
        "descripcion": "Cocinero de la tripulación. Usuario del estilo Diable Jambe.",
        "rol": "Cocinero",
        "imagen": "https://i.imgur.com/7vR9eZJ.png"
    },
    "Nico Robin": {
        "descripcion": "Arqueóloga capaz de leer los Poneglyphs.",
        "rol": "Arqueóloga",
        "imagen": "https://i.imgur.com/XnD3HQx.png"
    }
}

tripulaciones = {
    "Sombrero de Paja": {
        "descripcion": "La tripulación protagonista liderada por Luffy.",
        "imagen": "https://i.imgur.com/qetkRXn.png"
    },
    "Marina": {
        "descripcion": "La organización militar del Gobierno Mundial.",
        "imagen": "https://i.imgur.com/Uv1XHQH.png"
    }
}

geografia = {
    "East Blue": "Uno de los mares cardinales. Donde comienza la historia.",
    "Grand Line": "El mar más peligroso del mundo.",
    "Mariejois": "La capital del Gobierno Mundial."
}

arcos = {
    "Arco de East Blue": "Introducción de los primeros miembros de la tripulación.",
    "Arco de Alabasta": "Luffy y su tripulación ayudan a Vivi.",
    "Arco de Enies Lobby": "Rescate de Nico Robin."
}

peliculas = {
    "One Piece: Strong World": "Shiki el León Dorado amenaza al mundo.",
    "One Piece Film Z": "El ex almirante Zephyr busca destruir la marina.",
    "One Piece: Stampede": "Un festival pirata global lleno de acción."
}

# -------------------------------
#         MENÚ PRINCIPAL
# -------------------------------

menu = st.sidebar.radio(
    "Navega por el mundo de One Piece:",
    [
        "Inicio", 
        "Personajes", 
        "Tripulaciones", 
        "Geografía", 
        "Arcos de la Serie",
        "Información Extra",
        "Juegos Interactivos",
        "Mapa Geográfico"
    ]
)

# -------------------------------
#            INICIO
# -------------------------------
if menu == "Inicio":
    st.title("🏴‍☠️ One Piece Explorer")
    st.subheader("Una aplicación interactiva del mundo de One Piece")
    st.write("Explora personajes, ubicaciones, arcos y mucho más.")

# -------------------------------
#          PERSONAJES
# -------------------------------
elif menu == "Personajes":
    st.header("🧭 Personajes de One Piece")

    busqueda = st.text_input("Buscar personaje:")
    rol_seleccionado = st.selectbox("Filtrar por rol:", ["Todos"] + sorted({p["rol"] for p in personajes.values()}))

    for nombre, datos in personajes.items():

        coincide_nombre = busqueda.lower() in nombre.lower()
        coincide_rol = rol_seleccionado == "Todos" or datos["rol"] == rol_seleccionado

        if (not busqueda or coincide_nombre) and coincide_rol:
            with st.expander(nombre):
                st.image(datos["imagen"], width=200)
                st.write(f"**Rol:** {datos['rol']}")
                st.write(datos["descripcion"])

# -------------------------------
#          TRIPULACIONES
# -------------------------------
elif menu == "Tripulaciones":
    st.header("🏴 Tripulaciones")

    for nombre, datos in tripulaciones.items():
        with st.expander(nombre):
            st.image(datos["imagen"], width=250)
            st.write(datos["descripcion"])

# -------------------------------
#            GEOGRAFÍA
# -------------------------------
elif menu == "Geografía":
    st.header("🗺️ Geografía del Mundo de One Piece")

    for lugar, desc in geografia.items():
        st.write(f"### {lugar}")
        st.write(desc)

# -------------------------------
#              ARCOS
# -------------------------------
elif menu == "Arcos de la Serie":
    st.header("📜 Arcos importantes")

    for nombre, desc in arcos.items():
        with st.expander(nombre):
            st.write(desc)

# -------------------------------
#         INFORMACIÓN EXTRA
# -------------------------------
elif menu == "Información Extra":
    st.header("🎬 Películas y Curiosidades")

    for nombre, desc in peliculas.items():
        with st.expander(nombre):
            st.write(desc)

# -------------------------------
#         JUEGOS INTERACTIVOS
# -------------------------------
elif menu == "Juegos Interactivos":
    st.header("🎮 Juegos Interactivos")
    juego = st.selectbox("Elige un juego:", ["Ahorcado", "Piedra, Papel o Tijera"])

    # Ahorcado
    if juego == "Ahorcado":
        st.subheader("Ahorcado (versión simplificada)")
        palabra = random.choice(list(personajes.keys())).lower()
        st.write(f"La palabra tiene **{len(palabra)}** letras.")
        letra = st.text_input("Ingresa una letra:")

        if letra:
            if letra.lower() in palabra:
                st.success("¡Correcto!")
            else:
                st.error("Incorrecto")

    # PPT
    if juego == "Piedra, Papel o Tijera":
        st.subheader("Piedra, Papel o Tijera")
        opciones = ["Piedra", "Papel", "Tijera"]
        jugador = st.selectbox("Tu jugada:", opciones)
        ia = random.choice(opciones)
        st.write(f"La IA eligió: **{ia}**")

        if jugador == ia:
            st.info("Empate")
        elif (jugador == "Piedra" and ia == "Tijera") or \
             (jugador == "Papel" and ia == "Piedra") or \
             (jugador == "Tijera" and ia == "Papel"):
            st.success("¡Ganaste!")
        else:
            st.error("Perdiste")

# -------------------------------
#        MAPA GEOGRÁFICO
# -------------------------------
elif menu == "Mapa Geográfico":
    st.header("🗾 Estatuas de One Piece en Kumamoto, Japón")

    estatuas = [
        ("Luffy", 32.803, 130.707),
        ("Zoro", 32.804, 130.708),
        ("Nami", 32.805, 130.709)
    ]

    mapa = folium.Map(location=[32.803, 130.707], zoom_start=15)

    for nombre, lat, lon in estatuas:
        folium.Marker([lat, lon], popup=nombre).add_to(mapa)

    st_folium(mapa, width=700, height=500)