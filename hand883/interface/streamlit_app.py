import streamlit as st
import pandas as pd
from hand883.params import *


st.set_page_config(page_title="hand883", layout="wide")

html = """
<style>
.gradient-text {
    background: linear-gradient(45deg, #e16d33, #ae4f4d, #f3de82, #d59c0d);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-size: 3em;
    font-weight: bold;
}
.small_text {
    background: linear-gradient(45deg, #e16d33, #ae4f4d, #f3de82, #d59c0d);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-size: 1em;

}
</style>
<div class="gradient-text">hand883</div><div class="small_text"> - Python helping hand.</div>
"""
st.markdown(html, unsafe_allow_html=True)

data = pd.read_csv(f"{RAW_DATA}/data.csv")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
    [
        "Dashboard",
        "Feedback Classification",
        "Improvement Suggestions",
        "Sentiment Analysis",
        "Word Clouds",
        "GPT-4 Summary Tool",
        "About",
    ]
)

with tab1:
    st.subheader("Dashboard")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.subheader("Feedback Classification")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.subheader("Improvement Suggestions")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
# Title of the app


with st.container(height=600):
    for index, row in data.iterrows():
        time = row["time"]
        feedback = row["free_text"]
        improve = row["do_better"]
        sentiment = row["sentiment"]
        if sentiment == "positive":
            icon = "😀"
        elif sentiment == "negative":
            icon = "😡"
        elif sentiment == "neutral":
            icon = "😐"
        st.write(f"{icon} :grey[{time}] {feedback} :orange[{improve}]")


col1, col2 = st.columns(2)

with col1.container(height=1000):
    temperature = "-10"
    st.markdown(":rainbow[**Feedback**]")
    st.write("blue, green, orange, red, violet, gray/grey, and rainbow")
    st.write(f"temprature: :red[{temperature}]")
    st.markdown(
        """:blue[**Feedback**] in bold textThis command forces pip to reinstall the package, which can sometimes resolve path issues.
:orange[Improvement Suggestion:] Ensure that the Python interpreter you're using to run your script is the one where hand883 is installed. Sometimes, especially in systems where multiple Python environments are present, it's easy to install a package in one interpreter and inadvertently use a different interpreter to run your script.
Importing Submodules: If your package has submodules, make sure you're importing them correctly. For instance, if hand883 has a submodule named submodule, you might need to import it explicitly:This is a new heading** in bold textThis command forces pip to reinstall the package, which can sometimes resolve path issues.
Python Path: Ensure that the Python interpreter you're using to run your script is the one where hand883 is installed. Sometimes, especially in systems where multiple Python environments are present, it's easy to install a package in one interpreter and inadvertently use a different interpreter to run your script.
Importing Submodules: If your package has submodules, make sure you're importing them correctly. For instance, if hand883 has a submodule named submodule, you might need to import it explicitly:"""
    )

with col2.container(height=300):
    st.write("Column 2")
    import numpy as np
    import matplotlib.pyplot as plt

    # Create a series of x values
    x = np.linspace(0, 10, 100)

    # Generate corresponding y values with some added noise
    y = np.sin(x) + np.random.normal(0, 0.1, 100)  # sin(x) function with noise

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="Bumpy Line", color="blue")

    # Adding title and labels
    plt.title("Bumpy Line Plot")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")

    # Show legend
    plt.legend()

    # Display the plot
    st.pyplot(plt)
