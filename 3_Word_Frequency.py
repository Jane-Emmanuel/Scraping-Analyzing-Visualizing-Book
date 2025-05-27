import streamlit as st
import pandas as pd
from collections import Counter
import re
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    return pd.read_csv("all_books.csv")

df = load_data()

st.title("🧠 Word Frequency in Titles")

all_words = " ".join(df["Title"]).lower()
word_list = re.findall(r'\b\w+\b', all_words)
word_freq = Counter(word_list)

top_words = dict(word_freq.most_common(10))
top_words_df = pd.DataFrame(list(top_words.items()), columns=["Word", "Frequency"])

st.dataframe(top_words_df)

fig, ax = plt.subplots()
sns.barplot(x="Frequency", y="Word", data=top_words_df, palette="mako")
ax.set_title("Top 10 Common Words in Titles")
st.pyplot(fig)
