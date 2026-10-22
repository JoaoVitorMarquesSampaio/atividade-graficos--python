import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent / "dados_distribuicao.csv"
df = pd.read_csv(ARQUIVO)

plt.figure(figsize=(9, 6))
plt.hist(df["idade"].dropna(), bins=12, edgecolor="black")
plt.title("Distribuição das idades dos clientes")
plt.xlabel("Idade")
plt.ylabel("Quantidade de clientes")
plt.tight_layout()
plt.savefig(Path(__file__).resolve().parent / "grafico_distribuicao.png", dpi=150)
plt.close()
