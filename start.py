import streamlit as st
import subprocess
import streamlit_option_menu
css_Styles = """
<style>
.appview-container.st-emotion-cache-1wrcr25.ea3mdgi9{
  background-image: url('https://i.pinimg.com/originals/68/3a/62/683a62ffa3980128290b9af66270f05e.png');
  height:650px;
  width:1250px;
  background-position:center center;
}
.st-emotion-cache-18ni7ap.ezrtsby2{
visibility:hidden;
}
.row-widget.stButton{
margin-top: 350px;
}
</style>"""
st.markdown(css_Styles,unsafe_allow_html=True)

if st.button("Get started"):
        subprocess.Popen(["streamlit", "run", "newMain\main.py"])