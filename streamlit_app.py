import streamlit
import pandas as pd
import requests
import snowflake.connector

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🍇 🥣 Omega 3 and Blueberry oatmeal')
streamlit.text('🥦 🥬 Kale, Spinach and Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled free range eggs')
streamlit.text('🥑 🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_cur.execute("insert into  fruit_load_list values ('from streamlit')")

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')


fruit_selected =streamlit.multiselect('Pick Some Fruits:',list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_show = my_fruit_list.loc[fruit_selected]
my_cur.execute("insert into  fruit_load_list values ('from streamlit')")

streamlit.dataframe(fruit_show)

streamlit.header('Fruityvice Fruit Advice')
my_cur.execute("insert into  fruit_load_list values ('from streamlit')")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
my_cur.execute("insert into  fruit_load_list values ('from streamlit')")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice )
# streamlit.text(fruityvice_response.json())


fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute('select * from fruit_load_list')
my_data_row = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
streamlit.text("The Fruit Load List contains:")
#streamlit.text(my_data_row)
streamlit.dataframe(my_data_row)

add_fruit = streamlit.text_input('What fruit would you like to add','Jackfruit')
streamlit.write('Thanks for adding ',add_fruit)

my_cur.execute("insert into  fruit_load_list values ('from streamlit')")
