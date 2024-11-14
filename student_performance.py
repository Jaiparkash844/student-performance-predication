import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("student_data.csv")

# Handling missing values by filling them with default values or dropping them
df.fillna({
    "Parent Education Level": "Unknown",
    "Passed": "No"
}, inplace=True)

# Convert relevant columns to numeric
df["Study Hours per Week"] = pd.to_numeric(df["Study Hours per Week"], errors='coerce')
df["Attendance Rate"] = pd.to_numeric(df["Attendance Rate"], errors='coerce')
df["Previous Grades"] = pd.to_numeric(df["Previous Grades"], errors='coerce')

st.title("Student Performance Prediction")

# Display the dataset
st.header("Dataset")
st.write(df)

# Correlation Heatmap
st.header("Correlation Heatmap")
plt.figure(figsize=(10, 8))
numeric_df = df.select_dtypes(include=['float64', 'int64'])
corr_matrix = numeric_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
st.pyplot(plt)

# Scatter Plot for Study Hours vs. Attendance Rate
st.header("Study Hours vs. Attendance Rate")
fig = px.scatter(df, x="Study Hours per Week", y="Attendance Rate", color="Passed",
                 title="Study Hours per Week vs Attendance Rate (Colored by Passed/Failed)")
st.plotly_chart(fig)

# Distribution of Previous Grades
st.header("Distribution of Previous Grades")
fig = px.histogram(df, x="Previous Grades", color="Passed", nbins=20,
                   title="Distribution of Previous Grades by Pass/Fail")
st.plotly_chart(fig)

# Attendance Rate by Parent Education Level
st.header("Attendance Rate by Parent Education Level")
fig = px.box(df, x="Parent Education Level", y="Attendance Rate", color="Passed",
             title="Attendance Rate by Parent Education Level")
st.plotly_chart(fig)

# Participation in Extracurricular Activities vs Grades
st.header("Extracurricular Activities vs Grades")
fig = px.box(df, x="Participation in Extracurricular Activities", y="Previous Grades", color="Passed",
             title="Grades by Participation in Extracurricular Activities")
st.plotly_chart(fig)
