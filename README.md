# 🏠 Gurgaon Real Estate Analytics Suite

A Streamlit app for exploring the Gurgaon property market — predict prices,
explore trends, and find similar apartments.

**Live app:** https://property-price-prediction-gurgaon.streamlit.app/

Built on data scraped and cleaned from real flat and independent-house
listings across Gurgaon.

## What's inside

### 💰 Price Predictor
Estimate a property's price range using a Random Forest model (R² ≈ 0.90)
trained on features like area, location, bedrooms/bathrooms, furnishing,
and luxury amenities.

**How to use it:**
1. Select property type (flat or house) and sector.
2. Fill in bedrooms, bathrooms, balconies, property age, and built-up area.
3. Choose servant room / store room, furnishing type, luxury category, and
   floor category.
4. Click **Predict** — you'll get an estimated price range in Cr (crores).
   The range widens for higher-priced properties, since price uncertainty
   grows with property value.

### 📊 Analysis App
Explore market trends across Gurgaon:
- A map of average price-per-sqft by sector
- A word cloud of common amenities per sector
- Built-up area vs. price scatter plots, split by property type
- BHK distribution as a pie chart, overall or per sector
- Side-by-side price comparisons across BHK sizes
- Price distribution by property type (flat vs. house)
- A map of average luxury score by sector

Most charts have a dropdown to filter by sector or property type.

### 📍 Recommend Apartments
Two tools in one page:
- **Location search** — pick a landmark/location and a radius (in km) to see
  which listed properties fall within that distance.
- **Similar apartments** — pick an apartment by name to get the top 5 most
  similar listings, ranked by a similarity score based on location,
  amenities, and pricing.

## Data & methodology

Property listings were scraped, deduplicated, and cleaned (handling missing
values and outliers), then engineered into model-ready features — see the
notebook history in this repo's commit log for the full pipeline from
raw data to trained model.

## Tech stack
Python · pandas · scikit-learn · Streamlit · Plotly · WordCloud
