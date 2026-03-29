import streamlit as st
from auth import signup_user, login_user
from utils import generate_content, generate_pdf
from db import content_col

st.set_page_config(page_title="ScriptCraft AI")

if "user" not in st.session_state:
    st.session_state.user = None

st.title("🎬 ScriptCraft AI")

# AUTH
if not st.session_state.user:
    option = st.selectbox("Login / Signup", ["Login", "Signup"])

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if option == "Signup":
        name = st.text_input("Name")
        if st.button("Signup"):
            st.success(signup_user(name, email, password))

    if option == "Login":
        if st.button("Login"):
            user = login_user(email, password)
            if user:
                st.session_state.user = user
                st.success("Logged in")
            else:
                st.error("Invalid credentials")

# MAIN
else:
    st.sidebar.write(f"Welcome {st.session_state.user['name']}")

    content_type = st.selectbox(
        "Content Type",
        ["Instagram Reel", "YouTube Script", "Podcast QnA"]
    )

    topic = st.text_input("Topic")

    tone = st.selectbox(
        "Tone",
        ["Casual", "Professional", "Funny", "Motivational"]
    )

    audience = st.selectbox(
        "Audience",
        ["Students", "Professionals", "Creators"]
    )

    if st.button("Generate"):
        result = generate_content(content_type, topic, tone, audience)

        st.write(result)

        content_col.insert_one({
            "user": st.session_state.user["email"],
            "type": content_type,
            "topic": topic,
            "content": result
        })

        pdf_file = generate_pdf(result)
        with open(pdf_file, "rb") as f:
            st.download_button("Download PDF", f, "script.pdf")

    st.subheader("📜 Your Content")

    data = content_col.find({"user": st.session_state.user["email"]})

    for item in data:
        st.write(f"*{item['type']} - {item['topic']}*")
        st.write(item["content"])
        st.write("---")