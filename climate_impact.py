import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
# Set the title of the app
st.title("Climate Coordination Network - Impact Map")
st.markdown("A snapshot of the evolution of the legacy Climate Round into Climate Coordination Network")

col1,col2,col3 = st.columns([1,1,2])
with col1:
    st.metric(label="Total Matching", value = "$2.7 million")
with col2:
    st.metric(label="Total Unique Projects", value = "469")

st.markdown("Click into a round to drill-down and explore participating projects.")
# Load your data
# Ensure your CSV file path is correct. Replace 'path_to_file' with your file path.
climate_data = pd.read_csv('./Climate_Impact.csv')

# Define non-linear bins due to the power-law distribution
# Adjust these based on the distribution of your specific data
max_value = climate_data['Matching Amount'].max()
bins = [0, 1000, 5000, 15000, 40000, max_value]

# Generate labels for these bins
bin_labels = [f"{bins[i-1]}-{bins[i]}" for i in range(1, len(bins))]

# Categorize 'Matching Amount' into non-linear, discrete bins
climate_data['Matching Amount Category'] = pd.cut(climate_data['Matching Amount'], bins=bins, labels=bin_labels)

# Create the tree map chart using the Viridis color palette
# Since you mentioned Viridis but used Sunset, I'll assume you want to stick with Sunset for the palette.
fig = px.treemap(climate_data, 
                 path=['Round', 'Project'], 
                 values='Matching Amount',
                 color='Matching Amount Category',
                 color_discrete_sequence=px.colors.sequential.Bluyl,
                 width=1500,  # Specify the width here
                 height=1000)  # Specify the height here


fig.update_traces(textfont_size=20, use_container_width=True)

# Display the figure in the Streamlit app
st.plotly_chart(fig)

st.markdown("Made at [GrantsScope](https://grantsscope.xyz)")
