import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Viz-Demo')

st.title('Analytics')

####################### Used files ####################
new_df = pd.read_csv('datasets/data_viz1.csv')
secwise = pickle.load(open('datasets/secwise.pkl', 'rb'))


##################### Geomap #######################
st.header('Geomap of Price-per-sqft by Sector')
group_df = new_df.groupby('sector')[['price','price_per_sqft','built_up_area','latitude','longitude']].mean()

fig = px.scatter_map(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size="built_up_area",
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10, width=1200, height=700, hover_name=group_df.index,
                    hover_data={
                            'price_per_sqft': True,
                            'built_up_area': True,
                            'latitude': False,
                            'longitude': False
                        }                  
                  )

st.plotly_chart(fig,width='stretch')


################### WordCloud #######################
st.header('Sector-wise Amenities Word Cloud')
selected_sector  = st.selectbox('Select a sector', sorted(secwise.keys()))


if selected_sector : 
    feature_text = ' '.join(secwise[selected_sector ])

    wordcloud = WordCloud(width = 800, height = 800,
                        background_color='white',
                        stopwords = set(['s']),  # Any stopwords you'd like to exlude
                        min_font_size = 10).generate(feature_text)

    fig, ax = plt.subplots(figsize=(8,8))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)


################# scatterplot graph ###################
st.header('Area Vs Price')

property_type = st.selectbox('Select Property Type', ['Flat','House'])

if property_type == 'House':
    fig1 = px.scatter(new_df[new_df['property_type']=='house'], x='built_up_area', y='price', color='bedRoom')
else:    
    fig1 = px.scatter(new_df[new_df['property_type']=='flat'], x='built_up_area', y='price', color='bedRoom')
st.plotly_chart(fig1,width='stretch')


################# Pie Chart ####################
st.header('BHK Pie Chart')

sector_options =  new_df['sector'].unique().tolist()
sector_options.insert(0, 'Overall')

selected_sector_pie = st.selectbox('Select Sector', sector_options)

if selected_sector_pie == 'Overall':
    fig2 = px.pie(new_df, names='bedRoom')
else:
    fig2 = px.pie(new_df[new_df['sector']== selected_sector_pie], names='bedRoom')


st.plotly_chart(fig2, width='stretch')

################## Box Plot ##################
st.header('Side by Side BHK price comparision')

fig3 = px.box(new_df[new_df['bedRoom'] <=4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, width='stretch')


##################### Distplot ###############
st.header('Side by Side Distplot for property type')

fig, ax = plt.subplots(figsize=(10, 6))

sns.histplot(new_df[new_df['property_type'] == 'house']['price'], kde=True, label='House', ax=ax)
sns.histplot(new_df[new_df['property_type'] == 'flat']['price'], kde=True, label='Flat', ax=ax)

ax.set_title('Price Distribution by Property Type')
ax.set_xlabel('Price')
ax.set_ylabel('Density')
ax.legend()

st.pyplot(fig)


######################### Luxury Score ###################
st.header('Average Luxury Score by Sector')

group2_df = new_df.groupby('sector').agg(
    latitude=('latitude', 'mean'),
    longitude=('longitude', 'mean'),
    avg_luxury_score=('luxury_score', 'mean'),
    property_count=('luxury_score', 'count')
).reset_index()

fig = px.scatter_map(group2_df, lat='latitude', lon='longitude', size='property_count', color='avg_luxury_score', hover_name='sector',
    hover_data={
        'property_count': True,
        'avg_luxury_score': ':.1f',
        'latitude': False,
        'longitude': False
    },
    color_continuous_scale='electric', zoom=10, width=1200, height=700, size_max=30
)

st.plotly_chart(fig)