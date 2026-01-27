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
        "temperatura": "Fogo médio",
        "preparacao": [
            "Desfiar o bacalhau.",
            "Refogar cebola e alho em azeite.",
            "Adicionar o bacalhau desfiado.",
            "Juntar a batata palha.",
            "Envolver os ovos batidos.",
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
            "Cozer e desfiar o bacalhau.",
            "Fritar batatas em cubos.",
            "Refogar cebola e alho.",
            "Misturar bacalhau, batata e natas.",
            "Colocar num tabuleiro.",
            "Polvilhar com queijo e levar ao forno."
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
            "Dar um murro nas batatas.",
            "Aquecer azeite com alho.",
            "Regar tudo antes de servir."
        ]
    },
    {
        "nome": "Bacalhau à Gomes de Sá",
        "ingredientes": ["bacalhau", "batata", "cebola", "ovos", "azeite", "azeitonas"],
        "modo": "Forno",
        "tempo": "50 minutos",
        "temperatura": "180 ºC",
        "preparacao": [
            "Cozer o bacalhau e as batatas.",
            "Cortar tudo em rodelas.",
            "Dispor em camadas com cebola.",
            "Regar com azeite.",
            "Levar ao forno e adicionar ovos e azeitonas."
        ]
    },
    {
        "nome": "Bacalhau com Broa",
        "ingredientes": ["bacalhau", "broa", "alho", "azeite"],
        "modo": "Forno",
        "tempo": "40 minutos",
        "temperatura": "180 ºC",
        "preparacao": [
            "Assar o bacalhau.",
            "Triturar broa com alho e azeite.",
            "Cobrir o bacalhau.",
            "Levar novamente ao forno."
        ]
    },
    {
        "nome": "Salada de Bacalhau",
        "ingredientes": ["bacalhau", "grão", "cebola", "azeite", "vinagre"],
        "modo": "Frio",
        "tempo": "15 minutos",
        "temperatura": "Não aplicável",
        "preparacao": [
            "Cozer o bacalhau e o grão.",
            "Desfiar o bacalhau.",
            "Misturar todos os ingredientes.",
            "Temperar com azeite e vinagre."
        ]
    },
    {
        "nome": "Pataniscas",
        "ingredientes": ["bacalhau", "farinha", "ovos", "cebola", "salsa"],
        "modo": "Fritar",
        "tempo": "25 minutos",
        "temperatura": "Óleo médio",
        "preparacao": [
            "Desfiar o bacalhau.",
            "Misturar farinha e ovos.",
            "Adicionar cebola e salsa.",
            "Fritar colheradas até dourar."
        ]
    },
    {
        "nome": "Arroz de Bacalhau",
        "ingredientes": ["bacalhau", "arroz", "tomate", "cebola", "alho"],
        "modo": "Fogão",
        "tempo": "30 minutos",
        "temperatura": "Fogo médio",
        "preparacao": [
            "Refogar cebola e alho.",
            "Adicionar tomate.",
            "Juntar bacalhau desfiado.",
            "Adicionar arroz e água.",
            "Cozinhar até o arroz estar pronto."
        ]
    },
    {
        "nome": "Bacalhau à Portuguesa",
        "ingredientes": ["bacalhau", "batata", "ovos", "cebola", "azeite"],
        "modo": "Fogão",
        "tempo": "35 minutos",
        "temperatura": "Fogo médio",
        "preparacao": [
            "Cozer bacalhau, batatas e ovos.",
            "Cortar em rodelas.",
            "Regar com azeite e cebola."
        ]
    },
    {
        "nome": "Bacalhau Espiritual",
        "ingredientes": ["bacalhau", "cenoura", "pão", "leite", "cebola", "azeite"],
        "modo": "Forno",
        "tempo": "45 minutos",
        "temperatura": "180 ºC",
        "preparacao": [
            "Cozer o bacalhau.",
            "Demolhar pão em leite.",
            "Misturar todos os ingredientes.",
            "Levar ao forno até gratinar."
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

    nova["preparacao"] = [
        passo.replace("bacalhau", substituto)
             .replace("Bacalhau", substituto.capitalize())
        for passo in receita["preparacao"]
    ]

    return nova


def ingredientes_em_falta(receita, ingredientes_user):
    return [ing for ing in receita["ingredientes"] if ing not in ingredientes_user]


def receitas_possiveis(lista_receitas, ingredientes_user):
    return [r for r in lista_receitas if not ingredientes_em_falta(r, ingredientes_user)]

# =========================
# INTERFACE
# =========================

st.set_page_config(page_title="App de Receitas", layout="centered")
st.title("🍽️ App de Receitas Inteligente")

tem_bacalhau = st.radio("Tens bacalhau?", ["Sim", "Não"])

substituto = "bacalhau"

if tem_bacalhau == "Não":
    st.subheader("🔁 Ingredientes que podem substituir o bacalhau")
    substituto = st.selectbox(
        "Escolhe o ingrediente:",
        ["frango", "alho francês", "atum", "cogumelos", "legumes"]
    )

# Adaptar TODAS as receitas
receitas_ativas = [
    adaptar_receita(r, substituto) if substituto != "bacalhau" else r
    for r in receitas
]

# =========================
# INGREDIENTES DO UTILIZADOR
# =========================

st.subheader("🥗 Ingredientes que tens em casa")

todos_ingredientes = sorted({ing for r in receitas_ativas for ing in r["ingredientes"]})

ingredientes_user = st.multiselect("Seleciona:", todos_ingredientes)

# 👉 REGRA FINAL (bug resolvido definitivamente)
if substituto != "bacalhau" and substituto not in ingredientes_user:
    ingredientes_user.append(substituto)

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
                for i, passo in enumerate(r["preparacao"], 1):
                    st.write(f"{i}. {passo}")
