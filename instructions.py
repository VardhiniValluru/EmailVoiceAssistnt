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
  .instruc{
  font-size:14px;
  }
  .command{
  font-size:20px;
  color:red;
  }
  .questions{
  font-size:20px;
  color:green;
  }
  span{
  font-weight:bold;
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
  <h1>Instructions for using REXA</h1>
  
  """,unsafe_allow_html=True)
  st.markdown("""
  <p class='instruc'>Hey there! I'm Rexa, your helpful assistant.</p>

  <p class='instruc'>Ready to dive into your emails hassle-free? Let me guide you through it!</p>
  <h6>1. Getting started:</h6>
  <p class='instruc'>I've got your back when it comes to emails! I'll let you know if there are any new emails waiting for you in your inbox, so you're always in the loop. Just a little heads up to keep you in the know!</p>
  <h6>2. Use these Commands:</h6>
  <p class='instruc'>Just so you know, you've got some emails waiting in your inbox. If you need me to take care of them, just say the word! Ready to catch up on what's been happening? Just say the magic words!</p>
  <h6>a) Read my mails:</h6>
  <p class='instruc'>When you say <span style="color: red;">'Read my mails'</span> ,I'll dive right into your inbox and start sharing the latest emails with you. I'll let you know who sent the email, when it arrived, and what it's all about with the subject line and the juicy details in the body of the email. </p>
  <p class='instruc'>
  After I read every email, I'll check in with you and ask, <span style='color:green'>Do you want to delete this email?'</span> If you're ready to bid farewell to that message, just say <span style="color: red;">'Delete'</span>, and I'll make it vanish. But if you want to keep it around a little longer, say <span style="color: red;">'Never'</span>, to let me move on. If you decide to keep it, I'll ask if you want to star that email. If you're in the mood to give it some special treatment, say <span style="color: red;">'Proceed'</span>, and I'll make it shine bright like a star if not say <span style="color: red;">‘never’. </span></p>
  <h4>b) DELETE:</h4>
  <p class='instruc'>Now away from the current email and to delete emails from a specific sender, just say <span style="color: red;">'Delete'</span>, and I'll get to work. I'll be asking you, <span style="color:green'> 'Please tell me the name of the sender whose emails you want to delete?'</span> Simply speak out the name (like Google, Amazon, LinkedIn) and I'll whisk away all their emails from your inbox permanently.</p>
  <p class='instruc'>It's a quick and easy way to keep things organized and make room for new messages. Just sit back and let me handle the cleanup – your inbox will thank you!</p>
  <h4>c) EMPTY TRASH:</h4>
  <p class='instruc'>If you ever need to tidy up your inbox and clear out the clutter, just say <span style="color: red;">'Empty Trash'</span>, and I'll take care of the rest. It's like magic, but even cooler!</p>
  <h4>c) MARK AS READ:</h4>
  <p class='instruc'>When you're ready to mark all your unread emails as read and stay on top of your inbox game, just say <span style="color: red;">'Mark as read'</span>. With a single command, I'll swiftly update your inbox, ensuring that every message is flagged as read.</p>
  <h4>SO GO AHEAD, GIVE THE ABOVE COMMANDS AND LET'S GET THOSE EMAILS SORTED OUT IN NO TIME!</h4>
  <br><br><br>
  """,unsafe_allow_html=True)
  

  #st.sidebar.success("Select a page above.")