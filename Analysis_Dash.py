import streamlit as st
import pandas as pd
import plotly.express as px
import main_youtube_analysis as main
import altair as alt


st.subheader("Discription :", divider = "blue")
st.markdown("**This analysis is based on Kenn jee's youtube channel with many focused questions answered through visualizations such as: who are kenn jee's core subcribres, what are they intrested in etc.**")
st.markdown(''':red[Note:]**These dataset was alredy publically avalible on kaggle by kenn jee.There is also a tool i created to help beginner analysis clean and visualize data automatically! just by downloading it.**''')
st.markdown(''':red[ Note:]***This dataset was was made avalible on kaggle 4 years ago from today when i published this project,[5-sep-25]***''')
st.markdown('''***This analysis will help understand what viewers of data science related content are intrested in,whcich youtube content in data science channel has lead to most growth and more.This analysis has a chance to be about 30-70 percent similar in terms of growth ,viewer intrests depending on subs,views etc if someone produces data science related content ***''' )


#python -m streamlit run Analysis_Dash.py 
st.title("Data Anlysation on Ken jee's yData Science Youtube Channel")
col1, col2, col3 = st.columns(3)

st.write("These is the dataset i worked with :")
st.dataframe(main.df.head())

st.dataframe(main.df2.head())

option_for_country_fame = st.selectbox( "Select the parameters to check relation with countries",("Subcription added per country", "views per country", "Likes Added Per Country", "Dislikes Added Per Country"))
if option_for_country_fame == "Subcription added per country":
    fig = main.piechart_for_country_with_most_subcription_added(main.top_5_country_core_most_subs)
    st.plotly_chart(fig)
elif option_for_country_fame == "views per country":
    fig2 = main.piechart_for_country_with_most_views(main.top_5_country_core_most_views)
    st.plotly_chart(fig2)
elif option_for_country_fame == "Likes Added Per Country":
    fig3 = main.piechart_for_country_with_most_video_likes_added(main.top_5_country_core_most_video_likes_added)
    st.plotly_chart(fig3)
elif option_for_country_fame == "Dislikes Added Per Country":
    fig4 = main.piechart_for_country_with_most_video_dislikes_added(main.top_5_country_core_most_Video_Dislikes_Added)
    st.plotly_chart(fig4)


#In which time frames did ken jees channel have most growth
df_chart_growth = main.videos_growth()
df_chart_decay = main.videos_decay()
dates_containing_growth =  main.videos_growth_no_head()["date_formatted"]
dates_containing_decay = main.videos_decay_no_head()["date_formatted"]

all_dates = pd.concat([dates_containing_growth, dates_containing_decay]).dropna().sort_values().unique()
default_start = dates_containing_growth.iloc[0]
default_end = dates_containing_decay.iloc[-1]

all_growth_decy = pd.concat([df_chart_growth, df_chart_decay]).dropna().sort_values(by = "date_formatted")


 # Debug: make sure it’s not empty
if not df_chart_growth.empty:
    
    date_range = st.select_slider(label =
    "[1]Pick Range of dates to the most growth/most decay ",
    options = all_dates,
    value=(all_dates[0], all_dates[-1]))

    # Filter your DataFrame
    start, end = date_range
    filtered_df = main.df2[(main.df2["Date"] >= start) & (main.df2["Date"] <= end)]

    fig = px.scatter(filtered_df , x="date_formatted", y="Views", title="[1]Growth over time with passed range", size='Views',color="date_formatted")
    chart = st.plotly_chart(fig, selelction_mode = ("points"))
    
else:
    st.warning("No data available to plot")

# creating a similar
for_fixed_growth = st.select_slider(
    label="[2]Pick Range of dates to the most growth/most decay",
    options=all_dates,
    value=(all_dates[0], all_dates[-1])
)
# Filter DataFrame based on slider
start_date, end_date = for_fixed_growth
filtered_df1 = all_growth_decy[
    (all_growth_decy["date_formatted"] >= start_date) &
    (all_growth_decy["date_formatted"] <= end_date)
]



interactive_growth = px.line(filtered_df1 , x = "date_formatted", y="Views", markers = True, line_shape="spline", title = "[2]Growth over time with passed range")




st.plotly_chart(interactive_growth, use_container_width=True)



x = main.piechart_for_top_core_aud_by_intrests(main.top_core_aud_by_intrests)
x
st.markdown('''**#conclusion 1 :the most popular ken jee's videos are "how i would learn data science ,if i had to start over", "satring over videos seem to be more popular"
#counclusion 2: people are looking for free data science courses
**''')

y = main.scatterplot_for_top_core_aud_by_intrests(main.top_core_aud_by_intrests)
y

z =main.scatterplot_for_countries_with_most_subs(main.top_by_country)
st.markdown(''':red[Note]**The info graphed above might no be accurate**''')
z


u =  main.piecharts_for_countries_with_most_views(main.top_by_country)
u


st.markdown("**Growth over time (fixed datetime values,over whole dataframe)**")
interactive_growth2 = st.line_chart(main.df2 , x = "date_formatted", y="Views")
interactive_growth2


st.markdown('''**Conclusion to : What is the core audience and what are they intrested in?
Conclusion: 1 : top core audience by "Views" :
1 = "US with 285,593"
2 = "INDIA with 203,055"
3 = "UK with 49,982"
4 = "CANADA with 49,982"
5 = "Germany with  42,422"

conclusion : 2 : top core audience by "Videos Likes added":
1 = "US with 9165"
2 = "INDIA with 8442"
3 = "UK with 1589"
4 = "CANADA with 1318"
5 = "Germany with 1216"

conclusion : 3 : top core audience by "Average view Percentag":
1 = "UK with 921740455"
2 = "GERMANY with 916349624"
3 = "US with 9110105122"
4 = "CANADA with 899897833"
5 = "INDIA with 722197251"

conclusion : 4 : top core audience by "Average Watch Time":
1 = "CANADA with 873.361"
2 = "UK with 757.451"
3 = "US with 753.948"
4 = "GERMANY with 700.364"
5 = "INDIA with 475.984"

 what are the intrests of the core audiences?

result 1:data science if started over
result 2:best "free" data science courses "untold"
result 3:"Data science projects for "beginners"
Conclusion : Audiences are looking for fresh ways to learn data science from starting over as "most" are messed up in the "prosess",they are looking for "free ways" to learn and  need "beginner project ideas".
Final Conclusion : These are the 3 biggest intrests of ken Jee's audiences.


**''')




