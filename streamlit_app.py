import streamlit

streamlit.title('My StraemLit App')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
dataframe_fruits = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Set index for the table the Fruit column
dataframe_fruits = dataframe_fruits.set_index('Fruit')

# Lets add a multi choice button for user interaction
streamlit.multiselect("Pick fav fruits:", list(dataframe_fruits.index), ['Avacado', 'Apple'])

# Display the table result
streamlit.dataframe(dataframe_fruits)
