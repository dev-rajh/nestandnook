import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Load data
df = pd.read_excel("data/products.xlsx")

# Filter by category
category = "Lifestyle"  # or "Home Decor"
df = df[df['category'] == category]

st.title(category)

num_columns = st.slider("Columns", 1, 4, 4)

rows = [df.iloc[i:i+num_columns] for i in range(0, df.shape[0], num_columns)]
for row in rows:
    cols = st.columns(num_columns)
    for col, (_, item) in zip(cols, row.iterrows()):
        with col:
            st.image(item['image_url'], use_container_width =True)
            st.subheader(item['name'])
            st.caption(item['description'])
            st.markdown(f"**Price:** ₹{item['price']}")
