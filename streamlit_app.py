import streamlit
import pandas as pd

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🍇 🥣 Omega 3 and Blueberry oatmeal')
streamlit.text('🥦 🥬 Kale, Spinach and Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled free range eggs')
streamlit.text('🥑 🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.reset_index('Fruit')


streamlit.multiselect('Pick Some Fruits:',list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)


