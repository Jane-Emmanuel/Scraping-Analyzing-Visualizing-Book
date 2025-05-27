import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("all_books.csv")
    return df

df = load_data()

st.title("🔍 Filter and Explore Books")

rating_options = df["Rating"].unique().tolist()
availability_options = df["Availability"].unique().tolist()

selected_ratings = st.multiselect("Select Ratings", rating_options, default=rating_options)
selected_avail = st.multiselect("Select Availability", availability_options, default=availability_options)

filtered_df = df[df["Rating"].isin(selected_ratings) & df["Availability"].isin(selected_avail)]

st.dataframe(filtered_df)
st.markdown(f"**Total books after filter: {len(filtered_df)}**")
