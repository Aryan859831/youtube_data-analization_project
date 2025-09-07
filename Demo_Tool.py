import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import ast
import time

"st.session_state object:" ,st.session_state

#Load data set for analysation
uploaded_file = st.file_uploader("Choose a csv", type = "csv")



def button_2():
    rows, cols = df.shape
    if df.isna().sum().sum() > df[rows]*df[rows]/2 or df[rows]*df[rows]/4 :
        st.write("You have too much NaN values in your data frame, if you still want to visualize you might not get a properly displayed graph")
    elif df.duplicated().sum().sum() > df[rows]*df[rows]/5 or df[rows]*df[rows]/7:
        st.write("You have too much duplicated values in your data frame, if you still want to visualize you might not get a properly displayed graph")
    


if uploaded_file is not None:

               
    try:
        df = pd.read_csv(uploaded_file , on_bad_lines = "skip",   sep=None, engine="python")
        df.columns = df.columns.str.strip()
        time.sleep(3)
        st.write("Uploaded sucessfully.")
        st.write("Here's a quick view of your file:")
        st.dataframe(df.head())
        st.text("Which analysation methods do you want to perform on this dataset 🧐?")
        button1 = st.button("Data cleaning:includes cleaning the data first to remove missing, NaN values etc.")
        button2 = st.button("Data visualization : includes plotting data to point anomalies and hels with dicisionsupport, Do this only when your data is fully clean or else clean your data first.")
        
        if button1 or st.session_state.get("cleaning_started", False):
            st.session_state.cleaning_started = True
            
            nan_count = df.isna().sum().sum()
            if nan_count == 0:
                st.toast("Found no NaN values, prosessing next step")
                
                    
            else:
             st.warning(f"found {nan_count} NaN values")
             action = st.radio(
                    "How would you like to handle NaN values?",
                    ["Drop rows", "Fill with 0", "Forward fill (ffill)", "Backward fill (bfill)"]
                )
             if action == "Drop rows":
                    df.dropna(inplace=True)
                    st.success("All NaN values dropped.")
             elif action == "Fill with 0":
                    df.fillna(0, inplace=True)
                    st.success("NaN values replaced with 0.")
             elif action == "Forward fill (ffill)":
                    df.fillna(method="ffill", inplace=True)
                    st.success("NaN values forward-filled.")
             elif action == "Backward fill (bfill)":
                    df.fillna(method="bfill", inplace=True)
                    st.success("NaN values backward-filled.")
                    st.dataframe(df.head())  # Show updated dataframe

            st.toast("Checking for duplicates")
            duplicates = df.duplicated().sum()
            if duplicates > 0:
                st.toast(f'duplicates found {duplicates}')
                df.drop_duplicates(inplace=True)
                st.success("Duplicates removed ✅")
            else:
                st.toast("no duplicates found")

            time.sleep(2)
            enter_columns_to_perform_unique_on = st.text_input("Enter only the specific columns for fixing unique values exeption:(Case sencitive)")
            

            if enter_columns_to_perform_unique_on:
                # Convert user input into a list (supports commas or spaces)
                column_list = [col.strip() for col in enter_columns_to_perform_unique_on.replace(",", " ").split()]
                st.session_state.column_list = column_list
                # Check which columns exist in the DataFrame
                invalid_cols = [col for col in column_list if col not in df.columns]

                if invalid_cols:
                    st.error(f"These columns are not in the DataFrame: {invalid_cols}")
                    
                else:
                    st.success(f"All columns are valid for removing unique values: {column_list}")
                    # Now you can safely work with df[column_list]
                     

            else:
                st.write("please enter the specific columns for fixing unique values exeption:(Case sencitive)")
                time.sleep(2)


            for col in column_list:
                if col not in df.columns:
                    st.error(f"Column '{col}' not found in DataFrame! Available columns: {list(df.columns)}")
                else:
                    unique_vals = df[col].unique().tolist()
                    st.write(f"Unique values in **{col}**:", unique_vals)
                    replace_input = st.text_input(
                    f"Enter replacement values for {col} (comma-separated, same count as unique values):")
                    if replace_input:
                        replacement_list = [val.strip() for val in replace_input.split(",")]
                        if len(replacement_list) != len(unique_vals):
                            st.error(f"Number of replacements must match number of unique values in {col}!")
                        else:
                            # Create mapping dictionary and replace
                            mapping = {unique_vals[i]: replacement_list[i] for i in range(len(unique_vals))}
                            df[col] = df[col].replace(mapping)
                            st.success(f"Replaced unique values in {col}")
                            st.write("Nice!!, done.")
                    else:
                        st.write("Please enter a input to replace your unique values with")
                
           
        

     
    except pd.errors.EmptyDataError:
        st.error("⚠️ This dataframe is either empty or unreadable. Please choose another file.")
else:
    st.write("please upload a file with the specifications.")
   
            













    




    











































































































































































































































































































