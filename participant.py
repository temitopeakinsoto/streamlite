import streamlit as st


logo = './images/logo.png'

def participant():

    # Title and Introduction
    st.image(logo, caption="", use_column_width=False)
    st.subheader("Ethics Committee for Studies Involving the Use of Human Participants")
    st.subheader("HEALTH, SCIENCE, ENGINEERING AND TECHNOLOGY ECDA")
    st.write("")
    st.write("")

    st.title("Participant Information Sheet")

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
    - The UH protocol number is (SPECS/PGT/UH/05457)
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
    st.info("Proceed to Consent Form Page in the Navigation Menu to continue")