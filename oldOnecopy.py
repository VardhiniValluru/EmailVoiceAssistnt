import speech_recognition as sr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import imaplib
import email
import pyttsx3
from datetime import datetime
import os
import subprocess
import os
import re
import streamlit as st

current_directory = os.getcwd()

if current_directory.lower() != r'c:\users\rohith\onedrive\desktop\finalyearproject':
    print("Please run the script from the directory 'C:\\Users\\Rohith\\OneDrive\\Desktop\\FinalYearProject'")
    exit()
hidden_Styles= """
<style>
.st-emotion-cache-eqffof.e1nzilvr5{
visibility: hidden;
}
</style>
"""
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
.user{
text-align:left;
color:#222831
}
</style>
"""


speak_Styles = """
<style>
.speak{
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Platypi:ital,wght@0,300..800;1,300..800&family=Rubik+Mono+One&display=swap');
font-family: "Rubik Mono One", monospace;
color:black;
font-size:15px;
text-align: center;

}
</style>

"""

#def speak_now(image):
  #placeholder = st.empty()
  #placeholder = st.sidebar.image(f"{image}.gif")
  #return placeholder
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

def authenticate_gmail(username, password):
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(username, password)
    return mail

def delete_emails_by_sender_keyword(username, password, sender_keyword):
    mail = authenticate_gmail(username, password)
    mail.select("inbox")
    result, data = mail.search(None, f'(FROM "{sender_keyword}")')
    ids = data[0]
    id_list = ids.split()
    for email_id in id_list:
        mail.store(email_id, '+FLAGS', '\\Deleted')
    mail.expunge()
    print(f"Emails from  '{sender_keyword}'  deleted successfully!")
    
    st.markdown(f"<p class='system'><span class='border'>Emails from  '{sender_keyword}'  deleted successfully!</span></p>",unsafe_allow_html=True)
    st.markdown(convo_styles,unsafe_allow_html=True)
    speak(f"Emails from  '{sender_keyword}'  deleted successfully!")
    
def read_email(username, password):
    mail = authenticate_gmail(username, password)
    mail.select("inbox")
    result, data = mail.search(None, "ALL")
    ids = data[0]
    id_list = ids.split()
    id_list.reverse()  # Reverse the list of email IDs

    for email_id in id_list:
        result, data = mail.fetch(email_id, "(RFC822)")
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)

        subject = email_message["Subject"]
        sender = email.utils.parseaddr(email_message["From"])[1]
        date = email_message["Date"]

        # Prepare text to be spoken
        st.markdown(f'<p class="system"><span class="border">Subject: {email_message["Subject"]}</span></p>', unsafe_allow_html=True)
        st.markdown(convo_styles,unsafe_allow_html=True)
        st.markdown(f"<p class='system'><span class='border'>From: {email.utils.parseaddr(email_message['From'])[1]}</span></p>",unsafe_allow_html=True)

        text_to_speak = f"Subject: {subject}. From: {sender}."

        # Extract text content from the email body
        body = None
        for part in email_message.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":
                body = part.get_payload(decode=True).decode()
                break

        if body:
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body)
            if urls:
                st.markdown("<p class='system'><span class='border'>The email contains a link.</span></p>",unsafe_allow_html=True)
                st.markdown(convo_styles,unsafe_allow_html=True)
                body = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '',body)
                speak("The email contains a link")
            st.markdown(convo_styles,unsafe_allow_html=True)
            st.markdown(f"<p class='system'><span class='border'>Body: {body}<span></p>",unsafe_allow_html=True)
            
            

            text_to_speak += f" Body: {body} Do you want to delete this email? "


            # Speak and print the email details
            speak(text_to_speak)
            st.markdown("<p class='system'> <span class='border'> Do you want to delete this email?</span></p>",unsafe_allow_html=True)
            
            #st.write(text_to_speak)

            # Listen for the user's command
            # Listen for the user's command
            command = listen()
            print(command)
            
            # if "delete this email" in command.lower():
            #     delete_email(mail, email_id)
            #     break
            # elif "star" in command:
            #     star_email(mail, email_id)
            #     break
            # elif "next" in command:
            #     continue
            # elif "empty trash" in command:
            #     empty_trash(username, password)
            #     break
            # elif "mark as read" in command:
            #     mark_as_read(username, password)
            #     break
            if "delete" in command.lower():
                delete_email(mail, email_id)
            elif "never" in command:
                st.markdown("<p class='system'> <span class='border'> Okay, I won't delete the email.</span></p>",unsafe_allow_html=True)
                speak("Okay, I won't delete the email.")
                st.markdown("<p class='system'> <span class='border'>Can I proceed with starring this EMAIL?</span></p>",unsafe_allow_html=True)
                speak("Can I proceed with starring this EMAIL?")
                command = listen()
                print(command)
                if "proceed" in command.lower():
                    star_email(mail, email_id)
                elif "never" in command:
                    st.markdown("<p class='system'> <span class='border'>Okay, I won't star the email.</span></p>",unsafe_allow_html=True)
                    speak("Okay, I won't star the email.")
                else:
                    st.markdown("<p class='system'> <span class='border'>Invalid command.</span></p>",unsafe_allow_html=True)
                    speak("Invalid command.")
            else:
                st.markdown("<p class='system'> <span class='border'>Invalid command.</span></p>",unsafe_allow_html=True)
                speak("Invalid command.")

            speak("Do you want to read the next email?")
            st.markdown("<p class='system'> <span class='border'>Do you want to read the next email?</span></p>",unsafe_allow_html=True)
            command = listen()
            print(command)
            if "read the next mail" not in command:
                break
            else:
                print(" Please say 'next' to proceed to the next email.")
        else:
            speak("Sorry, I couldn't find the main body of the email. Do you want to read the next email?")
            command = listen()
            if "next" not in command:
                break

            else:
                st.markdown("<p class='system'><span class='border'>Invalid command.</span></p>",unsafe_allow_html=True)
                st.markdown(convo_styles,unsafe_allow_html=True)
                speak("Invalid command.")
                break

            
        # else:
        #     speak("Sorry, I couldn't find the main body of the email. Do you want to read the next email?")
        #     command = listen()
        #     if "next" not in command:
        #         break

def star_email(mail, email_id):
    mail.store(email_id, '+FLAGS', '\Flagged')
    st.markdown("<p class='system'><span class='border'>Email has been starred.</span></p>",unsafe_allow_html=True)
    st.markdown(convo_styles,unsafe_allow_html=True)
    speak("Email starred successfully!")


def delete_email(mail, email_id):
    # Mark the email for deletion
    mail.store(email_id, '+FLAGS', '\\Deleted')
    mail.expunge()
    st.markdown("<p class='system'><span class='border'>Email deleted successfully!</span></p>",unsafe_allow_html=True)
    st.markdown(convo_styles,unsafe_allow_html=True)
    speak("Email deleted successfully!")

def get_unseen_email_count(username, password):
    mail = authenticate_gmail(username, password)
    mail.select('inbox')
    result, data = mail.search(None, 'UNSEEN')
    email_ids = data[0].split()
    unseen_email_count = len(email_ids)
    st.markdown(f"<p class='system'><span class='border'>The number of unseen mails are: {unseen_email_count}</span></p>",unsafe_allow_html=True)
    st.markdown(convo_styles,unsafe_allow_html=True)
    speak("the number of unseen mails are: ")
    speak(unseen_email_count)
    return unseen_email_count

def get_new_email_count(username, password):
    mail = authenticate_gmail(username, password)
    mail.select('inbox')
    result, data = mail.search(None, 'UNSEEN', 'SINCE', datetime.now().strftime('%d-%b-%Y'))
    email_ids = data[0].split()
    new_email_count = len(email_ids)
    
    return new_email_count

def empty_trash(username, password):
    try:
        
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(username, password)

        
        mail.select('[Gmail]/Trash')


        result, data = mail.search(None, 'ALL')
        if result == 'OK':
            email_ids = data[0].split()
            for email_id in email_ids:
           
                mail.store(email_id, '+FLAGS', '\\Deleted')
            

            mail.expunge()
            print("Trash emptied successfully!")
            st.markdown("<p class='system'><span class='border'>Trash emptied successfully!</span></p>",unsafe_allow_html=True)
            st.markdown(convo_styles,unsafe_allow_html=True)
            speak("Trash emptied successfully!")
        else:
            print("Failed to fetch emails from Trash folder.")
            st.markdown("<p class='system'><span class='border'>Failed to fetch emails from Trash folder.</span></p>",unsafe_allow_html=True)
            st.markdown(convo_styles,unsafe_allow_html=True)
    except Exception as e:
        print("An error occurred:", str(e))
    finally:

        mail.logout()

def mark_as_read(username, password):
    try:

        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(username, password)


        mail.select('inbox')


        result, data = mail.search(None, 'UNSEEN')
        if result == 'OK':
            email_ids = data[0].split()
            for email_id in email_ids:
                
                mail.store(email_id, '+FLAGS', '\\Seen')
            print("All unread emails marked as read.")

            speak("All unread emails marked as read.")
            st.markdown("<p class='system'><span class='border'>All unread emails marked as read.</span></p>",unsafe_allow_html=True)
            st.markdown(convo_styles,unsafe_allow_html=True)
        else:
            print("No unread emails found.")
            st.markdown("<p class='system'>No unread emails found.</p>",unsafe_allow_html=True)
            st.markdown(convo_styles,unsafe_allow_html=True)
    except Exception as e:
        print("An error occurred:", str(e))
        st.markdown("<p class='system'>An error occurred:</p>",str(e),unsafe_allow_html=True)
    finally:

        mail.logout()
# def delete_command():
#     sender_keyword=""
#     command = listen()

    # if "spell it" in command:
    #     st.markdown("<p class='system'><span class='border'>Say the sender keyword:</span></p>.",unsafe_allow_html=True)
    #     st.markdown(convo_styles,unsafe_allow_html=True)
    #     speak("Say the sender keyword: ")
        
    #     sender_keyword = listen()
    # elif "type it" in command:
    #     sender_keyword = st.text_input("please provide the keyword: ")
    # else:
    #     speak("Sorry, I couldn't understand your command. Please try again.")
    #     st.markdown("<p class='system'>Sorry, I couldn't understand your command. Please try again.</p>",unsafe_allow_html=True)
    #     sender_keyword = delete_command()
        
    #return sender_keyword

def main():
    
    username = "savagegirlol8@gmail.com"  
    password = "xyot bdwo pbtg pygv"
    print("Hello mate!")
    speak("Hello mate!")
    new_email_count = get_new_email_count(username, password)
    if new_email_count == 0:
        print("You have no new emails. How can I assist you today?")
        speak("You have no new emails. How can I assist you today?")
    else:
        print(f"You have {new_email_count} new emails since your last login.")
        speak(f"You have {new_email_count} new emails since your last login.")
        print("Do you want to read these emails?")
        speak("Do you want to read these emails?")

        command = listen()
        if "yes" in command:
            read_email(username, password)
        else:
            print("How can I assist you today?")
            speak("How can I assist you today?")

    while True:
        command = listen()

        if "read my mails" in command:
            read_email(username, password)
        #elif "compose email" in command:
            #compose_email(username, password)
        elif "delete" in command:
            speak("Please provide the name of the sender you want to delete emails from:")
            speak("Do you wish to type the keyword or spell it?")
            
            #delete_emails_by_sender_keyword(username, password, delete_command())

        elif "empty trash" in command:
            empty_trash(username, password)
        elif "mark as read" in command:
            mark_as_read(username, password)
        elif "exit" in command:
            speak("Exiting... Goodbye!")
            st.markdown("<p clas='system'><span class='border'>Exiting... Goodbye!</span></p>",unsafe_allow_html=True)
            st.markdown(convo_styles,unsafe_allow_html=True)
            break
        else:
            speak("Sorry, I couldn't understand your command. Please try again.")
            st.markdown("<p class='system'><span class='border'> Sorry, I could not understand your command. Please try again.</span></p>",unsafe_allow_html=True)
            st.markdown(convo_styles,unsafe_allow_html=True)



if __name__ == "__main__":
    main()