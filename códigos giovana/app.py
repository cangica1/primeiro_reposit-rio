import streamlit as st
# st.title(" AAAAAAAAAAAAA 🎧ྀི♪⋆.✮")
# st.write("testando... esquerda, direita")
# st.sidebar.title("barra lateral")

# nomes = ["rihanna", "beyoncé", "Kali Uchis", "Joji", "frank ocean", "tyler the creator"]
# st.sidebar.selectbox("escolha um nome:" , nomes)
# st.video("https://youtu.be/_c76CRVVDE0?feature=shared")


st.sidebar.title("𝐀𝐥𝐮𝐠𝐮𝐞𝐥 𝐝𝐞 𝐂𝐚𝐫𝐫𝐨𝐬 ୨ৎ")
st.sidebar.image("logo.pngg")
st.sidebar.write("escolha o carro ideal para voce")
carros = ["Gol", "BMW", "corsa","Toro"]
opcao = st.sidebar.selectbox("selecione o modelo do carro:", carros)

st.title("𝐆𝐢𝐨𝐯𝐚𝐧𝐚 𝐌𝐨𝐭𝐨𝐫𝐬 - 𝐀𝐥𝐮𝐠𝐮𝐞𝐥 𝐝𝐞 𝐂𝐚𝐫𝐫𝐨𝐬 ⊹ ࣪ ˖")
st.image(f"{opcao}.png", width=800)
st.markdown(f'Voce alugou o modelo {opcao} ⊹ ࣪ ˖')

dias = st.text_input(f"Por quanros dias {opcao} foi alugado?")
km = st.text_input(f"quantos km voce rodou com o {opcao}?")

if opcao == "Toro":
    diaria = 450
elif opcao == "BMW":
    diaria = 500
elif opcao == "corsa":
    diaria =s 250
elif opcao == "Gol":
    diaria = 300

if st.button("calcular"):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st.warning(f" voce alugou o {opcao} por {dias} dias e rodou {km} km. O valor total a pagar é R${aluguel_total:.2f}")