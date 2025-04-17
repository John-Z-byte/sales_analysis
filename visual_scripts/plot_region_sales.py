import pandas as pd
import matplotlib.pyplot as plt
import os

# Asegúrate de tener esta ruta creada
os.makedirs("visuals", exist_ok=True)

# Cargar el CSV desde la carpeta Insights
df = pd.read_csv("Insights/sales_region.csv")

# Estilo oscuro tipo dashboard moderno
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
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(df["Region"], df["total_sales"], color="#4F46E5")  # Neon Indigo

# Etiquetas sobre cada barra
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 5000, f"${height:,.0f}", 
            ha='center', color='white', fontsize=10)

# Títulos
ax.set_title("Total Sales by Region", fontsize=16, color="white", pad=20)
ax.set_xlabel("Region", fontsize=12)
ax.set_ylabel("Total Sales", fontsize=12)

# Guardar imagen en la carpeta visuals
plt.tight_layout()
plt.savefig("visuals/sales_by_region_dark.png", dpi=300)
plt.show()
