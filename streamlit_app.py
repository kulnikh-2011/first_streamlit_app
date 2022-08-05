import streamlit
import pandas as pd
import requests
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#from urllib.error import URLError

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🍇 🥣 Omega 3 and Blueberry oatmeal')
streamlit.text('🥦 🥬 Kale, Spinach and Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled free range eggs')
streamlit.text('🥑 🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')


fruit_selected =streamlit.multiselect('Pick Some Fruits:',list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_show = my_fruit_list.loc[fruit_selected]


streamlit.dataframe(fruit_show)

streamlit.header('Fruityvice Fruit Advice')


new_fruit = streamlit.text_input('Which fruit would you like to add')
streamlit.write('The user added '+new_fruit+' fruit')

def insert_row_snowflake(new_fruit):
  new_fruit = streamlit.text_input('Which fruit would you like to add')
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  with my_cnx.cursor as my_cur:
    my_cur.execute("insert into fruit_load_list values ('"+new_fruit+"')")
    return "Thanks fro adding "+ new_fruit

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
