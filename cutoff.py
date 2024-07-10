import pandas as pd
import streamlit as st
df = pd.read_csv("cutoff.csv")
cutOff= st.sidebar.text_input("Enter your Cut-off")
community=st.sidebar.selectbox("Community",["OC","BC","BCM","MBC","SC","SCA","ST"],None)
maxBuffer= st.sidebar.slider("+Buffer",0.0,1.0,0.0,0.25)
minBuffer= st.sidebar.slider("-Buffer",0.0,10.0,0.0,0.5)
branchName= st.sidebar.multiselect("Branch Name",df['brn'].unique(),None)
collegeName= st.sidebar.multiselect("College Name",df['con'].unique(),None)
collegeCode= st.sidebar.selectbox("College Code",df['coc'].unique(),None)

selectedColumns=['coc', 'con','brn','OC','BC','BCM','MBC','SC','SCA','ST']
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


st.title("Last Year Cut-off TNEA 2023")
st.dataframe(filterdf[selectedColumns],use_container_width=True)