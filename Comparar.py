import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora de Descontos", layout="wide")
st.title("💸 Calculadora de Descontos")
st.markdown("Escolha o modo de utilização abaixo:")

# Menu de escolha
modo = st.radio("Selecione o modo:", ["🔹 Modo Normal", "⚖️ Comparação de Cenários"])

# --------------------------------------------------------
# MODO NORMAL (igual ao app_sem_uber original, mas ajustado)
# --------------------------------------------------------
if modo == "🔹 Modo Normal":
    st.subheader("Insira os valores:")

    valor_inicial = st.number_input("💰 Valor inicial", min_value=0.0, value=100.0, step=10.0)
    perc_pat = st.number_input("👔 Percentagem Patrão (%)", min_value=0.0, value=12.0, step=1.0)
    desc_seguro = st.number_input("🛡️ Desconto Seguro", min_value=0.0, value=6.0, step=1.0)
    desc_combustivel = st.number_input("⛽ Desconto Combustível", min_value=0.0, value=30.0, step=1.0)

    st.markdown("---")

    if st.button("Calcular 🔹", use_container_width=True):
        st.subheader("📊 Resultado detalhado:")

        valor = valor_inicial

        # Patrão
        desconto_pat = valor * (perc_pat / 100)
        valor -= desconto_pat
        st.markdown(f"<div style='background-color:#CCE5FF;padding:10px;border-radius:5px'>"
                    f"- {perc_pat}% Patrão: -{desconto_pat:.2f} → {valor:.2f}</div>", unsafe_allow_html=True)

        # Seguro
        valor -= desc_seguro
        st.markdown(f"<div style='background-color:#CCFFCC;padding:10px;border-radius:5px'>"
                    f"- Seguro: -{desc_seguro:.2f} → {valor:.2f}</div>", unsafe_allow_html=True)

        # Combustível
        valor -= desc_combustivel
        st.markdown(f"<div style='background-color:#FFF2CC;padding:10px;border-radius:5px'>"
                    f"- Combustível: -{desc_combustivel:.2f} → {valor:.2f}</div>", unsafe_allow_html=True)

        st.success(f"💰 Valor final após descontos: {valor:.2f}")

# --------------------------------------------------------
# MODO COMPARAÇÃO
# --------------------------------------------------------
else:
    st.subheader("Comparador: Empresa 7% + Aluguer 280€ vs 12% + Seguro 45€")

    valor_inicial = st.number_input("💰 Valor inicial", min_value=0.0, value=800.0, step=10.0)
    combustivel = st.number_input("⛽ Combustível", min_value=0.0, value=210.0, step=10.0)

    st.markdown("---")

    if st.button("Comparar ⚖️", use_container_width=True):
        # Cenário A
        valor_a = valor_inicial
        desconto_a = valor_a * 0.07
        valor_a -= desconto_a
        valor_a -= 280
        valor_a -= combustivel

        # Cenário B
        valor_b = valor_inicial
        desconto_b = valor_b * 0.12
        valor_b -= desconto_b
        valor_b -= 45
        valor_b -= combustivel

        # Mostrar comparação
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Cenário A (7% + Aluguer 280€)")
            st.markdown(f"""
            - Empresa 7%: -{desconto_a:.2f}  
            - Aluguer: -280.00  
            - Combustível: -{combustivel:.2f}  
            ---
            ✅ **Valor final: {valor_a:.2f}**
            """)

        with col2:
            st.subheader("📊 Cenário B (12% + Seguro 45€)")
            st.markdown(f"""
            - Empresa 12%: -{desconto_b:.2f}  
            - Seguro: -45.00  
            - Combustível: -{combustivel:.2f}  
            ---
            ✅ **Valor final: {valor_b:.2f}**
            """)

        # Melhor opção
        st.markdown("---")
        if valor_a > valor_b:
            st.success(f"💡 Melhor opção: **Cenário A (7% + Aluguer 280€)** → Diferença de {valor_a - valor_b:.2f} €")
        elif valor_b > valor_a:
            st.success(f"💡 Melhor opção: **Cenário B (12% + Seguro 45€)** → Diferença de {valor_b - valor_a:.2f} €")
        else:
            st.info("⚖️ Ambos os cenários dão o mesmo resultado.")
