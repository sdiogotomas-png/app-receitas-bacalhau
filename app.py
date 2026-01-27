import streamlit as st

# =========================
# BASE DE DADOS DE RECEITAS
# =========================

receitas = [
    # ---------- RECEITAS ANTERIORES ----------
    {
        "nome": "Bacalhau à Brás",
        "ingredientes": ["bacalhau", "batata palha", "ovos", "cebola", "alho", "azeite", "salsa"],
        "modo": "Fogão",
        "tempo": "20 minutos",
        "temperatura": "Fogo médio",
        "preparacao": [
            "Demolhar e desfiar o bacalhau.",
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
            "Colocar num tabuleiro e polvilhar com queijo.",
            "Levar ao forno até dourar."
        ]
    },
    {
        "nome": "Pataniscas de Bacalhau",
        "ingredientes": ["bacalhau", "farinha", "ovos", "cebola", "salsa"],
        "modo": "Fritar",
        "tempo": "25 minutos",
        "temperatura": "Óleo médio",
        "preparacao": [
            "Desfiar o bacalhau.",
            "Misturar farinha e ovos.",
            "Adicionar cebola, salsa e bacalhau.",
            "Aquecer o óleo.",
            "Fritar colheradas até ficarem douradas."
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
            "Regar o bacalhau e as batatas."
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

    # ---------- +10 NOVAS RECEITAS ----------
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
            "Levar ao forno e finalizar com ovos e azeitonas."
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
            "Triturar a broa com alho e azeite.",
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
        "nome": "Bacalhau à Portuguesa",
        "ingredientes": ["bacalhau", "batata", "ovos", "cebola", "azeite"],
        "modo": "Fogão",
        "tempo": "35 minutos",
        "temperatura": "Fogo médio",
        "preparacao": [
            "Cozer o bacalhau.",
            "Cozer batatas e ovos.",
            "Cortar tudo em rodelas.",
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
            "Misturar tudo.",
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
        ["alho francês", "frango", "atum", "cogumelos", "legumes"]
    )

# Aplicar substituição ANTES de qualquer verificação
receitas_ativas = [
    adaptar_receita(r, substituto) if substituto != "bacalhau" else r
    for r in receitas
]

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
                for i, passo in enumerate(r["preparacao"], 1):
                    st.write(f"{i}. {passo}")
