import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora de Descontos (sem Uber)", layout="centered")
st.title("💸 Calculadora de Descontos (sem Uber)")
st.markdown("Calcule rapidamente os descontos da Empresa, Aluguer, Seguro e Combustível.")

# Entrada principal
st.subheader("Insira os valores:")
valor_inicial = st.number_input("💰 Valor inicial", min_value=0.0, value=700.0, step=10.0)

# Linha dividida em 2 colunas
col1, col2 = st.columns(2)
with col1:
    perc_esq = st.number_input("👔 Empresa (%)", min_value=0.0, value=7.0, step=0.5)
    aluguer = st.number_input("🏠 Aluguer (€)", min_value=0.0, value=280.0, step=1.0)
with col2:
    perc_dir = st.number_input("👔 Empresa (%)", min_value=0.0, value=12.0, step=0.5)
    seguro = st.number_input("🛡️ Seguro (€)", min_value=0.0, value=45.0, step=1.0)

desc_combustivel = st.number_input("⛽ Desconto Combustível (€)", min_value=0.0, value=200.0, step=1.0)

st.markdown("---")

if st.button("Calcular 🔹", use_container_width=True):
    st.subheader("📊 Resultados Detalhados:")

    # Cálculos dos descontos
    desconto_dir = valor_inicial * (perc_dir / 100)
    desconto_esq = valor_inicial * (perc_esq / 100)

    # Valores intermediários
    subtotal1 = valor_inicial - desconto_dir
    subtotal2 = subtotal1 - desconto_esq
    subtotal3 = subtotal2 - aluguer
    subtotal4 = subtotal3 - seguro
    subtotal_final = subtotal4 - desc_combustivel

    # Mostrar cada desconto em cores diferentes
    st.markdown(f"<div style='background-color:#CCE5FF;padding:10px;border-radius:5px'>"
                f"- Empresa direita ({perc_dir}%): -{desconto_dir:.2f} € → {subtotal1:.2f} €</div>", unsafe_allow_html=True)

    st.markdown(f"<div style='background-color:#FFD9B3;padding:10px;border-radius:5px'>"
                f"- Empresa esquerda ({perc_esq}%): -{desconto_esq:.2f} € → {subtotal2:.2f} €</div>", unsafe_allow_html=True)

    st.markdown(f"<div style='background-color:#CCFFCC;padding:10px;border-radius:5px'>"
                f"- Aluguer: -{aluguer:.2f} € → {subtotal3:.2f} €</div>", unsafe_allow_html=True)

    st.markdown(f"<div style='background-color:#FFCCCC;padding:10px;border-radius:5px'>"
                f"- Seguro: -{seguro:.2f} € → {subtotal4:.2f} €</div>", unsafe_allow_html=True)

    st.markdown(f"<div style='background-color:#FFF2CC;padding:10px;border-radius:5px'>"
                f"- Combustível: -{desc_combustivel:.2f} € → {subtotal_final:.2f} €</div>", unsafe_allow_html=True)

    # Resultados finais lado a lado
    res1, res2 = st.columns(2)
    with res1:
        st.success(f"💰 Resultado 1 (Empresa direita + Combustível): {valor_inicial - desconto_dir - desc_combustivel:.2f} €")
    with res2:
        st.success(f"💰 Resultado 2 (Empresa esquerda + Empresa direita + Aluguer + Seguro + Combustível): {subtotal_final:.2f} €")
