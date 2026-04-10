import random
import string
import streamlit as st

def generate_password(length, use_letters, use_digits, use_symbols):
    """Generates a secure password based on specified criteria."""
    
    if not (use_letters or use_digits or use_symbols):
        return None
        
    # Ensure at least one character of each selected type is included
    password_chars = []
    characters = ""
    
    if use_letters:
        password_chars.append(random.choice(string.ascii_letters))
        characters += string.ascii_letters
    if use_digits:
        password_chars.append(random.choice(string.digits))
        characters += string.digits
    if use_symbols:
        password_chars.append(random.choice(string.punctuation))
        characters += string.punctuation
        
    # If the requested length is smaller than the required unique types, fallback to simple random
    if length < len(password_chars):
        return "".join(random.choice(characters) for _ in range(length))
        
    # Fill the remaining length with random choices from the allowed pool
    for _ in range(length - len(password_chars)):
        password_chars.append(random.choice(characters))
        
    # Shuffle the resulting list to prevent predictable patterns (like letters always being first)
    random.shuffle(password_chars)
    
    return "".join(password_chars)

def main():
    # Configure the Streamlit page
    st.set_page_config(page_title="Advanced Password Generator", page_icon="🔒", layout="centered")
    
    # UI Header
    st.title("🔒 Advanced Password Generator")
    st.markdown("Create secure, customized passwords easily. This project demonstrates secure random generation and interactive UI components.")
    st.divider()

    # Create a form to group the inputs
    with st.form("password_settings"):
        st.subheader("Configuration")
        
        # Slider for password length (safer than raw text input)
        length = st.slider("Select Password Length:", min_value=4, max_value=128, value=16)
        
        # Toggle options using columns for a cleaner layout
        col1, col2, col3 = st.columns(3)
        with col1:
            use_letters = st.checkbox("Letters (A-Z, a-z)", value=True)
        with col2:
            use_digits = st.checkbox("Numbers (0-9)", value=True)
        with col3:
            use_symbols = st.checkbox("Symbols (!@#$)", value=True)
            
        # Submit button for the form
        generate_btn = st.form_submit_button("Generate Password 🚀")

    # Handle the generation logic after clicking the button
    if generate_btn:
        if not (use_letters or use_digits or use_symbols):
            st.error("❌ You must select at least one character type (Letters, Numbers, or Symbols)!")
        else:
            password = generate_password(length, use_letters, use_digits, use_symbols)
            if password:
                st.success("Password Generated Successfully!")
                # Display the password in a code block for easy copying
                st.code(password, language="text")

if __name__ == "__main__":
    main()