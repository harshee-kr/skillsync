import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from data import load_employees, load_projects

employees = load_employees()
projects = load_projects()

st.set_page_config(
    page_title="JARVIS | Workforce Command Center",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- PAGE STYLE ----------------
st.markdown("""
<style>
    .stApp {
        background: #0b1120;
        color: white;
    }

    section[data-testid="stSidebar"] {
        background: #111827;
    }

    .main-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 0;
    }

    .subtitle {
        color: #94a3b8;
        font-size: 16px;
        margin-bottom: 25px;
    }

    .metric-card {
        background: #111827;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #1e293b;
    }

    .alert-card {
        background: #172033;
        padding: 18px;
        border-radius: 12px;
        border-left: 4px solid #f59e0b;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.markdown("## 🤖 JARVIS")

    st.caption("AI Workforce Command Agent")

    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "🏠 Command Center",
            "👥 Workforce",
            "📁 Projects",
            "🧠 AI Allocation",
            "⚠️ Risk & Alerts",
            "📊 Visualization",
            "📄 Reports"
        ]
    )

    st.divider()

    st.caption("SYSTEM STATUS")
    st.success("● JARVIS Online")


# ---------------- COMMAND CENTER ----------------
if page == "🏠 Command Center":

    st.markdown(
        '<div class="main-title">Workforce Command Center</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Real-time workforce intelligence and decision support</div>',
        unsafe_allow_html=True
    )

    # Metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Employees", len(employees))

    with col2:
        st.metric("Active Projects", len(projects))

    with col3:
        utilization = round(employees["Current_Workload"].mean())
    st.metric("Utilization", f"{utilization}%")

    with col4:
        projects_at_risk = len(
        projects[
            (projects["Deadline_Days"] <= 10) &
            (projects["Progress"] < 60)
        ]
    )

    st.metric("Projects At Risk", projects_at_risk) 

    st.divider()

    # AI Command
    st.subheader("💬 Ask JARVIS")

    command = st.text_input(
        "Give JARVIS a workforce command",
        placeholder="Example: Project Alpha is delayed. Allocate suitable employees."
    )

    if command:
        st.info("JARVIS received your request. AI decision engine will analyze it.")


    st.divider()

    # Alerts
    col1, col2 = st.columns(2)

    with col1:

        st.subheader("⚠️ Priority Alerts")

        st.markdown(
            '<div class="alert-card">🔴 Project Alpha — Resource shortage detected</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="alert-card">🟡 Employee E017 — High workload</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="alert-card">🟡 Project Gamma — Deadline approaching</div>',
            unsafe_allow_html=True
        )

    with col2:

        st.subheader("🧠 JARVIS Recommendation")

        st.info(
            "Project Alpha requires additional resources. "
            "JARVIS recommends assigning employees with matching "
            "skills and available capacity."
        )

        st.success("Potential workload risk: LOW")


# ---------------- OTHER PAGES ----------------
elif page == "👥 Workforce":

    st.title("👥 Workforce Intelligence")
    st.caption("Employee skills, availability and workload overview")

    employees = load_employees()

    st.dataframe(
        employees,
        use_container_width=True,
        hide_index=True
    )
elif page == "📁 Projects":

    st.title("📁 Project Intelligence")
    st.caption("Project requirements, deadlines, progress and resource needs")

    projects = load_projects()

    st.dataframe(
        projects,
        use_container_width=True,
        hide_index=True
    )

elif page == "🧠 AI Allocation":

    st.title("🧠 AI Resource Allocation")
    st.caption("Tell JARVIS what you need. It analyzes skills, workload and availability.")

    projects = load_projects()
    employees = load_employees()

    project_names = projects["Project_Name"].tolist()

    selected_project = st.selectbox(
        "Select Project",
        project_names
    )

    project = projects[
        projects["Project_Name"] == selected_project
    ].iloc[0]

    st.subheader("Project Requirements")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Priority", project["Priority"])

    with col2:
        st.metric("Deadline", f'{project["Deadline_Days"]} days')

    with col3:
        st.metric("Required Employees", project["Required_Employees"])

    st.write("**Required Skills:**", project["Required_Skills"])

    st.divider()

    command = st.text_area(
        "💬 Ask JARVIS",
        placeholder="Example: Allocate suitable employees for this project without overloading anyone."
    )

    if st.button("🤖 Generate Allocation"):

        required_skills = set(
            project["Required_Skills"].split("|")
        )

        available = employees[
            employees["Availability"] == "Available"
        ].copy()

        available["Skill_Match"] = available["Skills"].apply(
            lambda skills: len(
                required_skills.intersection(
                    set(skills.split("|"))
                )
            )
        )

        recommended = available.sort_values(
            by=["Skill_Match", "Current_Workload"],
            ascending=[False, True]
        ).head(
            int(project["Required_Employees"])
        )

        st.success("JARVIS Allocation Recommendation Generated")

        st.dataframe(
            recommended[
                [
                    "Employee_ID",
                    "Name",
                    "Skills",
                    "Experience",
                    "Availability",
                    "Current_Workload",
                    "Skill_Match"
                ]
            ],
            use_container_width=True,
            hide_index=True
        )

        st.subheader("🧠 JARVIS Explanation")

        st.info(
            "JARVIS selected available employees based on skill matching "
            "and lower current workload. This helps satisfy project "
            "requirements while reducing the risk of employee overload."
        )

elif page == "⚠️ Risk & Alerts":

    st.title("⚠️ Risk & Alerts")
    st.caption("JARVIS automatically identifies workforce and project risks")

    employees = load_employees()
    projects = load_projects()

    # ---------------- EMPLOYEE RISKS ----------------
    st.subheader("👥 Workforce Risks")

    overloaded = employees[
        employees["Current_Workload"] >= 70
    ]

    if len(overloaded) > 0:
        for _, employee in overloaded.iterrows():
            st.warning(
                f"⚠️ {employee['Name']} ({employee['Employee_ID']}) "
                f"has a workload of {employee['Current_Workload']}%"
            )
    else:
        st.success("No overloaded employees detected.")

    st.divider()

    # ---------------- PROJECT RISKS ----------------
    st.subheader("📁 Project Risks")

    for _, project in projects.iterrows():

        if (
            project["Deadline_Days"] <= 10
            and project["Progress"] < 60
        ):
            st.error(
                f"🔴 {project['Project_Name']} — "
                f"High risk: {project['Deadline_Days']} days remaining, "
                f"{project['Progress']}% progress"
            )

        elif project["Deadline_Days"] <= 15:
            st.warning(
                f"🟡 {project['Project_Name']} — "
                f"Deadline approaching ({project['Deadline_Days']} days)"
            )

        elif project["Priority"] == "High" and project["Progress"] < 50:
            st.warning(
                f"🟠 {project['Project_Name']} — "
                f"High priority with only {project['Progress']}% progress"
            )

    st.divider()

    st.subheader("🤖 JARVIS Risk Summary")

    st.info(
        "JARVIS continuously checks employee workload, "
        "project deadlines, priority and progress to identify "
        "potential resource and delivery risks."
    )

elif page == "📊 Visualization":

    st.title("📊 Workforce Visualization")
    st.caption("Interactive analytics for workforce and project decisions")

    employees = load_employees()
    projects = load_projects()

    # ---------------------------------------------------------
    # VISUALIZATION CONTROLS
    # ---------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        chart_type = st.selectbox(
            "📈 Choose Chart Type",
            [
                "📊 Bar Chart",
                "📈 Line Chart",
                "🥧 Pie Chart",
                "🔵 Scatter Chart"
            ]
        )

    with col2:
        data_type = st.selectbox(
            "📋 Choose Data",
            [
                "Employee Workload",
                "Project Progress",
                "Employee Availability",
                "Project Priority"
            ]
        )

    st.divider()

    # ---------------------------------------------------------
    # EMPLOYEE WORKLOAD
    # ---------------------------------------------------------

    if data_type == "Employee Workload":

        st.subheader("👥 Employee Workload")

        chart_data = employees[
            ["Name", "Current_Workload"]
        ].copy()

        chart_data["Current_Workload"] = pd.to_numeric(
            chart_data["Current_Workload"]
        )

        if chart_type == "📊 Bar Chart":

            st.bar_chart(
                chart_data.set_index("Name"),
                y="Current_Workload"
            )

        elif chart_type == "📈 Line Chart":

            st.line_chart(
                chart_data.set_index("Name"),
                y="Current_Workload"
            )

        elif chart_type == "🥧 Pie Chart":

            st.plotly_chart(
                go.Figure(
                    data=[
                        go.Pie(
                            labels=chart_data["Name"],
                            values=chart_data["Current_Workload"]
                        )
                    ]
                ),
                use_container_width=True
            )

        elif chart_type == "🔵 Scatter Chart":

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=chart_data["Name"],
                    y=chart_data["Current_Workload"],
                    mode="markers",
                    text=chart_data["Name"]
                )
            )

            fig.update_layout(
                xaxis_title="Employee",
                yaxis_title="Current Workload (%)"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # ---------------------------------------------------------
    # PROJECT PROGRESS
    # ---------------------------------------------------------

    elif data_type == "Project Progress":

        st.subheader("📁 Project Progress")

        chart_data = projects[
            ["Project_Name", "Progress"]
        ].copy()

        chart_data["Progress"] = pd.to_numeric(
            chart_data["Progress"]
        )

        if chart_type == "📊 Bar Chart":

            st.bar_chart(
                chart_data.set_index("Project_Name"),
                y="Progress"
            )

        elif chart_type == "📈 Line Chart":

            st.line_chart(
                chart_data.set_index("Project_Name"),
                y="Progress"
            )

        elif chart_type == "🥧 Pie Chart":

            st.plotly_chart(
                go.Figure(
                    data=[
                        go.Pie(
                            labels=chart_data["Project_Name"],
                            values=chart_data["Progress"]
                        )
                    ]
                ),
                use_container_width=True
            )

        elif chart_type == "🔵 Scatter Chart":

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=chart_data["Project_Name"],
                    y=chart_data["Progress"],
                    mode="markers",
                    text=chart_data["Project_Name"]
                )
            )

            fig.update_layout(
                xaxis_title="Project",
                yaxis_title="Progress (%)"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # ---------------------------------------------------------
    # EMPLOYEE AVAILABILITY
    # ---------------------------------------------------------

    elif data_type == "Employee Availability":

        st.subheader("🟢 Employee Availability")

        availability_data = (
            employees["Availability"]
            .value_counts()
            .reset_index()
        )

        availability_data.columns = [
            "Availability",
            "Count"
        ]

        if chart_type == "🥧 Pie Chart":

            st.plotly_chart(
                go.Figure(
                    data=[
                        go.Pie(
                            labels=availability_data["Availability"],
                            values=availability_data["Count"]
                        )
                    ]
                ),
                use_container_width=True
            )

        elif chart_type == "📊 Bar Chart":

            st.bar_chart(
                availability_data.set_index("Availability"),
                y="Count"
            )

        else:

            st.info(
                "Bar and Pie charts are most suitable "
                "for employee availability."
            )

    # ---------------------------------------------------------
    # PROJECT PRIORITY
    # ---------------------------------------------------------

    elif data_type == "Project Priority":

        st.subheader("🎯 Project Priority")

        priority_data = (
            projects["Priority"]
            .value_counts()
            .reset_index()
        )

        priority_data.columns = [
            "Priority",
            "Count"
        ]

        if chart_type == "🥧 Pie Chart":

            st.plotly_chart(
                go.Figure(
                    data=[
                        go.Pie(
                            labels=priority_data["Priority"],
                            values=priority_data["Count"]
                        )
                    ]
                ),
                use_container_width=True
            )

        elif chart_type == "📊 Bar Chart":

            st.bar_chart(
                priority_data.set_index("Priority"),
                y="Count"
            )

        else:

            st.info(
                "Bar and Pie charts are most suitable "
                "for project priority."
            )

    # ---------------------------------------------------------
    # JARVIS INSIGHT
    # ---------------------------------------------------------

    st.divider()

    st.subheader("🤖 JARVIS Insight")

    st.info(
        "Select different chart types and datasets to explore "
        "workforce utilization, project progress, employee "
        "availability and project priorities."
    )

elif page == "📄 Reports":

    st.title("📄 JARVIS Workforce Report")
    st.caption("Generate a workforce decision report for management")

    employees = load_employees()
    projects = load_projects()

    total_employees = len(employees)
    total_projects = len(projects)

    overloaded = len(
        employees[employees["Current_Workload"] >= 70]
    )

    high_priority = len(
        projects[projects["Priority"] == "High"]
    )

    at_risk = len(
        projects[
            (projects["Deadline_Days"] <= 10) &
            (projects["Progress"] < 60)
        ]
    )

    st.subheader("📊 Executive Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Employees", total_employees)

    with col2:
        st.metric("Active Projects", total_projects)

    with col3:
        st.metric("Overloaded Employees", overloaded)

    with col4:
        st.metric("Projects At Risk", at_risk)

    st.divider()

    st.subheader("📁 Project Status")

    st.dataframe(
        projects[
            [
                "Project_Name",
                "Priority",
                "Deadline_Days",
                "Progress",
                "Required_Employees"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("👥 Workforce Status")

    st.dataframe(
        employees[
            [
                "Employee_ID",
                "Name",
                "Skills",
                "Availability",
                "Current_Workload"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("🤖 JARVIS Management Recommendation")

    st.warning(
        "JARVIS recommends reviewing employee workload, "
        "project deadlines and skill requirements to maintain "
        "balanced workforce allocation."
    )

    st.divider()

    if st.button("📄 Generate Report"):

        report_text = f"""
JARVIS — AI WORKFORCE DECISION REPORT

EXECUTIVE SUMMARY

Total Employees: {total_employees}
Active Projects: {total_projects}
Overloaded Employees: {overloaded}
High Priority Projects: {high_priority}
Projects At Risk: {at_risk}

JARVIS RECOMMENDATION

Review workforce workload, project deadlines, skill requirements,
and employee availability to maintain balanced resource allocation.
"""

        st.download_button(
            "⬇️ Download Report",
            report_text,
            file_name="JARVIS_Workforce_Report.txt",
            mime="text/plain"
        )