import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

# ============================
# CONFIGURACIÓN DE LA PÁGINA
# ============================
st.set_page_config(
    page_title="CV - Yan Carlos Jimenez",
    page_icon="📊",
    layout="wide"
)

# ============================
# ESTILOS (CSS) - FOTO CIRCULAR
# ============================
st.markdown("""
<style>
h1 {color: #2E86C1; margin-bottom: 0;}
h2, h3 {color: #1F618D;}
div[data-testid="stProgress"] > div > div {
    background-color: #2E86C1;
}
/* Estilo para foto circular */
img {
    border-radius: 50%;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    object-fit: cover;
}
</style>
""", unsafe_allow_html=True)

# ============================
# DATOS PERSONALES
# ============================
NOMBRE_COMPLETO = "Yan Carlos Jimenez"
TELEFONO = "+1 (829) 453-0115"
EMAIL = "dauri02041116@gmail.com"
CIUDAD = "Santo Domingo"
PAIS = "República Dominicana"
CEDULA = "402-3005769-3"
LINKEDIN = "https://www.linkedin.com/in/yan-carlos-jimenez-178840264?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app"

# ============================
# PERFIL PROFESIONAL
# ============================
PERFIL_PROFESIONAL = """
Analista de datos junior con sólida formación en Python y Power BI.  
Especializado en transformar datos complejos en insights accionables mediante análisis descriptivo  
y visualización efectiva. Orientado a resultados con habilidades en atención al cliente  
y gestión de proyectos ágiles.
"""

# ============================
# EXPERIENCIA LABORAL
# ============================
EXPERIENCIA = {
    "Puesto": "Analista de Datos Junior",
    "Empresa": "Crismor",
    "Ubicación": "Santo Domingo, República Dominicana",
    "Periodo": "Septiembre 2024 - Octubre 2025"
}

LOGROS = [
    "Desarrollé dashboards interactivos en Power BI reduciendo tiempo de reportes en 40%",
    "Automaticé procesos ETL con Python (Pandas) para datasets de 5,000+ registros",
    "Implementé consultas SQL para métricas clave del negocio",
    "Colaboré con equipos multifuncionales para toma de decisiones basada en datos",
    "Soporte técnico a usuarios internos en herramientas BI"
]

# ============================
# EDUCACIÓN
# ============================
EDUCACION = [
    {
        "titulo": "Análisis de Datos con Power BI",
        "institucion": "Daxus Latam",
        "fecha": "2025"
    },
    {
        "titulo": "Certificación en Análisis de Datos con Python",
        "institucion": "Indotel",
        "fecha": "Actualidad"
    }
]

# ============================
# HABILIDADES
# ============================
HABILIDADES = [
    "Python (Pandas)",
    "Power BI",
    "Excel Avanzado",
    "Análisis de Datos",
    "Visualización de Datos",
    "Gestión de Proyectos",
    "Atención al Cliente"
]

NIVELES = [80, 85, 70, 75, 80, 70, 80]

# ========================
# REFERENCIAS
# ========================
REFERIDOS = {
    "Carlos Jimenez": "+1 (809) 384-7760",
    "Victoria Elizabeth": "+1 (829) 709-7541",
    "Abraham Matos": "+1 (849) 470-0706"
}

# ========================
# ENCABEZADO CON FOTO CIRCULAR
# ========================

col_foto, col_texto = st.columns([1, 4])

with col_foto:
    try:
        image = Image.open("yan.jpeg")  
        st.image(image, width=150)
    except FileNotFoundError:
        # Placeholder si no encuentra la foto
        st.markdown("📷 *Foto*")
        st.info("")

with col_texto:
    st.title(NOMBRE_COMPLETO)
    st.markdown("**Analista de Datos Junior**")
    st.markdown(f"Cedula de identidad: {CEDULA}")
    st.markdown(f"Ubicacion📍: {CIUDAD}, {PAIS}")
    st.markdown(f"Telefono📞: {TELEFONO}")
    st.markdown(f"Correo electronico:✉️ {EMAIL}")
    st.markdown(f"linkedin🔗: {LINKEDIN}")
st.divider()

# ========================
# LAYOUT EN COLUMNAS (CV)
# ========================
col_izq, col_der = st.columns([2, 1])

# -------- COLUMNA IZQUIERDA --------
with col_izq:

    st.header("👤 Perfil Profesional")
    st.write(PERFIL_PROFESIONAL)

    st.header("💼 Experiencia Laboral")
    st.subheader(EXPERIENCIA["Puesto"])
    st.write(f"**{EXPERIENCIA['Empresa']}** — {EXPERIENCIA['Ubicación']}")
    st.write(EXPERIENCIA["Periodo"])

    st.markdown("**Logros clave:**")
    for logro in LOGROS:
        st.markdown(f"✔️ {logro}")

    st.header("🎓 Educación")
    for edu in EDUCACION:
        st.markdown(f"**{edu['titulo']}**")
        st.markdown(f"{edu['institucion']} — {edu['fecha']}")
        st.write("")

# -------- COLUMNA DERECHA --------
with col_der:

    st.header("🛠️ Habilidades Técnicas")
    for habilidad, nivel in zip(HABILIDADES, NIVELES):
        st.markdown(f"**{habilidad}**")
        st.progress(nivel)

# ============================
# GRÁFICO TÉCNICO (OPCIONAL)
# ============================
st.divider()
st.subheader("📊 Nivel de Dominio Técnico")

fig, ax = plt.subplots(figsize=(7, 4))
ax.barh(HABILIDADES, NIVELES, color="#0E9456")
ax.set_xlim(0, 100)
ax.set_xlabel("Nivel (%)")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

for i, v in enumerate(NIVELES):
    ax.text(v + 1, i, f"{v}%", va="center")

st.pyplot(fig)

# ============================
# REFERENCIAS
# ============================
st.header("📞 Referencias")
for nombre, tel in REFERIDOS.items():
    st.write(f"**{nombre}:** {tel}")