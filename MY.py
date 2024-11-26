import streamlit as st
import datetime

# ---- Page Configuration ----
st.set_page_config(page_title="Bartley's Biography", page_icon="📘", layout="wide")



col1, col2, col3 = st.columns(3)

# Add content to the first column
with col1:
    st.write("")

# Add content to the second column
with col2:
    
    st.image("BART.jpg", use_container_width=True)

# Add content to the third column
with col3:
    st.write("")

# ---- Apply Custom CSS for Styling ----
st.markdown(
    """
    <style>
        body {
            background-color: #1E1E2F;
            color: #EDEDED;
            font-family: 'Arial', sans-serif;
        }
        .title {
            color: #FFD700;
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        .subheader {
            color: #FFD700;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .section {
            background: #2A2A3B;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
        }
        hr {
            border: 0;
            border-top: 1px solid #444;
            margin: 20px 0;
        }
        .stButton>button {
            background-color: #FFD700;
            color: black;
            border: none;
            border-radius: 5px;
            font-weight: bold;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #E5C100;
        }
        footer {
            text-align: center;
            color: #A9A9A9;
            font-size: 14px;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Header Section ----
st.markdown('<div class="title">Bartley\'s Biography</div>', unsafe_allow_html=True)

# ---- Initialize Session State ----
if 'bio_data' not in st.session_state:
    st.session_state['bio_data'] = {
        'name': "Bartley Josh D. Teleron",
        'age': "19",
        'gender': "Male",
        'mother': "Betsy D.Teleron",
        'mother_bday': datetime.date(1967, 2, 26),
        'father': "Joey Adelfo L. Teleron",
        'father_bday': datetime.date(1960, 10, 23),
        'guardian': "Jerry I. Teleron",
        'high_school': "Crossing Bayabas National High School",
        'senior_high_school': "Crossing Bayabas National High School",
        'college': "Surigao del Norte State University",
        'profile_picture': None,
        'achievements': [
            {"Year": "2020", "Achievement": "Graduated with honors from high school"},
            {"Year": "2022", "Achievement": "Top 10 in senior high school class"},
            {"Year": "2023", "Achievement": "Best Student in Research Awardee"}
        ]
    }

# ---- Editable Form ----
with st.form("edit_bio_form"):
    st.markdown('<div class="subheader">Personal Information</div>', unsafe_allow_html=True)
    with st.container():
        st.session_state['bio_data']['name'] = st.text_input("Full Name", st.session_state['bio_data']['name'])
        st.session_state['bio_data']['age'] = st.selectbox("Age", [str(i) for i in range(18, 101)], index=int(st.session_state['bio_data']['age']) - 18)
        st.session_state['bio_data']['gender'] = st.radio("Gender", ["Male", "Female"], index=["Male", "Female"].index(st.session_state['bio_data']['gender']))

    st.markdown('<div class="subheader">Family Background</div>', unsafe_allow_html=True)
    with st.container():
        st.session_state['bio_data']['mother'] = st.text_input("Mother's Name", st.session_state['bio_data']['mother'])
        st.session_state['bio_data']['mother_bday'] = st.date_input("Mother's Birthday", st.session_state['bio_data']['mother_bday'])
        st.session_state['bio_data']['father'] = st.text_input("Father's Name", st.session_state['bio_data']['father'])
        st.session_state['bio_data']['guardian'] = st.text_input("Guardian's Name", st.session_state['bio_data']['guardian'])

    st.markdown('<div class="subheader">Educational Attainment</div>', unsafe_allow_html=True)
    with st.container():
        st.session_state['bio_data']['high_school'] = st.text_input("High School", st.session_state['bio_data']['high_school'])
        st.session_state['bio_data']['senior_high_school'] = st.text_input("Senior High School", st.session_state['bio_data']['senior_high_school'])
        st.session_state['bio_data']['college'] = st.text_input("College", st.session_state['bio_data']['college'])

       
    # Submit Button
    submitted = st.form_submit_button("Save Changes")


# ---- Display Achievements Table ----
st.markdown('<div class="subheader">🏆 Achievements</div>', unsafe_allow_html=True)
achievements = st.session_state['bio_data']['achievements']
st.table(achievements)

# ---- Display Social Media Tabs ----
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<div class="subheader">🌐 Social Media</div>', unsafe_allow_html=True)
with st.container():
    st.markdown("[Facebook](https://www.facebook.com/bartleyjosh.teleron.5) | [Upwork](https://www.upwork.com/freelancers/~019a045a83472c8a1d)", unsafe_allow_html=True)

st.markdown('<footer>Created with 💻 using Streamlit</footer>', unsafe_allow_html=True)

