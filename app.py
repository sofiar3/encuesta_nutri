import streamlit as st

st.set_page_config(page_title="Herramienta de Alimentación Saludable", page_icon="🥗", layout="centered")

st.title("Cuestionario Nutricional para Cálculo del Índice Chileno de Dieta Mediterránea")
st.info("Responda cada pregunta. Las sub-preguntas aparecerán automáticamente si selecciona 'Sí'.")


# 1. Verduras
p1 = st.radio(
    "1. ¿Cuántas porciones de verduras consume al día?",
    ["Ninguna o menos de 1", "1 a 3 porciones", "3 o más porciones"],
    index=None,
    help="1 porción: 1 taza o 1 plato de entrada. 2 porciones: 2 tazas o 1 plato de fondo lleno."
)

# 2. Legumbres
p2 = st.radio(
    "2. ¿Cuántas veces a la semana consume un plato de legumbres?",
    ["Ninguna o menos de 1", "1 a 2 veces", "más de 2 veces"],
    index=None
)

# 3. Frutos Secos
p3 = st.radio(
    "3. ¿Cuántas veces a la semana consume un puñado de frutos secos?",
    ["Ninguna o menos de 1", "1 a 2 veces", "más de 2 veces"],
    index=None
)

# 4. Frutas
p4 = st.radio(
    "4. ¿Cuántas porciones de frutas consume al día?",
    ["Ninguna o menos de 1", "1 a 2 porciones", "2 o más porciones"],
    index=None
)

# 5. Cereales Integrales
p5 = st.radio(
    "5. ¿Cuántas porciones de cereales integrales consume regularmente cada día?",
    ["Ninguna o menos de 1", "1 a 2 porciones", "2 o más porciones"],
    index=None
)

# 6. Carnes Magras
p6 = st.radio(
    "6. ¿Cuántas veces a la semana consume carnes con poca grasa?",
    ["ninguna", "1 a 4 veces", "5 a 8 veces", "más de 8 veces"],
    index=None
)

# 7. Carnes Grasas
p7 = st.radio(
    "7. ¿Cuántas veces a la semana consume carnes altas en grasa o procesadas?",
    ["ninguna o menos de 1", "1 a 2 veces", "más de 2 veces"],
    index=None
)

# 8. Pescados
p8 = st.radio(
    "8. ¿Cuántas veces a la semana consume pescados o mariscos?",
    ["ninguna o menos de 1", "1 a 2 veces", "más de 2"],
    index=None
)

# --- Lógica Dinámica: Pregunta 9 ---
st.markdown("---")
p9_1 = st.radio("9.1. ¿Consume algún producto lácteo semidescremado, descremado o fermentado al día?", ["Sí", "No"], index=None)
p9_2 = "no consumo"
if p9_1 == "Sí":
    p9_2 = st.radio("9.2. ¿Cuántas tazas consume al día?", ["no consumo", "1 o menos tazas", "más de 1 taza"], index=None)

# --- Lógica Dinámica: Pregunta 10 ---
st.markdown("---")
p10_1 = st.radio("10.1. ¿Consume diariamente leche entera, mantequilla o crema?", ["Sí", "No"], index=None)
p10_2, p10_3 = "No", "No"
if p10_1 == "Sí":
    p10_2 = st.radio("10.2. ¿Consume regularmente más de 1 taza de leche entera al día?", ["Sí", "No"], index=None)
    p10_3 = st.radio("10.3. ¿Consume regularmente más de 2 cucharaditas (de té) de mantequilla o crema al día?", ["Sí", "No"], index=None)

# --- Lógica Dinámica: Pregunta 11 ---
st.markdown("---")
p11_1 = st.radio("11.1. ¿Consume regularmente aceite de oliva?", ["Sí", "No"], index=None)
p11_2 = "Ninguna"
if p11_1 == "Sí":
    p11_2 = st.radio("11.2. ¿Cuántas cucharaditas (de té) de aceite de oliva consume al día?", ["Ninguna", "1 a 2 cucharaditas", "3 o más cucharaditas"], index=None)

# 12. Canola y Palta
st.markdown("---")
p12_1 = st.radio("12.1. ¿Usa regularmente aceite canola puro en su casa?", ["Sí", "No", "Ocasionalmente", "No sabe / no lo conoce"], index=None)
p12_2 = st.radio("12.2. ¿Cuántas paltas consume a la semana regularmente?", ["ninguna o menos de ½ palta", "½ a 3 paltas", "más de 3 paltas"], index=None)

# --- Lógica Dinámica: Pregunta 13 ---
st.markdown("---")
p13_1 = st.radio("13.1. ¿Consume regularmente vino con las comidas (4 o más veces a la semana)?", ["Sí", "No"], index=None)
p13_2 = "menos de 1 copa"
if p13_1 == "Sí":
    p13_2 = st.radio("13.2. ¿Cuántas copas de vino consume al día en promedio?", ["menos de 1 copa", "1 a 2 copas", "más de 2 copas"], index=None)

# 14. Azúcares
st.markdown("---")
p14_1 = st.radio("14.1. ¿Consume regularmente dulces, golosinas o postres con azúcar más de 1 vez al día?", ["Sí", "No"], index=None)
p14_2 = st.radio("14.2. ¿Consume habitualmente bebidas gaseosas o jugos no light o azucarados?", ["Sí", "No"], index=None)
p14_3 = st.radio("14.3. ¿Cuántas cucharaditas (de té) de azúcar consume al día?", ["menos de 4 cucharaditas", "4 o más cucharaditas", "Ninguna o endulzantes"], index=None)

# Botón normal de Streamlit
st.divider()
boton_calcular = st.button("Finalizar y Calcular Puntaje", type="primary")

# --- LÓGICA DE CÁLCULO ---
if boton_calcular:
    chequeo = [p1, p2, p3, p4, p5, p6, p7, p8, p9_1, p10_1, p11_1, p12_1, p12_2, p13_1, p14_1, p14_2, p14_3]
    
    # Validaciones extras para sub-preguntas
    valid_sub = True
    if p9_1 == "Sí" and p9_2 is None: valid_sub = False
    if p10_1 == "Sí" and (p10_2 is None or p10_3 is None): valid_sub = False
    if p11_1 == "Sí" and p11_2 is None: valid_sub = False
    if p13_1 == "Sí" and p13_2 is None: valid_sub = False

    if None in chequeo or not valid_sub:
        st.error("⚠️ Por favor, responda todas las preguntas antes de calcular el puntaje.")
    else:
        # (Aquí va toda tu lógica de cálculo de puntos que ya tienes y es correcta)
        puntos = 0.0
        m_0_5_1 = {"Ninguna o menos de 1": 0.0, "1 a 3 porciones": 0.5, "3 o más porciones": 1.0,
                   "1 a 2 veces": 0.5, "más de 2 veces": 1.0, "1 a 2 porciones": 0.5, "2 o más porciones": 1.0,
                   "ninguna o menos de 1": 0.0, "1 a 2 veces": 0.5, "más de 2": 1.0}
        
        for p in [p1, p2, p3, p4, p5, p8]: puntos += m_0_5_1.get(p, 0)
        if p6 == "1 a 4 veces": puntos += 0.5
        elif p6 == "5 a 8 veces": puntos += 1.0
        if p7 == "ninguna o menos de 1": puntos += 1.0
        elif p7 == "1 a 2 veces": puntos += 0.5
        if p9_1 == "Sí":
            if p9_2 == "1 o menos tazas": puntos += 0.5
            elif p9_2 == "más de 1 taza": puntos += 1.0
        if p10_1 == "No": puntos += 1.0
        elif p10_2 == "No" and p10_3 == "No": puntos += 0.5
        if p13_1 == "Sí":
            if p13_2 == "1 a 2 copas": puntos += 1.0
            else: puntos += 0.5
        if p14_1 == "No" and p14_2 == "No" and (p14_3 == "menos de 4 cucharaditas" or p14_3 == "Ninguna o endulzantes"):
            puntos += 1.0
        elif (p14_1 == "No" and p14_2 == "No" and p14_3 == "4 o más cucharaditas") or \
             (p14_1 == "Sí" and p14_2 == "No" and p14_3 != "4 o más cucharaditas") or \
             (p14_1 == "No" and p14_2 == "Sí" and p14_3 != "4 o más cucharaditas"):
            puntos += 0.5

        # Grasas
        o = 1.0 if p11_2 == "3 o más cucharaditas" else (0.5 if p11_2 == "1 a 2 cucharaditas" else 0.0)
        c = 1.0 if p12_1 == "Sí" else (0.5 if p12_1 == "Ocasionalmente" else 0.0)
        p = 1.0 if p12_2 == "más de 3 paltas" else (0.5 if p12_2 == "½ a 3 paltas" else 0.0)
        sum_pc = c + p
        fats = 0.0
        if o == 1.0: fats = 2.0
        elif o == 0.5:
            fats = 1.5 if sum_pc >= 1.5 else (1.0 if sum_pc == 1.0 else 0.5)
        else:
            fats = 1.0 if sum_pc >= 1.5 else (0.5 if sum_pc == 1.0 else 0.0)
        puntos += fats

        st.header(f"Tu puntaje: {puntos} / 14")
        if puntos >= 9:
            st.success("### **Alta adherencia**")
            st.balloons()
        elif 5 <= puntos <= 8.5:
            st.warning("### **Adherencia moderada**")
        else:
            st.error("### **Baja adherencia**")
