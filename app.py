import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import tempfile

# =========================
# BASE DE DADOS DE RECEITAS
# =========================

receitas = [
    {
        "nome": "Bacalhau à Brás",
        "categoria": "Tradicional",
        "ingredientes": ["bacalhau", "batata palha", "ovos", "cebola", "alho", "azeite", "salsa"],
        "modo": "Fogão",
        "tempo": "20 minutos",
        "temperatura": "Médio",
        "preparacao": [
            "Demolhar o bacalhau durante 24 horas, trocando a água.",
            "Cozer ligeiramente e desfiar.",
            "Refogar cebola e alho em azeite.",
            "Adicionar o bacalhau desfiado.",
            "Juntar a batata palha.",
            "Adicionar ovos batidos lentamente.",
            "Finalizar com salsa."
        ]
    },
    {
        "nome": "Bacalhau com Natas",
        "categoria": "Forno",
        "ingredientes": ["bacalhau", "batata", "cebola", "alho", "natas", "azeite", "queijo"],
        "modo": "Forno",
        "tempo": "45 minutos",
        "temperatura": "180 ºC",
        "preparacao": [
            "Demolhar e desfiar o bacalhau.",
            "Cozer ou fritar as batatas.",
            "Refogar cebola e alho.",
            "Misturar bacalhau, batata e natas.",
            "Colocar num tabuleiro.",
            "Polvilhar com queijo.",
            "Levar ao forno até gratinar."
        ]
    },
    {
        "nome": "Bacalhau à Gomes de Sá",
        "categoria": "Forno",
        "ingredientes": ["bacalhau", "batata", "cebola", "ovos", "azeite", "azeitonas"],
        "modo": "Forno",
        "tempo": "40 minutos",
        "temperatura": "180 ºC",
        "preparacao": [
            "Demolhar e desfiar o bacalhau.",
            "Cozer batatas às rodelas.",
            "Refogar cebola em azeite.",
            "Dispor tudo em camadas.",
            "Adicionar ovos cozidos e azeitonas.",
            "Levar ao forno."
        ]
    },
    {
        "nome": "Bacalhau à Lagareiro",
        "categoria": "Forno",
        "ingredientes": ["bacalhau", "batata a murro", "alho", "azeite"],
        "modo": "Forno",
        "tempo": "50 minutos",
        "temperatura": "190 ºC",
        "preparacao": [
            "Assar o bacalhau no forno.",
            "Dar murro nas batatas.",
            "Aquecer azeite com alho.",
            "Regar tudo e levar novamente ao forno."
        ]
    },
    {
        "nome": "Bacalhau Assado no Forno",
        "categoria": "Forno",
        "ingredientes": ["bacalhau", "cebola", "alho", "azeite", "batata"],
        "modo": "Forno",
        "tempo": "50 minutos",
        "temperatura": "190 ºC",
        "preparacao": [
            "Colocar bacalhau num tabuleiro.",
            "Adicionar batatas e cebola.",
            "Regar com azeite e alho.",
            "Assar até dourar."
        ]
    },
    {
        "nome": "Bacalhau à Zé do Pipo",
        "categoria": "Forno",
        "ingredientes": ["bacalhau", "puré de batata", "cebola", "maionese", "azeite"],
        "modo": "Forno",
        "tempo": "35 minutos",
        "temperatura": "180 ºC",
        "preparacao": [
            "Assar o bacalhau.",
            "Cobrir com puré.",
            "Adicionar maionese.",
            "Levar ao forno até gratinar."
        ]
    },
    {
        "nome": "Bacalhau Espiritual",
        "categoria": "Forno",
        "ingredientes": ["bacalhau", "cenoura", "pão", "leite", "cebola", "azeite"],
        "modo": "Forno",
        "tempo": "40 minutos",
        "temperatura": "180 ºC",
        "preparacao": [
            "Demolhar pão no leite.",
            "Refogar cebola.",
            "Misturar bacalhau e cenoura.",
            "Levar ao forno."
        ]
    },
    {
        "nome": "Bacalhau à Minhota",
        "categoria": "Fritos",
        "ingredientes": ["bacalhau", "batata", "cebola", "azeite"],
        "modo": "Fritar",
        "tempo": "30 minutos",
        "temperatura": "Óleo médio",
        "preparacao": [
            "Fritar bacalhau.",
            "Fritar batatas.",
            "Refogar cebola.",
            "Juntar tudo."
        ]
    },
    {
        "nome": "Pataniscas de Bacalhau",
        "categoria": "Fritos",
        "ingredientes": ["bacalhau", "farinha", "ovos", "cebola", "salsa"],
        "modo": "Fritar",
        "tempo": "25 minutos",
        "temperatura": "Óleo médio",
        "preparacao": [
            "Misturar todos os ingredientes.",
            "Aquecer óleo.",
            "Fritar colheradas até dourar."
        ]
    },
    {
        "nome": "Arroz de Bacalhau",
        "categoria": "Fogão",
        "ingredientes": ["bacalhau", "arroz", "tomate", "cebola", "alho"],
        "modo": "Fogão",
        "tempo": "30 minutos",
        "temperatura": "Médio",
        "preparacao": [
            "Refogar cebola e alho.",
            "Adicionar tomate.",
            "Juntar bacalhau.",
            "Adicionar arroz e água.",
            "Cozinhar."
        ]
    },
    {
        "nome": "Massada de Bacalhau",
        "categoria": "Fogão",
        "ingredientes": ["bacalhau", "massa", "tomate", "cebola", "alho"],
        "modo": "Fogão",
        "tempo": "30 minutos",
        "temperatura": "Médio",
        "preparacao": [
            "Refogar cebola e alho.",
            "Adicionar tomate.",
            "Juntar bacalhau.",
            "Adicionar massa e água.",
            "Cozinhar."
        ]
    },
    {
        "nome": "Salada de Bacalhau",
        "categoria": "Leve",
        "ingredientes": ["bacalhau", "grão", "cebola", "azeite", "vinagre"],
        "modo": "Frio",
        "tempo": "15 minutos",
        "temperatura": "Não aplicável",
        "preparacao": [
            "Cozer bacalhau e grão.",
            "Misturar tudo.",
            "Temperar."
        ]
    },
    {
        "nome": "Bacalhau com Broa",
        "categoria": "Forno",
        "ingredientes": ["bacalhau", "broa", "alho", "azeite"],
        "modo": "Forno",
        "tempo": "35 minutos",
        "temperatura": "180 ºC",
        "preparacao": [
            "Assar bacalhau.",
            "Triturar broa com alho e azeite.",
            "Cobrir bacalhau.",
            "Levar ao forno."
        ]
    },
    {
        "nome": "Bacalhau à Portuguesa",
        "categoria": "Tradicional",
        "ingredientes": ["bacalhau", "batata", "ovos", "cebola", "azeite"],
        "modo": "Fogão",
        "tempo": "25 minutos",
        "temperatura": "Médio",
        "preparacao": [
            "Cozer bacalhau, batatas e ovos.",
            "Cortar tudo.",
            "Regar com azeite."
        ]
    },
    {
        "nome": "Bacalhau à Brás no Forno",
        "categoria": "Forno",
        "ingredientes": ["bacalhau", "batata palha", "ovos", "cebola", "azeite"],
        "modo": "Forno",
        "tempo": "30 minutos",
        "temperatura": "180 ºC",
        "preparacao": [
            "Preparar à Brás.",
            "Colocar no forno para gratinar."
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
    return [i for i in receita["ingredientes"] if i not in ingredientes_user]

def receitas_possiveis(lista, ingredientes_user):
    return [r for r in lista if not ingredientes_em_falta(r, ingredientes_user)]

def gerar_pdf(receita):
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    c = canvas.Canvas(temp.name, pagesize=A4)
    y = 800

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, receita["nome"])
    y -= 30

    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Modo: {receita['modo']}")
    y -= 20
    c.drawString(50, y, f"Tempo: {receita['tempo']}")
    y -= 20
    c.drawString(50, y, f"Temperatura: {receita['temperatura']}")
    y -= 30

    c.drawString(50, y, "Ingredientes:")
    y -= 20
    for ing in receita["ingredientes"]:
        c.drawString(60, y, f"- {ing}")
        y -= 15

    y -= 20
    c.drawString(50, y, "Preparação:")
    y -= 20
    for i, p in enumerate(receita["preparacao"], 1):
        c.drawString(60, y, f"{i}. {p}")
        y -= 15

    c.save()
    return temp.name

# =========================
# INTERFACE
# =========================

st.set_page_config("App de Receitas", layout="centered")
st.title("🍽️ App de Receitas Inteligente")

tem_bacalhau = st.radio("Tens bacalhau?", ["Sim", "Não"])
substituto = "bacalhau"

if tem_bacalhau == "Não":
    substituto = st.selectbox(
        "Substituir bacalhau por:",
        ["alho francês", "frango", "atum", "cogumelos", "legumes"]
    )

receitas_ativas = [
    adaptar_receita(r, substituto) if substituto != "bacalhau" else r
    for r in receitas
]

categoria = st.selectbox(
    "Categoria:",
    ["Todas"] + sorted({r["categoria"] for r in receitas_ativas})
)

modo = st.selectbox(
    "Modo de confeção:",
    ["Todos"] + sorted({r["modo"] for r in receitas_ativas})
)

filtradas = [
    r for r in receitas_ativas
    if (categoria == "Todas" or r["categoria"] == categoria)
    and (modo == "Todos" or r["modo"] == modo)
]

ingredientes_user = st.multiselect(
    "Ingredientes que tens:",
    sorted({i for r in filtradas for i in r["ingredientes"]})
)

if ingredientes_user:
    possiveis = receitas_possiveis(filtradas, ingredientes_user)

    if possiveis:
        st.success("Receitas possíveis:")
        for r in possiveis:
            with st.expander(r["nome"]):
                st.write("**Ingredientes:**", ", ".join(r["ingredientes"]))
                st.write("**Modo:**", r["modo"])
                st.write("**Tempo:**", r["tempo"])
                st.write("**Temperatura:**", r["temperatura"])
                st.write("**Preparação:**")
                for i, p in enumerate(r["preparacao"], 1):
                    st.write(f"{i}. {p}")

                pdf = gerar_pdf(r)
                with open(pdf, "rb") as f:
                    st.download_button("📄 Exportar PDF", f, file_name=f"{r['nome']}.pdf")
    else:
        st.error("Não tens ingredientes suficientes para nenhuma receita.")
