import streamlit as st
from datetime import datetime


# ✅ Page config must come right after Streamlit import
st.set_page_config(page_title="Books Dashboard", layout="wide")

import pandas as pd

# Load data once
@st.cache_data
def load_data():
    df = pd.read_csv("all_books.csv")
    df["Price"] = df["Price"].str.replace("£", "").astype(float)
    return df

df = load_data()

# Sidebar with metrics
st.sidebar.title("📚 Books Summary")

total_books = len(df)
avg_price = df["Price"].mean()
unique_ratings = df["Rating"].nunique()
availability_counts = df["Availability"].value_counts().to_dict()

st.sidebar.metric("Total Books", total_books)
st.sidebar.metric("Avg Price (£)", f"{avg_price:.2f}")
st.sidebar.metric("Rating Categories", unique_ratings)
st.sidebar.markdown("### Availability")
for key, val in availability_counts.items():
    st.sidebar.write(f"- {key}: {val}")

# Main page content
st.title("📘 Books Dashboard")
st.markdown("""
Welcome to the **Books to Scrape Dashboard**!

Use the left sidebar to navigate through:
- 🔎 Filter and Explore the Data  
- 📊 Visual Insights  
- 🧠 Word Frequency in Titles

---
""")

# Adding last updated timestamp
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

