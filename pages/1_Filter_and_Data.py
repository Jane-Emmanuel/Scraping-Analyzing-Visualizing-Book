import streamlit as st
import pandas as pd
from datetime import datetime


# Load data
df = pd.read_csv("all_books.csv")
df["Price"] = df["Price"].str.replace("£", "").astype(float)

st.markdown("## 🔎 Filter and Explore Books")

# Sidebar search input
search_term = st.sidebar.text_input("🔍 Search book titles:")

# Sidebar filters
price_range = st.sidebar.slider("💰 Price range (£)", float(df["Price"].min()), float(df["Price"].max()), (float(df["Price"].min()), float(df["Price"].max())))
rating_filter = st.sidebar.multiselect("⭐ Select Ratings", options=df["Rating"].unique(), default=list(df["Rating"].unique()))
availability_filter = st.sidebar.multiselect("📦 Availability", options=df["Availability"].unique(), default=list(df["Availability"].unique()))

# Filter data based on input
filtered_df = df.copy()

if search_term:
    filtered_df = filtered_df[filtered_df["Title"].str.contains(search_term, case=False, na=False)]

filtered_df = filtered_df[
    (filtered_df["Price"] >= price_range[0]) &
    (filtered_df["Price"] <= price_range[1]) &
    (filtered_df["Rating"].isin(rating_filter)) &
    (filtered_df["Availability"].isin(availability_filter))
]

# Show filtered results
st.markdown(f"### 📘 Showing {len(filtered_df)} matching books")
st.dataframe(filtered_df[["Title", "Price", "Rating", "Availability"]])

# Download button
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(filtered_df)
st.download_button(
    label="📥 Download Filtered CSV",
    data=csv,
    file_name="filtered_books.csv",
    mime="text/csv"
)

# Adding last updated timestamp
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
