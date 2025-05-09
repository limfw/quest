import streamlit as st

# Config
st.set_page_config(
    page_title="LLM Tokenization Demo", 
    page_icon="🧠",
    layout="centered"
)

# Header with your theme and project title
st.title("Hybrid Tokenization Strategies in LLMs")
st.markdown("""
*"AI isn’t magic, it’s math + data + smart processing."*  
**Demo Goal**: Show how tokenization impacts regression accuracy in decoding tasks.
""")

# Initialize chat with educational prompt
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": """
👋 Hi! I'm a demo for your **LLM tokenization project**. Ask me:  
- "What is tokenization?"  
- "How does math improve LLMs?"  
- "What’s hybrid tokenization?"  
- Or type "bye" to exit.
"""}
    ]

# Reset chat button
if st.sidebar.button("♻️ Reset Chat", help="Start a new conversation"):
    st.session_state.messages = [
        {"role": "assistant", "content": "🔄 Chat reset! Ask about tokenization, math in AI, or your project."}
    ]
    st.rerun()

# Display chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Knowledge base (customize with your research)
KNOWLEDGE = {
    "tokenization": """
**Tokenization** splits text into units (tokens) for LLMs. Your project explores:  
- **Hybrid Strategies**: Mixing subword + character-level tokens.  
- **Regression Impact**: Better tokenization → Fewer decoding errors → Higher accuracy.  
""",
    "math": """
**Math in LLMs**:  
1. **Linear Algebra**: Embeddings = Vectors  
2. **Probability**: Next-token prediction  
3. **Optimization**: Loss minimization (e.g., cross-entropy)  
""",
    "hybrid": """
**Hybrid Tokenization** (Your Focus):  
- Combines strengths of subword (BPE) + character-level methods.  
- **Goal**: Reduce outliers in regression tasks during decoding.  
- **Math Link**: Improves gradient stability in loss functions.  
""",
    "bye": "🌟 Goodbye! Remember: AI = Math + Data + Smart Processing. Keep coding!",
    "hi": "🧠 Hello! Let’s discuss tokenization and math in LLMs."
}

# User input
if user_input := st.chat_input("Ask about tokenization or math..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Generate response
    user_input_lower = user_input.lower()
    bot_response = None

    # Check greetings/bye
    if any(word in user_input_lower for word in ["hi", "hello"]):
        bot_response = KNOWLEDGE["hi"]
    elif any(word in user_input_lower for word in ["bye", "goodbye"]):
        bot_response = KNOWLEDGE["bye"]
    else:
        # Check knowledge base
        for keyword, answer in KNOWLEDGE.items():
            if keyword in user_input_lower:
                bot_response = answer
                break
    
    # Default response
    if not bot_response:
        bot_response = "💡 Try asking about: tokenization, math in AI, or hybrid methods."

    # Add bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.write(bot_response)

# Footer with your theme
st.sidebar.markdown("---")
st.sidebar.caption("""
**Theme**: AI = Math + Data + Smart Processing  
**Project**: Hybrid Tokenization for LLM Regression Accuracy  
""")
