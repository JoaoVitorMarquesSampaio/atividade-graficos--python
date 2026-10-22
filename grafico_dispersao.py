import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent / "dados_dispersao.csv"
df = pd.read_csv(ARQUIVO)

plt.figure(figsize=(9, 6))
for sexo, grupo in df.groupby("sexo"):
    plt.scatter(grupo["altura_cm"], grupo["peso_kg"], alpha=0.7, label=sexo)
plt.title("Altura x peso")
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")
plt.legend(title="Sexo")
plt.tight_layout()
plt.savefig(Path(__file__).resolve().parent / "grafico_dispersao.png", dpi=150)
plt.close()
