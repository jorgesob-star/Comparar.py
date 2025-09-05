import streamlit as st

# Configuração da página
st.set_page_config(page_title="Comparador de Descontos", layout="centered")
st.title("💸 Comparador de Descontos")

# --- Definição dos valores padrão iniciais ---
DEFAULTS = {
    'aluguer': 280.0,
    'perc_aluguer': 7.0,
    'seguro': 45.0,
    'perc_seguro': 12.0,
    'manutencao': 20.0
}

# Inicializa o estado da sessão com os valores padrão, se ainda não existirem
for key, value in DEFAULTS.items():
    if f'default_{key}' not in st.session_state:
        st.session_state[f'default_{key}'] = value

# --- Entradas do Usuário ---
st.header("Entradas do Usuário")

apuro = st.number_input("💰 Apuro total (€)", min_value=0.0, value=800.0, step=10.0, help="O valor total bruto que você recebeu.")
desc_combustivel = st.number_input("⛽ Desconto de Combustível (€)", min_value=0.0, value=200.0, step=1.0, help="O valor que você gasta com combustível e que é deduzido do apuro.")

st.markdown("---")

# --- Lógica para mostrar as opções ---
st.header("Opções da Empresa")

# Botão para alternar a visibilidade dos campos de entrada
if st.button("Modificar Opções Padrão"):
    st.session_state.show_inputs = not st.session_state.get('show_inputs', False)

def save_defaults():
    """Função de callback para salvar os valores dos inputs como novos padrões."""
    st.session_state.default_aluguer = st.session_state.aluguer_input
    st.session_state.default_perc_aluguer = st.session_state.perc_aluguer_input
    st.session_state.default_seguro = st.session_state.seguro_input
    st.session_state.default_perc_seguro = st.session_state.perc_seguro_input
    st.session_state.default_manutencao = st.session_state.manutencao_input
    st.success("Novos valores padrão salvos com sucesso!")

if st.session_state.get('show_inputs', False):
    # Colunas para organizar as opções lado a lado
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Opção 1")
        st.number_input("🏠 Aluguer (€)", min_value=0.0, value=st.session_state.default_aluguer, step=1.0, key='aluguer_input')
        st.number_input("👔 Percentual (%)", min_value=0.0, value=st.session_state.default_perc_aluguer, step=0.5, key='perc_aluguer_input')
    with col2:
        st.subheader("Opção 2")
        st.number_input("🛡️ Seguro (€)", min_value=0.0, value=st.session_state.default_seguro, step=1.0, key='seguro_input')
        st.number_input("👔 Percentual (%)", min_value=0.0, value=st.session_state.default_perc_seguro, step=0.5, key='perc_seguro_input')
        st.number_input("🛠️ Manutenção (€)", min_value=0.0, value=st.session_state.default_manutencao, step=1.0, key='manutencao_input')
        
    # Novo botão para salvar as alterações padrão
    st.button("💾 Salvar Alterações Padrão", on_click=save_defaults)

else:
    st.info("Valores padrão das opções estão sendo usados. Clique no botão acima para modificá-los.")

st.markdown("---")

# Botão para iniciar o cálculo
if st.button("Calcular 🔹", type="primary"):
    # Subtrair combustível do apuro para obter o valor líquido
    apuro_liquido = apuro - desc_combustivel
    
    # Pega os valores atuais (padrão ou modificados e salvos)
    aluguer_atual = st.session_state.default_aluguer
    perc_aluguer_atual = st.session_state.default_perc_aluguer
    seguro_atual = st.session_state.default_seguro
    perc_seguro_atual = st.session_state.default_perc_seguro
    manutencao_atual = st.session_state.default_manutencao

    # Cálculo do que sobra em cada opção
    sobra_opcao1 = apuro_liquido - (apuro * perc_aluguer_atual / 100) - aluguer_atual
    sobra_opcao2 = apuro_liquido - (apuro * perc_seguro_atual / 100) - seguro_atual - manutencao_atual
    
    st.subheader("📊 Resultados:")
    st.metric("Apuro Líquido", f"{apuro_liquido:,.2f} €", help="Apuro total menos o desconto de combustível.")
    st.markdown("---")

    # Exibir resultados detalhados
    st.markdown("### Visão Geral")
    col3, col4 = st.columns(2)
    with col3:
        st.metric(f"Sobra na Opção 1", f"{sobra_opcao1:,.2f} €")
    with col4:
        st.metric(f"Sobra na Opção 2", f"{sobra_opcao2:,.2f} €")
    
    # Determinar e exibir a melhor opção
    if sobra_opcao1 > sobra_opcao2:
        st.success(f"🎉 A **Opção 1** é a melhor escolha, com uma diferença de **{(sobra_opcao1 - sobra_opcao2):,.2f} €**.")
    elif sobra_opcao2 > sobra_opcao1:
        st.success(f"🎉 A **Opção 2** é a melhor escolha, com uma diferença de **{(sobra_opcao2 - sobra_opcao1):,.2f} €**.")
    else:
        st.info("As duas opções resultam no mesmo valor.")
        
    st.markdown("---")
    
    # Detalhe dos cálculos
    st.markdown("### Detalhes dos Cálculos")
    st.markdown(f"""
    **Cálculo da Opção 1:**
    * Apuro Líquido: {apuro_liquido:,.2f} €
    * Dedução da Empresa: {apuro:,.2f} € * ({perc_aluguer_atual} / 100) = **{(apuro * perc_aluguer_atual / 100):,.2f} €**
    * Dedução de Aluguer: **{aluguer_atual:,.2f} €**
    * **Valor Final:** {apuro_liquido:,.2f} - {(apuro * perc_aluguer_atual / 100):,.2f} - {aluguer_atual:,.2f} = **{sobra_opcao1:,.2f} €**
    """)
    
    st.markdown(f"""
    **Cálculo da Opção 2:**
    * Apuro Líquido: {apuro_liquido:,.2f} €
    * Dedução da Empresa: {apuro:,.2f} € * ({perc_seguro_atual} / 100) = **{(apuro * perc_seguro_atual / 100):,.2f} €**
    * Dedução de Seguro: **{seguro_atual:,.2f} €**
    * Dedução de Manutenção: **{manutencao_atual:,.2f} €**
    * **Valor Final:** {apuro_liquido:,.2f} - {(apuro * perc_seguro_atual / 100):,.2f} - {seguro_atual:,.2f} - {manutencao_atual:,.2f} = **{sobra_opcao2:,.2f} €**
    """)
