from dotenv import load_dotenv
load_dotenv() #load all the env variables
import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configure Genai key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

## Function to retrieve query from the database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define your prompt

prompt =[

    """ 
    You are an expert in converting English questions to SQL query! 
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,S​​ECTION 
    \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ; 
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this     SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or en​​d and sql word in output

    """ 
]

## Streamlit APP

st.set_page_config(page_title="Student Data Retrieval")
st.header("Provide prompts based on the :red[student data]")
st.subheader(":blue[to get best output] :lower_left_fountain_pen:", divider=True )
st.subheader("Try using - 'Tell me the student name with highest rank and provide his marks' ")

questions = st.text_input("Input: ",key="input")

submit = st.button("Ask the questions")


# if submit is clicked
if submit:
    response = get_gemini_response(questions,prompt)
    print(response)
    response = read_sql_query(response,"student.db")
    st.subheader("The response is")
    for row in response:
        print(row)
        st.header(row)

