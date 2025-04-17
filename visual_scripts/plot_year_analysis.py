import pandas as pd
import matplotlib.pyplot as plt
import os

# Crear carpeta visuals si no existe
os.makedirs("visuals", exist_ok=True)

# Cargar datos
df = pd.read_csv("Insights/year_analysis.csv")

# Verificar orden por mes
df = df.sort_values("month")

# Traducir número de mes a nombre corto
month_labels = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
    5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
    9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}
df["Month_Label"] = df["month"].map(month_labels)

# Estilo moderno oscuro
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

# Gráfico de línea
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df["Month_Label"], df["total_sales"], marker="o", color="#4F46E5", linewidth=2)

# Etiquetas de puntos
for i, v in enumerate(df["total_sales"]):
    ax.text(i, v + 1000, f"${v:,.0f}", ha='center', color='white', fontsize=9)

# Títulos
ax.set_title("Monthly Total Sales", fontsize=16, color="white", pad=20)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Total Sales", fontsize=12)

# Guardar imagen
plt.tight_layout()
plt.savefig("visuals/year_analysis_dark.png", dpi=300)
plt.show()
