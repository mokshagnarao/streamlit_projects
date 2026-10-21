import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

# Title
st.title("Sales Dashboard")

# ---------------- Sample Data ----------------
df = pd.DataFrame({
    "Year": np.random.choice([2022, 2023, 2024], 200),
    "Region": np.random.choice(
        ["North", "South", "East", "West"],
        200
    ),
    "Product": np.random.choice(
        ["A", "B", "C"],
        200
    ),
    "Sales": np.random.randint(
        1000,
        10000,
        200
    )
})

# ---------------- Sidebar Filters ----------------
st.sidebar.header("Filters")

year = st.sidebar.multiselect(
    "Year",
    df["Year"].unique(),
    default=df["Year"].unique()
)

region = st.sidebar.multiselect(
    "Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

product = st.sidebar.multiselect(
    "Product",
    df["Product"].unique(),
    default=df["Product"].unique()
)

# ---------------- Filter Data ----------------
filtered = df[
    (df["Year"].isin(year)) &
    (df["Region"].isin(region)) &
    (df["Product"].isin(product))
]

# ---------------- KPI Metrics ----------------
c1, c2, c3 = st.columns(3)

c1.metric(
    "Total Sales",
    f"{filtered['Sales'].sum():,}"
)

c2.metric(
    "Avg Sales",
    f"{int(filtered['Sales'].mean()):,}"
)

c3.metric(
    "Records",
    len(filtered)
)

# ---------------- Charts ----------------
st.subheader("Sales by Region")

region_sales = (
    filtered.groupby("Region")["Sales"]
    .sum()
)

st.bar_chart(region_sales)

st.subheader("Sales by Year")

year_sales = (
    filtered.groupby("Year")["Sales"]
    .sum()
)

st.line_chart(year_sales)
