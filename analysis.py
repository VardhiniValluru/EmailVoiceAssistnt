import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
def app():
    #VOICE INPUT
    st.markdown('<h3>Accuracy of VOICE INPUT</h3>',unsafe_allow_html=True)
    labels = ['Perfect Accuracy', 'Fair Accuracy', 'Low accuracy']
    values = [65, 32, 3]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.5)])
    #fig.update_layout(
    #title="Donut Chart",
    #font=dict(
        #family="Arial, sans-serif",
        #size=12,
        #color="RebeccaPurple"
      #))
    st.plotly_chart(fig)
    #READING MAILS
    read_data = {
        'read data' : ['Email1', 'Email2','Email3','Email4','Email5'],
        'Accuracy Rate (%)': [100, 100, 99, 95, 100]

    }
    df = pd.DataFrame(read_data)
    st.markdown('<h3>Accuracy of READING MAILS</h3>',unsafe_allow_html=True)
    st.bar_chart(df.set_index('read data'))
    


    #COMPOSING MAILS
    accuracy_data = {
        'User': ['User 1', 'User 2', 'User 3', 'User 4', 'User 5'],
        'Accuracy (%)': [92, 90, 94, 100, 97]
    }
    df = pd.DataFrame(accuracy_data)
    st.markdown('<h3>Testing Accuracy for Composing Email</h3>',unsafe_allow_html=True)
    st.bar_chart(df.set_index('User'))
    #DELETING
    delete_data = {
        'User': ['keyword 1', 'keyword 2', 'keyword 3', 'keyword 4', 'keyword 5'],
        'Accuracy (%)': [90, 84, 75, 100, 93]
    }
    df = pd.DataFrame(delete_data)
    st.markdown('<h3>Testing Accuracy for DELETE using keyword</h3>',unsafe_allow_html=True)
    st.bar_chart(df.set_index('User'))
    #ERROR RATE
    ERROR_data = {
        'User': ['Input 1', 'Input 2', 'Input 3', 'Input 4', 'Input 5'],
        'Accuracy (%)': [5,3,2,8,7]
    }
    df = pd.DataFrame(ERROR_data)
    st.markdown('<h3>ERROR RATE</h3>',unsafe_allow_html=True)
    st.bar_chart(df.set_index('User'))
    #EMPTYING TRASH
    st.markdown('<h3>Testing Accuracy for EMPTY TRASH</h3>',unsafe_allow_html=True)
    labels = ['Successful', 'Unsuccessful']
    sizes = [99.6, 0.4]  # Sample percentages for each category

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

    # Set the title
    #ax.set_title('Pie Chart Example')

    # Display the chart in Streamlit
    st.pyplot(fig)
    
    #TASK COMPLETION
    task_data = {
        'task' : ['Compose', 'Read', 'Empty trash','Mark as read', 'Delete', 'Delete using keyword', 'Unseen mail count', 'star'],
        'Completion' : [95, 90, 100, 100, 90, 95, 100, 90]
    }
    df = pd.DataFrame(task_data)
    st.title("TASK COMPLETION RATE")
    st.bar_chart(df.set_index('task'))
    
    #OVERALSTATS
    data = {
        'Command Types': ['Compose', 'Read', 'Empty trash','Mark as read', 'Delete', 'Delete using keyword', 'Unseen mail count', 'star'],
        'Accuracy Rate (%)': [92, 90, 99, 98, 88, 89, 93, 95]
    }
    df = pd.DataFrame(data)
    st.title("OVERALL STATS")
    st.bar_chart(df.set_index('Command Types'))

    