# crypto-news-sentiment
A Streamlit app that shows crypto news with sentiment analysis.
# 📰 Crypto News Sentiment Analyzer

A Streamlit web application that fetches real-time cryptocurrency news from CryptoPanic and analyzes the sentiment of each article using Natural Language Processing (NLP).

## 🚀 Features

- ✅ Real-time crypto news from CryptoPanic API  
- ✅ Sentiment analysis (Positive / Neutral / Negative) using VADER and TextBlob  
- ✅ Clean and responsive UI built with Streamlit  
- ✅ Easy to run locally

## 🛠️ Technologies Used

- Python
- Streamlit
- Requests
- VADER Sentiment
- TextBlob
- CryptoPanic API

## 📦 Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Create and activate a virtual environment:

bash
Copy code
python -m venv venv
.\venv\Scripts\activate  # For Windows
# source venv/bin/activate  # For macOS/Linux
Install the required packages:

bash
Copy code
pip install -r requirements.txt

Setup .env
Create a .env file in the root directory and add your CryptoPanic API key:

ini
Copy code
CRYPTOPANIC_API_KEY=your_api_key_here

Run the App
bash
Copy code
streamlit run dashboard.py

hen open your browser and go to:
👉 http://localhost:8501
https://cryptonewssentiment.streamlit.app

🙋‍♂️ Author
GitHub: @sahilmhatre4796
