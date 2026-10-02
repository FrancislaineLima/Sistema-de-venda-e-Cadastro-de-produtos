import pandas as pd
import streamlit as st
import plotly.express as px

#python -m streamlit run 4-SistemasdeVendas.pypython -m streamlit run 4-SistemasdeVendas.py
st.set_page_config(
    page_title="Sistema de Vendas",
    page_icon="🌸", # Um ícone combinando com o tema rosa
    layout="wide"
)

tabela_vendas = pd.read_csv("vendas.csv")
cores_rosa_pastel = [
    "#F8BBD0", # Rosa claro (Pink 100 do Material Design)
    "#F06292", # Rosa vibrante médio (Pink 300)
    "#C2185B", # Rosa escuro/magenta (Pink 700)
    "#FCE4EC", # Rosa super claro quase branco
    "#D81B60"  # Rosa forte
]

st.write("# 🌸 Sistemas de Vendas  🌸")

st.write("## Cadastrar Vendas")
data= st.date_input("Data", max_value="today")
vendedor= st.selectbox("Vendedor",["Ana", "Bruno", "Carla"])
produto =st.selectbox("Produto", ["Notebook", "Celular","Fone"])
quantidade = st.number_input("Quantidade", step=1)
valor = st.number_input("Valor")
botao_cadastrar = st.button("Cadastrar Vendas")


if botao_cadastrar :
 nova_venda= [str(data), vendedor, produto, quantidade, valor]
 ultima_linha= len(tabela_vendas)
 tabela_vendas.loc[ultima_linha] = nova_venda
 tabela_vendas.to_csv("vendas.csv", index=False)
 st.success(" Venda Cadastrada!") #uma mensagem para mostrar que funcionou.

st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)


st.write("## Dashboard")
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")
grafico1= px.bar(tabela_vendas, x="vendedor", y="valor", color="produto",  color_discrete_sequence=cores_rosa_pastel)
st.plotly_chart(grafico1)  #mostra o grafico no site
grafico2= px.pie(tabela_vendas, names="produto", values= "valor", color_discrete_sequence=cores_rosa_pastel)
st.plotly_chart(grafico2) #mostra o grafico no site



