import pandas as pd
import matplotlib.pyplot as plt
import os

# Crear carpeta si no existe
os.makedirs("visuals", exist_ok=True)

# Leer datos
df = pd.read_csv("Insights/top_product_month.csv")

# Asegurar orden por mes
df = df.sort_values("month")

# Traducir número de mes a texto corto
month_labels = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
    5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
    9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}
df["Month_Label"] = df["month"].map(month_labels)

# Estilo oscuro
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

# Crear gráfico
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(df["Month_Label"], df["total_sales"], color="#4F46E5")

# Etiquetas sobre barras
for i, v in enumerate(df["total_sales"]):
    ax.text(i, v + 1000, f"${v:,.0f}", ha='center', color='white', fontsize=9)

# Título y etiquetas
ax.set_title("Top Product Sales per Month", fontsize=16, color="white", pad=20)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Total Sales", fontsize=12)

# Guardar gráfico
plt.tight_layout()
plt.savefig("visuals/top_product_month_dark.png", dpi=300)
plt.show()
