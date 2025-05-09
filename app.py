import streamlit as st

# Config
st.set_page_config(
    page_title="LLM Tokenization Demo", 
    page_icon="🧠",
    layout="centered"
)

# Header with theme
st.title("Hybrid Tokenization Strategies in LLMs")
st.markdown("""
*"AI isn’t magic, it’s math + data + smart processing."*  
**Demo Goal**: Show how tokenization impacts regression accuracy.
""")

# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": """
👋 Hi! I'm your LLM tokenization demo bot. I know basics now, but in 5 weeks...  
**What we'll discover together**:  
1. How hybrid tokenization reduces decoding errors  
2. The math behind regression accuracy  
3. Your innovative ideas!  

Try asking:  
- "What's the hardest part of tokenization?"  
- "How could we improve this?"  
- "Show me a math example"  
"""}
    ]

# Knowledge base with humble responses
KNOWLEDGE = {
    "tokenization": """
**Current Understanding**:  
Tokenization splits text into units (tokens).  

**5-Week Potential**:  
We'll test if hybrid approaches (BPE + characters) reduce outliers in regression tasks.
""",
    "math": """
**Current Math**:  
Basic linear algebra for embeddings.  

**Future Exploration**:  
- Gradient stability in loss functions  
- Probability distributions for decoding  
*What math would you want to implement?*  
""",
    "improve": """
🤔 **Great question! Right now I don't know - but here's how we could find out**:  
1. Collect tokenization error cases (Week 2)  
2. Analyze regression outliers (Week 3)  
3. Prototype hybrid strategies (Week 5)  

*What variables would you track?*  
""",
    "hardest": """
❗ **Current Challenge**:  
Balancing token granularity vs. computational cost.  

💡 **Your 5-Week Mission**:  
Find the sweet spot using:  
- Entropy measurements  
- Error rate analysis  
""",
    "don't know": """
🧠 **Admission**: I don't have that answer yet... but here's how WE will solve it:  
1. Identify the knowledge gap (Week 1)  
2. Research papers + datasets (Week 2-3)  
3. Build/test solutions (Week 4-5)  

*What hypothesis would you test?*  
"""
}

# Dynamic response generator
def generate_response(user_input: str) -> str:
    user_input_lower = user_input.lower()
    
    # Direct matches
    for keyword, response in KNOWLEDGE.items():
        if keyword in user_input_lower:
            return response
    
    # Catch-alls for unknown questions
    if any(w in user_input_lower for w in ["how", "why", "what if"]):
        return KNOWLEDGE["don't know"]
    if any(w in user_input_lower for w in ["better", "improve", "enhance"]):
        return KNOWLEDGE["improve"]
    
    return """🔮 Interesting question! While I can't answer this yet, in 5 weeks we might:  
- Develop new evaluation metrics  
- Create visualization tools  
- Discover unexpected patterns  

*Where would you start investigating?*  
"""

# Chat UI
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_input := st.chat_input("Ask about tokenization..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    bot_response = generate_response(user_input)
    
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.write(bot_response)

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("""
**Pedagogical Strategy**:  
1. Admit knowledge limits  
2. Model problem-solving  
3. Invite co-creation  
""")
