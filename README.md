# sem-III_python_projects

# 🛡️ Cyber Crime Reporting and Analysis System

A **Python and Streamlit-based Cyber Crime Reporting and Analysis System** designed to provide a simple platform for citizens to report cyber crimes and for administrators/police officers to manage, investigate, and analyze complaints.

The system includes user authentication, CAPTCHA verification, complaint tracking, automatic crime severity assignment, police station assignment, evidence management, and interactive crime analytics.

---

## 📌 Project Overview

Cybercrime is increasing rapidly, and managing cybercrime complaints manually can be time-consuming and difficult to track.

This project provides a centralized web-based system where:

* Citizens can register and securely log in.
* Users can report cybercrime incidents.
* Each complaint receives a unique sequential complaint ID.
* Crime severity is automatically assigned according to the crime type.
* Users can upload supporting evidence.
* Administrators can review and manage complaints.
* Police officers/stations can be assigned to cases.
* Administrators can update complaint status.
* Crime statistics can be visualized through interactive charts.
* Users can recover forgotten passwords/emails.

The application is built using **Python, Streamlit, Pandas, Plotly, and JSON file storage**.

---

## ✨ Features

### 👤 User Registration

Users can create an account by providing:

* Full Name
* Email
* Mobile Number
* Gender
* City
* Address
* Password
* Confirm Password

The system validates email, mobile number, and password requirements during registration.

### 🔐 Authentication & Security

The project provides:

* Login system
* Password hashing using SHA-256
* CAPTCHA verification
* CAPTCHA expiry
* Password strength validation
* Forgot Password functionality
* Forgot Email functionality

CAPTCHA codes are generated using Python's `random` module and contain six alphanumeric characters.

---

## 📝 Cyber Crime Complaint System

Citizens can submit complaints by entering:

* Crime Type
* Incident Description
* Location
* Date of Incident
* Financial Loss
* Latitude
* Longitude
* Supporting Evidence

The system supports crime categories such as:

* Online Fraud
* Hacking
* Identity Theft
* Phishing
* Cyberbullying
* Data Breach
* Ransomware
* Social Media Crime

---

## 🎯 Automatic Severity Assignment

The system automatically assigns a severity level from **1–10** according to the selected crime type.

| Crime Type         | Severity |
| ------------------ | -------: |
| Online Fraud       |        8 |
| Hacking            |        9 |
| Identity Theft     |        9 |
| Phishing           |        7 |
| Cyberbullying      |        6 |
| Data Breach        |       10 |
| Ransomware         |       10 |
| Social Media Crime |        5 |

These severity mappings are defined directly in the application.

---

## 🆔 Complaint Tracking

Every complaint receives a sequential ID in the following format:

```text
CYB-YYYY-NNNNNN
```

Example:

```text
CYB-2026-000001
CYB-2026-000002
CYB-2026-000003
```

This makes individual complaints easier to identify and track.

---

## 📍 Location & Maps

Users can provide geographical coordinates for a reported incident.

The application displays the selected location using Streamlit's map component.

```text
Latitude
Longitude
     ↓
Map Preview
```

This helps administrators understand the geographical location associated with a complaint.

---

## 📎 Evidence Management

Users can upload multiple supporting files such as:

* Screenshots
* Documents
* Other digital evidence

The uploaded filenames are associated with the complaint for tracking purposes.

---

## 👮 Admin Dashboard

Administrators can manage all complaints from a centralized dashboard.

Admin features include:

* View all complaints
* View complainant details
* Filter complaints
* Sort complaints
* Assign officers
* Assign police stations
* Update complaint status
* View complaint severity
* View financial loss
* View evidence count

Supported complaint statuses include:

```text
Pending
Under Investigation
Resolved
Closed
```

---

## 🏢 Police Station Management

The system contains predefined police stations:

| ID    | Police Station         | Location  |
| ----- | ---------------------- | --------- |
| PS001 | Cyber Cell HQ          | Mumbai    |
| PS002 | Delhi Cyber Unit       | Delhi     |
| PS003 | Bangalore Tech Crime   | Bangalore |
| PS004 | Chennai Cyber Division | Chennai   |
| PS005 | Kolkata Digital Crime  | Kolkata   |

Each station has an associated priority weight used by the project configuration.

---

## 📊 Crime Analytics

The administrator can access an analytics dashboard containing:

### Overview Metrics

* Total Complaints
* Resolved Complaints
* Pending Complaints
* Complaints Under Investigation

### Interactive Charts

* Complaint Status Distribution
* Crime Type Distribution
* Severity Distribution

The project uses **Plotly** to generate interactive charts.

---

## 🧮 Case Priority Algorithm

The project includes a case priority algorithm to calculate the priority of a complaint.

### Formula

```text
Priority =
(Severity × 0.4)
+ (Evidence × 0.3)
+ (Time × 0.2)
+ (Financial Loss × 0.1)
```

The resulting score is used to classify cases as:

|   Score | Priority    |
| ------: | ----------- |
|    8–10 | 🔴 Critical |
|  6–7.99 | 🟠 High     |
|  4–5.99 | 🟡 Medium   |
| Below 4 | 🟢 Low      |

The algorithm uses severity, evidence count, pending time, and financial loss as factors.

---

## 🔒 Cyber Safety Tips

The application provides users with basic cybersecurity awareness tips covering:

* Password Security
* Phishing Prevention
* Social Media Safety
* Online Shopping Security

Examples include using strong passwords, enabling 2FA, avoiding suspicious links, checking HTTPS, and using trusted payment methods.

---

# 🛠️ Technology Stack

| Technology  | Purpose                        |
| ----------- | ------------------------------ |
| Python      | Core programming language      |
| Streamlit   | Web application interface      |
| Pandas      | Data processing                |
| NumPy       | Numerical operations           |
| Plotly      | Interactive data visualization |
| JSON        | Data storage                   |
| hashlib     | Password hashing               |
| Regex       | Input validation               |
| Random      | CAPTCHA generation             |
| Dataclasses | Data models                    |
| Collections | Complaint analytics            |

The main application imports and uses these Python libraries directly.

---

# 📂 Project Structure

```text
Cyber-Crime-Reporting-System/
│
├── cybercrime.py
├── cybercrime_data.json
├── README.md
└── requirements.txt
```

### `cybercrime.py`

Main Python application containing:

* User authentication
* Registration
* CAPTCHA
* Complaint management
* Admin dashboard
* Analytics
* Safety tips
* Database operations

### `cybercrime_data.json`

Stores application data including:

* Users
* Complaints
* Counters

The application loads and saves this JSON file during operation.

---

# 🚀 Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/cyber-crime-reporting-system.git
cd cyber-crime-reporting-system
```

## 2. Create a Virtual Environment

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

Then install the dependencies:

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

```bash
streamlit run cybercrime.py
```

The Streamlit application will open in your browser.

---

# 🔑 Application Workflow

```text
                 ┌──────────────────┐
                 │      Start       │
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │ Login / Register │
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │ CAPTCHA Verify   │
                 └────────┬─────────┘
                          ↓
                ┌─────────┴─────────┐
                ↓                   ↓
        ┌──────────────┐    ┌──────────────┐
        │   Citizen    │    │    Admin     │
        └──────┬───────┘    └──────┬───────┘
               ↓                   ↓
       ┌───────────────┐    ┌───────────────┐
       │ File Complaint│    │ All Complaints│
       └───────┬───────┘    └───────┬───────┘
               ↓                    ↓
       ┌───────────────┐    ┌───────────────┐
       │Auto Severity  │    │Assign Officer │
       └───────┬───────┘    │ / Station     │
               ↓             └───────┬───────┘
       ┌───────────────┐             ↓
       │Generate ID    │      ┌───────────────┐
       └───────┬───────┘      │Update Status  │
               ↓              └───────┬───────┘
       ┌───────────────┐              ↓
       │Track Complaint│      ┌───────────────┐
       └───────────────┘      │   Analytics   │
                              └───────────────┘
```

---

# 💾 Data Storage

This project uses a **JSON file as its local data store** instead of a traditional database.

The data structure contains:

```text
users
 ├── user_id
 ├── name
 ├── email
 ├── password_hash
 ├── mobile
 ├── gender
 ├── city
 ├── address
 └── role

complaints
 ├── complaint_id
 ├── complaint_number
 ├── user_id
 ├── crime_type
 ├── description
 ├── location
 ├── date
 ├── latitude
 ├── longitude
 ├── financial_loss
 ├── severity
 ├── status
 ├── assigned_officer
 └── evidence_files
```

## The supplied project data follows this structure for users and complaints.

# 👥 User Roles

## Citizen

Citizens can:

* Register
* Login
* Verify CAPTCHA
* File cybercrime complaints
* Upload evidence
* View their complaints
* Track complaint status
* View cyber safety tips
* Reset password

## Admin

Administrators can:

* View all complaints
* View citizen information
* Filter complaints
* Sort complaints
* Assign officers
* Assign police stations
* Update complaint status
* View analytics

The application directs users to different dashboards according to their role.

---

# 🎓 Educational Concepts Demonstrated

This project demonstrates several Python programming concepts:

* Variables and data types
* Conditional statements
* Loops
* Functions
* Classes and objects
* Dataclasses
* Lists and dictionaries
* File handling
* JSON
* Exception handling
* Regular expressions
* Random functions
* Date and time handling
* Hashing
* List comprehensions
* Lambda functions
* `Counter`
* Pandas
* NumPy
* Data visualization
* Streamlit UI development

---

# 🔮 Future Scope

The current project can be further enhanced with:

* MySQL / PostgreSQL / MongoDB database
* Real police department authentication
* Email/SMS notifications
* Real-time case tracking
* AI-based cybercrime classification
* Machine-learning-based fraud detection
* OCR for evidence documents
* Secure cloud file storage
* Real Google Maps integration
* Advanced role-based access control
* Police investigation workflow
* Automatic report generation
* PDF complaint reports
* Mobile application
* Deployment on cloud platforms

---

# ⚠️ Security Note

This project is intended primarily for **educational and demonstration purposes**.

For production deployment:

* Use a production-grade database.
* Use stronger password hashing such as Argon2 or bcrypt.
* Never store real passwords or sensitive personal information in source-controlled JSON files.
* Store secrets in environment variables.
* Implement proper authorization and session security.
* Validate and securely store uploaded files.
* Use HTTPS.
* Add audit logging.
* Follow applicable privacy and cybersecurity regulations.

---

# 📸 Project Highlights

### Citizen Module

```text
Register → Login → CAPTCHA
       ↓
File Cyber Crime Complaint
       ↓
Automatic Severity
       ↓
Complaint ID Generated
       ↓
Track Complaint Status
```

### Admin Module

```text
Admin Login
    ↓
All Complaints
    ↓
Filter / Sort
    ↓
Review Citizen Details
    ↓
Assign Officer / Station
    ↓
Update Status
    ↓
View Analytics
```

---

# 👨‍💻 Author

**Harsh Patel**

* B.Tech / Engineering Student
* Python Developer
* Full Stack Development Learner
* Interested in Web Development, Python and Cybersecurity

---

# 📄 Project Information

**Project Name:** Cyber Crime Reporting and Analysis System

**Type:** Academic / Educational Project

**Language:** Python

**Framework:** Streamlit

**Data Storage:** JSON

**Visualization:** Plotly

**Application:** Web-based Cyber Crime Reporting & Analysis

---

# ⭐ Acknowledgement

This project was developed as an academic project to demonstrate Python programming, Streamlit application development, data management, authentication, visualization, and cybersecurity-related concepts.

If you find this project useful, consider giving the repository a ⭐ on GitHub.
