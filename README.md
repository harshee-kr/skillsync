# 🚀 SkillSync

### AI Workforce Decision & Resource Allocation Agent

> **Sync Skills. Build Better Teams.**

SkillSync is a workforce decision-support platform designed to help managers make better resource allocation decisions. It brings employee skills, availability, workload, and project requirements together to suggest suitable employees for different projects.

The application provides a central workspace for viewing workforce information, monitoring project progress, identifying risks, and generating resource allocation recommendations.

---

## 📌 Overview

Managing people across multiple projects can become difficult when employee availability, workload, skills, deadlines, and project priorities keep changing.

SkillSync provides a simple way to bring these factors together and support workforce planning through data-driven recommendations.

The current application includes a workforce command center, employee and project views, resource allocation, risk monitoring, interactive visualizations, and management reports.

---

## ✨ Features

### 🏠 Workforce Command Center

A central dashboard that gives a quick overview of the workforce and ongoing projects.

It includes:

* Total employees
* Active projects
* Workforce utilization
* Projects at risk
* Priority alerts
* Workforce recommendations

The dashboard also provides a command interface where managers can enter workforce-related requests.

---

### 👥 Workforce Intelligence

View employee information in one place, including details related to:

* Employee ID
* Name
* Skills
* Experience
* Availability
* Current workload

This helps managers understand the current state of their workforce before making allocation decisions.

---

### 📁 Project Intelligence

The project section provides an overview of project requirements and status, including:

* Project name
* Priority
* Deadline
* Progress
* Required employees
* Required skills

This information is used as the basis for workforce allocation.

---

### 🧠 AI Resource Allocation

SkillSync recommends suitable employees for a selected project by considering employee availability, matching skills, and current workload.

The allocation process:

```text
Select Project
      ↓
Read Project Requirements
      ↓
Check Employee Availability
      ↓
Compare Required Skills
      ↓
Consider Current Workload
      ↓
Generate Recommended Employees
```

The current implementation calculates skill overlap between employee skills and the project's required skills, then considers current workload while selecting available employees.

---

### ⚠️ Risk & Alerts

SkillSync highlights workforce and project situations that may require attention.

It checks for:

* Employees with high workloads
* Projects approaching their deadlines
* Projects with low progress
* High-priority projects that are falling behind

This gives managers an early view of potential resource and delivery risks.

---

### 📊 Interactive Visualization

The visualization section allows users to explore workforce and project information through different chart types.

Available data includes:

* Employee workload
* Project progress
* Employee availability
* Project priority

Supported visualizations include:

* Bar charts
* Line charts
* Pie charts
* Scatter charts

---

### 📄 Workforce Reports

SkillSync provides a management-oriented report containing key workforce and project information.

The report includes:

* Total employees
* Active projects
* Overloaded employees
* High-priority projects
* Projects at risk
* Project status
* Workforce status
* Management recommendation

Reports can also be generated and downloaded as a text file.

---

## 🔄 How SkillSync Works

```text
              👥 Employee Data
                    │
       ┌────────────┼────────────┐
       │            │            │
    Skills     Availability   Workload
       │            │            │
       └────────────┼────────────┘
                    │
                    ▼
             📁 Project Data
                    │
       ┌────────────┼────────────┐
       │            │            │
   Required      Priority     Deadline
    Skills
       │            │            │
       └────────────┼────────────┘
                    ▼
          🧠 SkillSync Allocation
                    │
                    ▼
          👥 Team Recommendation
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
      Risk Analysis      Workforce Insights
          │                   │
          └─────────┬─────────┘
                    ▼
              📊 Reports
```

---

## 🧮 Resource Matching

SkillSync currently uses skill overlap as one of the main factors for resource allocation.

For each available employee, the system compares their skills with the skills required by the selected project.

```text
Skill Match
     ↓
Number of matching skills
     ↓
Consider employee workload
     ↓
Generate recommendation
```

Employees with stronger skill overlap and lower current workload are prioritized in the current allocation logic.

---

## 🛠️ Technology Stack

| Technology   | Purpose                                   |
| ------------ | ----------------------------------------- |
| 🐍 Python    | Application development                   |
| 🎨 Streamlit | Web interface and dashboard               |
| 🐼 Pandas    | Employee and project data processing      |
| 📊 Plotly    | Interactive visualizations                |
| 📁 CSV       | Current employee and project data storage |

The application currently loads employee and project data from CSV files through the data-loading module.

---

## 📂 Project Structure

```text
skillsync/
│
├── app.py
├── data.py
├── employees.csv
├── projects.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/skillsync.git
```

```bash
cd skillsync
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run SkillSync

```bash
streamlit run app.py
```

The application will open locally at:

```text
http://localhost:8501
```

---

## 📊 Application Sections

```text
🏠 Command Center
        │
        ├── 👥 Workforce
        │
        ├── 📁 Projects
        │
        ├── 🧠 AI Allocation
        │
        ├── ⚠️ Risk & Alerts
        │
        ├── 📊 Visualization
        │
        └── 📄 Reports
```

These sections are available through the application's sidebar navigation.

---

## 🎯 Project Goals

SkillSync aims to make workforce planning simpler by helping managers:

* Find employees whose skills fit project requirements
* Consider employee availability before allocation
* Avoid unnecessary workload concentration
* Keep track of project progress and deadlines
* Identify potential workforce and project risks
* Understand workforce data through visualizations
* Generate clear management reports

---

## 🔮 Future Enhancements

The project can be extended with:

* 🤖 More advanced AI-based team recommendations
* ⚙️ Optimization-based team formation
* 🔍 Detailed skill-gap analysis
* 🔄 What-if workforce simulation
* 📚 Employee training recommendations
* 📈 Workforce demand forecasting
* 🗄️ MySQL database integration
* 🔐 User authentication and role-based access
* ☁️ Cloud deployment
* 📊 Historical workforce analytics

---

## 📸 Screenshots

Add screenshots of the application here as the project develops.

### Command Center

```text
[ Add Dashboard Screenshot ]
```

### AI Allocation

```text
[ Add Allocation Screenshot ]
```

### Workforce Visualization

```text
[ Add Visualization Screenshot ]
```

### Risk & Alerts

```text
[ Add Risk Dashboard Screenshot ]
```

---

## 👥 Target Users

SkillSync is designed to support:

* Project Managers
* Resource Managers
* Team Leads
* HR and Workforce Planning Teams

---

## 🎓 Project Context

**AI-04 — AI Workforce Decision & Resource Allocation Agent**

SkillSync explores how workforce data, skill matching, project requirements, and data-driven analysis can be brought together to support better resource allocation and team formation.

---

## 🤝 Contributing

Contributions and suggestions are welcome.

```bash
git checkout -b feature/new-feature
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
```

Create a pull request after pushing your changes.

---

## 📄 License

This project is developed for educational and research purposes.

---

# 🚀 SkillSync

### **Sync Skills. Build Better Teams.**

**Python • Streamlit • Pandas • Plotly**
