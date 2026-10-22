import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent / "dados_pizza.csv"
df = pd.read_csv(ARQUIVO)

plt.figure(figsize=(8, 8))
plt.pie(df["faturamento"], labels=df["canal_venda"], autopct="%1.1f%%", startangle=90)
plt.title("Participação do faturamento por canal")
plt.axis("equal")
plt.tight_layout()
plt.savefig(Path(__file__).resolve().parent / "grafico_pizza.png", dpi=150)
plt.close()
