import streamlit as st
import cv2
from deepface import DeepFace
import time
import os
from pytube import YouTube
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
# import pygwalker as pyg
import json

# Create a sidebar with navigation links
page_selection = st.sidebar.selectbox("Select a page", ["Participant Information", "Consent Form", "App Page", "Questionnaire" ])

consent_data_list = []
questionnaire_data_list = []
questionnaire_data = './database/questionnaire_data.json'
consent_data = './database/consent_data.json'


def consent():
    global consent_data_list
    global consent_data
    # Title
    st.title("Consent Form for Study Participation")

    # Participant Information
    st.header("Participant Information")
    name = st.text_input("Full Name ")
    contact_details = st.text_input("Contact Details (postal or email address):")

    # Study Information
    st.header("Study Information")
    st.markdown("""
    ## 1. Title of Study
    Web-Based Emotion Recognition System for E-Learning Engagement Management

    ## 2. The UH protocol number:
    SPECS/PGT/UH/05457
    """)

    # st.markdown("""
    # ## 7. What Will Happen to Me If I Take Part?
    # The first thing to happen will be a short video clip, not longer than 5 minutes, which will be played for you to watch. The purpose of the video is to elicit emotions of joy, laughter, etc. While this video is being watched, the emotion recognition system will collect and analyze facial expression data through your computer’s webcam. The different facial expressions predicted by the app will be visible for you to see and decide if it matches the actual facial expression/emotion shown by you. After the completion of this session, you are free to exit the study as your involvement in the study would have been completed. A questionnaire will be used to capture your feedback about using the emotion recognition app.
    # """)

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
    st.header("Signature")
    participant_signature = st.text_input("Signature of Participant:")
    date = st.date_input("Date:")

    # Principal Investigator Information
    st.header("Principal Investigator Information")
    pi_signature = st.text_input("Signature of Principal Investigator:")
    pi_name = st.text_input("Name of Principal Investigator (BLOCK CAPITALS):")

    # Display the PI's contact information
    st.text("Contact Information of Principal Investigator:")
    st.text("TEMITOPE SAMSON AKINSOTO")

    # Disclaimer
    st.write("By submitting this form, you acknowledge that you have read and understood the information provided.")
    if st.button("Submit"):

        if not name or not contact_details:
            st.warning("Full Name and Contact Details are required.")
            return
        
        if not participant_signature or not date:
            st.warning("Participant signature and date fields are required.")
            return

        # Check if at least one consent question is selected
        if not all([consent_given, withdraw, recording, data_handling, medical_advice, unlawful_activity, future_contact]):
            st.warning("Please give full consent by clicking all the checkboxes.")
            return
        # Save data to a JSON file
        consent_form_data = {
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
            "Signature of Participant": participant_signature,
            "Date": str(date),
            "Signature of Principal Investigator": pi_signature,
            "Name of Principal Investigator": pi_name,
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

def participant():

    # Title and Introduction
    st.title("Participant Information Sheet")
    st.header("University of Hertfordshire")
    st.subheader("Ethics Committee for Studies Involving the Use of Human Participants")

    st.markdown("""
    ## 1. Title of Study
    Web-Based Emotion Recognition System for E-Learning Engagement Management
    (The UH protocol number: SPECS/PGT/UH/05457)

    ## 2. Introduction
    You are being invited to take part in a study. Before you decide whether to do so, it is important that you understand the study that is being undertaken and what your involvement will include. Please take the time to read the following information carefully and discuss it with others if you wish. Do not hesitate to ask us anything that is not clear or for any further information you would like to help you make your decision. Please do take your time to decide whether or not you wish to take part. The University’s regulation, UPR RE01, 'Studies Involving the Use of Human Participants,' can be accessed via this [link](https://www.herts.ac.uk/about-us/governance/university-policies-and-regulations-uprs/uprs) (after accessing this website, scroll down to Letter S where you will find the regulation).
    """)

    # Purpose of the Study
    st.markdown("""
    ## 3. What is the Purpose of this Study?
    The study involves the development and evaluation of an emotion recognition system capable of recognizing and classifying facial expressions/emotions in real-time during e-learning activities. The study aims to gain insights into learners' emotional states during educational activities using facial expressions. By understanding learners' emotional engagement, we seek to enhance e-learning experiences and provide valuable feedback for tailored interventions, ultimately improving learning outcomes.
    """)

    # Do I have to take part?
    st.markdown("""
    ## 4. Do I Have to Take Part?
    It is completely up to you whether or not you decide to take part in this study. If you do decide to take part, you will be given this information sheet to keep and be asked to sign a consent form. Agreeing to join the study does not mean that you have to complete it. You are free to withdraw at any stage without giving a reason. A decision to withdraw at any time or a decision not to take part at all will not affect any treatment/care that you may receive (should this be relevant).
    """)

    # Age and Other Restrictions
    st.markdown("""
    ## 5. Are There Any Age or Other Restrictions?
    This study is for individuals who are aged 18 and above and hence not suitable for minors.
    """)

    # Duration of Participation
    st.markdown("""
    ## 6. How Long Will My Part in the Study Take?
    If you decide to take part in this study, you will be involved in it for not more than 5-10 minutes.
    """)

    # What Will Happen if I Take Part?
    st.markdown("""
    ## 7. What Will Happen to Me If I Take Part?
    The first thing to happen will be a short video clip, not longer than 5 minutes, which will be played for you to watch. The purpose of the video is to elicit emotions of joy, laughter, etc. While this video is being watched, the emotion recognition system will collect and analyze facial expression data through your computer’s webcam. The different facial expressions predicted by the app will be visible for you to see and decide if it matches the actual facial expression/emotion shown by you. After the completion of this session, you are free to exit the study as your involvement in the study would have been completed. A questionnaire will be used to capture your feedback about using the emotion recognition app.
    """)

    # Possible Disadvantages, Risks, or Side Effects
    st.markdown("""
    ## 8. What Are the Possible Disadvantages, Risks, or Side Effects of Taking Part?
    Privacy concerns and potential data breaches are minimized through strict security measures. Technical issues with webcam usage and limitations in accurately interpreting emotions are possible. While the study aims to advance e-learning, there are no direct personal benefits. Participants have the right to decline or withdraw without consequences, and the research team is available for support and clarifications.
    """)

    # Possible Benefits
    st.markdown("""
    ## 9. What Are the Possible Benefits of Taking Part?
    Participation in this study will give you some feedback on your facial expressions during a learning activity. You can contemplate on your emotional response and see how this could enhance your learning by comparing with what you can recall feeling during the session. Your contribution will help advance the field of emotion recognition in e-learning, benefiting future learners and educational practices. The potential risks associated with participating are minimal. The webcam usage for facial data collection poses no harm, and we will take precautions to ensure your comfort throughout the study.
    """)

    # Confidentiality
    st.markdown("""
    ## 10. How Will My Taking Part in This Study Be Kept Confidential?
    The personal data to be obtained include the facial web stream of the participant with a view to analyzing facial expressions and emotions. Data regarding emotions captured during this study will not be stored. All facial emotions tracked and captured during each webcam streaming session will only be used to generate an emotion time which will predict/suggest the predominant emotion of a participant after the study. Personal data collected from the completed consent form study will not be retained for more than 6 weeks with an assurance that ALL data captured will be completely destroyed under secure conditions on or before October 10, 2023.
    """)

    # Audio-visual Material
    st.markdown("""
    ## 11. Audio-visual Material
    During the session, instances of your face will be temporarily captured. VIDEO OR PHOTO DATA WILL NOT BE STORED beyond the successful completion of the project or in the unlikely event of the failure of the project, not beyond the end of my studies at the University of Hertfordshire. Any parts of the face used on the final project report will be heavily blurred and appropriately cropped and shown only for proof-of-concept purposes. Any non-blurred part of the video frame used for the final project report will be cropped and re-sized so that the identity of the person will not be recognizable with the use of any current facial recognition programs I am aware of.
    """)

    # What Will Happen to the Data
    st.markdown("""
    ## 12. What Will Happen to the Data Collected Within This Study?
    - The data collected will be stored electronically, in a password-protected environment, until the successful completion and demonstration of this project (estimated mid-Sept 2023), after which time it will be destroyed under secure conditions.
    - The data will be anonymized prior to storage.
    """)

    # Data for Further Studies
    st.markdown("""
    ## 13. Will the Data Be Required for Use in Further Studies?
    The data will not be used in any further studies.
    """)

    # Review of the Study
    st.markdown("""
    ## 14. Who Has Reviewed This Study?
    This study has been reviewed by:
    - The University of Hertfordshire Health, Science, Engineering, and Technology Ethics Committee with Delegated Authority
    - The UH protocol number is <enter>
    """)

    # Factors That Might Put Others at Risk
    st.markdown("""
    ## 15. Factors That Might Put Others at Risk
    Please note that if, during the study, any medical conditions or non-medical circumstances such as unlawful activity become apparent that might or had put others at risk, the University may refer the matter to the appropriate authorities and, under such circumstances, you will be withdrawn from the study.
    """)

    # Contact Information
    st.markdown("""
    ## 16. Who Can I Contact If I Have Any Questions?
    If you would like further information or would like to discuss any details personally, please get in touch with me, in writing, by phone or by email: takinsoto@gmail.com or 07867385583.
    Although we hope it is not the case, if you have any complaints or concerns about any aspect of the way you have been approached or treated during the course of this study, please write to the University’s Secretary and Registrar at the following address:
    Secretary and Registrar
    University of Hertfordshire
    College Lane
    Hatfield
    Herts
    AL10  9AB
    Thank you very much for reading this information and giving consideration to taking part in this study.
    """)


def questionnaire():
    global questionnaire_data_list
    st.title("University of Hertfordshire - Ethics Approval Study")
    st.title("QUESTIONNAIRE")

    # Introduction
    st.markdown("""
    Thank you for your interest in participating in this survey for our research project titled 'Web-based Emotion Recognition System for E-Learning Audience Management.' Your valuable insights will contribute to enhancing the usability and effectiveness of our prototype application. 

    This questionnaire aims to gather your feedback and opinions on your experience with the emotion recognition app during e-learning activities. Your honest responses will enable us to make informed improvements to the system. 

    Please take a few moments to share your thoughts and experiences by answering the following questions. Your input is greatly appreciated and will have a significant impact on the future development of our application.
    """)

    # Age
    age = st.selectbox("Please tell us your age:", ["", "18-24", "25-34", "35-44", "45-54", "55 and above"])

    # Gender
    gender = st.selectbox("Please tell us your gender:", ["", "Male", "Female", "Non-binary/Other", "Prefer not to say"])

    # Ethnicity/Race
    ethnicity = st.selectbox("What is your Ethnicity/Race:", ["", "White", "Black", "Asian", "Others"])

    # Frequency of e-learning activities
    frequency = st.selectbox("How often do you engage in e-learning activities via online platforms?", ["", "Daily", "Weekly", "Monthly", "Rarely", "Never"])

    # Highest level of education
    education = st.selectbox("Tell us your highest level of education:", ["High School or Below", "Some College/Associate Degree", "Bachelor's Degree", "Master's Degree or Higher"])

    # Ratings and feedback
    overall_experience = st.slider("On a scale of 1 - 10 (10 Being the highest), how would you rate your overall experience with using the emotion recognition app?", 1, 10)
    comfort_level = st.slider("On a scale of 1 - 10 (10 Being the highest), How comfortable were you using the emotion recognition system during the session?", 1, 10)
    accuracy = st.slider("On a scale of 1-10 (10 Being the highest), How accurately did the system detect your emotional state/facial expressions?", 1, 10)
    recognized_emotions = st.text_input("Which emotions/facial expressions do you feel were accurately recognized by the system? (Happy, Sad, Angry, Confused, etc.)")
    misinterpreted_emotions = st.text_input("Were there any emotions/facial expressions that the system misinterpreted? If yes, please specify.")
    technical_issues = st.radio("Were there any technical issues or challenges while using the emotion recognition app? (YES/NO)", ["YES", "NO"])
    if technical_issues == "YES":
        issue_details = st.text_input("If yes, please specify.")

    feedback_timeliness = st.radio("Did the system provide timely and relevant feedback to your emotional state based on your facial expression during the session? (YES/NO)", ["YES", "NO"])

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
            "Age": age,
            "Gender": gender,
            "Ethnicity/Race": ethnicity,
            "Frequency of e-learning activities": frequency,
            "Highest level of education": education,
            "Overall experience rating": overall_experience,
            "Comfort level rating": comfort_level,
            "Accuracy rating": accuracy,
            "Recognized emotions": recognized_emotions,
            "Misinterpreted emotions": misinterpreted_emotions,
            "Technical issues": technical_issues,
            "Technical issue details": issue_details if technical_issues == "YES" else "",
            "Feedback timeliness": feedback_timeliness
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


def apppage():
    st.title("Real-time Emotion Analysis")
    st.write("This is the App Page content.")

    # Use 0 for the default webcam
    video_capture = cv2.VideoCapture(0)

    haar_cascade = cv2.CascadeClassifier('./classifier/haar_face.xml')

    # Emotion timeline data structure
    emotion_timeline = []

    # Create lists to store timestamps and emotions
    emotion_timestamps = []
    emotion_values = []

    # Define a unique key for the checkbox
    analysis_checkbox = st.checkbox("Start Analysis", key="start_analysis_checkbox")

    # Create an empty space for displaying the video frames
    video_display = st.empty()

    # Define a scaling factor for the webcam stream
    scaling_factor = 0.5  # You can adjust this as needed

    # YouTube video URL
    youtube_url = "https://www.youtube.com/shorts/KzeFa_knP5E?feature=share"

    # Download the YouTube video (if not already downloaded)
    video_path = "./vid.mp4"  # Local path to save the video
    if not os.path.exists(video_path):
        st.write("Downloading the YouTube video... (This may take a moment)")
        yt = YouTube(youtube_url)
        yt.streams.filter(file_extension="mp4", progressive=True).order_by("resolution").desc().first().download(filename="youtube_video")

    while analysis_checkbox:
        # Read a frame from the webcam
        ret, frame = video_capture.read()

        # Resize the frame by the specified scaling factor
        height, width = frame.shape[:2]
        new_width = int(width * scaling_factor)
        new_height = int(height * scaling_factor)
        resized_frame = cv2.resize(frame, (new_width, new_height))

        result = DeepFace.analyze(img_path=resized_frame, actions=['emotion'], enforce_detection=False)

        # Convert video stream to gray
        gray_video = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        faces = haar_cascade.detectMultiScale(gray_video, 1.1, 4)

        # Loop through points numpy array in faces and construct a facial rectangle
        for (x, y, w, h) in faces:
            cv2.rectangle(resized_frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

        # Extract dominant emotion and timestamp
        emotion = result[0]['dominant_emotion']
        timestamp = time.time()
        txt = f"{emotion} (Timestamp: {timestamp:.2f})"

        # Append emotion and timestamp to the lists

        emotion_timestamps.append(timestamp)
        emotion_values.append(emotion)
        data = {'Timestamp': emotion_timestamps, 'Emotion': emotion_values}
        df = pd.DataFrame(data)
        df.to_csv('emotion_data.csv', index=False)

        cv2.putText(resized_frame, txt, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        # Display the frame with emotion using Streamlit in the empty space
        video_display.image(resized_frame, channels="BGR", use_column_width=True)

    # Release the webcam when the checkbox is unchecked
    if not analysis_checkbox:
        video_capture.release()

    # Save the emotion and timestamp data to a CSV file

    # Print the emotion timeline after the analysis is stopped
    # st.write('Total emotions detected:', emotion_timeline)

    # Embed the YouTube video using st.video
    st.video(video_path, format='video/mp4')

    if not analysis_checkbox:
        # Read emotion and timestamp data from the CSV file
        df = pd.read_csv('emotion_data.csv')
        emotion_timestamps = df['Timestamp'].tolist()
        emotion_values = df['Emotion'].tolist()

        # Create a Matplotlib line graph
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(emotion_timestamps, emotion_values, marker='o', linestyle='-', markersize=5)
        ax.set_xlabel('Timestamp')
        ax.set_ylabel('Emotion')
        ax.set_title('Emotion vs. Timestamp')
        plt.xticks(rotation=45)

        # Display the Matplotlib figure using Streamlit
        st.pyplot(fig)
        # walker = pyg.walk(df)
        

# Call the selected page function
if page_selection == "Consent Form":
    consent()
elif page_selection == "Participant Information":
    participant()
elif page_selection == "Questionnaire":
    questionnaire()
elif page_selection == "App Page":
    apppage()
