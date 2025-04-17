import pandas as pd
import matplotlib.pyplot as plt
import os

# Crear carpeta visuals si no existe
os.makedirs("visuals", exist_ok=True)

# Leer CSV real
df = pd.read_csv("Insights/yoy_growt.csv")

# Ordenar por categoría y año
df = df.sort_values(["Category", "year"])

# Estilo dark
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

# Gráfico por categoría
fig, ax = plt.subplots(figsize=(12, 6))

for category in df["Category"].unique():
    sub_df = df[df["Category"] == category]
    ax.plot(sub_df["year"], sub_df["yoy_growth_percent"], marker="o", label=category)

# Títulos
ax.set_title("YoY Growth by Category", fontsize=16, color="white", pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("YoY Growth (%)", fontsize=12)
ax.legend(title="Category", loc="best", facecolor="#1f2937", edgecolor="#374151", labelcolor='white', title_fontsize=10)

# Etiquetas sobre puntos
for category in df["Category"].unique():
    sub_df = df[df["Category"] == category]
    for x, y in zip(sub_df["year"], sub_df["yoy_growth_percent"]):
        ax.text(x, y + 1, f"{y:.1f}%", ha='center', color='white', fontsize=9)

# Guardar
plt.tight_layout()
plt.savefig("visuals/yoy_growth_dark.png", dpi=300)
plt.show()
