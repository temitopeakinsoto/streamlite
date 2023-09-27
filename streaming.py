import streamlit as st
import cv2
import os
import matplotlib.pyplot as plt
import pandas as pd
import time
import json
from deepface import DeepFace
import base64


facial_data = './database/facial_data.json'

facial_data_list = []

def image_to_base64(image):
    _, buffer = cv2.imencode('.jpg', image)
    base64_frame = base64.b64encode(buffer).decode('utf-8')
    return base64_frame

def webcam():

    global facial_data_list
    st.title("Real-time Emotion Analysis Page")
    st.write("**Welcome to this emotion recognition app. In this test session,  a 2-minute video eliciting different facial expressions will be watched, with facial expression data being collected and analysed by an emotion recognition system. Below are the steps you need to follow to complete this testing**")
    st.write("1. Click the play button on the youtube video")
    st.write("2. Click the START ANALYSIS checkbox to START the image streaming process")
    st.write("3. Click the START ANALYSIS checkbox again to STOP the image streaming process")
    st.write("4. Exit the page and proceed to the questionnaire form on the navigation panel")
    st.write("Thank you :)")

    st.markdown("""
    
    """)
    st.markdown("""
    
    """)

    # Use 0 for the default webcam
    video_capture = cv2.VideoCapture(0)

    haar_cascade = cv2.CascadeClassifier('./classifier/haar_face.xml')

    # Create lists to store timestamps and emotions
    emotion_timestamps = []
    emotion_values = []

    # Define a unique key for the checkbox
    analysis_checkbox = st.checkbox("Start Analysis", key="start_analysis_checkbox")

    # Create an empty space for displaying the video frames
    video_display = st.empty()

    # Define a scaling factor for the webcam stream
    scaling_factor = 0.5  # You can adjust this as needed

   # Path to locally saved video
    video_path = "./vid.mp4"  

    while analysis_checkbox:
        # Read a frame from the webcam
        ret, frame = video_capture.read()

        if not ret:
            break 

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
        data = {'Timestamp': emotion_timestamps, 'Emotion': emotion_values, 'frame': image_to_base64(resized_frame), 'ID': st.session_state.session_state['unique_id']}
        
        
        df = pd.DataFrame(data)
        df.to_csv('./database/emotion_data.csv', index=False)

        cv2.putText(resized_frame, txt, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        # Display the frame with emotion using Streamlit in the empty space
        video_display.image(resized_frame, channels="BGR", use_column_width=True)


        # SAVE DATA TO DB
        face_expression_data = {
            'ID': st.session_state.session_state['unique_id'],
            'Timestamp': emotion_timestamps, 
            'Emotion': emotion_values
        }
        facial_data_list.append(face_expression_data)
        # Load existing data from the JSON file (if any)
        if os.path.exists(facial_data):
            with open(facial_data, 'r') as json_file:
                facial_data_list = json.load(json_file)
        else:
            facial_data_list = []


        try:
            facial_data_list.append(face_expression_data)
        except Exception as e:
            str_msg = str(e)
            print('Error Message: ', str_msg)

        # Save the updated data back to the JSON file
        with open(facial_data, 'w') as json_file:
            json.dump(facial_data_list, json_file, indent=4)

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
        df = pd.read_csv('./database/emotion_data.csv')
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

    st.write("")
    st.write("")
    st.info("Proceed to Questionnaire Page in the Navigation Menu to continue")