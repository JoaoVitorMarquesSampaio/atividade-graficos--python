import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent / "dados_heatmap.csv"
df = pd.read_csv(ARQUIVO)

ordem = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
tabela = df.pivot(index="dia_semana", columns="horario", values="movimento_clientes")
tabela = tabela.reindex([dia for dia in ordem if dia in tabela.index])
tabela = tabela.reindex(sorted(tabela.columns), axis=1)
fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(tabela.values, aspect="auto", cmap="YlOrRd")
ax.set_xticks(range(len(tabela.columns)), tabela.columns)
ax.set_yticks(range(len(tabela.index)), tabela.index)
ax.set_title("Movimento de clientes por dia e horário")
ax.set_xlabel("Horário")
ax.set_ylabel("Dia da semana")
fig.colorbar(im, ax=ax, label="Clientes")
plt.tight_layout()
plt.savefig(Path(__file__).resolve().parent / "grafico_heatmap.png", dpi=150)
plt.close()
