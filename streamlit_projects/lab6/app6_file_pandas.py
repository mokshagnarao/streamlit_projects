import streamlit as st
import pandas as pd

# Title
st.title("Upload CSV and Analyze")

# File Upload
file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if file is not None:

    # Read CSV
    df = pd.read_csv(file)

    # ---------------- Data Preview ----------------
    st.subheader("Data Preview")
    st.dataframe(df)

    # ---------------- Statistics ----------------
    st.subheader("Statistics")
    st.write(df.describe())

    # ---------------- Filter Data ----------------
    st.subheader("Filter by Column")

    col = st.selectbox(
        "Choose Column",
        df.columns
    )

    value = st.text_input("Filter Value")

    if value:
        filtered = df[
            df[col]
            .astype(str)
            .str.contains(value, case=False, na=False)
        ]

        st.dataframe(filtered)

    # ---------------- Sort Data ----------------
    st.subheader("Sort Data")

    sort_col = st.selectbox(
        "Sort By",
        df.columns,
        key="sort"
    )

    sorted_df = df.sort_values(sort_col)

    st.dataframe(sorted_df)