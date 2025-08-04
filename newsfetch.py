from newspaper import Article
import feedparser
import re
from transformers import pipeline
import feedparser
import streamlit as st

MACRO_KEYWORDS = [
    "interest rates", "GDP", "unemployment", "inflation", "monetary policy",
    "federal reserve", "ECB", "central bank", "economic growth", "job market",
    "labor market", "deflation", "recession", "economic data"
]

def fetch_and_filter_rss(feed_url, keywords):
    """
    Fetches articles from an RSS feed and filters them by macroeconomic keywords.
    Args:
        feed_url (str): The URL of the RSS feed to fetch.
        keywords (list): A list of keywords to filter articles.
    Returns:
        list: A list of filtered articles containing title, link, and summary.  
    """
    feed = feedparser.parse(feed_url)
    if not feed.entries:
        st.warning("No articles found in the RSS feed.")
        return []

    filtered_articles = []
    for entry in feed.entries:
        content_to_check = f"{entry.title} {entry.get('summary', '')} {entry.get('description', '')}".lower()
        if any(re.search(keyword, content_to_check, re.IGNORECASE) for keyword in keywords):
            filtered_articles.append({
                "title": entry.title,
                "link": entry.link,
                "summary": entry.get("summary", entry.get("description", "No summary available"))
            })

    return filtered_articles

def get_full_article(url):
    """
    Downloads and parses the full text of an article using the Newspaper library.
    Args:
        url (str): The URL of the article to fetch.
    Returns:
        str: The full text of the article, or None if an error occurs.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        st.error(f"Failed to fetch article content: {e}")
        return None
    
# Summarize Article Text
def summarize_article(summarizer, article_text):
    """
    Summarizes the given article text using a Hugging Face model.
    """
    try:
        summary = summarizer(article_text, max_length=130, min_length=30, do_sample=False)
        return summary[0]["summary_text"]
    except Exception as e:
        st.error(f"Summarization error: {e}")
        return "Could not summarize the article."