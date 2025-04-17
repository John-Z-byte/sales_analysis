import streamlit as st
from PIL import Image

# CONFIGURACIÓN GENERAL
st.set_page_config(
    page_title="Executive Sales Dashboard",
    layout="wide",
)

# CSS ESTILIZADO
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            background-color: #0f172a;
            color: #e2e8f0;
        }
        h1, h2, h3, .stTitle {
            color: #f1f5f9;
        }
        img {
            border-radius: 10px;
        }
        .block-container {
            padding: 2rem 4rem;
        }
        hr {
            border: 1px solid #334155;
            margin: 2rem 0;
        }
        .kpi-card {
            background: rgba(0, 0, 0, 0, 4);
            border: 1px solid #334155;
            padding: 1.5rem;
            border-radius: 1rem;
            box-shadow: 0 8px 20px rgba(0,0,0,0.25);
            text-align: center;
        }
        .kpi-value {
            font-size: 2rem;
            font-weight: bold;
            color: #38bdf8;
        }
        .kpi-label {
            font-size: 1rem;
            color: #94a3b8;
        }
        .kpi-delta {
            font-size: 0.9rem;
            color: #22c55e;
        }
    </style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("Dashboard Navigation")
section = st.sidebar.radio("Go to Section:", ["Regional Sales Overview", "Advanced Insights"])
year = st.sidebar.selectbox("Select Year", ["2023", "2024", "2025"], index=2)

# HEADER
st.title("Executive Sales Insights")
st.markdown(f"""
Welcome to your interactive dashboard.

You're viewing data from **{year}**. Use the sidebar to switch sections.
""")

# KPIs - CUSTOM CARDS
kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-value">$2.9M</div>
            <div class="kpi-label">Total Sales</div>
            <div class="kpi-delta">+8.3% vs last year</div>
        </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-value">$241K</div>
            <div class="kpi-label">Avg Monthly Sales</div>
            <div class="kpi-delta">+2.1% YoY</div>
        </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-value">12.6%</div>
            <div class="kpi-label">YoY Growth Rate</div>
            <div class="kpi-delta">High Growth</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# SECCIÓN 1
if section == "Regional Sales Overview":
    st.header("Regional Sales Overview")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Sales by Region")
        st.image("visuals/sales_by_region_dark.png", use_container_width=True)
    with col2:
        st.subheader("Sales by State")
        st.image("visuals/sales_by_state_dark.png", use_container_width=True)

    st.subheader("Top 10 Cities by Sales")
    st.image("visuals/top_cities_sales_dark.png", use_container_width=True)

# SECCIÓN 2
elif section == "Advanced Insights":
    st.header("Advanced Insights")

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Top Product Sales by Month")
        st.image("visuals/top_product_month_dark.png", use_container_width=True)
    with col4:
        st.subheader("Monthly Total Sales")
        st.image("visuals/year_analysis_dark.png", use_container_width=True)

    st.subheader("YoY Growth by Category")
    st.image("visuals/yoy_growth_dark.png", use_container_width=True)
