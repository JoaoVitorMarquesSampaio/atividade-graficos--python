import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent / "dados_regressao.csv"
df = pd.read_csv(ARQUIVO)

import numpy as np
x = df["renda_mensal"]
y = df["gasto_mensal"]
coeficientes = np.polyfit(x, y, 1)
reta_x = np.linspace(x.min(), x.max(), 100)
reta_y = np.polyval(coeficientes, reta_x)
plt.figure(figsize=(9, 6))
plt.scatter(x, y, alpha=0.65, label="Observações")
plt.plot(reta_x, reta_y, color="red", label="Regressão linear")
plt.title("Renda mensal x gasto mensal")
plt.xlabel("Renda mensal (R$)")
plt.ylabel("Gasto mensal (R$)")
plt.legend()
plt.tight_layout()
plt.savefig(Path(__file__).resolve().parent / "grafico_regressao.png", dpi=150)
plt.close()
