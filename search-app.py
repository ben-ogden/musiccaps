from PIL import Image
import pinecone
import streamlit as st
import torch
from sentence_transformers import SentenceTransformer
from ui import *

PINECONE_KEY = st.secrets["PINECONE_KEY"]
PINECONE_ENV = st.secrets["PINECONE_ENV"]
PINECONE_INDEX = "music-caps-index"


@st.cache_resource
def get_pinecone_index():
    # connect to pinecone environment
    pinecone.init(
        api_key=PINECONE_KEY,
        environment=PINECONE_ENV,
    )
    return pinecone.Index(PINECONE_INDEX)


@st.cache_resource
def get_device():
    # set device to GPU if available
    return torch.cuda.current_device() if torch.cuda.is_available() else None


@st.cache_resource
def get_transformer():
    # load the model from huggingface
    return SentenceTransformer(
        "flax-sentence-embeddings/all_datasets_v3_mpnet-base", get_device()
    )


def search_pinecone(query):
    # create embeddings for the query
    xq = retriever.encode(query).tolist()
    # query the pinecone index
    return index.query(xq, top_k=10, include_metadata=True)


index = get_pinecone_index()
retriever = get_transformer()

# layout
bg()
title()
query = st.text_input("", "")

# Query event handling
if query != "":
    results = search_pinecone(query)

    for context in results["matches"]:
        ytid = context["metadata"]["ytid"]
        start_s = int(context["metadata"]["start_s"])
        caption = context["metadata"]["caption"]
        aspect_list = context["metadata"]["aspect_list"]
        score = context["score"]
        video_card(ytid, start_s, caption, score)

footer()
