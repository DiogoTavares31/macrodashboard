import newsfetch
import macrofetch
import financefetch
import summarizermodel
import streamlit as st
import matplotlib.pyplot as plt

# Streamlit app layout
st.set_page_config(page_title="Macro News and Data App", layout="wide")

def main():
    st.title("📚 Macro Feed")

    # ----- Sidebar: Macroeconomic Data -----
    # st.sidebar.header("📈 Key Macroeconomic Indicators")

    interest_rate = macrofetch.get_interest_rate()
    inflation_rate = macrofetch.get_inflation_rate()
    unemployment_rate = macrofetch.get_unemployment_rate()
    gdp_growth_rate = macrofetch.get_gdp_growth_rate()
    fgi_value, fgi_description = financefetch.get_fear_and_greed_index()

    with st.sidebar:

        with st.container():
            
            financefetch.display_fear_and_greed_gauge(int(fgi_value), fgi_description)

        st.divider()

        with st.container():
            st.markdown("#### 🔍 Key Indicators")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                <b>Prime Rate:</b><br>
                <span style='font-size: 18px'>{interest_rate:.2f}%</span>
                """, unsafe_allow_html=True, help="Interest rate that commercial banks charge their most creditworthy customers.")

                st.markdown(f"""
                <b>Unemployment:</b><br>
                <span style='font-size: 18px'>{unemployment_rate:.2f}%</span>
                """, unsafe_allow_html=True,help="Current unemployment rate in the US.")

            with col2:
                st.markdown(f"""
                <b>Inflation (YoY):</b><br>
                <span style='font-size: 18px'>{inflation_rate:.2f}%</span>
                """, unsafe_allow_html=True,help="Current inflation rate in the US, year-over-year.")

                st.markdown(f"""
                <b>GDP Growth:</b><br>
                <span style='font-size: 18px'>{gdp_growth_rate:.2f}%</span>
                """, unsafe_allow_html=True,help="Current GDP growth rate in the US.")

        st.caption("Latest official data (updated periodically)")

    # ----- Main Section -----

    # Define asset tickers
    
    #st.title("📊 Market Snapshot (Last 3 Months)")

    market_data = financefetch.fetch_market_data()

    cols = st.columns(2)
    for i, (label, series) in enumerate(market_data.items()):
        with cols[i % 2]:
            st.markdown(f"**{label}**")
            fig, ax = plt.subplots(figsize=(5, 2.5))
            ax.plot(series.index, series.values, color="#1f77b4")
            ax.set_ylabel("Price (USD)")
            ax.set_xlabel("")
            ax.set_title(label, fontsize=12)
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)

    st.markdown("---")

    if any("Summarize Article" in k for k in st.session_state.keys()):
        with st.spinner("Loading summarizer..."):
            summarizer = summarizermodel.initialize_summarizer()
    else:
        summarizer = None


    RSS_FEEDS = {
        "The New York Times": "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml",
        "CNBC": "https://www.cnbc.com/id/100003114/device/rss/rss.html",
        "BBC Business": "http://feeds.bbci.co.uk/news/business/rss.xml"
    }

    # Create pill selector with default
    news_source = st.pills(
        label="News Source",
        options=list(RSS_FEEDS.keys()),
        default="The New York Times",
        help="Select a news source to fetch macroeconomic articles."
    )

    feed_url = RSS_FEEDS[news_source]

    articles = newsfetch.fetch_and_filter_rss(feed_url, newsfetch.MACRO_KEYWORDS)

    if articles:
        for idx, article in enumerate(articles):
            st.write(f"### {article['title']}")
            st.write(f"[Read Full Article]({article['link']})")
            st.write(f"**Snippet:** {article['summary']}")
            
            if st.button(f"Summarize Article", key=f"summary_{idx}"):
                if summarizer is None:
                    with st.spinner("Loading summarizer..."):
                        summarizer = summarizermodel.initialize_summarizer()
                full_text = newsfetch.get_full_article(article['link'])
                if full_text:
                    st.write("**Summary:**")
                    st.write(summarizermodel.summarize_article(summarizer, full_text))
                else:
                    st.error("Failed to fetch the full article content.")
    else:
        st.warning("No macroeconomic news articles found.")

    

if __name__ == '__main__':
    main()
