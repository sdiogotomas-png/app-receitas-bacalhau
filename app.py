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
            "Adicionar o bacalhau desfiado.",
            "Juntar batata palha.",
            "Adicionar ovos batidos e envolver.",
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
            "Fritar a batata em cubos.",
            "Refogar cebola e alho.",
            "Misturar tudo com natas.",
            "Colocar num tabuleiro.",
            "Polvilhar queijo e levar ao forno."
        ]
    },
    {
        "nome": "Pataniscas de Bacalhau",
        "ingredientes": ["bacalhau", "farinha", "ovos", "cebola", "salsa"],
        "modo": "Fritar",
        "tempo": "25 minutos",
        "temperatura": "Óleo médio",
        "preparacao": [
            "Desfiar bacalhau cozido.",
            "Misturar farinha, ovos e água.",
            "Adicionar cebola e salsa.",
            "Envolver o bacalhau.",
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
            "Assar o bacalhau no forno.",
            "Dar murro nas batatas.",
            "Aquecer azeite com alho.",
            "Regar bacalhau e batatas."
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
    },

    # ====== +10 RECEITAS NOVAS ======

    {
        "nome": "Bacalhau à Gomes de Sá",
        "ingredientes": ["bacalhau", "batata", "cebola", "ovos", "azeite", "azeitonas"],
        "modo": "Forno",
        "tempo": "40 minutos",
        "temperatura": "180 ºC",
        "preparacao": [
            "Cozer o bacalhau e desfiar.",
            "Cozer as batatas em rodelas.",
            "Refogar cebola em azeite.",
            "Misturar tudo num tabuleiro.",
            "Adicionar ovos cozidos e azeitonas.",
            "Levar ao forno."
        ]
    },
    {
        "nome": "Bacalhau Assado no Forno",
        "ingredientes": ["bacalhau", "cebola", "alho", "azeite", "batata"],
        "modo": "Forno",
        "tempo": "50 minutos",
        "temperatura": "190 ºC",
        "preparacao": [
            "Colocar bacalhau num tabuleiro.",
            "Adicionar batatas e cebola.",
            "Regar com azeite e alho.",
            "Levar ao forno até assar."
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
        "nome": "Bacalhau com Broa",
        "ingredientes": ["bacalhau", "broa", "alho", "azeite"],
        "modo": "Forno",
        "tempo": "35 minutos",
        "temperatura": "180 ºC",
        "preparacao": [
            "Assar o bacalhau ligeiramente.",
            "Triturar broa com alho e azeite.",
            "Cobrir o bacalhau.",
            "Levar novamente ao forno."
        ]
    },
    {
        "nome": "Bacalhau à Minhota",
        "ingredientes": ["bacalhau", "batata", "cebola", "azeite"],
        "modo": "Fritar",
        "tempo": "30 minutos",
        "temperatura": "Óleo médio",
        "preparacao": [
            "Fritar o bacalhau.",
            "Fritar as batatas.",
            "Refogar cebola em azeite.",
            "Juntar tudo e servir."
        ]
    },
    {
        "nome": "Bacalhau Espiritual",
        "ingredientes": ["bacalhau", "cenoura", "pão", "leite", "cebola", "azeite"],
        "modo": "Forno",
        "tempo": "40 minutos",
        "temperatura": "180 ºC",
        "preparacao": [
            "Demolhar pão no leite.",
            "Refogar cebola.",
            "Misturar bacalhau e cenoura.",
            "Envolver tudo e levar ao forno."
        ]
    },
    {
        "nome": "Massada de Bacalhau",
        "ingredientes": ["bacalhau", "massa", "tomate", "cebola", "alho"],
        "modo": "Fogão",
        "tempo": "30 minutos",
        "temperatura": "Médio",
        "preparacao": [
            "Refogar cebola e alho.",
            "Adicionar tomate.",
            "Juntar bacalhau desfiado.",
            "Adicionar massa e água.",
            "Cozinhar até a massa estar pronta."
        ]
    },
    {
        "nome": "Bacalhau à Portuguesa",
        "ingredientes": ["bacalhau", "batata", "ovos", "cebola", "azeite"],
        "modo": "Fogão",
        "tempo": "25 minutos",
        "temperatura": "Médio",
        "preparacao": [
            "Cozer bacalhau, batatas e ovos.",
            "Cortar tudo.",
            "Regar com azeite.",
            "Adicionar cebola crua."
        ]
    },
    {
        "nome": "Bacalhau à Zé do Pipo",
        "ingredientes": ["bacalhau", "puré de batata", "cebola", "maionese", "azeite"],
        "modo": "Forno",
        "tempo": "35 minutos",
        "temperatura": "180 ºC",
        "preparacao": [
            "Assar bacalhau.",
            "Cobrir com puré.",
            "Adicionar maionese.",
            "Levar ao forno até gratinar."
        ]
    },
    {
        "nome": "Bacalhau à Brás no Forno",
        "ingredientes": ["bacalhau", "batata palha", "ovos", "cebola", "azeite"],
        "modo": "Forno",
        "tempo": "30 minutos",
        "temperatura": "180 ºC",
        "preparacao": [
            "Preparar bacalhau à Brás.",
            "Colocar num tabuleiro.",
            "Levar ao forno para gratinar."
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
# INTERFACE STREAMLIT
# =========================

st.set_page_config(page_title="App de Receitas", layout="centered")
st.title("🍽️ App de Receitas Inteligente")

tem_bacalhau = st.radio("Tens bacalhau?", ["Sim", "Não"])
substituto = "bacalhau"

if tem_bacalhau == "Não":
    st.subheader("🔁 Ingredientes que podem substituir o bacalhau")
    substituto = st.selectbox(
        "Escolhe um ingrediente:",
        ["alho francês", "frango", "atum", "cogumelos", "legumes"]
    )

receitas_ativas = [
    adaptar_receita(r, substituto) if substituto != "bacalhau" else r
    for r in receitas
]

st.subheader("🥗 Ingredientes que tens em casa")
ingredientes_user = st.multiselect(
    "Seleciona:",
    sorted({ing for r in receitas_ativas for ing in r["ingredientes"]})
)

if ingredientes_user:
    possiveis = receitas_possiveis(receitas_ativas, ingredientes_user)

    if possiveis:
        st.success("✅ Receitas possíveis")
        for r in possiveis:
            with st.expander(r["nome"]):
                st.write("**Ingredientes:**", ", ".join(r["ingredientes"]))
                st.write("**Modo:**", r["modo"])
                st.write("**Tempo:**", r["tempo"])
                st.write("**Temperatura:**", r["temperatura"])
                st.write("**Preparação:**")
                for i, p in enumerate(r["preparacao"], 1):
                    st.write(f"{i}. {p}")
    else:
        st.error("❌ Não tens ingredientes suficientes")
        for r in receitas_ativas:
            with st.expander(r["nome"]):
                st.write("❗ Faltam:", ", ".join(ingredientes_em_falta(r, ingredientes_user)))
