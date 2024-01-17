#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
file_path = r'C:\Users\Jasleen Kaur\Desktop\DEVP-II_Project_Dataset.csv'
df = pd.read_csv(file_path)

# Sidebar with slicers and dropdown
st.sidebar.header("Filter Data")
selected_severity = st.sidebar.selectbox("Select Accident Severity", df["Accident_Severity"].unique())
selected_day_of_week = st.sidebar.selectbox("Select Day of Week", df["Day_of_Week"].unique())
selected_urban_rural_area = st.sidebar.selectbox("Select Urban or Rural Area", df["Urban_or_Rural_Area"].unique())

# Filter data based on selected values
filtered_data = df[
    (df["Accident_Severity"] == selected_severity)
    & (df["Day_of_Week"] == selected_day_of_week)
    & (df["Urban_or_Rural_Area"] == selected_urban_rural_area)
]

# Main content area with charts
st.title("Accident Analysis Dashboard")

# Display filtered data
st.write("Filtered Data:")
st.write(filtered_data)

# Chart 1: Bar chart - Number of accidents by day of the week
fig1 = px.bar(
    filtered_data.groupby("Day_of_Week").size().reset_index(name="Count"),
    x="Day_of_Week",
    y="Count",
    title="Number of Accidents by Day of the Week",
)
st.plotly_chart(fig1)

# Chart 2: Pie chart - Distribution of accident severity
fig2 = px.pie(
    filtered_data.groupby("Accident_Severity").size().reset_index(name="Count"),
    names="Accident_Severity",
    values="Count",
    title="Distribution of Accident Severity",
)
st.plotly_chart(fig2)

# Chart 3: Scatter plot - Number of casualties vs. number of vehicles
fig3 = px.scatter(
    filtered_data,
    x="Number_of_Vehicles",
    y="Number_of_Casualties",
    color="Accident_Severity",
    title="Number of Casualties vs. Number of Vehicles",
)
st.plotly_chart(fig3)

# Chart 4: Bar chart - Number of accidents by road type
fig4 = px.bar(
    filtered_data.groupby("Road_Type").size().reset_index(name="Count"),
    x="Road_Type",
    y="Count",
    title="Number of Accidents by Road Type",
)
st.plotly_chart(fig4)

# Chart 5: Bar chart - Number of accidents by light conditions
fig5 = px.bar(
    filtered_data.groupby("Light_Conditions").size().reset_index(name="Count"),
    x="Light_Conditions",
    y="Count",
    title="Number of Accidents by Light Conditions",
)
st.plotly_chart(fig5)


# # OBJECTIVES

# Creating a dashboard for accident data can serve various objectives, helping the viewer to gain insights, make informed decisions, and communicate findings effectively with the help of following objectives:
# 
# 1. **Accident Trends Analysis:**
#    - Visualize and analyze the trends in accident occurrences over time, days of the week, or months.
#    - Identify patterns or spikes in accidents that may correlate with specific periods or conditions.
# 
# 
# 2. **Casualty and Vehicle Analysis:**
#    - Explore the distribution of casualties and vehicles involved in accidents.
#    - Investigate the relationship between the number of casualties, vehicles, and other factors like road type or weather conditions.
# 
# 
# 3. **Geographical Analysis:**
#    - Map the geographical distribution of accidents to identify high-risk areas.
#    - Explore spatial patterns and potential hotspots of accidents.
# 
# 
# 4. **Road Type and Conditions Impact:**
#    - Analyze the impact of road type, surface conditions, and weather on accident severity.
#    - Understand how these factors contribute to the likelihood and severity of accidents.
# 
# 
# 5. **Speed Limit Analysis:**
#    - Analyze the relationship between speed limits and accident severity.
#    - Identify areas where speed limits may need adjustment for improved safety.
# 
# 
# 6. **Data-Driven Decision Making:**
#     - Provide actionable insights for policymakers, law enforcement, and transportation authorities to enhance road safety.
#     - Use the dashboard to make informed decisions on traffic management, infrastructure improvements, and safety measures.
# 
# 
# 7. **Interactive Exploration:**
#     - Enable users to interactively explore the data, filter information based on specific criteria, and gain a deeper         understanding of accident patterns.

# In[4]:


from IPython.display import Image, display

# Specify the path to your JPEG image
image_path = r'C:\Users\Jasleen Kaur\Downloads\Dashboard.jpeg'

# Display the image
display(Image(filename=image_path))


# # ABOUT THE DATASET

# The dataset under consideration presents a comprehensive repository of detailed records documenting road accidents that transpired in the month of January 2021. This compilation encompasses a wealth of information crucial for dissecting the dynamics of each incident, offering insights into various aspects such as the accident date, day of the week, junction control, accident severity, geographical coordinates, lighting conditions, weather details, and specifics regarding the involved vehicles. The dataset's temporal focus on a single month allows for a more granular examination of the contributing factors to road accidents, offering a snapshot of the urban area's road safety landscape during this specific timeframe.
# 
# The significance of this dataset lies in its potential to facilitate in-depth analyses and investigations into the multifaceted causes and consequences of road accidents. By scrutinizing variables such as accident severity and weather conditions, researchers, policymakers, and transportation authorities can gain a nuanced understanding of the challenges and risks present in the urban road network. This knowledge, in turn, can inform the development and implementation of targeted strategies and interventions aimed at enhancing road safety and mitigating the frequency and severity of accidents. Furthermore, the dataset's inclusion of vehicle details and geographical coordinates provides a foundation for spatial analyses, enabling a geographic perspective on accident patterns and hotspots. Altogether, this dataset serves as a valuable resource for those dedicated to unraveling the complexities of road safety, contributing to the ongoing efforts to create safer and more efficient urban roadways.
# 
# The incorporation of dynamic filters such as "Accident Severity," "Day of the Week," and "Urban or Rural Area" in the dashboard enhances its interactivity and functionality, providing users with a robust tool for making informed decisions. The dropdown feature allows users to customize their data view, tailoring the dashboard to their specific needs. By selecting different options within these filters, users can easily analyze and compare accident data based on severity levels, days of the week, and urban or rural settings. This not only streamlines the data exploration process but also empowers users to uncover patterns and trends that may otherwise go unnoticed. The interactive nature of the dashboard fosters a user-friendly experience, facilitating a deeper understanding of the underlying factors influencing accident outcomes. In essence, the integration of these dropdown filters within the Streamlit framework transforms the dashboard into a powerful and intuitive tool for decision-makers seeking valuable insights from the presented data.

# In[6]:


from IPython.display import Image, display

# Specify the path to your JPEG image
image_path = r'C:\Users\Jasleen Kaur\Downloads\Plot 1.jpeg'

# Display the image
display(Image(filename=image_path))


# # OBSERVATION 1

# The graph you sent me shows the number of accidents that occurred under different lighting conditions. It looks like the most accidents happen in darkness with no lighting, followed by darkness with lights unlit, and then darkness with lights lit. The least accidents happen in daylight.
# 
# Overall, the graph suggests that there is a correlation between poor lighting conditions and accidents. This is likely because it is more difficult to see in the dark, which can make it more difficult to avoid hazards. Here are some possible explanations for the observed pattern:
# 
# - Drivers may be more likely to speed in the dark because they think there are fewer police officers on the road.
# - Drivers may be more likely to be distracted in the dark, for example, by looking at their phones.
# - Older drivers may have more difficulty seeing in the dark, which could make them more likely to be involved in accidents.

# In[7]:


from IPython.display import Image, display

# Specify the path to your JPEG image
image_path = r'C:\Users\Jasleen Kaur\Downloads\Plot 2.jpeg'

# Display the image
display(Image(filename=image_path))


# # OBSERVATION 2

# This scatter plot highlights the relationship between the number of vehicles involved in accidents and the resulting number of casualties, categorized by accident severity: slight, serious, and fatal. Expect few, high-casualty points for fatal accidents, wider spread for serious, and denser, low-casualty clusters for slight ones. The viewer must look for trends within each severity and compare their distributions for potential relationships or outliers.

# In[8]:


from IPython.display import Image, display

# Specify the path to your JPEG image
image_path = r'C:\Users\Jasleen Kaur\Downloads\Plot 3.jpeg'

# Display the image
display(Image(filename=image_path))


# # OBSERVATION 3

# The graph you sent shows the number of accidents that occurred on different road types. According to the graph, the most common type of road accident occurs on single carriageways, with 521 accidents. This is followed by dual carriageways, with 223 accidents. Roundabouts and slip roads had the least number of accidents, with 59 and 37 respectively.
# 
# Overall, the graph suggests that single carriageways are the most dangerous type of road in this dataset. However, without more information, it is difficult to say for sure why this is the case. There are many possible factors that could contribute to the higher accident rate on single carriageways, such as the speed limit, the presence of hazards such as parked cars or bends, or the amount of traffic.

# In[10]:


import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Load your dataset
file_path = r'C:\Users\Jasleen Kaur\Desktop\DEVP-II_Project_Dataset.csv'
df = pd.read_csv(file_path)

df.head()


# In[11]:


# Convert 'Accident Date' to datetime
df['Accident Date'] = pd.to_datetime(df['Accident Date'])

# Initialize the Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("Accident Analysis Dashboard", style={'color': 'darkblue'}),
    
    dcc.Dropdown(
        id='day-dropdown',
        options=[{'label': day, 'value': day} for day in df['Day_of_Week'].unique()],
        value='Monday',
        multi=False,
        placeholder='Select a day',
        style={'color': 'blue'}
    ),
    
    dcc.Graph(id='bar-chart'),
    
    dcc.Graph(id='scatter-plot'),
    
    dcc.DatePickerRange(
        id='date-picker',
        start_date=df['Accident Date'].min(),
        end_date=df['Accident Date'].max(),
        display_format='YYYY-MM-DD',
        style={'margin-top': 20}
    )
])

# Define callback to update the charts based on user input
@app.callback(
    [Output('bar-chart', 'figure'),
     Output('scatter-plot', 'figure')],
    [Input('day-dropdown', 'value'),
     Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')]
)
def update_charts(selected_day, start_date, end_date):
    filtered_df = df if selected_day == 'All' else df[df['Day_of_Week'] == selected_day]
    filtered_df = filtered_df[(filtered_df['Accident Date'] >= start_date) & (filtered_df['Accident Date'] <= end_date)]

    # Bar chart
    bar_fig = px.bar(filtered_df, x='Road_Type', y='Number_of_Casualties', color='Road_Type', title='Casualties by Road Type')

    # Scatter plot
    scatter_fig = px.scatter(filtered_df, x='Accident Date', y='Number_of_Vehicles', color='Road_Type', title='Vehicles Involved over Time')

    return bar_fig.update_layout(
        plot_bgcolor='lightBlue',
        paper_bgcolor='White',
        font=dict(color='darkblue'),
        title=dict(text='Casualties by Road Type', font=dict(color='darkblue')),
        xaxis=dict(tickfont=dict(color='darkblue')),
        yaxis=dict(tickfont=dict(color='darkblue'))
    ), scatter_fig.update_layout(
        plot_bgcolor='lightBlue',
        paper_bgcolor='White',
        font=dict(color='darkblue'),
        title=dict(text='Vehicles Involved over Time', font=dict(color='darkblue')),
        xaxis=dict(tickfont=dict(color='darkblue')),
        yaxis=dict(tickfont=dict(color='darkblue'))
    )

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8070)


# # OBSERVATION 4

# **1. Purpose:**
# 
# - The code creates an interactive dashboard using Dash and Plotly to visualize accident data.
# - It's designed to help users explore relationships between accidents, road types, casualties, and dates.
# 
# 
# **2. Data:**
# 
# - It works with a DataFrame named `df` containing accident information.
# - Relevant columns include: `Accident Date`, `Day_of_Week`, `Road_Type`, `Number_of_Casualties`, and `Number_of_Vehicles`.
# 
# 
# **3. Components:**
# 
# - **Dropdown:** Users can select a specific day of the week or view data for all days.
# - **Bar Chart:** Visualizes the number of casualties for different road types.
# - **Scatter Plot:** Shows the number of vehicles involved in accidents over time, differentiated by road type.
# - **Date Picker:** Allows users to filter data within a chosen date range.
# 
# 
# **4. Features:**
# 
# - **Interactivity:** Charts dynamically update based on user selections in dropdown and date picker.
# - **Customization:** Charts have consistent styling with light blue backgrounds, white paper backgrounds, and dark blue fonts.
# - **Filtering:** Users can explore data for specific days or date ranges.
# 
# 
# **5. Insights:** (Potential, depending on data)
# 
# - Identify patterns in accident occurrences related to road types and days of the week.
# - Understand the relationship between the number of vehicles involved and casualties.
# - Observe trends in accident frequency over time.
# - Potentially uncover factors contributing to accidents on specific road types.
# 
# 
# **6. Additional Observations:**
# 
# - Code is well-structured and uses clear variable names, making it easier to understand.
# - Employs Plotly Express for concise chart creation and aesthetic appeal.
# - Incorporates a callback function to efficiently handle user interactions and chart updates.

# # MANAGERIAL INSIGHTS

# 1. **Lighting and Visibility:** 
# 
# The data reveals a clear link between poor lighting and accidents. Most collisions occur in darkness with no lights, highlighting the need for improved street lighting and driver awareness during low-visibility conditions. Additionally, addressing distractions like phone usage while driving could further enhance safety. Our data paints a concerning picture – crashes spike in darkness, particularly when lights are off. To illuminate a safer path, let's focus on two avenues: first, brightening the cityscape by strategically upgrading street lighting. Second, we must enlighten drivers about the perils of poor visibility, urging them to adapt speeds and ditch distractions like phones in the shadowy hours. By shedding light on both infrastructure and behavior, we can navigate towards a safer nocturnal journey for all.
# 
# 2. **Accident Severity and Vehicle Involvement:** 
# 
# Investigating the relationship between accident severity, casualties, and number of vehicles involved can offer valuable insights. Analyzing patterns within each severity category (slight, serious, and fatal) and comparing their distributions can expose potential hotspots and inform targeted interventions. For instance, prioritizing infrastructure improvements on roads with frequent high-casualty accidents could save lives. Our data holds the key to unlocking safer roads. By analyzing how accident severity, casualties, and vehicle involvement interact, we can uncover hidden patterns within each category: slight, serious, and fatal. Comparing their distributions exposes high-risk hotspots, where targeted interventions can save lives. Imagine focusing infrastructure upgrades on roads plagued by frequent, high-casualty collisions - a strategic strike against the deadliest accidents. This data-driven approach holds the promise of a safer tomorrow, one crash prevented at a time.
# 
# 3. **Road Type Analysis:** 
# 
# The dominance of single carriageways as accident hotspots warrants further investigation. Factors like speed limits, hazard presence, and traffic volume might contribute to this trend. By pinpointing these contributing factors, targeted strategies like speed limit adjustments, hazard removal, or traffic flow optimization can be implemented to improve safety on these critical road types. Our data exposes a troubling truth – single carriageways reign supreme as accident zones. But why? Let's dive deeper, scrutinizing factors like speed limits, hazardous obstacles, and traffic flow. Unmasking these culprits could empower us to launch targeted interventions: adjusting speeds, removing hazards, or even optimizing traffic flow. By reclaiming control of these critical arteries, we can pave the way for a safer journey for all.

# # SOURCES

# 1. https://www.kaggle.com/ (Kaggle) For Dataset- Car Accidents in 2021
# 2. https://chat.openai.com/ (ChatGpt) for Code Correction & Assistance
# 3. GitHub for Inspiration from the Analysts and Coders
