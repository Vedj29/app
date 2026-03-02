import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="AI Career Guidance Platform",
    layout="wide"
)

st.title("AI Career Guidance and Skill Gap Platform")

# --------------------------------------------------
# Career Data (Stored in lowercase for consistency)
# --------------------------------------------------
career_data = {
    "data scientist": {
        "required_skills": ["python", "machine learning", "statistics", "sql", "data visualization"],
        "salary": [6, 8, 12, 18, 25],
        "trend": [50, 60, 75, 90, 110]
    },
    "ai engineer": {
        "required_skills": ["python", "deep learning", "tensorflow", "nlp", "math"],
        "salary": [7, 10, 15, 22, 30],
        "trend": [55, 70, 85, 100, 130]
    },
    "web developer": {
        "required_skills": ["html", "css", "javascript", "react", "node.js"],
        "salary": [4, 6, 9, 14, 18],
        "trend": [40, 50, 60, 75, 85]
    },
    "cyber security analyst": {
        "required_skills": ["networking", "linux", "ethical hacking", "python", "security tools"],
        "salary": [5, 7, 11, 16, 22],
        "trend": [45, 60, 70, 85, 100]
    },
    "java developer": {
        "required_skills": ["java", "oop", "spring boot", "sql", "data structures"],
        "salary": [4, 6, 10, 15, 20],
        "trend": [35, 45, 60, 75, 90]
    },
    "c++ developer": {
        "required_skills": ["c++", "oop", "data structures", "algorithms", "stl"],
        "salary": [5, 7, 12, 18, 24],
        "trend": [30, 40, 55, 70, 85]
    }
}

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Section",
    ["Skill Gap Analysis", "Salary Insights", "Industry Trends", "Career Chatbot"]
)

goal = st.sidebar.selectbox(
    "Select Career Goal",
    list(career_data.keys())
)

# --------------------------------------------------
# Skill Gap Analysis
# --------------------------------------------------
if page == "Skill Gap Analysis":

    st.header("Skill Gap Analysis")

    user_input = st.text_area("Enter your current skills (comma separated)")

    if user_input:
        user_skills = [skill.strip().lower() for skill in user_input.split(",")]
        required_skills = career_data[goal]["required_skills"]

        missing_skills = [
            skill for skill in required_skills
            if skill not in user_skills
        ]

        st.subheader("Selected Career Goal")
        st.write(goal.title())

        st.subheader("Your Skills")
        st.write([skill.title() for skill in user_skills])

        st.subheader("Required Skills")
        st.write([skill.title() for skill in required_skills])

        st.subheader("Missing Skills")
        if missing_skills:
            st.write([skill.title() for skill in missing_skills])
        else:
            st.write("You already have all required skills.")

        match = len(required_skills) - len(missing_skills)
        percent = int((match / len(required_skills)) * 100)

        st.subheader("Skill Match Percentage")

        fig = px.pie(
            names=["Matched", "Missing"],
            values=[match, len(missing_skills)],
            hole=0.6,
            title=f"{goal.title()} Skill Match ({percent}%)"
        )

        st.plotly_chart(fig)

# --------------------------------------------------
# Salary Insights
# --------------------------------------------------
elif page == "Salary Insights":

    st.header("Salary Growth Insights")

    salary = career_data[goal]["salary"]
    years = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]

    fig_salary = px.line(
        x=years,
        y=salary,
        markers=True,
        title=f"{goal.title()} Salary Growth (LPA)"
    )

    fig_salary.update_layout(
        xaxis_title="Experience",
        yaxis_title="Salary (LPA)"
    )

    st.plotly_chart(fig_salary)

# --------------------------------------------------
# Industry Trends
# --------------------------------------------------
elif page == "Industry Trends":

    st.header("Industry Demand Trends")

    trend = career_data[goal]["trend"]
    years = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]

    fig_trend = px.area(
        x=years,
        y=trend,
        title=f"{goal.title()} Market Demand Growth"
    )

    fig_trend.update_layout(
        xaxis_title="Years",
        yaxis_title="Demand Index"
    )

    st.plotly_chart(fig_trend)

# --------------------------------------------------
# Career Chatbot
# --------------------------------------------------
elif page == "Career Chatbot":

    st.header("Career Chatbot")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    faqs = {
        "What is Data Science?": """
Data Science is a field that combines statistics, programming and domain knowledge 
to extract meaningful insights from data.

Key skills:
- Python
- Machine Learning
- Statistics
- SQL
- Data Visualization

Data Scientists are in high demand across industries like finance, healthcare and tech.
""",

        "What does an AI Engineer do?": """
An AI Engineer builds intelligent systems using machine learning and deep learning.

Core skills:
- Python
- Deep Learning
- TensorFlow / PyTorch
- NLP
- Mathematics

AI Engineers work on automation, chatbots, recommendation systems and computer vision.
""",

        "What skills are required for Web Development?": """
Web Developers build websites and web applications.

Important skills:
- HTML
- CSS
- JavaScript
- React
- Node.js

Web development has strong demand in startups and product companies.
""",

        "How is salary growth in AI careers?": """
AI careers show strong salary growth.

Typical progression:
Year 1: Entry level salary
Year 3: Mid level growth
Year 5+: Senior level with high compensation

AI and Data Science roles usually offer higher salary compared to traditional IT roles.
""",

        "Which careers are trending in tech?": """
Currently trending tech careers include:

- Artificial Intelligence
- Data Science
- Cyber Security
- Cloud Computing
- Full Stack Development

These fields show continuous industry demand growth.
"""
    }

    selected_question = st.selectbox("Select a question", list(faqs.keys()))

    if st.button("Get Answer"):
        if selected_question:
            response = faqs[selected_question]
            st.session_state.chat_history.append(("You", selected_question))
            st.session_state.chat_history.append(("Bot", response))

    for sender, message in st.session_state.chat_history:
        if sender == "You":
            st.write("You:", message)
        else:
            st.write("Bot:", message)