import streamlit as st


st.title("My Projects")


with st.expander("1. Binary Market Prediction APP"):
    st.write("""
    This project involves a machine learning model built to predict the direction of synthetic trades on the Deriv platform. 
    Using a Linear Regression algorithm, it aims to forecast if a trade will "Rise" or "Fall" based on historical data.
    """)
    st.write("- **Technologies**: Python, Machine Learning, Linear Regression, Deriv API")
    
    st.write("[View Project on GitHub](https://github.com/Latesh-Splendler/Deriv-Model/blob/main/Deriv%20Model/index.html)")  


with st.expander("2. Income Expense Tracker"):
    st.write("""
    This Projects used Streamlit python Framework to develop an application that trackes income
             and expenses. It allows users to add, edit, and delete transactions, as well as view them to 
             manage themselves
    """)
    st.write("- **Technologies**: Python, Streamlit")
    
    st.write("[View Project on GitHub](https://github.com/Latesh-Splendler/Income-Expense-Tracker)")  


with st.expander("3. Deriv Model App"):
    st.write("""
    This project is a machine learning Algorithm that was developed to predict the movement of trades
             on the Deriv platform. It uses a Linear Regression algorithm to forecast if a trade will
             it also uses a Random Forest Algorithm to perform HyperParameter Tuning to enhance the model performance
    """)
    st.write("- **Technologies**:  Python, Machine Learning")
    
    st.write("[View Project on GitHub](https://github.com/Latesh-Splendler/Deriv-Model)")  


with st.expander("4. Chat Application"):
    st.write("""
     This is a Projects that is deveoped to enable users to communicate effectively with one another effectively.
             it uses the SocketIO library to enable real time communication between users
    """)
    st.write("- **Technologies**: Python, Django")
    
    st.write("[View Project on GitHub](https://github.com/Latesh-Splendler/Chat-APP/tree/main)")  

with st.expander("5. Dead-Pool Movie Site"):
    st.write("""
     This Projects enables user to purchase Movie tickets for the movie deadpool effectively
             it uses the react Framework to enable user to purchase tickets effectively
""")
    st.write("- **Technologies**: HTNL,CSS,JavaScript")
    st.write("[View Project on Github](https://github.com/Latesh-Splendler/Dead-Pool-2)")

st.write("Feel free to explore each project for more details and code samples!")
