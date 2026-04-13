import streamlit as st

st.set_page_config(page_title="Encuesta IDM-Chile", page_icon="🥗")

st.title("🥗 Cuestionario Nutricional IDM-Chile")
st.markdown("""
Esta encuesta calcula el **Índice Chileno de Dieta Mediterránea**. 
Por favor, responde con sinceridad basándote en tus hábitos habituales.
""")

with st.form("idm_form"):
    # 1. Verduras
    st.subheader("1. Consumo de Vegetales")
    p1 = st.radio("¿Cuántas porciones de verduras consume al día?", 
                  ["Ninguna o menos de 1", "1 a 3 porciones", "3 o más porciones"], index=0)

    # 2. Legumbres
    p2 = st.radio("¿Cuántas veces a la semana consume un plato de legumbres?", 
                  ["Ninguna o menos de 1", "1 a 2 veces", "más de 2 veces"])

    # 3. Frutos Secos
    p3 = st.radio("¿Cuántas veces a la semana consume un puñado de frutos secos?", 
                  ["Ninguna o menos de 1", "1 a 2 veces", "más de 2 veces"])

    # 4. Frutas
    p4 = st.radio("¿Cuántas porciones de frutas consume al día?", 
                  ["Ninguna o menos de 1", "1 a 2 porciones", "2 o más porciones"])

    # 5. Cereales Integrales
    p5 = st.radio("¿Cuántas porciones de cereales integrales consume al día?", 
                  ["Ninguna o menos de 1", "1 a 2 porciones", "2 o más porciones"])

    # 6. Carnes Magras
    p6 = st.radio("¿Cuántas veces a la semana consume carnes con poca grasa (ave, pavo, cerdo magro)?", 
                  ["Ninguna", "1 a 4 veces", "5 a 8 veces", "más de 8 veces"])

    # 7. Carnes Grasas
    p7 = st.radio("¿Cuántas veces a la semana consume carnes altas en grasa o procesadas?", 
                  ["Ninguna o menos de 1", "1 a 2 veces", "más de 2 veces"])

    # 8. Pescados
    p8 = st.radio("¿Cuántas veces a la semana consume pescados o mariscos?", 
                  ["ninguna o menos de 1", "1 a 2 veces", "más de 2"])

    # 9. Lácteos Descremados
    st.subheader("Lácteos y Otros")
    p9_1 = st.selectbox("¿Consume lácteos descremados o fermentados al día?", ["No", "Sí"])
    p9_2 = "no consumo"
    if p9_1 == "Sí":
        p9_2 = st.radio("¿Cuántas tazas al día?", ["1 o menos tazas", "más de 1 taza"])

    # 10. Lácteos Enteros
    p10_1 = st.selectbox("¿Consume diariamente leche entera, mantequilla o crema?", ["No", "Sí"])
    p10_2 = "No"
    p10_3 = "No"
    if p10_1 == "Sí":
        p10_2 = st.checkbox("¿Consume regularmente más de 1 taza de leche entera al día?")
        p10_3 = st.checkbox("¿Consume regularmente más de 2 cucharaditas de mantequilla/crema al día?")

    # 11, 12. Grasas Saludables (Oliva, Canola, Palta)
    st.subheader("Grasas Saludables")
    p11_1 = st.selectbox("¿Consume regularmente aceite de oliva?", ["No", "Sí"])
    p11_2 = "Ninguna"
    if p11_1 == "Sí":
        p11_2 = st.radio("¿Cuántas cucharaditas al día?", ["1 a 2 cucharaditas", "3 o más cucharaditas"])
    
    p12_1 = st.radio("¿Usa aceite de canola puro?", ["No", "No sabe / no lo conoce", "Ocasionalmente", "Sí"])
    p12_2 = st.radio("¿Cuántas paltas consume a la semana?", ["ninguna o menos de ½ palta", "½ a 3 paltas", "más de 3 paltas"])

    # 13. Vino
    p13_1 = st.selectbox("¿Consume regularmente vino con las comidas (4+ veces semana)?", ["No", "Sí"])
    p13_2 = "menos de 1 copa"
    if p13_1 == "Sí":
        p13_2 = st.radio("¿Cuántas copas al día en promedio?", ["menos de 1 copa", "1 a 2 copas", "más de 2 copas"])

    # 14. Azúcar y Bebidas
    st.subheader("Azúcares")
    p14_1 = st.selectbox("¿Consume dulces/postres con azúcar más de 1 vez al día?", ["No", "Sí"])
    p14_2 = st.selectbox("¿Consume bebidas gaseosas o jugos con azúcar?", ["No", "Sí"])
    p14_3 = st.radio("¿Cuántas cucharaditas de azúcar consume al día?", ["Ninguna o endulzantes", "menos de 4 cucharaditas", "4 o más cucharaditas"])

    submit = st.form_submit_button("Calcular mi Puntaje")

if submit:
    score = 0.0

    # Lógica de Puntaje simple (0, 0.5, 1)
    mapping = {"Ninguna o menos de 1": 0, "1 a 3 porciones": 0.5, "3 o más porciones": 1,
               "1 a 2 veces": 0.5, "más de 2 veces": 1, "1 a 2 porciones": 0.5, "2 o más porciones": 1,
               "1 a 2": 0.5, "más de 2": 1, "más de 3": 1}

    # 1-5, 8
    score += 0 if "menos de 1" in p1 else (0.5 if "1 a 3" in p1 else 1)
    score += 0 if "menos de 1" in p2 else (0.5 if "1 a 2" in p2 else 1)
    score += 0 if "menos de 1" in p3 else (0.5 if "1 a 2" in p3 else 1)
    score += 0 if "menos de 1" in p4 else (0.5 if "1 a 2" in p4 else 1)
    score += 0 if "menos de 1" in p5 else (0.5 if "1 a 2" in p5 else 1)
    score += 0 if "menos de 1" in p8 else (0.5 if "1 a 2" in p8 else 1)

    # 6. Carnes Magras
    if p6 == "1 a 4 veces": score += 0.5
    elif p6 == "5 a 8 veces": score += 1
    
    # 7. Carnes Grasas
    if p7 == "Ninguna o menos de 1": score += 1
    elif p7 == "1 a 2 veces": score += 0.5

    # 9. Lácteos Descremados
    if p9_1 == "Sí":
        score += 1 if p9_2 == "más de 1 taza" else 0.5

    # 10. Lácteos Enteros
    if p10_1 == "No": score += 1
    elif not p10_2 and not p10_3: score += 0.5

    # 13. Vino
    if p13_1 == "Sí" and p13_2 == "1 a 2 copas": score += 1
    elif p13_1 == "Sí": score += 0.5

    # 14. Azúcar
    if p14_1 == "No" and p14_2 == "No" and "Ninguna" in p14_3: score += 1
    elif p14_1 == "No" and p14_2 == "No" and "menos de 4" in p14_3: score += 0.5

    # --- Lógica Especial de Aceite de Oliva/Palta/Canola (0 a 2 pts) ---
    pts_oliva = 0
    if p11_1 == "Sí":
        pts_oliva = 1 if "3 o más" in p11_2 else 0.5
    
    pts_canola = 1 if p12_1 == "Sí" else (0.5 if p12_1 == "Ocasionalmente" else 0)
    pts_palta = 1 if "más de 3" in p12_2 else (0.5 if "½ a 3" in p12_2 else 0)
    
    suma_pc = pts_canola + pts_palta
    
    extra_fat_score = 0
    if pts_oliva == 1: extra_fat_score = 2
    elif pts_oliva == 0.5:
        extra_fat_score = 1.5 if suma_pc >= 1.5 else (1.0 if suma_pc == 1 else 0.5)
    else: # Oliva = 0
        extra_fat_score = 1.0 if suma_pc >= 1.5 else (0.5 if suma_pc == 1 else 0)
    
    score += extra_fat_score

# Mostrar Resultado Final basado en la imagen técnica
    st.divider()
    st.header(f"Tu puntaje final es: {score} / 14")
    
    if 9 <= score <= 14:
        st.success("### **Alta adherencia**")
        st.write("Tu alimentación es de tipo mediterráneo (buena calidad o saludable).")
        st.balloons() # Un pequeño efecto visual de celebración
        
    elif 5 <= score <= 8.5:
        st.warning("### **Adherencia moderada**")
        st.write("Tu dieta tiene una adherencia moderada a la alimentación mediterránea (regular calidad).")
        
    else: # Menos de 5 puntos
        st.error("### **Baja adherencia**")
        st.write("Tu dieta se define con baja adherencia a este patrón alimentario (mala calidad).")

    st.info("""
    **Nota:** Esta categorización se realiza según terciles de puntaje establecidos 
    en el protocolo del Índice Chileno de Dieta Mediterránea (IDM-Chile).
    """)