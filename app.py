import streamlit as st

st.set_page_config(page_title="Herramienta Alimentación Saludable", page_icon="🥗")

st.title("Cuestionario nutricional para cálculo del índice chileno de dieta mediterránea")

# Estilo para mejorar la visualización de las subpreguntas
st.markdown("""
    <style>
    .stRadio [data-testid="stMarkdownContainer"] { font-size: 16px; }
    .sub-pregunta { margin-left: 20px; border-left: 2px solid #f0f2f6; padding-left: 15px; }
    </style>
    """, unsafe_allow_html=True)

with st.form("idm_form"):
    
    # --- BLOQUE 1 A 8 ---
    p1 = st.radio("1. ¿Cuántas porciones de verduras consume al día?", ["Ninguna o menos de 1", "1 a 3 porciones", "3 o más porciones"], index=None)
    
    p2 = st.radio("2. ¿Cuántas veces a la semana, en promedio, consume un plato de legumbres?", ["Ninguna o menos de 1", "1 a 2 veces", "más de 2 veces"], index=None)
    
    p3 = st.radio("3. ¿Cuántas veces a la semana, en promedio, consume un puñado de frutos secos?", ["Ninguna o menos de 1", "1 a 2 veces", "más de 2 veces"], index=None)
    
    p4 = st.radio("4. ¿Cuántas porciones de frutas consume al día?", ["Ninguna o menos de 1", "1 a 2 porciones", "2 o más porciones"], index=None)
    
    p5 = st.radio("5. ¿Cuántas porciones de cereales integrales consume regularmente cada día?", ["Ninguna o menos de 1", "1 a 2 porciones", "2 o más porciones"], index=None)
    
    p6 = st.radio("6. ¿Cuántas veces a la semana, en promedio, consume carnes con poca grasa?", ["ninguna", "1 a 4 veces", "5 a 8 veces", "más de 8 veces"], index=None)
    
    p7 = st.radio("7. ¿Cuántas veces a la semana, en promedio, consume carnes altas en grasa o procesadas?", ["ninguna o menos de 1", "1 a 2 veces", "más de 2 veces"], index=None)
    
    p8 = st.radio("8. ¿Cuántas veces a la semana, en promedio, consume pescados o mariscos?", ["ninguna o menos de 1", "1 a 2 veces", "más de 2"], index=None)

    # --- BLOQUE 9 (Lácteos Descremados) ---
    st.markdown("---")
    p9_1 = st.radio("9.1. ¿Consume algún producto lácteo semidescremado, descremado o fermentado al día?", ["Sí", "No"], index=None)
    
    p9_2 = None
    if p9_1 == "Sí":
        with st.container():
            st.markdown('<div class="sub-pregunta">', unsafe_allow_html=True)
            p9_2 = st.radio("9.2. ¿Cuántas tazas de lácteos descremados, semidescremados o fermentados consume al día?", ["no consumo", "1 o menos tazas", "más de 1 taza"], index=None)
            st.markdown('</div>', unsafe_allow_html=True)

    # --- BLOQUE 10 (Lácteos Enteros) ---
    st.markdown("---")
    p10_1 = st.radio("10.1. ¿Consume diariamente leche entera, mantequilla o crema?", ["Sí", "No"], index=None)
    
    p10_2 = None
    p10_3 = None
    if p10_1 == "Sí":
        with st.container():
            st.markdown('<div class="sub-pregunta">', unsafe_allow_html=True)
            p10_2 = st.radio("10.2. ¿Consume regularmente más de 1 taza de leche entera al día?", ["Sí", "No"], index=None)
            p10_3 = st.radio("10.3. ¿Consume regularmente más de 2 cucharaditas (de té) de mantequilla o crema al día?", ["Sí", "No"], index=None)
            st.markdown('</div>', unsafe_allow_html=True)

    # --- BLOQUE 11 (Aceite de Oliva) ---
    st.markdown("---")
    p11_1 = st.radio("11.1. ¿Consume regularmente aceite de oliva?", ["Sí", "No"], index=None)
    
    p11_2 = None
    if p11_1 == "Sí":
        with st.container():
            st.markdown('<div class="sub-pregunta">', unsafe_allow_html=True)
            p11_2 = st.radio("11.2. ¿Cuántas cucharaditas (de té) de aceite de oliva consume al día?", ["Ninguna", "1 a 2 cucharaditas", "3 o más cucharaditas"], index=None)
            st.markdown('</div>', unsafe_allow_html=True)

    # --- BLOQUE 12 (Canola y Palta) ---
    st.markdown("---")
    p12_1 = st.radio("12.1. ¿Usa regularmente aceite canola puro en su casa?", ["Sí", "No", "Ocasionalmente", "No sabe / no lo conoce"], index=None)
    
    p12_2 = st.radio("12.2. ¿Cuántas paltas consume a la semana regularmente?", ["ninguna o menos de ½ palta", "½ a 3 paltas", "más de 3 paltas"], index=None)

    # --- BLOQUE 13 (Vino) ---
    st.markdown("---")
    p13_1 = st.radio("13.1. ¿Consume regularmente vino con las comidas (4 o más veces a la semana)?", ["Sí", "No"], index=None)
    
    p13_2 = None
    if p13_1 == "Sí":
        with st.container():
            st.markdown('<div class="sub-pregunta">', unsafe_allow_html=True)
            p13_2 = st.radio("13.2. ¿Cuántas copas de vino consume al día en promedio?", ["menos de 1 copa", "1 a 2 copas", "más de 2 copas"], index=None)
            st.markdown('</div>', unsafe_allow_html=True)

    # --- BLOQUE 14 (Azúcar) ---
    st.markdown("---")
    p14_1 = st.radio("14.1. ¿Consume regularmente dulces, golosinas o postres con azúcar más de 1 vez al día?", ["Sí", "No"], index=None)
    p14_2 = st.radio("14.2. ¿Consume habitualmente bebidas gaseosas o jugos no light o azucarados durante el día?", ["Sí", "No"], index=None)
    p14_3 = st.radio("14.3. En promedio, ¿cuántas cucharaditas (de té) de azúcar consume al día?", ["menos de 4 cucharaditas", "4 o más cucharaditas", "Ninguna o endulzantes (sacarina, aspartame, sucralosa, estevia, otro)"], index=None)

    enviar = st.form_submit_button("Calcular Puntaje IDM-Chile")

# --- LÓGICA DE CÁLCULO ---
if enviar:
    # Verificación básica de que lo principal esté contestado
    principales = [p1, p2, p3, p4, p5, p6, p7, p8, p9_1, p10_1, p11_1, p12_1, p12_2, p13_1, p14_1, p14_2, p14_3]
    if None in principales:
        st.error("Por favor, responda todas las preguntas. Si la instrucción dice saltar una subpregunta, asegúrese de haber marcado al menos la pregunta principal.")
    else:
        score = 0.0

        # 1 a 5 y 8
        m = {"Ninguna o menos de 1": 0, "1 a 3 porciones": 0.5, "3 o más porciones": 1, 
             "1 a 2 veces": 0.5, "más de 2 veces": 1, "1 a 2 porciones": 0.5, "2 o más porciones": 1,
             "ninguna o menos de 1": 0, "1 a 2 veces": 0.5, "más de 2": 1}
        score += m.get(p1, 0)
        score += m.get(p2, 0)
        score += m.get(p3, 0)
        score += m.get(p4, 0)
        score += m.get(p5, 0)
        score += m.get(p8, 0)

        # 6. Carnes Magras
        if p6 == "1 a 4 veces": score += 0.5
        elif p6 == "5 a 8 veces": score += 1.0
        
        # 7. Carnes Grasas
        if p7 == "ninguna o menos de 1": score += 1.0
        elif p7 == "1 a 2 veces": score += 0.5

        # 9. Lácteos Descremados (9.1 y 9.2)
        if p9_1 == "No": score += 0
        elif p9_1 == "Sí":
            if p9_2 == "1 o menos tazas": score += 0.5
            elif p9_2 == "más de 1 taza": score += 1.0

        # 10. Lácteos Enteros (10.1, 10.2, 10.3)
        if p10_1 == "No": 
            score += 1.0
        else:
            # Si consume, evaluamos combinaciones de 10.2 y 10.3 según algoritmo
            if p10_2 == "No" and p10_3 == "No": score += 0.5
            else: score += 0 # (P10.1 alt 1 y P10.2 alt 1 etc es 0 ptos)

        # 13. Vino (13.1 y 13.2)
        if p13_1 == "No": score += 0
        else:
            if p13_2 == "1 a 2 copas": score += 1.0
            else: score += 0.5

        # 14. Azúcar (14.1, 14.2, 14.3)
        # 1 pto: No a dulces (14.1 alt 2), No a bebidas (14.2 alt 2) y < 4 cdtas (14.3 alt 1 o 3)
        if p14_1 == "No" and p14_2 == "No" and (p14_3 == "menos de 4 cucharaditas" or "Ninguna" in p14_3):
            score += 1.0
        # 0.5 ptos: según combinaciones del algoritmo (una de las negativas es afirmativa)
        elif (p14_1 == "No" and p14_2 == "No" and p14_3 == "4 o más cucharaditas") or \
             (p14_1 == "Sí" and p14_2 == "No" and (p14_3 == "menos de 4 cucharaditas" or "Ninguna" in p14_3)) or \
             (p14_1 == "No" and p14_2 == "Sí" and (p14_3 == "menos de 4 cucharaditas" or "Ninguna" in p14_3)):
            score += 0.5

        # --- Algoritmo Grasas (11 y 12) ---
        pts_oliva = 0
        if p11_1 == "Sí":
            if p11_2 == "3 o más cucharaditas": pts_oliva = 1.0
            elif p11_2 == "1 a 2 cucharaditas": pts_oliva = 0.5
        
        pts_canola = 1.0 if p12_1 == "Sí" else (0.5 if p12_1 == "Ocasionalmente" else 0)
        pts_palta = 1.0 if p12_2 == "más de 3 paltas" else (0.5 if p12_2 == "½ a 3 paltas" else 0)
        
        suma_pc = pts_canola + pts_palta
        
        fat_score = 0
        if pts_oliva == 1.0: fat_score = 2.0
        elif pts_oliva == 0.5:
            if suma_pc >= 1.5: fat_score = 1.5
            elif suma_pc == 1.0: fat_score = 1.0
            else: fat_score = 0.5
        else: # Oliva = 0
            if suma_pc >= 1.5: fat_score = 1.0
            elif suma_pc == 1.0: fat_score = 0.5
            else: fat_score = 0
        
        score += fat_score

        # --- RESULTADOS FINALES ---
        st.divider()
        st.subheader(f"Puntaje Obtenido: {score} puntos")
        
        if score >= 9:
            st.success("### **Alta adherencia**\nAlimentación de tipo mediterráneo (buena calidad o saludable).")
            st.balloons() # Un pequeño efecto visual de celebración
        elif 5 <= score <= 8.5:
            st.warning("### **Adherencia moderada**\nAlimentación mediterránea de regular calidad.")
        else:
            st.error("### **Baja adherencia**\nDieta de mala calidad.")
        st.info("""
        **Nota:** Esta categorización se realiza según terciles de puntaje establecidos 
        en el protocolo del Índice Chileno de Dieta Mediterránea (IDM-Chile).
        """)
