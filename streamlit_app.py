import streamlit
import pandas

streamlit.title("hello world wake its morning!")

streamlit.text("test1")
streamlit.text("test2")

streamlit.header("😂😂haslo bhai")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
