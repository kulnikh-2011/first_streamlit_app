import streamlit
import pandas as pd
import requests
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
from urllib.error import URLError

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
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('Please select a fruit to get information')
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice )
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()
    
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute('select * from fruit_load_list')
my_data_row = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")







streamlit.text("The Fruit Load List contains:")
def get_fruit_load_list():
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_cur = my_cnx.cursor()
  my_cur.execute('select * from from fruit_load_list')
  return my_cur.fetchall()

# Add a button to fetch the details:
if streamlit.button('Get Fruit Load List'):
  #my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_row = get_fruit_load_list()
  streamlit.dataframe(my_data_row)
#streamlit.text(my_data_row)
#streamlit.dataframe(my_data_row)

add_fruit = streamlit.text_input('What fruit would you like to add','Jackfruit')
streamlit.write('Thanks for adding ',add_fruit)

my_cur.execute("insert into  fruit_load_list values ('from streamlit')")
