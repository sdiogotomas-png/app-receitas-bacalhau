import streamlit as st

# =========================
# BASE DE DADOS DE RECEITAS
# =========================

receitas = [
    {
        "nome": "Bacalhau à Brás",
        "ingredientes": ["bacalhau", "batata palha", "ovos", "cebola", "alho", "azeite", "salsa"],
        "modo": "Fogão",
        "tempo": "20 minutos",
        "temperatura": "Médio",
        "preparacao": [
            "Demolhar e desfiar o bacalhau.",
            "Refogar cebola e alho em azeite.",
            "Juntar o bacalhau desfiado.",
            "Adicionar batata palha.",
            "Envolver ovos batidos.",
            "Finalizar com salsa."
        ]
    },
    {
        "nome": "Bacalhau com Natas",
        "ingredientes": ["bacalhau", "batata", "cebola", "alho", "natas", "azeite", "queijo"],
        "modo": "Forno",
        "tempo": "45 minutos",
        "temperatura": "180 ºC",
        "preparacao": [
            "Cozer o bacalhau e desfiar.",
            "Fritar batatas em cubos.",
            "Refogar cebola e alho.",
            "Misturar bacalhau, batata e natas.",
            "Colocar num tabuleiro.",
            "Polvilhar com queijo e levar ao forno."
        ]
    },
    {
        "nome": "Pataniscas",
        "ingredientes": ["bacalhau", "farinha", "ovos", "cebola", "salsa"],
        "modo": "Fritar",
        "tempo": "25 minutos",
        "temperatura": "Óleo médio",
        "preparacao": [
            "Desfiar bacalhau cozido.",
            "Misturar farinha, ovos e água.",
            "Juntar cebola, salsa e bacalhau.",
            "Aquecer óleo.",
            "Fritar colheradas até dourar."
        ]
    },
    {
        "nome": "Bacalhau à Lagareiro",
        "ingredientes": ["bacalhau", "batata a murro", "alho", "azeite"],
        "modo": "Forno",
        "tempo": "50 minutos",
        "temperatura": "190 ºC",
        "preparacao": [
            "Assar o bacalhau.",
            "Dar murro nas batatas.",
            "Aquecer azeite com alho.",
            "Regar tudo e levar novamente ao forno."
        ]
    },
    {
        "nome": "Arroz de Bacalhau",
        "ingredientes": ["bacalhau", "arroz", "tomate", "cebola", "alho"],
        "modo": "Fogão",
        "tempo": "30 minutos",
        "temperatura": "Médio",
        "preparacao": [
            "Refogar cebola e alho.",
            "Adicionar tomate.",
            "Juntar bacalhau desfiado.",
            "Adicionar arroz e água.",
            "Cozinhar até o arroz estar pronto."
        ]
    }
]

# =========================
# FUNÇÕES
# =========================

def adaptar_receita(receita, substituto):
    nova = receita.copy()
    nova["nome"] = receita["nome"].replace("Bacalhau", substituto.capitalize())
    nova["ingredientes"] = [
        substituto if ing == "bacalhau" else ing
        for ing in receita["ingredientes"]
    ]
    return nova

def ingredientes_em_falta(receita, ingredientes_user):
    return [ing for ing in receita["ingredientes"] if ing not in ingredientes_user]

def receitas_possiveis(receitas_lista, ingredientes_user):
    return [
        r for r in receitas_lista
        if not ingredientes_em_falta(r, ingredientes_user)
    ]

# =========================
# INTERFACE WEB
# =========================

st.set_page_config(page_title="App de Receitas", layout="centered")
st.title("🍽️ App de Receitas Inteligente")

tem_bacalhau = st.radio("Tens bacalhau?", ["Sim", "Não"])

substituto = "bacalhau"

if tem_bacalhau == "Não":
    st.subheader("🔁 Ingredientes que podem substituir o bacalhau")
    opcoes = ["alho francês", "frango", "atum", "cogumelos", "legumes"]
    substituto = st.selectbox("Escolhe o substituto:", opcoes)

# Adaptar TODAS as receitas se necessário
receitas_ativas = []
for r in receitas:
    if substituto != "bacalhau":
        receitas_ativas.append(adaptar_receita(r, substituto))
    else:
        receitas_ativas.append(r)

st.subheader("🥗 Ingredientes que tens em casa")
ingredientes_user = st.multiselect(
    "Seleciona:",
    sorted({ing for r in receitas_ativas for ing in r["ingredientes"]})
)

# =========================
# RESULTADOS
# =========================

if ingredientes_user:
    possiveis = receitas_possiveis(receitas_ativas, ingredientes_user)

    if possiveis:
        st.success("✅ Receitas que podes fazer:")
        for r in possiveis:
            with st.expander(r["nome"]):
                st.write("**Ingredientes:**", ", ".join(r["ingredientes"]))
                st.write("**Modo:**", r["modo"])
                st.write("**Tempo:**", r["tempo"])
                st.write("**Temperatura:**", r["temperatura"])
                st.write("**Preparação:**")
                for i, passo in enumerate(r["preparacao"], 1):
                    st.write(f"{i}. {passo}")
    else:
        st.error("❌ Não tens ingredientes suficientes.")
        st.subheader("🔍 O que falta para cada receita:")
        for r in receitas_ativas:
            with st.expander(r["nome"]):
                st.write("❗ Faltam:", ", ".join(ingredientes_em_falta(r, ingredientes_user)))
                st.write("**Preparação:**")
                for i, passo in enumerate(r["preparacao"], 1):
                    st.write(f"{i}. {passo}")
