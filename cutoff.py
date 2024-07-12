import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
df = pd.read_csv("cutoff.csv")
cutOff= st.sidebar.text_input("Enter your Cut-off")
community=st.sidebar.selectbox("Community",["OC","BC","BCM","MBC","SC","SCA","ST"],None)
maxBuffer= st.sidebar.slider("+Buffer",0.0,2.0,0.0,0.25)
minBuffer= st.sidebar.slider("-Buffer",0.0,15.0,0.0,0.5)
branchName= st.sidebar.multiselect("Branch Name",df['brn'].unique(),None)
collegeName= st.sidebar.multiselect("College Name",df['con'].unique(),None)
collegeCode= st.sidebar.selectbox("College Code",df['coc'].unique(),None)
filterdf= df

if(collegeCode != None):
    filterdf= filterdf[filterdf['coc']==collegeCode]
if collegeName:
    filterdf= filterdf[filterdf['con'].isin(collegeName)]
if branchName:
    filterdf= filterdf[filterdf['brn'].isin(branchName)]

if(cutOff != None and community != None):
    if(community=="OC"):
        filterdf= filterdf[(filterdf['OC'] <= (float(cutOff)+float(maxBuffer))) & (filterdf['OC'] >= (float(cutOff)-float(minBuffer)))]
    elif(community=="BC"):
        filterdf= filterdf[(filterdf['BC'] <= (float(cutOff)+float(maxBuffer))) & (filterdf['BC'] >= (float(cutOff)-float(minBuffer)))]
    elif(community=="BCM"):
        filterdf= filterdf[(filterdf['BCM'] <= (float(cutOff)+float(maxBuffer))) & (filterdf['BCM'] >= (float(cutOff)-float(minBuffer)))]
    elif(community=="MBC"):
        filterdf= filterdf[(filterdf['MBC'] <= (float(cutOff)+float(maxBuffer))) & (filterdf['MBC'] >= (float(cutOff)-float(minBuffer)))]
    elif(community=="SC"):
        filterdf= filterdf[(filterdf['SC'] <= (float(cutOff)+float(maxBuffer))) & (filterdf['SC'] >= (float(cutOff)-float(minBuffer)))]
    elif(community=="SCA"):
        filterdf= filterdf[(filterdf['SCA'] <= (float(cutOff)+float(maxBuffer))) & (filterdf['SCA'] >= (float(cutOff)-float(minBuffer)))]
    elif(community=="ST"):
        filterdf= filterdf[(filterdf['ST'] <= (float(cutOff)+float(maxBuffer))) & (filterdf['ST'] >= (float(cutOff)-float(minBuffer)))]


st.title("Cutoff Compass TNEA 2024")
if(cutOff != ''):
    if(minBuffer > 0 or maxBuffer > 0):
        st.text("Cut-Off:"+ str(float(cutOff)-float(minBuffer)) +"-"+ str(float(cutOff)+float(maxBuffer)))
    else:
        st.text("Cut-Off:"+ cutOff)
if branchName:
    st.write("Branch Name:")
    for branch in branchName:
        st.text(branch)
if collegeName:
    st.text("College Name:")
    for college in collegeName:
        st.text(college)
if collegeCode:
    st.text("College Code:" + str(collegeCode))

filterdf = filterdf.rename(columns={'coc': 'College Code', 'con': 'College Name', 'brn': 'Branch Name'})
selectedColumns=['College Code', 'College Name','Branch Name','OC','BC','BCM','MBC','SC','SCA','ST']

filterdf.index= filterdf.index+1
st.dataframe(filterdf[selectedColumns])

st.markdown("""
    <meta name="description" content="TNEA 2023 - DOTE, Chennai">
    <meta name="keywords" content="tnea2024,tnea2023,engineering,cutoff,engineering,counselling,bestcollege,tamilnadu">
    <meta name="author" content="Shunmugapriyan Murugan">
    <title>TNEA 2024</title>
    """, unsafe_allow_html=True)

st.header('Project Description')
st.write(
    """
    The TNEA Cutoff Compass 2024 project is designed to assist students in navigating the Tamil Nadu Engineering Admissions (TNEA) process. 
    Our tool provides an easy-to-use interface for students to find information about cutoff scores for various engineering colleges in Tamil Nadu.
    The main goals of this project are to:
    - Provide accurate and updated cutoff data for TNEA 2024.
    - Help students make informed decisions about their college preferences.
    - Offer a user-friendly platform for accessing TNEA-related information.
    """
)

st.header('Fair Use Statement')
st.write(
    """
    This project adheres to the principles of fair use. Fair use is a doctrine in United States copyright law that allows limited use of copyrighted material 
    without requiring permission from the rights holders. Fair use is a defense against a claim of copyright infringement. It can be applied in a variety of contexts, 
    including criticism, comment, news reporting, teaching, scholarship, and research. The use of copyrighted material in this project is transformative, 
    meaning it adds new expression or meaning to the original material and does not infringe on the market for the original work.
    """
)

st.header('References')
st.markdown(
    """
    - Follow us on Instagram: 
      <a href="https://www.instagram.com/travel_with_priyan" target="_blank">
      <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="30" height="30">
      </a>
    - Check out our YouTube channel: 
      <a href="https://www.youtube.com/@Travelwithpriyan" target="_blank">
      <img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" width="30" height="30">
      </a>
    """,
    unsafe_allow_html=True
)