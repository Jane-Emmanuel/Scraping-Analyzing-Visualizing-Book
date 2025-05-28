import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from datetime import datetime

sns.set(style="whitegrid")
warnings.simplefilter(action='ignore', category=FutureWarning)

@st.cache_data
def load_data():
    df = pd.read_csv("all_books.csv")
    df["Price"] = df["Price"].str.replace("£", "").astype(float)
    return df

df = load_data()

st.markdown("<h4 style='color:#4CAF50;'>📚 Explore Book Insights by Rating, Price, and Availability</h4>", unsafe_allow_html=True)

st.title("📊 Visual Analysis")

with st.expander("⭐ Rating Distribution"):
    fig, ax = plt.subplots()
    sns.countplot(
        x="Rating", 
        data=df, 
        order=["One", "Two", "Three", "Four", "Five"], 
        hue="Rating", 
        palette="viridis", 
        legend=False,
        ax=ax
    )
    ax.set_title("Rating Distribution")
    st.pyplot(fig)

with st.expander("💵 Price Distribution"):
    fig, ax = plt.subplots()
    sns.histplot(df["Price"], bins=20, kde=True, color="skyblue", ax=ax)
    ax.set_title("Price Distribution")
    st.pyplot(fig)

with st.expander("📈 Avg Price by Rating"):
    avg_price = df.groupby("Rating")["Price"].mean().reindex(["One", "Two", "Three", "Four", "Five"])
    fig, ax = plt.subplots()
    avg_price.plot(kind="bar", color="coral", ax=ax)
    ax.set_title("Average Price by Rating")
    st.pyplot(fig)

with st.expander("✅ Book Availability"):
    fig, ax = plt.subplots()
    sns.countplot(
        y="Availability", 
        data=df, 
        hue="Availability", 
        palette="Set2", 
        legend=False,
        ax=ax
    )
    ax.set_title("Book Availability")
    st.pyplot(fig)

import plotly.express as px

st.markdown("""
### 🚀 Let's make one chart interactive!

This is an interactive version of **Top 5 Most Expensive Books** chart using Plotly.  
Try hovering over the bars to see detailed info!
""")

with st.expander("💖 Top 5 most expensive books (Interactive)"):
    top_expensive = df.sort_values(by="Price", ascending=False).head(5)
    st.subheader("💰 Top 5 Most Expensive Books")

    fig = px.bar(
        top_expensive,
        x="Price",
        y="Title",
        orientation='h',
        color="Price",
        color_continuous_scale='RdPu',
        title="Top 5 Most Expensive Books"
    )
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig)

# Add last updated timestamp
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
