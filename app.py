import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Loading dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/metadata.csv")
    df = df.dropna(subset=["publish_time", "title"])
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year
    return df

df = load_data()

# Streamlit App
st.title("CORD-19 Data Explorer")
st.write("An interactive exploration of COVID-19 research papers.")

# Year filter
year_range = st.slider("Select year range", 2015, 2025, (2019, 2021))
filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Publications by year
st.subheader("Publications per Year")
year_counts = filtered["year"].value_counts().sort_index()
st.bar_chart(year_counts)

# Top Journals
st.subheader("Top Journals")
top_journals = filtered["journal"].value_counts().head(10)
st.bar_chart(top_journals)

# Word Cloud
st.subheader("Word Cloud of Titles")
text = " ".join(filtered["title"].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Show sample data
st.subheader("Sample Data")
st.write(filtered.head())
