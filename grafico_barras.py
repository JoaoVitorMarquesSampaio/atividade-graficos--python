import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent / "dados_barras.csv"
df = pd.read_csv(ARQUIVO)

tabela = df.pivot(index="categoria", columns="regiao", values="vendas_medias")
tabela.plot(kind="bar", figsize=(11, 6))
plt.title("Vendas médias por categoria e região")
plt.xlabel("Categoria")
plt.ylabel("Vendas médias")
plt.xticks(rotation=30, ha="right")
plt.legend(title="Região")
plt.tight_layout()
plt.savefig(Path(__file__).resolve().parent / "grafico_barras.png", dpi=150)
plt.close()
