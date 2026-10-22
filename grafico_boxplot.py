import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent / "dados_boxplot.csv"
df = pd.read_csv(ARQUIVO)

df.boxplot(column="salario", by="departamento", figsize=(9, 6))
plt.suptitle("")
plt.title("Distribuição salarial por departamento")
plt.xlabel("Departamento")
plt.ylabel("Salário (R$)")
plt.tight_layout()
plt.savefig(Path(__file__).resolve().parent / "grafico_boxplot.png", dpi=150)
plt.close()
