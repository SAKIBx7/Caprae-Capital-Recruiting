import streamlit as st
import pandas as pd
from utils import is_valid_email, is_business_email, is_website_live, has_linkedin, calculate_score

st.title("Smart Lead Scorer 🔍✨")
st.write("Upload your CSV with leads (email, website, LinkedIn, etc.)")

uploaded = st.file_uploader("Upload CSV", type=['csv'])

if uploaded:
    df = pd.read_csv(uploaded)
    st.write("Original Data:", df.head())

    # ✅ Apply all validation & scoring first
    df['Valid Email'] = df['email'].apply(is_valid_email)
    df['Business Email'] = df['email'].apply(is_business_email)
    df['Website Live'] = df['website'].apply(is_website_live)
    df['LinkedIn Present'] = df['linkedin'].apply(has_linkedin)
    df['Lead Score'] = df.apply(calculate_score, axis=1)

    # ✅ THEN show the final verified table
    st.write("Verified Leads Table:", df)

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Cleaned CSV", csv, "cleaned_leads.csv", "text/csv")
