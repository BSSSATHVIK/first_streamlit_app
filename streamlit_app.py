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
fruits_selected = streamlit.multiselect("Pick fav fruits:", list(dataframe_fruits.index), ['Avocado', 'Apple'])

# Variable to get the result for the selected fruits
fruits_to_show = dataframe_fruits.loc[fruits_selected]

# Display the table result
streamlit.dataframe(fruits_to_show)
