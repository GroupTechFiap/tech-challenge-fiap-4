import streamlit as st
import pandas as pd
import pickle
import sklearn.compose._column_transformer as ct

# 🔧 Correção para modelos salvos em outra versão
if not hasattr(ct, "_RemainderColsList"):
    class _RemainderColsList(list):
        pass
    ct._RemainderColsList = _RemainderColsList

# Configuração da página
st.set_page_config(
    page_title="Sistema Preditivo de Saúde",
    page_icon="🏥",
    layout="centered"
)

# Carregar modelo
with open("modelo_treinado.pkl", "rb") as f:
    modelo = pickle.load(f)

# Título
st.title("Classificação de Peso Corporal")
st.markdown("---")

st.subheader("📋 Informações do Paciente")

# Inputs organizados verticalmente
genero = st.selectbox("Gênero", ["Masculino", "Feminino"])
idade = st.number_input("Idade", min_value=10, max_value=100)
altura = st.number_input("Altura (m)", format="%.2f")
peso = st.number_input("Peso (kg)", format="%.1f")

historico = st.selectbox("Histórico Familiar de Obesidade", ["há histórico", "não há"])
caloricos = st.selectbox("Consumo frequente de alimentos muito calóricos", ["sim", "não"])
vegetais = st.selectbox("Frequência de consumo de vegetais", ["nunca", "raramente", "às vezes", "sempre"])
refeicoes = st.selectbox("Número de refeições principais por dia", ["uma refeição", "duas", "três", "quatro ou mais"])
lanches = st.selectbox("Consumo de lanches", ["nunca", "às vezes", "frequentemente"])
fumante = st.selectbox("Fumante", ["fuma", "não fuma"])
agua = st.selectbox("Consumo diário de água", ["< 1 L/dia", "1-2 L/dia", "2 L/dia", "> 2 L/dia"])
monitora = st.selectbox("Monitora ingestão calórica", ["sim", "não"])
atividade = st.selectbox("Atividade física semanal", ["nenhuma", "~1-2x/sem", "3-4x/sem", "5x/sem"])
tempo_tela = st.selectbox("Tempo diário de tela", ["~0-2 h/dia", "~3-5 h/dia", "> 5 h/dia"])
alcool = st.selectbox("Consumo de álcool", ["não bebe", "às vezes", "frequentemente"])
transporte = st.selectbox("Transporte habitual", ["a pé", "bicicleta", "carro", "transporte público", "moto"])

st.markdown("---")

# Criar DataFrame
input_df = pd.DataFrame({
    "Gênero": [genero],
    "Idade": [idade],
    "Altura": [altura],
    "Peso": [peso],
    "Histórico Familiar": [historico],
    "Consumo frequente de alimentos muito calóricos": [caloricos],
    "Frequência de consumo de vegetais nas refeições": [vegetais],
    "Número de refeições principais por dia": [refeicoes],
    "Consumo de lanches/comes entre as refeições": [lanches],
    "Fumante": [fumante],
    "Consumo diário de água": [agua],
    "Monitora a ingestão calórica diária": [monitora],
    "Frequência semanal de atividade física": [atividade],
    "Tempo diário usando dispositivos eletrônicos": [tempo_tela],
    "Consumo de bebida alcoólica": [alcool],
    "Meio de transporte habitual": [transporte]
})

# Botão centralizado
if st.button("🔍 Realizar Previsão"):
    resultado = modelo.predict(input_df)

    st.markdown("## 🎯 Resultado da Análise")
    st.success(f"Classe prevista: {resultado[0]}")

st.markdown("---")