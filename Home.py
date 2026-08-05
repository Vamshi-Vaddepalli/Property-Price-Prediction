import streamlit as st

# st.set_page_config(
#     page_title="Hello",
#     page_icon="👋",
# )

st.set_page_config(
    page_title="Gurgaon Real Estate Suite",
    page_icon="🏠",
)

st.title("🏠 Gurgaon Real Estate Analytics Suite")

st.write("""
This app helps buyers, sellers, and analysts make sense of the Gurgaon 
property market using data scraped and cleaned from real listings across 
flats and independent houses.
""")

st.subheader("What's inside")

st.markdown("""
- **Price Predictor** — Estimates a property's price range using a 
  Random Forest model (R² ≈ 0.90) trained on property features like area, 
  location, furnishing, and luxury features. The predicted range widens 
  for higher-priced properties, since price uncertainty grows with property value.

- **Analysis App** — Explore market trends: price-per-sqft by sector, 
  amenity word clouds, price distributions by property type and BHK, 
  and luxury scoring by location.

- **Recommend Apartments** — Search for properties near a chosen 
  location within a given radius, and get similar-apartment recommendations 
  based on location, amenities, and pricing similarity.
""")

st.sidebar.success("Select a tool above to get started")

st.markdown("---")
st.caption("Built with Python, scikit-learn, and Streamlit | [GitHub](your-repo-link) | [LinkedIn](https://www.linkedin.com/in/vamshi-vaddepalli-b286501b6/)")