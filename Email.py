import streamlit as st
from oldOnecopy import listen, speak, get_new_email_count, read_email,  delete_emails_by_sender_keyword,empty_trash,mark_as_read,get_new_email_count,get_unseen_email_count
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
  
  
  header_style = """
  <style>

  @import url('https://fonts.googleapis.com/css2?family=Anton&family=Platypi:ital,wght@0,300..800;1,300..800&family=Rubik+Mono+One&display=swap');

  #head {

    color:#222831;
    font-family: "Rubik Mono One", monospace;
    font-size:40px;
    text-align: right;
    margin-bottom:1px;

  }

  #ass{

    font-family: "Rubik Mono One", monospace;
    font-size:30px;
    text-align: right;
    color:#222831;
    margin-top:1px;

  }

  #voice{
  margin-top:1px;
  font-family: "Rubik Mono One", monospace;
    font-size:50px;
    text-align: right;
    color:#EEEEEE;
    margin-bottom:1px;
    background-color:#76ABAE;

  }
  .sidebar-section{
  background-color:#76ABAE;


  }
  .st-emotion-cache-vk3wp9.eczjsme11{
  background-color:#76ABAE;

  }
  /* GIF */

  </style>"""

  css_styles = """
  <style>
  @import url('https://fonts.googleapis.com/css2?family=Anton&family=Platypi:ital,wght@0,300..800;1,300..800&family=Rubik+Mono+One&display=swap');

  .appview-container.st-emotion-cache-1wrcr25.ea3mdgi9{
  background-image: whitesmoke;
  }
  .st-emotion-cache-10fz3ls.e1nzilvr5{
  font-family: "Rubik Mono One", monospace;
  font-size:200px;
  }
  .st-emotion-cache-zq5wmm.ezrtsby0{
  visibility:hidden;
  }

  </style>
  """
  logo_styles="""

  <style>
  
    @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap');

  .logo{
  color:black;
  font-family:"Archivo Black", sans-serif;
  font-weight:bold;
  text-align:left;
  font-size:30px;
  margin-left:10px;

  }
  /*.logos{
  border:1px solid deepskyblue;
  padding: 4px;
  background-color:lavender;
  border-radius:6px;
  }*/
  .rescue{
  color:black;
  font-weight:bold;
  text-align:left;
  font-size:15px;
  margin-left:10px;
  }
  </style>"""
  convo_styles= """
  <style>
  .system{
  text-align:right;
  color:#222831;

  }
  .border{
  
  padding:4px;
  border-radius: 4px;
  }

  </style>
  """

  username = "savagegirlol8@gmail.com"  
  password = "xyot bdwo pbtg pygv" 
  def compose(username,password):
          sender_email = username
          receiver_email = st.session_state["receiver_email"]
        
          print("Please say the subject of the email.")
          st.markdown('<p class="system">Please say the subject of the email.</p>',unsafe_allow_html=True)
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
              st.markdown('<p class="system"></p>',unsafe_allow_html=True)
              speak("Email sent successfully!")
              smtp.quit()
          else:
              print("Sorry, I couldn't understand the subject or body of the email. Please try again.")
              st.markdown('<p class="system">Sorry, I couldnot understand the subject or body of the email. Please try again.</p>',unsafe_allow_html=True)
              speak("Sorry, I couldnot understand the subject or body of the email. Please try again.")
          
  def form_callback():
      #st.write(st.session_state["receiver_email"])
      compose(username,password)
      #st.write(st.session_state["my_checkbox"])
      
  def compose_email():
      with st.form(key = "my_form"):
        receiver_email = st.text_input("Enter the receiver's email address:",key = "receiver_email")
        #check_box = st.checkbox("Yes or No",key = "my_checkbox")
        submit_button = st.form_submit_button("Submit", on_click = form_callback)
        
      

  st.markdown(css_styles, unsafe_allow_html=True)
  st.markdown(header_style,unsafe_allow_html=True)
  # Define the content for the upper section
  upper_section = """
  <style>
  .st-emotion-cache-9aoz2h.e1vs0wn30{
  width:20px;
  height:20px;
  }
  </style>
  <div class="sidebar-section">
      <p id="head"><b>Email</b></p> <p id="voice"><b>Voice</b></p> <p id="ass"><b>Assistant</b></p>
  </div>
  """


  # Define the content for the lower section (with an image)


  # Add HTML content to the sidebar with custom classes
  #st.sidebar.markdown(upper_section, unsafe_allow_html=True)

  #st.sidebar.image("mainfolder\icongif.gif")
  st.markdown(convo_styles,unsafe_allow_html=True)
  st.sidebar.markdown(""" <p class='logo'><span class='logos'>Hey, It's REXA</span></p>""",unsafe_allow_html=True)
  st.sidebar.markdown(""" <p class='rescue'><span class='logos'>Your Inbox will Thank You!</span></p>""",unsafe_allow_html=True)
  st.markdown(logo_styles,unsafe_allow_html=True)
  def main():

      
      print("Hello mate!")
      st.markdown("<p class='system'><span class='border'>Hey, It's Rexa, your personalized voice assistant.</span></p>",unsafe_allow_html=True)
      speak("Hey, It's Rexa. your personalized voice assistant.")

      new_email_count = get_new_email_count(username, password)

      if new_email_count == 0:

          print("You have no new emails. How can I assist you today?")
          st.markdown('<p class="system"><span class="border">You have no new emails. How can I assist you today?</span></p>',unsafe_allow_html=True)
          st.markdown(convo_styles,unsafe_allow_html=True)
          
          speak("You have no new emails. How can I assist you today?")
          
      else:
          print(f"You have {new_email_count} new emails since your last login.")
          st.markdown(f'<p class="system"><span class="border">You have {new_email_count} emails since your last login.</span></p>',unsafe_allow_html=True)
          speak(f"You have {new_email_count} new emails since your last login.")
          #st.markdown('<p class="system"><span class="border">Do you want to read these emails?</span></p>',unsafe_allow_html=True)
          st.markdown(convo_styles,unsafe_allow_html=True)
          #print("Do you want to read these emails?")
          #speak("Do you want to read these emails?")
          speak("How can I assist you today?")
          st.markdown('<p class="system"><span class="border">How can I assist you today?</span></p>',unsafe_allow_html=True)
          #command = listen()
          #if "read" in command:
              #read_email(username, password)
          #else:
              #print("How can I assist you today?")
              #st.markdown('<p class="system">How can I assist you today?</p>',unsafe_allow_html=True)
              #speak("How can I assist you today?")

      while True:
          command = listen()

          if "read my mails" in command:
              read_email(username, password)
          #elif "compose email" in command:
              #compose_email()
          elif "delete" in command:
              speak("Please provide the name of the sender you want to delete emails from:")
              st.markdown('<p class="system"><span class="border">Please provide the name of the sender you want to delete emails from: </span></p>',unsafe_allow_html=True)
              st.markdown(convo_styles,unsafe_allow_html=True)
              #speak("Do you wish to type the keyword or spell it?")
              #st.markdown('<p class="system"><span class="border">Do you wish to type the keyword or spell it?</span></p>',unsafe_allow_html=True)
              sender_keyword = listen()              
              delete_emails_by_sender_keyword(username, password, sender_keyword)
        

          elif "empty trash" in command:
              empty_trash(username, password)
          elif "mark as read" in command:
              mark_as_read(username, password)
          elif "exit the console" in command:
              speak("Exiting... Goodbye!")
              st.markdown('<p class="system"><span class="border">Exiting... Goodbye!</span></p>',unsafe_allow_html=True)
              st.markdown(convo_styles,unsafe_allow_html=True)

              break
          
          elif "get unseen emails" in command:
              get_unseen_email_count(username,password)


              
              
          else:
              speak("Sorry, I couldn't understand your command. Please try again.")
              st.markdown('<p class="system">Sorry, I could not understand your command. Please try again.</p>',unsafe_allow_html=True)
              st.markdown(convo_styles,unsafe_allow_html=True)

  #not working
  #text="Lets get started"
  #if "click" not in st.session_state:
    #st.session_state.click = False
  #else:
    #if st.session_state.click == False:
      #text="Started"
      #st.session_state.click = True

  button_clicked = st.button("Let's get started")

  if button_clicked:
      main()
    