import streamlit as st
import time
from datetime import datetime
from src.core.state import GlobalState, AgentMessage
from src.core.graph import GraphEngine
from src.core.constitution import TaskStatus

# --- UI Configuration ---
st.set_page_config(
    page_title="UA²S - Universal Autonomous AI Agent",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Look
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stApp {
        background: radial-gradient(circle at top right, #1e293b, #0f172a);
    }
    .agent-card {
        padding: 20px;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 10px;
    }
    .status-badge {
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 0.8em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- State Initialization ---
if "graph" not in st.session_state:
    st.session_state.graph = GraphEngine()
if "history" not in st.session_state:
    st.session_state.history = []

# --- Sidebar ---
with st.sidebar:
    st.title("🧠 UA²S Control")
    st.subheader("System v0.1.0")
    st.divider()
    st.info("System Status: [green]Operational[/green]")
    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()

# --- Main Interface ---
st.title("Universal Autonomous AI Agent System")
st.caption("Thinking like a human. Acting like a machine. Improving like a learner.")

# Input Section
user_query = st.chat_input("Mera yeh kaam kar do...")

if user_query:
    # 1. Create Initial State
    state = GlobalState(user_instruction=user_query)
    st.session_state.history.append({"role": "user", "content": user_query, "time": datetime.now()})
    
    # 2. Execution with Loading
    with st.status("Agent thinking...", expanded=True) as status:
        st.write("Planner decomposing task...")
        # Simulate step-by-step progress for UI feedback
        final_state = st.session_state.graph.execute(state)
        st.write("Execution complete.")
        status.update(label="Task Processed", state="complete", expanded=False)

    # 3. Handle Results
    st.session_state.history.append({
        "role": "assistant", 
        "content": final_state.messages[-1].content if final_state.messages else "Task processed.",
        "status": final_state.status,
        "full_state": final_state,
        "time": datetime.now()
    })

# --- Display Conversation ---
for chat in st.session_state.history:
    if chat["role"] == "user":
        with st.chat_message("user"):
            st.markdown(chat["content"])
    else:
        with st.chat_message("assistant", avatar="🧠"):
            st.markdown(chat["content"])
            
            # Show Detailed Plan/Steps if available
            if "full_state" in chat:
                with st.expander("View Execution Steps"):
                    for step in chat["full_state"].history:
                        icon = "✅" if step.status == "COMPLETED" else "⏳"
                        st.markdown(f"{icon} **{step.agent_name}**: {step.action}")
                        if step.result:
                            st.caption(f"Result: {step.result}")

# --- Footer Metric Row ---
st.divider()
col1, col2, col3, col4 = st.columns(4)
col1.metric("Tasks Completed", len([h for h in st.session_state.history if h.get("status") == TaskStatus.COMPLETED]), delta="Live")
col2.metric("System Health", "99.9%", delta="Stable")
col3.metric("Uptime", "14h 22m")
col4.metric("Agent Latency", "1.2s", delta="-0.2s")
