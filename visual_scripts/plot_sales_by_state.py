import pandas as pd
import matplotlib.pyplot as plt
import os

# Asegurar que la carpeta visuals exista
os.makedirs("visuals", exist_ok=True)

# Cargar datos desde carpeta Insights
df = pd.read_csv("Insights/sales_by_state.csv")

# Top 10 estados con más ventas
df_top = df.sort_values(by="total_sales", ascending=False).head(10)

# Estilo oscuro profesional
plt.style.use('dark_background')
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.edgecolor": "#1F2937",
    "axes.labelcolor": "white",
    "xtick.color": "gray",
    "ytick.color": "gray",
    "axes.facecolor": "#111827",
    "figure.facecolor": "#111827",
    "axes.grid": True,
    "grid.color": "#374151",
    "grid.alpha": 0.3
})

# Crear gráfico horizontal
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(df_top["State"][::-1], df_top["total_sales"][::-1], color="#4F46E5")

# Añadir etiquetas encima de cada barra
for i, v in enumerate(df_top["total_sales"][::-1]):
    ax.text(v + 2000, i, f"${v:,.0f}", color='white', va='center', fontsize=10)

# Títulos
ax.set_title("Top 10 States by Total Sales", fontsize=16, color="white", pad=20)
ax.set_xlabel("Total Sales", fontsize=12)
ax.set_ylabel("State", fontsize=12)

# Guardar imagen
plt.tight_layout()
plt.savefig("visuals/sales_by_state_dark.png", dpi=300)
plt.show()
