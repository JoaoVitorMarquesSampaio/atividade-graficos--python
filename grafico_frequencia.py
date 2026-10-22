import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent / "dados_frequencia.csv"
df = pd.read_csv(ARQUIVO)

contagem = df["tipo_atendimento"].value_counts()
plt.figure(figsize=(9, 6))
contagem.plot(kind="bar")
plt.title("Frequência dos tipos de atendimento")
plt.xlabel("Tipo de atendimento")
plt.ylabel("Quantidade de chamados")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(Path(__file__).resolve().parent / "grafico_frequencia.png", dpi=150)
plt.close()
