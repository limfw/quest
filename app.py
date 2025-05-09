import streamlit as st

# Set page config
st.set_page_config(page_title="QUEST Chatbot Demo", page_icon="🌱")

# Title with teaching caption
st.title("From 5-Week QUEST to AI Assistant")
st.caption("Can you build a better app after 5 weeks and enhance it with math knowledge you learn? 🚀")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your QUEST demo bot. Ask me about: 'What is QUEST?', 'How to deploy a bot?', or 'What can you do?'"}
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Document-based answers (your template)
DOC_KNOWLEDGE = {
    "what is quest": "QUEST is a 5-week activity where students build chatbots. Week 1-2: Basics, Week 3-4: APIs, Week 5: Advanced features!",
    "how to deploy a bot": "1. Write code (like this demo), 2. Push to GitHub, 3. Deploy on Streamlit Cloud. Takes 5 minutes!",
    "what can you do": "Right now, I answer simple Qs. But in 5 weeks, I could solve math problems or analyze data!"
}

# User input
if user_input := st.chat_input("Ask about QUEST..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Check document knowledge first
    user_input_lower = user_input.lower()
    bot_response = None

    for keyword, answer in DOC_KNOWLEDGE.items():
        if keyword in user_input_lower:
            bot_response = answer
            break

    # Default response if no keyword matched
    if not bot_response:
        bot_response = "Great question! Soon, I'll use APIs to answer complex queries. For now, ask about QUEST, deployment, or my capabilities."

    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.write(bot_response)
