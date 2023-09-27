import streamlit as st
import uuid

import questionnaire
import streaming
import participant
import consent


logo = './images/logo.png'

# Create a sidebar with navigation links
st.sidebar.title("Navigation")
page_selection = st.sidebar.radio("", ["Participant Information", "Consent Form", "App Page", "Questionnaire" ])

# consent_data_list = []
# questionnaire_data_list = []
# facial_data_list = []

# questionnaire_data = './database/questionnaire_data.json'
# consent_data = './database/consent_data.json'
# facial_data = './database/facial_data.json'
unique_id = str(uuid.uuid4())

if 'session_state' not in st.session_state:
    st.session_state.session_state = {}
    st.session_state.session_state['unique_id'] = str(uuid.uuid4())


        
# Call the selected page function
if page_selection == "Consent Form":
    consent.consent()
elif page_selection == "Participant Information":
    participant.participant()
elif page_selection == "Questionnaire":
    questionnaire.questionnaire()
elif page_selection == "App Page":
    streaming.webcam()