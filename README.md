# 🏥 Sistema Preditivo de Obesidade

## Tech Challenge FIAP -- Machine Learning aplicado à Saúde

------------------------------------------------------------------------

## 📌 Visão Geral Executiva

Este projeto foi desenvolvido como parte do Tech Challenge da FIAP com
foco na aplicação de técnicas de Machine Learning para apoio à tomada de
decisão médica.

A solução consiste em um modelo preditivo capaz de classificar o nível
de obesidade de um paciente com base em variáveis demográficas,
comportamentais e de estilo de vida. O modelo foi disponibilizado em
produção por meio de uma aplicação web interativa construída com
Streamlit.

O objetivo estratégico da solução é apoiar diagnósticos, reduzir
subjetividade clínica e fornecer uma ferramenta baseada em dados para
suporte à decisão.

------------------------------------------------------------------------

## 🎯 Objetivo de Negócio

Desenvolver um sistema inteligente capaz de:

-   Auxiliar profissionais de saúde na identificação do nível de
    obesidade
-   Apoiar estratégias preventivas
-   Reduzir riscos associados a diagnósticos tardios
-   Transformar dados em informação acionável

------------------------------------------------------------------------

## 🧠 Arquitetura da Solução

A solução foi estruturada em duas camadas principais:

### 1️⃣ Camada de Machine Learning

-   Tratamento e preparação dos dados
-   Codificação de variáveis categóricas
-   Treinamento de modelo de classificação
-   Avaliação com métricas de desempenho (acurácia \> 75%)
-   Serialização do modelo treinado

O modelo final está armazenado no arquivo:

    modelo_treinado.pkl

### 2️⃣ Camada de Aplicação (Interface)

-   Desenvolvida com Streamlit
-   Interface interativa para inserção dos dados do paciente
-   Processamento automático das entradas
-   Predição em tempo real
-   Exibição clara e objetiva do resultado

Arquivo principal da aplicação:

    app.py

------------------------------------------------------------------------

## 📂 Estrutura do Repositório

    GroupTechFiap/
    │
    ├── app.py                 # Aplicação Streamlit
    ├── modelo_treinado.pkl    # Modelo de Machine Learning treinado
    ├── requirements.txt       # Dependências do projeto
    ├── runtime.txt            # Versão do Python utilizada no deploy

------------------------------------------------------------------------

## 🛠️ Stack Tecnológica

-   Python
-   Pandas
-   NumPy
-   Scikit-learn
-   Streamlit
-   Git & GitHub

------------------------------------------------------------------------

## 🚀 Deploy e Produção

A aplicação foi publicada via Streamlit Cloud, com deploy contínuo
integrado ao GitHub.

Arquivos críticos para o deploy:

-   requirements.txt → Gerenciamento de dependências
-   runtime.txt → Definição da versão do Python

O modelo é carregado dinamicamente na inicialização da aplicação,
garantindo inferência rápida e estável.

------------------------------------------------------------------------

## 📊 Impacto Estratégico

Esta solução demonstra a aplicação prática de Data Science no setor da
saúde, permitindo:

-   Apoio à decisão clínica baseada em dados
-   Maior padronização na análise de risco
-   Escalabilidade da solução via web
-   Integração entre Machine Learning e aplicação em produção

O projeto evidencia a capacidade de transformar um modelo analítico em
um produto funcional, pronto para uso em ambiente real.

------------------------------------------------------------------------
