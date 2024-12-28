import streamlit as st


st.title("Car Purchase Amount Prediction Model")

def gradient_background(start_color, end_color):
    """
    Creates a gradient background for the Streamlit app.

    Args:
        start_color: Starting color of the gradient in RGB format (e.g., (255, 0, 0) for red).
        end_color: Ending color of the gradient in RGB format.

    Returns:
        None
    """
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(to right, 
                rgba({start_color[0]}, {start_color[1]}, {start_color[2]}, 1), 
                rgba({end_color[0]}, {end_color[1]}, {end_color[2]}, 1));
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Define the starting and ending colors of the gradient
start_color = (35, 35, 35)  # Red
end_color = (35, 35, 35)  # Blue

# Apply the gradient background
gradient_background(start_color, end_color)

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(to bottom, #1B1833, #441752, #AB4459, #000000); /* Gradient */
        color: white; /* Text color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    .texta {
        font-size: 25px;
        font-weight: bold;
        color: white;
        position: relative;
        padding-bottom: px;
    }
    .texta::after {
        content: '';
        display: block;
        width: 100%;
        height: 3px;
        background-color: #6495ED;
        position: absolute;
        bottom: 0px;
        left: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.markdown('<div class="texta">About the Model</div>', unsafe_allow_html=True)
st.sidebar.write("")
st.sidebar.info("The model used is **Linear Regression.**", icon=":material/model_training:")

st.sidebar.image("images/dalle.webp")
st.sidebar.text("")
st.sidebar.text("🔊 We used a Linear Regression model and the following features. You can make a new car purchase prediction by specifying these values.")

first_column, second_column = st.columns(2)

with first_column:

    if st.sidebar.checkbox("Gender"):
        st.markdown("""
        <style>
        .title1 {
            font-size: 20px;
            font-weight: bold;
            color: red;
            position: relative;
            padding-bottom: px;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<div class="title1">Select your Gender:</div>', unsafe_allow_html=True)
        st.sidebar.success("You must choose whether you are a man or a woman.")
    else:
        st.markdown("""
    <style>
    .title2 {
        font-size: 20px;
        font-weight: bold;
        color: white;
        position: relative;
        padding-bottom: px;
    }
    .title2::after {
        content: '';
        display: block;
        width: 20%;
        height: 3px;
        background-color: #6495ED;
        position: absolute;
        bottom: -8px;
        left: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

        st.markdown('<div class="title2">Select your Gender:</div>', unsafe_allow_html=True)
    
    
    gender_ = st.radio("", ("Female", "Male"))

with second_column:
    if st.sidebar.checkbox("Age"):
        st.markdown("""
        <style>
        .title1 {
            font-size: 20px;
            font-weight: bold;
            color: red;
            position: relative;
            padding-bottom: px;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<div class="title1">Select your Age:</div>', unsafe_allow_html=True)
        st.sidebar.success("You must select your current age.")
    else:
        st.markdown("""
    <style>
    .title3 {
        font-size: 20px;
        font-weight: bold;
        color: white;
        position: relative;
        padding-bottom: px;
    }
    .title3::after {
        content: '';
        display: block;
        width: 20%;
        height: 3px;
        background-color: #6495ED;
        position: absolute;
        bottom: -8px;
        left: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

        st.markdown('<div class="title3">Select your Age:</div>', unsafe_allow_html=True)
    
    age = st.selectbox("", 
                        list(range(20, 71)),
                        index=None,
                        placeholder="Choose your age...")


if gender_ == "Female":
    gender = 1
else:
    gender = 0

if st.sidebar.checkbox("Annual Salary"):
    st.markdown("""
        <style>
        .title1 {
            font-size: 20px;
            font-weight: bold;
            color: red;
            position: relative;
            padding-bottom: px;
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown('<div class="title1">Select your Annual Salary:</div>', unsafe_allow_html=True)
    st.sidebar.success("You must indicate the total amount of money you earn in a year.")
    
else:
    st.markdown("""
    <style>
    .title {
        font-size: 20px;
        font-weight: bold;
        color: white;
        position: relative;
        padding-bottom: px;
    }
    .title::after {
        content: '';
        display: block;
        width: 10%;
        height: 3px;
        background-color: #6495ED;
        position: absolute;
        bottom: -8px;
        left: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Select your Annual Salary:</div>', unsafe_allow_html=True)

annual_salary = st.slider("", 20000, 100000, step=1000)

if st.sidebar.checkbox("Credit Card Dept"):
    st.markdown("""
        <style>
        .title1 {
            font-size: 20px;
            font-weight: bold;
            color: red;
            position: relative;
            padding-bottom: px;
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown('<div class="title1">Select your Credit Card Dept:</div>', unsafe_allow_html=True)
    st.sidebar.success("You must indicate the total debt of your credit cards.")
else:
    st.markdown("""
    <style>
    .title {
        font-size: 20px;
        font-weight: bold;
        color: white;
        position: relative;
        padding-bottom: px;
    }
    .title::after {
        content: '';
        display: block;
        width: 10%;
        height: 3px;
        background-color: #6495ED;
        position: absolute;
        bottom: -8px;
        left: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Select your Credit Card Dept:</div>', unsafe_allow_html=True)

dept = st.slider("", 100, 20000, step=100)

if st.sidebar.checkbox("Net Worth"):
    st.markdown("""
        <style>
        .title1 {
            font-size: 20px;
            font-weight: bold;
            color: red;
            position: relative;
            padding-bottom: px;
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown('<div class="title1">Select your Net Worth:</div>', unsafe_allow_html=True)
    st.sidebar.success("You must indicate your net worth, which is the total value of assets minus the total value of liabilities.")
else:
    st.markdown("""
    <style>
    .title {
        font-size: 20px;
        font-weight: bold;
        color: white;
        position: relative;
        padding-bottom: px;
    }
    .title::after {
        content: '';
        display: block;
        width: 10%;
        height: 3px;
        background-color: #6495ED;
        position: absolute;
        bottom: -8px;
        left: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Select your Net Worth:</div>', unsafe_allow_html=True)

worth = st.slider("", 20000, 1000000, step=10000)


import pandas as pd
import pickle

with open('Machine Learning Algorithms/Linear Regression/Car_Price_Prediction.pkl', 'rb') as f:
    loaded_pipeline = pickle.load(f)

if type(age) is not int:
    age = 1
    
new_data = {
    "gender": gender,
    "age": age,
    "annual_Salary": annual_salary,
    "credit_card_debt": dept,
    "net_worth": worth
}

new_data_2 = {
    "Gender": gender_,
    "Age": age,
    "Annual Salary": annual_salary,
    "Credit Card Debt": dept,
    "Net Worth": worth
}

new_df = pd.DataFrame(data=new_data, index=["Values"])
new_df_2 = pd.DataFrame(data=new_data_2, index=["Values"])
new_y_pred = loaded_pipeline.predict(new_df)


if "prediction_made" not in st.session_state:
    st.session_state["prediction_made"] = False  # Initialize the prediction state

if st.button("Make a Prediction"):
    if age == 1:
        st.session_state["error_message"] = "Age is not specified. Please provide the age information."
        st.session_state["prediction_made"] = False
    elif new_y_pred[0] < 0:
        st.session_state["error_message"] = "Car purchasing seems not possible according to these values above."
        st.session_state["prediction_made"] = False
    else:
        st.session_state["error_message"] = None
        st.session_state["prediction_made"] = True
        st.session_state["new_df_2"] = new_df_2
        st.session_state["prediction_result"] = f"Approximate amount of the car purchase is {new_y_pred[0]:,.2f}$"

# Display the results
if st.session_state["prediction_made"]:
    st.success("Prediction is Made!", icon=":material/thumb_up:")
    st.dataframe(st.session_state["new_df_2"])
    st.warning(st.session_state["prediction_result"], icon=":material/arrow_forward_ios:")
elif "error_message" in st.session_state and st.session_state["error_message"]:
    st.error(st.session_state["error_message"], icon=":material/warning:")

st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")

st.sidebar.write("*Created by Emre Çakır*")
    


















