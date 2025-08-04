from transformers import pipeline
import torch
import streamlit as st

@st.cache_resource

def initialize_summarizer():
    """
    Initialize the summarization pipeline with the Pegasus model.
    Model Options:
        - "google/pegasus-xsum": A model fine-tuned for summarization tasks.
        - "t5-base": A versatile model that can also be used for summarization.
        - "facebook/bart-large-cnn": Another popular model for summarization tasks.
        - "t5-small": A smaller version of the T5 model, suitable for less resource-intensive tasks.
        - "google/pegasus-large": A larger version of the Pegasus model for more complex summarization tasks.
        - "google/pegasus-cnn_dailymail": A model trained on the CNN/Daily Mail dataset for summarization.
        - "Falconsai/text_summarization": A model specifically designed for text summarization tasks.

    Returns:
        A Hugging Face pipeline for summarization.

    """
    device = 0 if torch.backends.mps.is_available() else -1
    #return pipeline("summarization", model="t5-small", device=device, tokenizer_kwargs={"use_fast": True})
    return pipeline("summarization", model="t5-small")