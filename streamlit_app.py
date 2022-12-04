import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spanich & Rocket Smoothie')
streamlit.text('🐔 Hard--Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#create the repeatative code block called fuctions
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('Please select a fruit to get information')
  else:
    back_from_fuction = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_fuction)
except URLError as e:
    streamlit.error()

streamlit.header("The fruit load list contains:")
#streamlit related function
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    my_cur.fetchone()
    
#add this button to load the fruit
if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.text(my_data_rows)
    
#will not execute anything below this
streamlit.stop()
#import snowflake.connector

streamlit.dataframe(my_data_row)
fruit_choice = streamlit.text_input('What fruit would you like to add?',fruit_choice)
streamlit.write('Thanks for adding ', fruit_choice)

#this will not work correctly 
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
