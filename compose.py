
import streamlit as st
import speech_recognition as sr
import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyttsx3
from datetime import datetime
import os
import subprocess
import os
import re
def app():
  side_bar_Styles= """
  <style>
  .st-emotion-cache-6qob1r.eczjsme3{
  background-color:#829E9E;
  }

  </style>
  """
  convo_styles = """
  <style>
  .system{
  text-align:right;
  color:black;
  }
  .user{
  text-align:left;
  color:black;
  }
  .border{

  padding:4px;
  border-radius:4px;
  }
  </style>
  """
  css_styles="""
  <style>
  .appview-container.st-emotion-cache-1wrcr25.ea3mdgi9{
  background-color:#C7C7C7;
  }
  .st-emotion-cache-zq5wmm.ezrtsby0{
  visibility:hidden;
  }
  </style>"""

  speak_Styles = """
  <style>
  .speak{

  color:#E27966;
  font-weight:bold;
  font-size:15px;
  text-align: center;
  }
  </style>

  """
  st.markdown(side_bar_Styles,unsafe_allow_html=True)
  st.markdown(css_styles,unsafe_allow_html=True)
  username = "savagegirlol8@gmail.com"  
  password = "xyot bdwo pbtg pygv" 
  def listen():
      recognizer = sr.Recognizer()
      with sr.Microphone() as source:
          print("Listening...")
          st.markdown("<p class='speak'> Speak Now </p>",unsafe_allow_html=True)
          st.markdown(speak_Styles,unsafe_allow_html=True)
          recognizer.adjust_for_ambient_noise(source)
          audio = recognizer.listen(source)
      try:
          print("Recognizing...")
          st.markdown("<p class='speak'> Recognizing.. </p>",unsafe_allow_html=True)
          st.markdown(speak_Styles,unsafe_allow_html=True)

          command = recognizer.recognize_google(audio).lower()
          st.markdown(f'<p class="user"><span class="border">{command}<span></p>',unsafe_allow_html=True)
          st.markdown(convo_styles,unsafe_allow_html=True)
          print("You said:", command)
          return command
      except sr.UnknownValueError:
          print("Sorry, I could not understand that.")
          st.markdown("<p class='system'><span class='border'>Sorry, I could not understand that.</span></p>",unsafe_allow_html=True)
          st.markdown(convo_styles,unsafe_allow_html=True)
          
          return ""
      except sr.RequestError as e:
          print("Could not request results from Google Speech Recognition service; {0}".format(e))
          
          st.markdown(f'<p class="system"><span class="border">Could not request results from Google Speech Recognition service; {0}</span></p>'.format(e),unsafe_allow_html=True)
          st.markdown(convo_styles,unsafe_allow_html=True)
          return ""

  def speak(text):
      engine = pyttsx3.init()
      engine.say(text)
      engine.runAndWait()

  def compose(username,password):
          sender_email = username
          receiver_email = st.session_state["receiver_email"]
        
          print("Please say the subject of the email.")
          st.markdown('<p class="system">Please say the subject of the email.</p>',unsafe_allow_html=True)
          st.markdown(convo_styles,unsafe_allow_html=True)
          speak("Please say the subject of the email.")
          subject = listen()

          print("Please say the body of the email.")
          st.markdown('<p class="system">Please say the body of the email.</p>',unsafe_allow_html=True)
          speak("Please say the body of the email.")
          body = listen()

          if subject and body:
              message = MIMEMultipart()
              message["From"] = sender_email
              message["To"] = receiver_email
              message["Subject"] = subject
              message.attach(MIMEText(body, "plain"))

              text = message.as_string()

              smtp = smtplib.SMTP('smtp.gmail.com', 587)
              smtp.starttls()
              smtp.login(username, password)
              smtp.sendmail(sender_email, receiver_email, text)
              print("Email sent successfully!")
              st.markdown('<p class="system">Email sent successfully!</p>',unsafe_allow_html=True)
              speak("Email sent successfully!")
              st.markdown(convo_styles,unsafe_allow_html=True)
              smtp.quit()
          else:
              print("Sorry, I couldn't understand the subject or body of the email. Please try again.")
              st.markdown('<p class="system">Sorry, I couldnot understand the subject or body of the email. Please try again.</p>',unsafe_allow_html=True)
              st.markdown(convo_styles,unsafe_allow_html=True)
              speak("Sorry, I couldnot understand the subject or body of the email. Please try again.")
          
  def form_callback():
      #st.write(st.session_state["receiver_email"])
      compose(username,password)
      #st.write(st.session_state["my_checkbox"])
      
  def compose_email():
      speak("Please enter receiver's mail address")
      with st.form(key = "my_form"):
        receiver_email = st.text_input("Enter the receiver's email address:",key = "receiver_email")
        #check_box = st.checkbox("Yes or No",key = "my_checkbox")
        submit_button = st.form_submit_button("Submit", on_click = form_callback)
  def main():
      compose_email()
  button_clicked = st.button("Let's get started")

  if button_clicked:
      main()