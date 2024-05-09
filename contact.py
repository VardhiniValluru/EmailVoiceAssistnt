import streamlit as st
def app():
  styles="""
  <style>
  .col-md-8.offset-md-2.text-center{
  visibility:hidden;
  }

  .header{
  ;
  height:50px;
  font-size: 35px;
  padding: 5px;
  border-radius: 4px;
  font-weight:bold;
  }
  </style>
  """
  sidebar_styles="""
  <style>
  .st-emotion-cache-6qob1r.eczjsme3{
  background-color:#C7C7C7;

  }
  """
  st.markdown(sidebar_styles,unsafe_allow_html=True)
  st.markdown(styles,unsafe_allow_html=True)
  with st.container():
    st.markdown("""<div class="header">Get in touch with Us!</div>""",unsafe_allow_html=True)
    
    st.write("---")
    
    st.write("##")

    contact_form = """
    <style>
    
    input[type=message], input[type=email], input[type=text], textarea {
    width: 100%; /* Full width */
    padding: 12px; /* Some padding */ 
    border: 1px solid #ccc; /* Gray border */
    border-radius: 4px; /* Rounded borders */
    box-sizing: border-box; /* Make sure that padding and width stays in place */
    margin-top: 3px; /* Add a top margin */
    margin-bottom: 16px; /* Bottom margin */
    resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
  }

  /* Style the submit button with a specific background color etc */
  button[type=submit] {
    background-color: #04AA6D;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  /* When moving the mouse over the submit button, add a darker green color */
  button[type=submit]:hover {
    background-color: #45a049;
  }


  /* Hide Streamlit Branding */
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
  header {visibility: hidden;}
    </style>
    
  <form action="https://formsubmit.co/vvvardhiniv@gmail.com" method="POST">
      <input type="text" name="name" placeholder="Your name"  required size="30" required> <br>
      <input type="hidden" name="_captcha" value="false"> <br>
      <input type="email" name="email" placeholder= "email" required size="30" required><br>
      <textarea name="message" placeholder="Your message here" rows="6" cols="50" required></textarea><br>
      <button type="submit">Send</button>

  </form>
  """
  st.markdown(contact_form, unsafe_allow_html=True)

