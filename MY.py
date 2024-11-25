import streamlit as st
import datetime
from subprocess import Popen
from streamlit.runtime.scriptrunner import add_script_run_ctx, get_script_run_ctx

# ---- Page Configuration ----
st.set_page_config(page_title="Biography", page_icon="📄", layout="wide")

# ---- Apply Custom CSS ----
st.markdown(
    """
    <style>
        /* Dark theme background */
        body {
            background-color: #121212;
            color: #e0e0e0;
        }

        /* Title and Subheader styles */
        .title {
            color: #FFD700;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
        
        .subheader {
            color: #FFD700;
            font-size: 24px;
            font-weight: bold;
            margin-top: 30px;
        }

        /* Input fields */
        .stTextInput, .stSelectbox, .stRadio, .stDateInput {
            background-color: #2e2e2e;
            color: #e0e0e0;
            border: 1px solid #444;
        }

        .stTextInput:focus, .stSelectbox:focus, .stRadio:focus, .stDateInput:focus {
            border-color: #FFD700;
        }

        /* Section divider */
        hr {
            border: 0;
            border-top: 1px solid #444;
            margin: 20px 0;
        }

        /* Hyperlink color */
        a {
            color: #1E90FF;
        }

        /* Button style */
        .stButton>button {
            background-color: #FFD700;
            color: black;
            border-radius: 5px;
            font-weight: bold;
        }

        /* Image style */
        .stImage {
            border-radius: 10px;
            border: 5px solid #444;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- HEADER SECTION ----
st.markdown('<div class="title">My Biography</div>', unsafe_allow_html=True)

# ---- Get Streamlit Context ----
ctx = get_script_run_ctx()

# ---- Personal Information ----
st.subheader("Personal Information")

# Name Input
name = st.text_input("Name", "Enter your name")

# Age Selection
age = st.selectbox("Age", [str(i) for i in range(18, 101)])

# Gender Selection
gender = st.radio("Gender", ["Male", "Female"])

# ---- Family Background ----
st.subheader("Family Background")

# Mother's Name
mother = st.text_input("Mother's Name", "Enter mother's name")
mbday = st.date_input("Mother's Birthday", datetime.date(1970, 1, 1))  # Default date

# Father's Name
father = st.text_input("Father's Name", "Enter father's name")

# Guardian's Name
guardian = st.text_input("Guardian's Name", "Enter guardian's name")

# ---- Educational Attainment ----
st.subheader("Educational Attainment")

hs = st.text_input("High School", "Surigao City National Highschool")
shs = st.text_input("Senior High School", "Surigao del Norte National highschool")
college = st.text_input("College", "Surigao del Norte State University")

# ---- Social Media Section ----
st.subheader("Social Media Accounts")
st.write("[Facebook](https://facebook.com)")  # Hyperlink example

# ---- Profile Picture ----
st.subheader("Profile Picture")
image = st.file_uploader("Upload your photo", type=["jpg", "png", "jpeg"])

if image:
    st.image(image, caption="Your Profile Picture", use_column_width=True)

# ---- Additional Notes ----
st.write("""
    This is a brief biography page created with Streamlit. You can add any additional information you like 
    about your background, achievements, or anything you'd like to share!
""")

# ---- Subprocess Example (Context Management) ----
if st.button("Run Subprocess"):
    # Launch a subprocess and add Streamlit context to it
    process = Popen(['python', 'your_subprocess_script.py'])
    add_script_run_ctx(process, ctx)  # Add Streamlit context to subprocess

    # Optionally wait for the process to finish if needed
    process.wait()

# ---- Footer Section (Optional) ----
st.write("---")
st.markdown("""
    <footer style="text-align: center; color: #A9A9A9;">
        <p>Created with 💻 using Streamlit</p>
    </footer>
    """, unsafe_allow_html=True)
