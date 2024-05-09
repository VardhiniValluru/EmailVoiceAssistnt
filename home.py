import streamlit as st
def app():
  
  css_styles="""
  <style>
  .main.st-emotion-cache-uf99v8.ea3mdgi8{
  background-image: url('https://i.pinimg.com/originals/91/53/f9/9153f9845ae1ff55661d779fe8e854df.png');
  height:750px;
  background-position:center center;
  }
  p{
  font-size:20px;
  text-align:justify;
  }
  h2{
  font-weight:bold;

  }
  .st-emotion-cache-zq5wmm.ezrtsby0{
  visibility:hidden;
  
  }

  </style>"""
  sidebar_styles="""
  <style>
  .st-emotion-cache-vk3wp9.eczjsme11{
  background-color:#829E9E;

  }

  </style>
  """
  st.markdown(sidebar_styles,unsafe_allow_html=True)

  st.markdown(css_styles,unsafe_allow_html=True)
  st.markdown("""
  <h1>EMAIL VOICE ASSISTANT</h1>
  
  """,unsafe_allow_html=True)
  st.markdown("""
  <p>Introducing REXA: the Email Voice Assistant. Say goodbye to tedious typing and hello to effortless communication. With just the sound of your voice, managing your inbox becomes a breeze. Whether you're composing messages, reding your important mails or organizing your priorities, our Email Voice Assistant is your ultimate productivity companion. Experience the future of email management today!</p>""",unsafe_allow_html=True)

  #st.sidebar.success("Select a page above.")