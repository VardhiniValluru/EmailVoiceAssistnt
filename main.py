import streamlit as st

from streamlit_option_menu import option_menu


import home,instructions, Email, compose, contact, analysis
st.set_page_config(
        page_title="EMAIL ASSISTANT",
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='EmailAssistant',
                options=['Home','Instructions','EmailAssistant','Compose','Contact','Analysis'],
                icons=['house-fill','info-circle-fill','shield-fill','chat-fill','person-circle','reception-4'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "15px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#C7C7C7"},
        "nav-link-selected": {"background-color": "#829E9E"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Instructions":
            instructions.app()
        if app == "EmailAssistant":
            Email.app()   
        if app == "Compose":
            compose.app()      
        if app == 'Contact':
            contact.app()   
        if app == 'Analysis':
            analysis.app() 
             
          
             
    run()            
         