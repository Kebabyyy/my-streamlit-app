import streamlit as st 
import pandas as pd 
import numpy as np 
st.set_page_config(page_title="Educational Institution Performance Dashboard", layout="wide") 
st.title("Educational Institution Performance Dashboard") 
st.markdown("Business Analytics - Case Study 12") 
st.sidebar.header("Filter Options") 
selected_dept = st.sidebar.selectbox("Select Department", ["All Departments", "Computer Science", "Information Technology", "Electronics"]) 
selected_year = st.sidebar.selectbox("Select Academic Year", ["2025-2026", "2024-2025"]) 
col1, col2, col3, col4 = st.columns(4) 
col1.metric("Total Students", "1,250", "+5%") 
col2.metric("Overall Pass Rate", "92.4%", "+1.2%") 
col3.metric("Placement Rate", "88.5%", "+3.1%") 
col4.metric("Faculty-Student Ratio", "1:15", "Optimal") 
st.markdown("---")
st.subheader("Student Performance Overview") 
chart_data = pd.DataFrame( 
    np.random.randn(5, 3), 
    columns=['Sem 1', 'Sem 2', 'Sem 3'] 
)
st.line_chart(chart_data) 
col_a, col_b = st.columns(2) 
with col_a:      
    st.subheader("Department-wise Placement Statistics")      
    placement_data = pd.DataFrame({          
        'Department': ['CSE', 'IT', 'ECE', 'EEE'],          
        'Placement %': [95, 90, 85, 80]      
    })      
    st.bar_chart(placement_data.set_index('Department'))  
with col_b:      
    st.subheader("Faculty Productivity Metrics")      
    faculty_data = pd.DataFrame({          
        'Department': ['CSE', 'IT', 'ECE', 'EEE'],          
        'Avg Feedback Score': [4.8, 4.6, 4.5, 4.3],          
        'Research Papers': [12, 10, 8, 6]      
    })
    st.dataframe(faculty_data, use_container_width=True)
