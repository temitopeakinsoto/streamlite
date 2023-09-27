import streamlit as st
import json
import os

logo = './images/logo.png'

consent_data_list = []
consent_data = './database/consent_data.json'


def consent():
    global consent_data_list
    # global consent_data
    # Title
    st.image(logo, caption="", use_column_width=False)
    st.title("Consent Form for Study Participation")
    st.subheader("HEALTH, SCIENCE, ENGINEERING AND TECHNOLOGY ECDA")

    # Participant Information
    st.header("Participant Information")
    # name = st.text_input("Full Name ")
    contact_details = st.text_input("Contact Details (postal or email address):")

    # Study Information
    st.header("Study Information")
    st.markdown("""
    ## 1. Title of Study
    Web-Based Emotion Recognition System for E-Learning Engagement Management

    ## 2. The UH protocol number:
    SPECS/PGT/UH/05457
    """)

    # Consent Questions
    st.header("Consent Questions")
    consent_given = st.checkbox("I confirm that I have been given a Participant Information Sheet")
    withdraw = st.checkbox("I have been assured that I may withdraw from the study at any time without disadvantage or having to give a reason.")
    recording = st.checkbox("In giving my consent to participate in this study, I understand that voice, video, or photo-recording will take place.")
    data_handling = st.checkbox("I have been told how information relating to me will be handled.")
    medical_advice = st.checkbox("I understand that my participation may reveal findings that could indicate that I may require medical advice.")
    unlawful_activity = st.checkbox("I understand that if there is any revelation of unlawful activity or any indication of non-medical circumstances that would or has put others at risk, the University may refer the matter to the appropriate authorities.")
    future_contact = st.checkbox("I have been told that I may at some time in the future be contacted again in connection with this or another study.")

    # Signature
    name = st.text_input("Please Enter Your Full Name ")
    date = st.date_input("Date:")

    # Principal Investigator Information
    st.header("Principal Investigator Information")

    # Display the PI's contact information
    st.text("Contact Information of Principal Investigator:")
    st.text("TEMITOPE SAMSON AKINSOTO (ta22acf@herts.ac.uk)")

    # Disclaimer
    st.write("By submitting this form, you acknowledge that you have read and understood the information provided.")
    if st.button("Submit"):

        if not name or not contact_details:
            st.warning("Full Name and Contact Details are required.")
            return
        

        # Check if at least one consent question is selected
        if not all([consent_given, withdraw, recording, data_handling, medical_advice, unlawful_activity, future_contact]):
            st.warning("Please give full consent by clicking all the checkboxes.")
            return
        # Save data to a JSON file
        consent_form_data = {
            "ID": st.session_state.session_state['unique_id'],
            "Full Name ": name,
            "Contact Details (postal or email address)": contact_details,
            "Consent Questions": {
                "I confirm that I have been given a Participant Information Sheet": consent_given,
                "I have been assured that I may withdraw from the study at any time without disadvantage or having to give a reason.": withdraw,
                "In giving my consent to participate in this study, I understand that voice, video, or photo-recording will take place.": recording,
                "I have been told how information relating to me will be handled.": data_handling,
                "I understand that my participation may reveal findings that could indicate that I may require medical advice.": medical_advice,
                "I understand that if there is any revelation of unlawful activity or any indication of non-medical circumstances that would or has put others at risk, the University may refer the matter to the appropriate authorities.": unlawful_activity,
                "I have been told that I may at some time in the future be contacted again in connection with this or another study.": future_contact
            },
            "Date": str(date),
            "Contact Information of Principal Investigator": "TEMITOPE SAMSON AKINSOTO"
        }

        # Load existing data from the JSON file (if any)
        if os.path.exists(consent_data):
            with open(consent_data, 'r') as json_file:
                consent_data_list = json.load(json_file)
        else:
            consent_data_list = []


        try:
            consent_data_list.append(consent_form_data)
        except Exception as e:
            str_ms = str(e)
            print('Error Message: ', str_ms)

        # Save the updated data back to the JSON file
        with open(consent_data, 'w') as json_file:
            json.dump(consent_data_list, json_file, indent=4)
        
        # Display a success message
        st.success("Consent Form Submitted Successfully!")
        st.info("Proceed to App Page in the Navigation Menu")