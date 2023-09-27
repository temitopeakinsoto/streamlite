import streamlit as st
import cv2
import base64
import csv
import numpy as np
import json
import os
logo = './images/logo.png'


questionnaire_data_list = []
questionnaire_data = './database/questionnaire_data.json'


def getData():
    # Specify the CSV file name
    csv_file = './database/emotion_data.csv'
    # Initialize variables to store values from row 10
    emotion = None
    frame = None
    # Open the CSV file and read its contents
    with open(csv_file, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        
        # Skip the first 9 rows (0-indexed) to reach row 10
        for _ in range(9):
            next(csv_reader)
        try:
            row = next(csv_reader)
            # Check if row has at least 3 columns
            if len(row) >= 3:
                emotion = row[1]  # Value from col2
                frame = row[2]  # Value from col3
            else:
                print("Row 10 does not have enough columns.")
        except StopIteration:
            print("Reached the end of the file before reaching row 10.")
    # Check if values were found
    if emotion is not None and frame is not None:
        binary_image = base64.b64decode(frame)

        # Convert the binary image data to a NumPy array
        image_array = np.frombuffer(binary_image, np.uint8)

        # Decode the image using OpenCV
        decoded_image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        return([emotion, decoded_image])

def questionnaire():

    global questionnaire_data_list
    st.image(logo, caption="", use_column_width=False)
    st.title("University of Hertfordshire - Ethics Approval Study")
    st.subheader("HEALTH, SCIENCE, ENGINEERING AND TECHNOLOGY ECDA")
    st.write("The UH protocol number: SPECS/PGT/UH/05457")
    st.write("")
    st.write("")
    st.title("QUESTIONNAIRE")

    # Introduction
    st.markdown("""
    Thank you for your interest in participating in this survey for our research project titled 'Web-based Emotion Recognition System for E-Learning Audience Management.' Your valuable insights will contribute to enhancing the usability and effectiveness of our prototype application. 

    This questionnaire aims to gather your feedback and opinions on your experience with the emotion recognition app during e-learning activities. Your honest responses will enable us to make informed improvements to the system. 

    Please take a few moments to share your thoughts and experiences by answering the following questions. Your input is greatly appreciated and will have a significant impact on the future development of our application.
    """)

    # Age
    age = st.selectbox("**Please tell us your age:**", ["18-24", "25-34", "35-44", "45-54", "55 and above"])
    
    # Gender
    gender = st.selectbox("**Please tell us your gender:**", ["Male", "Female", "Non-binary/Other", "Prefer not to say"])

    # Ethnicity/Race
    ethnicity = st.selectbox("**What is your Ethnicity/Race:**", ["English", "Welsh", "Scottish", "Northern Irish" , "British Irish", "Indian", "Indian British", "Chinese", "Chinese British", "Any other Asian", "Caribbean", "Black African", "Black British", "Any other Black", "Asian", "Others"])

    # Frequency of e-learning activities
    frequency = st.selectbox("**How often do you engage in e-learning activities via online platforms?**", ["Never", "Daily", "Weekly", "Monthly", "Rarely", "Never"])
    learningPreference = st.selectbox("**What is your preferred model for learning**", ["Face-to-Face Classroom settings", "Online (E-Learning)", "Hybrid Model"])

    # Highest level of education
    education = st.selectbox("**Tell us your highest level of education:**", ["High School or Below", "Some College/Associate Degree", "Bachelor's Degree", "Master's Degree or Higher"])
    st.image(getData()[1])
    agree = st.radio("According to our app, your emotion in the image above is: ** "+getData()[0] + " ** Do you agree?", ["YES", "NO"])
    
    # Ratings and feedback
    overall_experience = st.slider("**On a scale of 1 - 10 (10 Being the highest), how would you rate your overall experience with using the emotion recognition app?**", 1, 10)
    comfort_level = st.slider("**On a scale of 1 - 10 (10 Being the highest), How comfortable were you using the emotion recognition system during the session?**", 1, 10)
    accuracy = st.slider("**On a scale of 1-10 (10 Being the highest), How accurately did the system detect your emotional state/facial expressions?**", 1, 10)
    recognized_emotions = st.selectbox("**Which emotions/facial expressions do you feel were accurately recognized by the system? (Happy, Sad, Angry, Confused, etc.)**", ["None", "Happy", "Neutral", "Sad", "Angry", "Confused", "Suprised", "Fear"])
    misinterpreted_emotions = st.selectbox("**Were there any emotions/facial expressions that the system misinterpreted? If yes, please specify.**", ["None", "Happy",  "Neutral", "Sad", "Angry", "Confused", "Suprised", "Fear"])
    technical_issues = st.radio("**Were there any technical issues or challenges while using the emotion recognition app? (YES/NO)**", ["YES", "NO"])
    if technical_issues == "YES":
        issue_details = st.text_input("**If yes, please specify.")

    feedback_timeliness = st.radio("**Did the system provide timely and relevant feedback to your emotional state based on your facial expression during the session? (YES/NO)**", ["YES", "NO"])
    date = st.date_input("Date:")
    # Submit button
    if st.button("Submit"):
        if not age or not gender:
            st.warning("Age and Gender Details are required.")
            return
        if not ethnicity or not frequency:
            st.warning("Ethnicity and frequency of learning are required.")
            return
        if not education:
            st.warning("Education level is required.")
            return
        # You can save or process the user's responses here
        response_data = {
            "ID": st.session_state.session_state['unique_id'],
            "Age": age,
            "Gender": gender,
            "Ethnicity/Race": ethnicity,
            "Frequency of e-learning activities": frequency,
            "Highest level of education": education,
            "Overall experience rating": overall_experience,
            "Comfort level rating": comfort_level,
            "Accuracy rating": accuracy,
            "Prefered learning Mode": learningPreference,
            "Recognized emotions": recognized_emotions,
            "Misinterpreted emotions": misinterpreted_emotions,
            "Technical issues": technical_issues,
            "Technical issue details": issue_details if technical_issues == "YES" else "",
            "Feedback timeliness": feedback_timeliness,
            "Accuracy of system": accuracy,
            "Date": str(date)
        }

        # Append the response data to the list
        questionnaire_data_list.append(response_data)

        # Load existing data from the JSON file (if any)
        if os.path.exists(questionnaire_data):
            with open(questionnaire_data, 'r') as json_file:
                questionnaire_data_list = json.load(json_file)
        else:
            questionnaire_data_list = []
        try:
            questionnaire_data_list.append(response_data)
        except Exception as e:
            str_ms = str(e)
            print('Error Message: ', str_ms)

        # Save the updated data back to the JSON file
        with open(questionnaire_data, 'w') as json_file:
            json.dump(questionnaire_data_list, json_file, indent=4)
        
        st.success("Thank you for completing the questionnaire. Your feedback is invaluable for improving our emotion recognition app for e-learning purposes.")
        st.success("You have now completed this survey and may close the browser!")
        getData()