# -2-Password-Strength-Meter
🔐 Password Strength Meter (Python + Streamlit) A simple and effective Password Strength Meter built using Python and Streamlit. It checks your password against multiple security rules and gives a score (Weak, Moderate, Strong) along with improvement suggestions.

# 🔐 Password Strength Meter

A Python project that analyzes password strength based on length, character types, and complexity rules. Built using regular expressions and optionally deployed with Streamlit.

## ✅ Features
- Strength scoring: Weak, Moderate, Strong
- Real-time suggestions to improve weak passwords
- Supports GUI using Streamlit
- Bonus: Strong password generator

## 🚀 Tech
- Python
- re (regex)
- Optional: Streamlit for GUI

## 🎯 How It Works
The program checks:
- Length (8+ characters)
- Upper & Lowercase mix
- At least one digit
- At least one special character (!@#$%^&*)

## 🔧 Run Locally
```bash
pip install streamlit
streamlit run app.py
