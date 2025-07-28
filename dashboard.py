import streamlit as st
from news_aggregator import get_crypto_news
from sentiment_analyzer import analyze_sentiment

st.title("📰 Crypto News & Sentiment Analysis")

news_list = get_crypto_news()
for article in news_list:
    sentiment = analyze_sentiment(article["description"] or article["title"])
    st.write(f"**{article['title']}** ({sentiment})")
    st.write(article["description"])
    st.write("---")
