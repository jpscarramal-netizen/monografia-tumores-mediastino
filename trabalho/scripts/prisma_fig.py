"""PRISMA 2020 flow diagram (Portuguese) for the review."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams["font.family"] = "Times New Roman"
fig, ax = plt.subplots(figsize=(8.3, 9.2), dpi=300)
ax.set_xlim(0, 100); ax.set_ylim(0, 110); ax.axis("off")

def box(x, y, w, h, text, fs=9):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="square,pad=0", fc="white", ec="black", lw=1))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, wrap=True)

def arrow(x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="-|>", lw=1, color="black"))

def side(y, h, text):
    ax.add_patch(FancyBboxPatch((1, y), 6, h, boxstyle="square,pad=0", fc="#d9d9d9", ec="black", lw=1))
    ax.text(4, y + h / 2, text, ha="center", va="center", rotation=90, fontsize=9, fontweight="bold")

side(84, 22, "Identificação"); side(36, 46, "Triagem"); side(4, 30, "Incluídos")
box(10, 88, 40, 16, "Registros identificados (n = 1.467)\nPubMed/MEDLINE (n = 415)\nScopus (n = 589)\nWeb of Science (n = 463)")
box(58, 88, 40, 16, "Registros removidos antes da triagem:\nduplicatas (n = 755)")
arrow(50, 96, 58, 96)
box(10, 66, 40, 12, "Registros triados por título\ne resumo (n = 712)")
box(58, 60, 40, 24, "Registros excluídos (n = 662)\nPopulação fora do escopo (n = 287)\nDesenho de menor peso (n = 196)\nComparação fora do PICO (n = 101)\nSem comparação de vias (n = 76)\nSem desfecho de interesse (n = 2)", fs=8.5)
arrow(30, 88, 30, 78); arrow(50, 72, 58, 72)
box(10, 40, 40, 12, "Artigos avaliados no texto\ncompleto (n = 50)")
box(58, 38, 40, 16, "Artigos excluídos (n = 10)\nPopulação mista ou fora do\nmediastino anterior, sem resultados\nseparados para tumor (n = 10)", fs=8.5)
arrow(30, 66, 30, 52); arrow(50, 46, 58, 46)
box(10, 8, 40, 20, "Estudos incluídos (n = 40)\nMetanálises (n = 12)\nRegistros multicêntricos\nou nacionais (n = 24)\nUnicêntricos em doença\nlocalmente avançada (n = 4)", fs=8.5)
arrow(30, 40, 30, 28)
plt.savefig("trabalho/figuras/figura1_prisma.png", bbox_inches="tight", facecolor="white")
print("ok")
