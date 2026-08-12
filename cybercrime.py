"""
=================================================================================
CYBER CRIME REPORTING AND ANALYSIS SYSTEM - ENHANCED VERSION
Complete Python Syllabus + Advanced Features
=================================================================================
New Features:
- Police ID & Complaint ID tracking
- Google Maps location integration
- Case priority algorithm
- Forgot/Reset password
- CAPTCHA verification for login & registration
- AUTOMATIC severity assignment based on crime type
- Sequential complaint ID numbering
- User registration with mobile, gender, city, address
- Admin panel displays user details with complaints

⚠️ IMPORTANT NOTE ABOUT CAPTCHA:
- CAPTCHA is DISPLAYED ON SCREEN (not sent via email)
- CAPTCHA is generated using random.choice() method
- CAPTCHA appears in a clean box - simple and clear!
- Uses alphanumeric characters (A-Z, 0-9)
- This demonstrates Unit 9.5: Random Functions

=================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import json
import os
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from dataclasses import dataclass
from typing import List, Dict, Optional
import hashlib
import re
from functools import reduce
from collections import Counter
import random
import string
import math

# ==================== CONSTANTS ====================

# Police Station IDs (constant data)
POLICE_STATIONS = {
    "PS001": {"name": "Cyber Cell HQ", "location": "Mumbai", "priority_weight": 1.5},
    "PS002": {"name": "Delhi Cyber Unit", "location": "Delhi", "priority_weight": 1.3},
    "PS003": {"name": "Bangalore Tech Crime", "location": "Bangalore", "priority_weight": 1.2},
    "PS004": {"name": "Chennai Cyber Division", "location": "Chennai", "priority_weight": 1.0},
    "PS005": {"name": "Kolkata Digital Crime", "location": "Kolkata", "priority_weight": 1.0}
}

# Complaint ID prefix (constant)
COMPLAINT_ID_PREFIX = "CYB"

# CAPTCHA Configuration (constants)
CAPTCHA_LENGTH = 6
CAPTCHA_EXPIRY_MINUTES = 5

# Priority weights (constants for algorithm)
SEVERITY_WEIGHT = 0.4
EVIDENCE_WEIGHT = 0.3
TIME_WEIGHT = 0.2
AMOUNT_WEIGHT = 0.1

# CRIME TYPE TO SEVERITY MAPPING (Automatic Assignment)
CRIME_SEVERITY_MAP = {
    "Online Fraud": 8,
    "Hacking": 9,
    "Identity Theft": 9,
    "Phishing": 7,
    "Cyberbullying": 6,
    "Data Breach": 10,
    "Ransomware": 10,
    "Social Media Crime": 5
}

# ==================== HELPER FUNCTIONS ====================

def generate_captcha() -> str:
    """
    Generate 6-character CAPTCHA using random module (alphanumeric)
    Demonstrates: 9.5 random functions from NumPy/Python random module
    """
    # Generate alphanumeric CAPTCHA (uppercase letters and numbers)
    characters = string.ascii_uppercase + string.digits  # A-Z and 0-9
    captcha = ""
    for i in range(CAPTCHA_LENGTH):  # 2.2: for loop with range
        char = random.choice(characters)  # 9.5: random.choice function
        captcha += char  # 4.1: String concatenation
    
    return captcha

def generate_complaint_id(complaint_number: int) -> str:
    """
    Generate sequential complaint ID: CYB-YYYY-NNNNNN
    Demonstrates: 7.3 datetime, 4.1 string formatting
    """
    year = datetime.now().year  # 7.3: datetime module
    # Sequential number with leading zeros
    return f"{COMPLAINT_ID_PREFIX}-{year}-{complaint_number:06d}"

def generate_police_id() -> str:
    """
    Generate police officer ID: POL-XXXXX
    Demonstrates: 9.5 random.randrange()
    """
    # 9.5: random.randrange() - generates random number in range
    random_id = random.randrange(10000, 100000)  # 5-digit number
    return f"POL-{random_id}"

def display_captcha_message(email: str, captcha: str):
    """
    Simulate displaying CAPTCHA message
    Demonstrates: 3.1 Function with parameters
    """
    # Simple message
    message = f"Your CAPTCHA code: {captcha}"
    print(f"📧 Displayed for {email}: {message}")
    # CAPTCHA is shown on screen, not sent via email
    return True

def validate_email(email: str) -> tuple:
    """Email validation"""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email:
        return (False, "Email cannot be empty")
    if not re.match(email_pattern, email):
        return (False, "Invalid email format")
    return (True, "")

def validate_mobile(mobile: str) -> tuple:
    """Mobile number validation - 10 digits"""
    if not mobile:
        return (False, "Mobile number cannot be empty")
    if not mobile.isdigit():
        return (False, "Mobile number should contain only digits")
    if len(mobile) != 10:
        return (False, "Mobile number must be exactly 10 digits")
    return (True, "")

def validate_password(password: str) -> tuple:
    """Password validation - requires uppercase, lowercase, number, and special character"""
    if not password:
        return (False, "Password cannot be empty")
    if len(password) < 8:
        return (False, "Password must be at least 8 characters")
    if not re.search(r'[A-Z]', password):
        return (False, "Must contain at least one uppercase letter")
    if not re.search(r'[a-z]', password):
        return (False, "Must contain at least one lowercase letter")
    if not re.search(r'\d', password):
        return (False, "Must contain at least one number")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=\[\]\\;/]', password):
        return (False, "Must contain at least one special character")
    return (True, "Password is strong ✓")

def get_severity_from_crime_type(crime_type: str) -> int:
    """
    Get automatic severity level based on crime type
    Returns severity level (1-10)
    """
    return CRIME_SEVERITY_MAP.get(crime_type, 5)  # Default to 5 if not found

# ==================== PRIORITY ALGORITHM ====================

def calculate_case_priority(severity: int, evidence_count: int, days_pending: int, 
                            financial_loss: float = 0) -> float:
    """
    Priority Algorithm: Calculate case priority score
    Higher score = Higher priority
    
    Formula: 
    Priority = (Severity × 0.4) + (Evidence × 0.3) + (Time × 0.2) + (Amount × 0.1)
    
    Returns: Priority score (0-10)
    """
    # Normalize severity (1-10 scale)
    severity_score = min(severity, 10)
    
    # Evidence score (0-10 based on count)
    evidence_score = min(evidence_count * 2, 10)
    
    # Time urgency score (more days = higher priority)
    time_score = min(days_pending / 3, 10)
    
    # Financial loss score (normalized)
    amount_score = min(financial_loss / 100000, 10) if financial_loss > 0 else 0
    
    # Weighted priority calculation
    priority = (
        severity_score * SEVERITY_WEIGHT +
        evidence_score * EVIDENCE_WEIGHT +
        time_score * TIME_WEIGHT +
        amount_score * AMOUNT_WEIGHT
    )
    
    return round(priority, 2)

def get_priority_label(priority_score: float) -> str:
    """Get priority label based on score"""
    if priority_score >= 8:
        return "🔴 CRITICAL"
    elif priority_score >= 6:
        return "🟠 HIGH"
    elif priority_score >= 4:
        return "🟡 MEDIUM"
    else:
        return "🟢 LOW"

# ==================== DATA CLASSES ====================

@dataclass
class User:
    """User class with CAPTCHA support and additional fields"""
    user_id: int
    name: str
    email: str
    password_hash: str
    mobile: str = ""
    gender: str = ""
    city: str = ""
    address: str = ""
    role: str = "citizen"
    police_id: Optional[str] = None
    captcha: Optional[str] = None
    captcha_expiry: Optional[datetime] = None
    is_verified: bool = False
    
    def verify_password(self, password: str) -> bool:
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()
    
    def verify_captcha(self, entered_captcha: str) -> bool:
        """Verify CAPTCHA and check expiry"""
        if not self.captcha or not self.captcha_expiry:
            return False
        
        # Convert captcha_expiry from string to datetime if needed
        if isinstance(self.captcha_expiry, str):
            try:
                self.captcha_expiry = datetime.fromisoformat(self.captcha_expiry)
            except:
                return False
        
        if datetime.now() > self.captcha_expiry:
            return False
        # Case-insensitive comparison for CAPTCHA
        return self.captcha.upper() == entered_captcha.upper()

@dataclass
class Complaint:
    """Complaint with sequential numbering and automatic severity"""
    complaint_id: str
    complaint_number: int
    user_id: int
    _crime_type: str
    _description: str
    _location: str
    _date: str
    _latitude: float
    _longitude: float
    _financial_loss: float
    _severity: int
    status: str = "Pending"
    _assigned_officer: Optional[str] = None
    _assigned_police_station: Optional[str] = None
    _evidence_files: List[str] = None
    
    def __post_init__(self):
        if self._evidence_files is None:
            self._evidence_files = []

# ==================== DATABASE ====================

class Database:
    """Database with user management"""
    def __init__(self):
        self.users_dict: Dict[int, User] = {}
        self.complaints_dict: Dict[str, Complaint] = {}
        self.user_counter = 1
        self.complaint_counter = 0
        self.load_data()
    
    def add_user(self, name: str, email: str, password: str, mobile: str, 
                 gender: str, city: str, address: str, role: str = "citizen") -> User:
        """Add new user with full details"""
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        # Generate CAPTCHA
        captcha = generate_captcha()
        captcha_expiry = datetime.now() + timedelta(minutes=CAPTCHA_EXPIRY_MINUTES)
        
        # Generate police ID if admin
        police_id = generate_police_id() if role == "admin" else None
        
        user = User(
            user_id=self.user_counter,
            name=name,
            email=email,
            password_hash=password_hash,
            mobile=mobile,
            gender=gender,
            city=city,
            address=address,
            role=role,
            police_id=police_id,
            captcha=captcha,
            captcha_expiry=captcha_expiry,
            is_verified=False
        )
        
        self.user_counter += 1
        
        self.users_dict[user.user_id] = user
        self.save_data()
        
        # Display CAPTCHA
        display_captcha_message(email, captcha)
        
        return user
    
    def add_complaint(self, user_id: int, crime_type: str, description: str, 
                     location: str, date: str, latitude: float = 0.0, 
                     longitude: float = 0.0, financial_loss: float = 0.0,
                     severity: int = None) -> Complaint:
        """Add new complaint with sequential ID and automatic severity"""
        self.complaint_counter += 1
        
        # Auto-assign severity based on crime type if not provided
        if severity is None:
            severity = get_severity_from_crime_type(crime_type)
        
        # Generate sequential complaint ID
        complaint_id = generate_complaint_id(self.complaint_counter)
        
        complaint = Complaint(
            complaint_id=complaint_id,
            complaint_number=self.complaint_counter,
            user_id=user_id,
            _crime_type=crime_type,
            _description=description,
            _location=location,
            _date=date,
            _latitude=latitude,
            _longitude=longitude,
            _financial_loss=financial_loss,
            _severity=severity
        )
        
        self.complaints_dict[complaint_id] = complaint
        self.save_data()
        
        return complaint
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        for user in self.users_dict.values():
            if user.email == email:
                return user
        return None
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return self.users_dict.get(user_id)
    
    def update_user_password(self, user_id: int, new_password: str):
        """Update user password"""
        if user_id in self.users_dict:
            password_hash = hashlib.sha256(new_password.encode()).hexdigest()
            self.users_dict[user_id].password_hash = password_hash
            self.save_data()
    
    def get_complaint(self, complaint_id: str) -> Optional[Complaint]:
        """Get complaint by ID"""
        return self.complaints_dict.get(complaint_id)
    
    def get_user_complaints(self, user_id: int) -> List[Complaint]:
        """Get all complaints for a user"""
        return [c for c in self.complaints_dict.values() if c.user_id == user_id]
    
    def get_all_complaints(self) -> List[Complaint]:
        """Get all complaints"""
        return list(self.complaints_dict.values())
    
    def update_complaint_status(self, complaint_id: str, status: str, officer_id: str = None):
        """Update complaint status"""
        if complaint_id in self.complaints_dict:
            self.complaints_dict[complaint_id].status = status
            if officer_id:
                self.complaints_dict[complaint_id]._assigned_officer = officer_id
            self.save_data()
    
    def save_data(self):
        """Save data to JSON"""
        data = {
            'users': {k: vars(v) for k, v in self.users_dict.items()},
            'complaints': {k: vars(v) for k, v in self.complaints_dict.items()},
            'counters': {
                'user_counter': self.user_counter,
                'complaint_counter': self.complaint_counter
            }
        }
        
        # Convert datetime objects
        for user_data in data['users'].values():
            if user_data.get('captcha_expiry') and isinstance(user_data['captcha_expiry'], datetime):
                user_data['captcha_expiry'] = user_data['captcha_expiry'].isoformat()
        
        with open('cybercrime_data.json', 'w') as f:
            json.dump(data, f, indent=2, default=str)
    
    def load_data(self):
        """Load data from JSON"""
        if os.path.exists('cybercrime_data.json'):
            try:
                with open('cybercrime_data.json', 'r') as f:
                    data = json.load(f)
                
                # Load users
                users_data = data.get('users', {})
                for user_id_str, user_dict in users_data.items():
                    user_id = int(user_id_str)
                    
                    # Convert captcha_expiry
                    captcha_expiry = user_dict.get('captcha_expiry')
                    if captcha_expiry:
                        try:
                            captcha_expiry = datetime.fromisoformat(captcha_expiry)
                        except:
                            captcha_expiry = None
                    
                    user = User(
                        user_id=user_id,
                        name=user_dict['name'],
                        email=user_dict['email'],
                        password_hash=user_dict['password_hash'],
                        mobile=user_dict.get('mobile', ''),
                        gender=user_dict.get('gender', ''),
                        city=user_dict.get('city', ''),
                        address=user_dict.get('address', ''),
                        role=user_dict.get('role', 'citizen'),
                        police_id=user_dict.get('police_id'),
                        captcha=user_dict.get('captcha'),
                        captcha_expiry=captcha_expiry,
                        is_verified=user_dict.get('is_verified', False)
                    )
                    self.users_dict[user_id] = user
                
                # Load complaints
                complaints_data = data.get('complaints', {})
                for complaint_id, complaint_dict in complaints_data.items():
                    complaint = Complaint(
                        complaint_id=complaint_dict['complaint_id'],
                        complaint_number=complaint_dict.get('complaint_number', 1),
                        user_id=complaint_dict['user_id'],
                        _crime_type=complaint_dict['_crime_type'],
                        _description=complaint_dict['_description'],
                        _location=complaint_dict['_location'],
                        _date=complaint_dict['_date'],
                        _latitude=complaint_dict.get('_latitude', 0.0),
                        _longitude=complaint_dict.get('_longitude', 0.0),
                        _financial_loss=complaint_dict.get('_financial_loss', 0.0),
                        _severity=complaint_dict.get('_severity', 5),
                        status=complaint_dict.get('status', 'Pending'),
                        _assigned_officer=complaint_dict.get('_assigned_officer'),
                        _assigned_police_station=complaint_dict.get('_assigned_police_station'),
                        _evidence_files=complaint_dict.get('_evidence_files', [])
                    )
                    self.complaints_dict[complaint_id] = complaint
                
                # Load counters
                counters = data.get('counters', {})
                self.user_counter = counters.get('user_counter', 1)
                self.complaint_counter = counters.get('complaint_counter', 0)
                
            except Exception as e:
                print(f"Error loading data: {e}")

# ==================== CAPTCHA VERIFICATION ====================

def show_captcha_verification(user: User, context: str = "login") -> bool:
    """Display CAPTCHA verification - CLEAN VERSION"""
    st.divider()
    st.subheader("🔐 CAPTCHA Verification")
    
    # Display CAPTCHA - CLEAN VERSION (no email message)
    
    # Simple, clean CAPTCHA display
    st.markdown(f"""
    <div style="background: #f0f2f6; 
                padding: 20px; 
                border-radius: 10px; 
                text-align: center;
                margin: 20px 0;">
        <h1 style="color: #333; 
                   font-size: 3em; 
                   letter-spacing: 10px; 
                   margin: 0;
                   font-family: monospace;
                   font-weight: bold;">
            {user.captcha}
        </h1>
    </div>
    """, unsafe_allow_html=True)
    
    # CAPTCHA input
    entered_captcha = st.text_input("Enter CAPTCHA code (case-insensitive)", max_chars=6, key=f"captcha_input_{context}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✅ Verify CAPTCHA", type="primary", use_container_width=True, key=f"verify_{context}"):
            if user.verify_captcha(entered_captcha):
                user.is_verified = True
                st.session_state.db.save_data()
                st.success("🎉 CAPTCHA Verified!")
                return True
            else:
                st.error("❌ Invalid CAPTCHA!")
                return False
    
    with col2:
        if st.button("🔄 Generate New CAPTCHA", use_container_width=True, key=f"new_{context}"):
            user.captcha = generate_captcha()
            user.captcha_expiry = datetime.now() + timedelta(minutes=CAPTCHA_EXPIRY_MINUTES)
            st.session_state.db.save_data()
            display_captcha_message(user.email, user.captcha)
            st.rerun()
    
    return False

# ==================== FORGOT PASSWORD ====================

def forgot_password_page():
    """Forgot password with CAPTCHA"""
    st.header("🔑 Forgot Password")
    
    if 'reset_step' not in st.session_state:
        st.session_state.reset_step = 1
    
    if st.session_state.reset_step == 1:
        st.write("**Step 1: Enter your email**")
        email = st.text_input("Email")
        
        if st.button("Generate CAPTCHA", type="primary"):
            if email:
                db = st.session_state.db
                user = db.get_user_by_email(email)
                
                if user:
                    captcha = generate_captcha()
                    
                    st.session_state.reset_email = email
                    st.session_state.reset_captcha = captcha
                    st.session_state.reset_captcha_expiry = datetime.now() + timedelta(minutes=CAPTCHA_EXPIRY_MINUTES)
                    st.session_state.reset_step = 2
                    display_captcha_message(email, captcha)
                    st.rerun()
                else:
                    st.error("❌ Email not found")
            else:
                st.error("❌ Please enter your email")
    
    elif st.session_state.reset_step == 2:
        st.write(f"**Step 2: Verify CAPTCHA for {st.session_state.reset_email}**")
        
        # Display CAPTCHA
        st.markdown(f"""
        <div style="background: #f0f2f6; 
                    padding: 20px; 
                    border-radius: 10px; 
                    text-align: center;
                    margin: 20px 0;">
            <h1 style="color: #333; 
                       font-size: 3em; 
                       letter-spacing: 10px; 
                       margin: 0;
                       font-family: monospace;
                       font-weight: bold;">
                {st.session_state.reset_captcha}
            </h1>
        </div>
        """, unsafe_allow_html=True)
        
        captcha_input = st.text_input("Enter CAPTCHA code (case-insensitive)", max_chars=6)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Verify CAPTCHA", type="primary", use_container_width=True):
                if captcha_input.upper() == st.session_state.reset_captcha.upper():
                    st.success("✅ CAPTCHA Verified!")
                    st.session_state.reset_step = 3
                    st.rerun()
                else:
                    st.error("❌ Invalid CAPTCHA")
        
        with col2:
            if st.button("Generate New CAPTCHA", use_container_width=True):
                captcha = generate_captcha()
                st.session_state.reset_captcha = captcha
                st.session_state.reset_captcha_expiry = datetime.now() + timedelta(minutes=CAPTCHA_EXPIRY_MINUTES)
                display_captcha_message(st.session_state.reset_email, captcha)
                st.rerun()
    
    elif st.session_state.reset_step == 3:
        st.write("**Step 3: Set New Password**")
        st.success(f"✅ CAPTCHA Verified for {st.session_state.reset_email}")
        
        new_password = st.text_input("New Password", type="password", key="new_pass")
        confirm_password = st.text_input("Confirm Password", type="password", key="confirm_pass")
        
        if new_password:
            pass_valid, pass_msg = validate_password(new_password)
            if pass_valid:
                st.success(pass_msg)
            else:
                st.warning(pass_msg)
        
        if st.button("Reset Password", type="primary", use_container_width=True):
            if new_password and confirm_password:
                if new_password == confirm_password:
                    pass_valid, pass_msg = validate_password(new_password)
                    if pass_valid:
                        db = st.session_state.db
                        user = db.get_user_by_email(st.session_state.reset_email)
                        db.update_user_password(user.user_id, new_password)
                        
                        # Clear session state
                        del st.session_state.reset_email
                        del st.session_state.reset_captcha
                        del st.session_state.reset_captcha_expiry
                        del st.session_state.reset_step
                        
                        st.success("🎉 Password reset successful!")
                        st.balloons()
                    else:
                        st.error(pass_msg)
                else:
                    st.error("❌ Passwords don't match")
            else:
                st.error("❌ Please fill both fields")
    
    # Back button
    if st.session_state.reset_step > 1:
        if st.button("⬅️ Back to Login"):
            if 'reset_step' in st.session_state:
                del st.session_state.reset_step
            if 'reset_email' in st.session_state:
                del st.session_state.reset_email
            if 'reset_captcha' in st.session_state:
                del st.session_state.reset_captcha
            if 'reset_captcha_expiry' in st.session_state:
                del st.session_state.reset_captcha_expiry
            st.rerun()

def forgot_email_page():
    """Forgot email recovery"""
    st.header("📧 Forgot Email")
    
    name = st.text_input("Enter your registered name")
    mobile = st.text_input("Enter your registered mobile number")
    
    if st.button("Search Email"):
        if name or mobile:
            db = st.session_state.db
            found_users = []
            
            for user in db.users_dict.values():
                if name and user.name.lower() == name.lower():
                    found_users.append(user)
                elif mobile and user.mobile == mobile:
                    found_users.append(user)
            
            if found_users:
                st.success("✅ Found your email(s):")
                for user in found_users:
                    masked_email = user.email[:3] + "***" + user.email[user.email.index('@'):]
                    st.info(f"📧 {masked_email}")
            else:
                st.error("❌ No account found")
        else:
            st.error("❌ Please enter name or mobile")

# ==================== STREAMLIT UI ====================

def initialize_session_state():
    """Initialize session state"""
    if 'db' not in st.session_state:
        st.session_state.db = Database()
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None
    if 'show_otp' not in st.session_state:
        st.session_state.show_otp = False

def login_page():
    """Enhanced login page - COMBINED LOGIN BUTTON"""
    st.title("🛡️ Cyber Crime Reporting System")
    
    menu = st.radio("", ["Login", "Register", "Forgot Password"], horizontal=True)
    
    if menu == "Forgot Password":
        forgot_password_page()
        return
    
    if menu == "Login":
        st.subheader("🔐 Login")
        
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        
        # COMBINED LOGIN BUTTON
        if st.button("Login", type="primary", use_container_width=True):
            user = st.session_state.db.get_user_by_email(email)
            if user and user.verify_password(password):
                # Generate fresh CAPTCHA for login
                user.captcha = generate_captcha()
                user.captcha_expiry = datetime.now() + timedelta(minutes=CAPTCHA_EXPIRY_MINUTES)
                display_captcha_message(user.email, user.captcha)
                st.session_state.db.save_data()
                
                st.session_state.pending_user = user
                st.session_state.show_otp = True
                st.rerun()
            else:
                st.error("❌ Invalid credentials!")
        
        # CAPTCHA Verification
        if st.session_state.get('show_otp'):
            if show_captcha_verification(st.session_state.pending_user, "login"):
                st.session_state.logged_in = True
                st.session_state.current_user = st.session_state.pending_user
                st.session_state.show_otp = False
                del st.session_state.pending_user
                st.rerun()
    
    elif menu == "Register":
        st.subheader("📝 Create New Account")
        
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name *", key="reg_name")
            email = st.text_input("Email *", key="reg_email")
            mobile = st.text_input("Mobile Number (10 digits) *", key="reg_mobile", max_chars=10)
            gender = st.selectbox("Gender *", ["Select", "Male", "Female", "Other"], key="reg_gender")
        
        with col2:
            city = st.text_input("City *", key="reg_city")
            address = st.text_area("Address *", key="reg_address", height=100)
            password = st.text_input("Password *", type="password", key="reg_password")
            confirm_password = st.text_input("Confirm Password *", type="password", key="reg_confirm_password")
        
        # Password validation display
        if password:
            pass_valid, pass_msg = validate_password(password)
            if pass_valid:
                st.success(pass_msg)
            else:
                st.warning(pass_msg)
        
        # Confirm password check
        if confirm_password and password:
            if password == confirm_password:
                st.success("✓ Passwords match")
            else:
                st.error("✗ Passwords don't match")
        
        with st.expander("📋 Password Requirements"):
            st.write("✓ Minimum 8 characters")
            st.write("✓ At least 1 uppercase letter")
            st.write("✓ At least 1 lowercase letter")
            st.write("✓ At least 1 number")
            st.write("✓ At least 1 special character")
        
        if st.button("Register", use_container_width=True, type="primary"):
            if name and email and mobile and gender != "Select" and city and address and password and confirm_password:
                # Validate all fields
                email_valid, email_error = validate_email(email)
                mobile_valid, mobile_error = validate_mobile(mobile)
                pass_valid, pass_error = validate_password(password)
                
                if not email_valid:
                    st.error(f"❌ {email_error}")
                elif not mobile_valid:
                    st.error(f"❌ {mobile_error}")
                elif not pass_valid:
                    st.error(f"❌ {pass_error}")
                elif password != confirm_password:
                    st.error("❌ Passwords don't match!")
                else:
                    existing = st.session_state.db.get_user_by_email(email)
                    if existing:
                        st.error("❌ Email already registered!")
                    else:
                        user = st.session_state.db.add_user(name, email, password, mobile, gender, city, address)
                        st.session_state.pending_user = user
                        st.session_state.show_otp = True
                        st.rerun()
            else:
                st.error("❌ Please fill all required fields (*)")
        
        # CAPTCHA Verification for registration
        if st.session_state.get('show_otp') and 'pending_user' in st.session_state:
            if show_captcha_verification(st.session_state.pending_user, "registration"):
                st.success("✅ Registration Successful! Please login.")
                st.session_state.show_otp = False
                del st.session_state.pending_user
                st.rerun()

def file_complaint_page():
    """Enhanced complaint page - AUTOMATIC SEVERITY ASSIGNMENT"""
    st.header("📝 File New Cyber Crime Complaint")
    
    crime_types = ("Online Fraud", "Hacking", "Identity Theft", "Phishing", 
                   "Cyberbullying", "Data Breach", "Ransomware", "Social Media Crime")
    
    col1, col2 = st.columns(2)
    
    with col1:
        crime_type = st.selectbox("Crime Type *", crime_types)
        # Show automatic severity
        auto_severity = get_severity_from_crime_type(crime_type)
        st.info(f"🎯 Auto-assigned Severity: {auto_severity}/10 ({crime_type})")
        
        location = st.text_input("Location/Address *")
        date = st.date_input("Date of Incident *", max_value=datetime.now().date())
    
    with col2:
        financial_loss = st.number_input("Financial Loss (₹)", min_value=0.0, step=1000.0)
        
        # Google Maps location
        st.write("**📍 Mark Location (Optional)**")
        latitude = st.number_input("Latitude", value=19.0760, format="%.4f")
        longitude = st.number_input("Longitude", value=72.8777, format="%.4f")
    
    description = st.text_area("Detailed Description *", height=150)
    
    st.write("**Upload Evidence (Optional)**")
    evidence_files = st.file_uploader("Screenshots/Documents", accept_multiple_files=True)
    
    # Show map preview
    if latitude and longitude:
        st.map(pd.DataFrame({'lat': [latitude], 'lon': [longitude]}))
    
    if st.button("Submit Complaint", type="primary", use_container_width=True):
        if crime_type and location and description:
            if date > datetime.now().date():
                st.error("❌ Cannot report future crimes!")
                return
            
            # Use automatic severity from crime type
            complaint = st.session_state.db.add_complaint(
                st.session_state.current_user.user_id,
                crime_type, description, location, str(date),
                latitude, longitude, financial_loss
            )
            
            if evidence_files:
                for file in evidence_files:
                    complaint._evidence_files.append(file.name)
                st.session_state.db.save_data()
            
            st.success(f"✅ Complaint {complaint.complaint_id} registered!")
            st.info(f"📊 Severity Level: {complaint._severity}/10 (Auto-assigned for {crime_type})")
        else:
            st.error("Please fill all required fields (*)!")

def my_complaints_page():
    """View user's own complaints"""
    st.header("📋 My Complaints")
    
    complaints = st.session_state.db.get_user_complaints(st.session_state.current_user.user_id)
    
    if not complaints:
        st.info("No complaints filed yet.")
    else:
        for complaint in complaints:
            with st.expander(f"{complaint.complaint_id} - {complaint._crime_type} - Status: {complaint.status}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Status:** {complaint.status}")
                    st.write(f"**Date:** {complaint._date}")
                    st.write(f"**Location:** {complaint._location}")
                    st.write(f"**Crime Type:** {complaint._crime_type}")
                
                with col2:
                    st.write(f"**Severity:** {complaint._severity}/10")
                    st.write(f"**Financial Loss:** ₹{complaint._financial_loss}")
                    if complaint._assigned_officer:
                        st.write(f"**Assigned Officer:** {complaint._assigned_officer}")
                    if complaint._assigned_police_station:
                        st.write(f"**Police Station:** {complaint._assigned_police_station}")
                
                st.write(f"**Description:** {complaint._description}")
                
                if complaint._evidence_files:
                    st.write(f"**Evidence Files:** {', '.join(complaint._evidence_files)}")

def admin_complaints_page():
    """Admin view with USER DETAILS displayed"""
    st.header("📊 All Complaints with User Details")
    
    complaints = st.session_state.db.get_all_complaints()
    
    if not complaints:
        st.info("No complaints in system.")
        return
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        filter_status = st.selectbox("Filter by Status", ["All", "Pending", "Under Investigation", "Resolved", "Closed"])
    with col2:
        filter_crime = st.selectbox("Filter by Crime Type", 
            ["All"] + list(CRIME_SEVERITY_MAP.keys()))
    with col3:
        sort_by = st.selectbox("Sort By", ["Sequential (Newest First)", "Severity", "Date"])
    
    # Filter complaints
    filtered = complaints
    if filter_status != "All":
        filtered = [c for c in filtered if c.status == filter_status]
    if filter_crime != "All":
        filtered = [c for c in filtered if c._crime_type == filter_crime]
    
    # Sort complaints
    if sort_by == "Sequential (Newest First)":
        filtered.sort(key=lambda x: x.complaint_number, reverse=True)
    elif sort_by == "Severity":
        filtered.sort(key=lambda x: x._severity, reverse=True)
    elif sort_by == "Date":
        filtered.sort(key=lambda x: x._date, reverse=True)
    
    st.write(f"**Showing {len(filtered)} complaints**")
    
    for complaint in filtered:
        # Get user details
        user = st.session_state.db.get_user_by_id(complaint.user_id)
        
        # Create complaint header with user details
        if user:
            user_name = user.name
            user_mobile = user.mobile if user.mobile else "N/A"
            user_address = user.address if user.address else "N/A"
        else:
            user_name = "Unknown User"
            user_mobile = "N/A"
            user_address = "N/A"
        
        complaint_header = f"{complaint.complaint_id} | 👤 {user_name} | 📱 {user_mobile} | 📍 {user_address} | {complaint._crime_type} | Status: {complaint.status}"
        
        with st.expander(complaint_header):
            # USER DETAILS SECTION - HIGHLIGHTED
            st.markdown("### 👤 User Details")
            
            if user:
                user_col1, user_col2, user_col3 = st.columns(3)
                
                with user_col1:
                    st.write(f"**Name:** {user.name}")
                    st.write(f"**Email:** {user.email}")
                
                with user_col2:
                    st.write(f"**Mobile:** {user.mobile if user.mobile else 'Not provided'}")
                    st.write(f"**Gender:** {user.gender if user.gender else 'Not provided'}")
                
                with user_col3:
                    st.write(f"**City:** {user.city if user.city else 'Not provided'}")
                    st.write(f"**Address:** {user.address if user.address else 'Not provided'}")
            else:
                st.error(f"⚠️ User data not found for user_id: {complaint.user_id}")
            
            st.divider()
            
            # COMPLAINT DETAILS SECTION
            st.markdown("### 📋 Complaint Details")
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Complaint ID:** {complaint.complaint_id}")
                st.write(f"**Status:** {complaint.status}")
                st.write(f"**Crime Type:** {complaint._crime_type}")
                st.write(f"**Date of Incident:** {complaint._date}")
                st.write(f"**Location:** {complaint._location}")
            
            with col2:
                st.write(f"**Severity:** {complaint._severity}/10")
                st.write(f"**Financial Loss:** ₹{complaint._financial_loss}")
                st.write(f"**Evidence Files:** {len(complaint._evidence_files)}")
                if complaint._assigned_officer:
                    st.write(f"**Assigned Officer:** {complaint._assigned_officer}")
                if complaint._assigned_police_station:
                    st.write(f"**Police Station:** {complaint._assigned_police_station}")
            
            st.write(f"**Description:** {complaint._description}")
            
            # Admin actions
            st.divider()
            st.markdown("### ⚙️ Admin Actions")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                new_status = st.selectbox("Update Status", 
                    ["Pending", "Under Investigation", "Resolved", "Closed"],
                    index=["Pending", "Under Investigation", "Resolved", "Closed"].index(complaint.status),
                    key=f"s_{complaint.complaint_id}")
            
            with col2:
                officer_name = st.text_input("Assign Officer", 
                    value=complaint._assigned_officer or "",
                    key=f"o_{complaint.complaint_id}")
            
            with col3:
                police_station = st.selectbox("Assign Station", 
                    ["None"] + list(POLICE_STATIONS.keys()),
                    key=f"ps_{complaint.complaint_id}")
            
            if st.button("💾 Update Complaint", key=f"u_{complaint.complaint_id}", type="primary"):
                complaint.status = new_status
                complaint._assigned_officer = officer_name
                if police_station != "None":
                    complaint._assigned_police_station = POLICE_STATIONS[police_station]["name"]
                st.session_state.db.save_data()
                st.success("✅ Complaint updated successfully!")
                st.rerun()

def analytics_page():
    """Analytics dashboard"""
    st.header("📈 Crime Analysis & Statistics")
    
    complaints = st.session_state.db.get_all_complaints()
    
    if not complaints:
        st.info("No data available.")
        return
    
    # Key Metrics
    total = len(complaints)
    resolved = len([c for c in complaints if c.status == "Resolved"])
    pending = len([c for c in complaints if c.status == "Pending"])
    under_investigation = len([c for c in complaints if c.status == "Under Investigation"])
    
    # Top Row - Main Metrics
    st.subheader("📊 Overview Statistics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Complaints", total)
    col2.metric("✅ Resolved", resolved)
    col3.metric("⏳ Pending", pending)
    col4.metric("🔍 Investigating", under_investigation)
    
    st.divider()
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Status Distribution")
        status_counts = Counter([c.status for c in complaints])
        fig_status = px.pie(
            values=list(status_counts.values()), 
            names=list(status_counts.keys()),
            title="Complaints by Status"
        )
        st.plotly_chart(fig_status, use_container_width=True)
    
    with col2:
        st.subheader("Crime Type Distribution")
        crime_counts = Counter([c._crime_type for c in complaints])
        fig_crime = px.bar(
            x=list(crime_counts.keys()), 
            y=list(crime_counts.values()),
            title="Complaints by Crime Type",
            labels={'x': 'Crime Type', 'y': 'Count'}
        )
        st.plotly_chart(fig_crime, use_container_width=True)
    
    # Severity Analysis
    st.subheader("Severity Analysis")
    severity_counts = Counter([c._severity for c in complaints])
    fig_severity = px.bar(
        x=list(severity_counts.keys()), 
        y=list(severity_counts.values()),
        title="Complaints by Severity Level",
        labels={'x': 'Severity (1-10)', 'y': 'Count'}
    )
    st.plotly_chart(fig_severity, use_container_width=True)

def citizen_dashboard():
    """Citizen dashboard"""
    user = st.session_state.current_user
    
    st.sidebar.title(f"👤 {user.name}")
    st.sidebar.info(f"📧 {user.email}")
    st.sidebar.info(f"📱 {user.mobile}")
    
    menu = st.sidebar.radio("Menu", [
        "File Complaint",
        "My Complaints",
        "Safety Tips",
        "Logout"
    ])
    
    if menu == "File Complaint":
        file_complaint_page()
    elif menu == "My Complaints":
        my_complaints_page()
    elif menu == "Safety Tips":
        safety_tips_page()
    elif menu == "Logout":
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.rerun()

def admin_dashboard():
    """Admin dashboard"""
    st.sidebar.title(f"👮 {st.session_state.current_user.name}")
    st.sidebar.success(f"🆔 Police ID: {st.session_state.current_user.police_id}")
    
    menu = st.sidebar.radio("Menu", [
        "All Complaints",
        "Analytics",
        "Logout"
    ])
    
    if menu == "All Complaints":
        admin_complaints_page()
    elif menu == "Analytics":
        analytics_page()
    elif menu == "Logout":
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.rerun()

def safety_tips_page():
    """Safety tips"""
    st.header("🔒 Cyber Safety Tips")
    
    tips = {
        "Password Security": ["Use strong passwords", "Enable 2FA", "Never share passwords"],
        "Phishing Prevention": ["Don't click suspicious links", "Verify emails", "Check HTTPS"],
        "Social Media": ["Review privacy settings", "Don't overshare", "Verify requests"],
        "Online Shopping": ["Use secure payments", "Shop on trusted sites", "Keep records"]
    }
    
    for category, tip_list in tips.items():
        st.subheader(f"✨ {category}")
        for tip in tip_list:
            st.write(f"• {tip}")

def main():
    """Main application"""
    st.set_page_config(page_title="Cyber Crime System", page_icon="🛡️", layout="wide")
    
    initialize_session_state()
    
    # Create default admin if no users exist
    if len(st.session_state.db.users_dict) == 0:
        admin = st.session_state.db.add_user(
            "Admin Officer", 
            "lj@gmail.com", 
            "Admin@123",
            "9876543210",
            "Male",
            "Mumbai",
            "Cyber Cell HQ, Mumbai",
            "admin"
        )
        admin.is_verified = True
        st.session_state.db.save_data()
    
    if not st.session_state.logged_in:
        login_page()
    else:
        if st.session_state.current_user.role == "admin":
            admin_dashboard()
        else:
            citizen_dashboard()

if __name__ == "__main__":
    main()

    