import streamlit as st
import re

def check_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("At least 8 characters.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Use both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include at least one number.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Include a special character (!@#$%^&*).")

    return score, suggestions

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter a password:", type="password")

if password:
    score, suggestions = check_strength(password)

    st.write(f"**Score:** {score}/4")

    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password. Consider improvements.")
    else:
        st.error("❌ Weak Password. Please improve it.")

    if suggestions:
        st.subheader("Suggestions:")
        for s in suggestions:
            st.write(f"- {s}")
