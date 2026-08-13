# 🛡️ Cyber Crime Reporting and Analysis System

A web-based **Cyber Crime Reporting and Analysis System** developed using **Python and Streamlit**.

The system provides an easy platform for citizens to register, report cybercrime incidents, upload evidence, and track complaints. Police/Admin users can manage complaints, assign cases, update case status, and analyze cybercrime data using interactive dashboards.

---

## 📌 Project Overview

Cybercrime such as online fraud, hacking, phishing, identity theft, ransomware, and data breaches is increasing rapidly.

Many victims hesitate to report cybercrime because traditional reporting processes can be complicated and time-consuming.

This project provides a simple **24/7 online cybercrime reporting platform** where users can report incidents and police/admin users can manage and analyze reported cases.

### 👤 Citizens

Citizens can:

- Register an account
- Verify CAPTCHA
- Login securely
- Report cybercrime
- Enter crime details
- Provide GPS location
- Upload evidence
- Track complaint status

### 👮 Police / Admin

Police/Admin users can:

- View complaints
- Sort cases by priority
- Assign Police ID
- Update complaint status
- Manage investigations
- View analytics
- Analyze crime trends

---

# ✨ Key Features

## 🆔 1. Unique Complaint ID

Every complaint receives a unique ID.

Format:

```text
CYB-YYYY-000001
```

Example:

```text
CYB-2026-000001
CYB-2026-000002
CYB-2026-000003
```

This makes every complaint easy to track.

---

## 🎯 2. Automatic Severity Score

The system automatically assigns a severity score between **1 and 10** according to the selected crime type.

| Crime Type | Severity | Level |
|---|---:|---|
| Data Breach | 10/10 | Critical |
| Ransomware | 10/10 | Critical |
| Hacking | 9/10 | Critical |
| Identity Theft | 9/10 | Critical |
| Online Fraud | 8/10 | High |
| Phishing | 7/10 | High |
| Cyberbullying | 6/10 | Medium |
| Social Media Crime | 5/10 | Medium |

---

# 🚨 3. Smart Priority Algorithm

The system calculates a priority score to determine which cases require more immediate attention.

### Formula

```text
Priority =
(Severity × 0.4)
+ (Evidence × 0.3)
+ (Time × 0.2)
+ (Financial Loss × 0.1)
```

### Weight Distribution

| Factor | Weight |
|---|---:|
| Severity | 40% |
| Evidence | 30% |
| Time Pending | 20% |
| Financial Loss | 10% |

### Priority Levels

| Score | Priority |
|---:|---|
| ≥ 8 | 🔴 Critical |
| ≥ 6 | 🟠 High |
| ≥ 4 | 🟡 Medium |
| < 4 | 🟢 Low |

---

# 🔐 4. Security Features

The application includes several security mechanisms.

### CAPTCHA Verification

- 6-character alphanumeric CAPTCHA
- Uses uppercase letters and numbers
- CAPTCHA expires after 5 minutes
- Used during registration, login, and password recovery

### Password Security

Passwords are protected using:

```text
SHA-256 Hashing
```

### Password Rules

A valid password must contain:

- Minimum 8 characters
- At least 1 uppercase letter
- At least 1 number
- At least 1 special character

### Email Validation

Email addresses are validated using Regular Expressions.

### Police ID

Police/Admin users receive a unique Police ID such as:

```text
POL-XXXXX
```

---

# 🔑 5. Forgot Password System

The system provides a secure three-step password recovery process:

```text
Email
  ↓
CAPTCHA Verification
  ↓
Set New Password
```

This allows users to recover their account without exposing their existing password.

---

# 📍 6. GPS Location

Citizens can provide the geographical location of a cybercrime incident using:

```text
Latitude
Longitude
```

The location is displayed using Streamlit's interactive map functionality.

---

# 📎 7. Evidence Upload

Users can upload supporting evidence such as:

- Screenshots
- Documents
- Images
- Other digital evidence

The number of uploaded evidence files contributes to the case priority score.

---

# 👮 Police Dashboard

The Police/Admin dashboard allows authorized users to manage cybercrime cases.

### Dashboard Functions

- View all complaints
- Sort cases according to priority
- View complaint details
- Assign Police ID
- Update complaint status
- Track investigations
- Analyze crime statistics

### Case Status

```text
Pending
    ↓
Under Investigation
    ↓
Resolved
    ↓
Closed
```

Police/Admin users can prioritize cases using the calculated priority score.

---

# 📊 Analytics Dashboard

The project provides an interactive analytics dashboard using **Plotly**.

### Dashboard Statistics

The dashboard can display:

- Total Complaints
- Resolved Cases
- Critical Cases
- Average Priority
- Total Financial Loss
- Crime Type Distribution
- Case Status Distribution
- Severity Distribution
- Crime Timeline
- Financial Loss by Crime Type

### Visualizations

The system uses interactive:

- Bar Charts
- Pie Charts
- Line Charts
- Histograms

---

# 🔄 System Workflow

```text
                    ┌──────────────────┐
                    │      START       │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Register Account │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ CAPTCHA Verify   │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │      Login       │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ File Complaint   │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Select Crime Type│
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Auto Severity    │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Upload Evidence  │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Priority Score   │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Police Dashboard │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Update Status    │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │    Analytics     │
                    └──────────────────┘
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python 3 | Core programming language |
| ⚡ Streamlit | Web application framework |
| 📊 Plotly | Interactive charts |
| 🐼 Pandas | Data processing |
| 🔢 NumPy | Numerical calculations |
| 💾 JSON | Local data storage |
| 🔐 Hashlib | Password hashing |
| 🔎 Regex | Input validation |

---

# 📂 Project Structure

```text
Cyber-Crime-Reporting-System/
│
├── cybercrime.py
├── cybercrime_data.json
├── requirements.txt
├── README.md
└── screenshots/
    ├── login.png
    ├── registration.png
    ├── complaint.png
    ├── dashboard.png
    └── analytics.png
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/cyber-crime-reporting-system.git
```

Go to the project directory:

```bash
cd cyber-crime-reporting-system
```

---

## 2. Create Virtual Environment

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

Create a `requirements.txt` file:

```text
streamlit
pandas
numpy
plotly
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

Run the Streamlit application:

```bash
streamlit run cybercrime.py
```

The application will open in your default web browser.

---

# 💾 Data Storage

The project uses **JSON as a local database/storage mechanism**.

The JSON file stores information such as:

```text
Users
Complaints
Complaint Counter
```

Example structure:

```json
{
    "users": [],
    "complaints": [],
    "counters": {}
}
```

For a production system, this can be replaced with:

- MySQL
- PostgreSQL
- MongoDB
- Firebase
- Cloud Database

---

# 👥 Group Members

| Name | Enrollment Number |
|---|---|
| **Patel Harshkumar Kanaiyalal** | 24002171710023 |
| **Shah Ansh Shashinbhai** | 25002170420012 |
| **Gediya Poojan Hareshbhai** | 24002170210025 |

---

# 🎓 Academic Project

This project demonstrates practical knowledge of:

- Python Programming
- Object-Oriented Programming
- File Handling
- JSON Data Management
- Authentication
- Password Hashing
- Regular Expressions
- Streamlit
- Data Visualization
- Pandas
- NumPy
- Cybersecurity Concepts
- Data Analysis
- Algorithm Design

---

# 🚀 Future Enhancements

The system can be improved by adding:

- 🗄️ MySQL/PostgreSQL/MongoDB database
- 🤖 AI-based cybercrime classification
- 📧 Email notifications
- 📱 SMS notifications
- 📱 Mobile application
- ☁️ Cloud deployment
- 🗺️ Google Maps API
- 🔔 Real-time notifications
- 📄 PDF complaint generation
- 📈 Advanced crime prediction
- 🔍 AI-based evidence analysis
- 👮 Multiple police department roles
- 🔒 Multi-factor authentication
- 🌐 REST API integration

---

# ⚠️ Disclaimer

This project is developed for **educational and academic purposes**.

It is not intended to replace official government or police cybercrime reporting systems.

For real-world deployment, additional security, privacy, authentication, database, audit logging, and legal compliance mechanisms should be implemented.

---

# ⭐ Project Highlights

```text
✅ Cyber Crime Reporting
✅ User Registration & Login
✅ CAPTCHA Verification
✅ Password Hashing
✅ Unique Complaint IDs
✅ Automatic Severity
✅ Smart Priority Algorithm
✅ Evidence Upload
✅ GPS Location
✅ Police Dashboard
✅ Case Status Management
✅ Interactive Analytics
✅ Plotly Visualizations
✅ JSON Data Storage
```

---

# 📜 License

This project is created for educational purposes.

You may modify and extend it for academic learning and portfolio purposes.

---

## 👨‍💻 Developed By

**Patel Harshkumar Kanaiyalal**  
**Shah Ansh Shashinbhai**  
**Gediya Poojan Hareshbhai**

### 🛡️ Cyber Crime Reporting and Analysis System

> **Report. Track. Analyze. Protect.**
