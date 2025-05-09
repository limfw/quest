import streamlit as st

# Config
st.set_page_config(
    page_title="LLM Tokenization Lab", 
    page_icon="🔍",
    layout="centered"
)

# Header with interactive elements
st.title("🔬 Tokenization Research Lab")
with st.expander("About this demo"):
    st.markdown("""
    *"AI isn’t magic, it’s math + data + smart processing."*  
    **Pedagogical Approach**:  
    - Week 1-2: Identify knowledge gaps  
    - Week 3-4: Prototype solutions  
    - Week 5: Implement enhancements  
    """)

# Initialize with growth mindset
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": """
👋 Welcome to our 5-week research journey! I'm your baseline bot with limited knowledge.  

**Try asking**:  
- "What makes tokenization hard?"  
- "How could math help?"  
- Any technical question (I'll show how we'll solve it!)  
"""}
    ]

# Knowledge base with YOUR preferred response style
RESPONSE_TEMPLATES = {
    "known": {
        "tokenization": """
🧩 **Current Knowledge**:  
Tokenization breaks text into meaningful units (tokens).  

🚀 **Our 5-Week Target**:  
Hybrid approaches to reduce decoding errors by {}%  
*What measurement approach would you use?*  
""",
        "math": """
📐 **Current Tools**:  
Basic linear algebra for embeddings.  

🔮 **Future Exploration**:  
- Gradient stability analysis  
- Probability distributions for outlier detection  
*Which math concept excites you most?*  
"""
    },
    "unknown": """
🔍 Interesting question! While I can't answer this yet...  

💡 **How we'll tackle it**:  
1. Week 1: Define the problem  
2. Week 2-3: Research existing solutions  
3. Week 4-5: Test our own approach  

Do you have any initial ideas how to improve this? We'll discuss it over our 5-week activity!  
"""
}

# Smart response generator
def generate_response(user_input: str) -> str:
    user_input_lower = user_input.lower()
    
    # Known topics
    if "tokeniz" in user_input_lower:
        return RESPONSE_TEMPLATES["known"]["tokenization"].format("X")  # Placeholder for student input
    
    if any(w in user_input_lower for w in ["math", "algebra", "probability"]):
        return RESPONSE_TEMPLATES["known"]["math"]
    
    # Unknown topics - YOUR PREFERRED STYLE
    return RESPONSE_TEMPLATES["unknown"].format(user_input)

# Chat UI
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_input := st.chat_input("Ask a technical question..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    # Generate and display response
    bot_response = generate_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.write(bot_response)

    # Auto-prompt for brainstorming
    if "unknown" in bot_response:
        st.session_state.messages.append({
            "role": "assistant", 
            "content": "💬 *Quick brainstorming*: Jot down one idea you'd want to explore first:"
        })
        with st.chat_message("assistant"):
            st.text_input("My initial idea...", key="brainstorm")

# Progress tracker
st.sidebar.markdown("### Research Milestones")
st.sidebar.progress(0.2)
st.sidebar.caption("Week 1: Knowledge Mapping")
