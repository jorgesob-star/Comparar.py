import streamlit as st

# Configuração da página
st.set_page_config(page_title="Comparador Empresa vs Aluguer/Seguro", layout="wide")
st.title("⚖️ Comparador de Cenários")
st.markdown("Compare dois modelos: **Empresa 7% + Aluguer 280€** vs **Empresa 12% + Seguro 45€**")

# Entrada
valor_inicial = st.number_input("💰 Valor inicial", min_value=0.0, value=800.0, step=10.0)
combustivel = st.number_input("⛽ Combustível", min_value=0.0, value=210.0, step=10.0)

st.markdown("---")

if st.button("Comparar 🔹", use_container_width=True):
    # -----------------------
    # Cenário A - Empresa 7% + Aluguer 280€
    # -----------------------
    valor_a = valor_inicial

    # Empresa 7%
    desconto_empresa_a = valor_a * 0.07
    valor_a -= desconto_empresa_a

    # Aluguer
    valor_a -= 280

    # Combustível
    valor_a -= combustivel

    # -----------------------
    # Cenário B - Empresa 12% + Seguro 45€
    # -----------------------
    valor_b = valor_inicial

    # Empresa 12%
    desconto_empresa_b = valor_b * 0.12
    valor_b -= desconto_empresa_b

    # Seguro
    valor_b -= 45

    # Combustível
    valor_b -= combustivel

    # -----------------------
    # Mostrar comparação
    # -----------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Cenário A")
        st.markdown(f"""
        - Empresa 7%: -{desconto_empresa_a:.2f}  
        - Aluguer: -280.00  
        - Combustível: -{combustivel:.2f}  
        ---
        ✅ **Valor final: {valor_a:.2f}**
        """)

    with col2:
        st.subheader("📊 Cenário B")
        st.markdown(f"""
        - Empresa 12%: -{desconto_empresa_b:.2f}  
        - Seguro: -45.00  
        - Combustível: -{combustivel:.2f}  
        ---
        ✅ **Valor final: {valor_b:.2f}**
        """)

    # Resultado da comparação
    st.markdown("---")
    if valor_a > valor_b:
        st.success(f"💡 Melhor opção: **Cenário A (7% + Aluguer 280€)** → Diferença de {valor_a - valor_b:.2f}")
    elif valor_b > valor_a:
        st.success(f"💡 Melhor opção: **Cenário B (12% + Seguro 45€)** → Diferença de {valor_b - valor_a:.2f}")
    else:
        st.info("⚖️ Ambos os cenários dão o mesmo resultado.")
