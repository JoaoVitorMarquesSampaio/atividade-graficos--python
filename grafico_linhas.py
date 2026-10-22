import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent / "dados_linhas.csv"
df = pd.read_csv(ARQUIVO)

df["data"] = pd.to_datetime(df["data"])
plt.figure(figsize=(11, 6))
for loja, grupo in df.groupby("loja"):
    grupo = grupo.sort_values("data")
    plt.plot(grupo["data"], grupo["vendas"], label=loja)
plt.title("Vendas ao longo do tempo por loja")
plt.xlabel("Data")
plt.ylabel("Vendas")
plt.legend(title="Loja")
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.savefig(Path(__file__).resolve().parent / "grafico_linhas.png", dpi=150)
plt.close()
