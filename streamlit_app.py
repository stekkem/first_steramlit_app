import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('🥣 Breakfast Favorites')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice')

import requests

fruit_choise=streamlit.text_input('What fruit would you like information about?', 'kiwi')
streamlit.write('The user entered ', fruit_choise)

fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choise)
#streamlit.text(fruityvice_response.json())

fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.header('Fruityvice Fruit Load List - One')
streamlit.dataframe(my_data_row)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header('Fruityvice Fruit Load List - All')
streamlit.dataframe(my_data_row)

fruit_choise=streamlit.text_input('What fruit would you like to add?', 'kiwi')
streamlit.write('Thanks for adding ', fruit_choise)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
#fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choise)
#streamlit.text(fruityvice_response.json())

#fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalized)

