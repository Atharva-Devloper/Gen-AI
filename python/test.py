import streamlit as st
import pandas as pd

st.title("Search Algorithm Performance Comparison")

data = {
    "Algorithm": [
        "Linear Search (Iterative)",
        "Binary Search (Iterative)",
        "Binary Search (Recursive)"
    ],

    "N(1-100) Comparisons": [75, 6, 7],
    "N(1-100) Time(ns)": [11200, 1700, 5000],

    "N(100-500) Comparisons": [441, 4, 4],
    "N(100-500) Time(ns)": [17400, 14000, 5100],

    "N(500-1000) Comparisons": [392, 9, 9],
    "N(500-1000) Time(ns)": [18000, 1500, 5500],
}

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True, hide_index=True)