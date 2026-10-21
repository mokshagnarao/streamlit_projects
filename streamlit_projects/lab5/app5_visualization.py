import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Data Visualization")

# ---------------- Sample Data ----------------
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Math", "Science", "English"]
)

# ---------------- Built-in Charts ----------------
st.subheader("Built-in Charts")

st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

# ---------------- Matplotlib Chart ----------------
st.subheader("Matplotlib Chart")

fig, ax = plt.subplots()

ax.hist(
    df["Math"],
    bins=10,
    color="skyblue",
    edgecolor="black"
)

ax.set_title("Math Score Distribution")
ax.set_xlabel("Math Scores")
ax.set_ylabel("Frequency")

st.pyplot(fig)