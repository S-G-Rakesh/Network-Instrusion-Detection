# Import statements
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from pathlib import Path

# Set page config FIRST - before any other st commands
st.set_page_config(
    page_title="Network Intrusion Detection",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Set paths and constants
MODEL_PATH = Path(r"Network_Intrusion_Detection.pkl")
DATA_PATH = Path(r"Network_Intrusion_Detection_Dataset.csv")
LOGO_PATH = Path(r"logo.webp")

FEATURES = [
    'Port Number', 'Received Packets', 'Received Bytes', 'Sent Bytes', 
    'Sent Packets', 'Port alive Duration (S)', 'Packets Rx Dropped',
    'Packets Tx Dropped', 'Packets Rx Errors', 'Packets Tx Errors',
    'Delta Received Packets', 'Delta Received Bytes', 'Delta Sent Bytes',
    'Delta Sent Packets', 'Delta Port alive Duration (S)',
    'Delta Packets Rx Dropped', ' Delta Packets Tx Dropped',
    'Delta Packets Rx Errors', 'Delta Packets Tx Errors',
    'Connection Point', 'Total Load/Rate', 'Total Load/Latest',
    'Unknown Load/Rate', 'Unknown Load/Latest', 'Latest bytes counter',
    'is_valid', 'Table ID', 'Active Flow Entries', 'Packets Looked Up',
    'Packets Matched', 'Max Size'
]

# Custom CSS with neon blue theme
st.markdown("""
    <style>
    /* Main background and text colors */
    .main {
        background-color: #00001a;
        color: #00ccff;
    }
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #001a33;
        color: #00ccff;
    }
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #00ccff !important;
        text-shadow: 0 0 10px #00ccff;
        font-family: 'Courier New', monospace;
    }
    /* Text elements */
    p, label, span {
        color: #99e6ff !important;
        font-family: 'Courier New', monospace;
    }
    /* Buttons */
    .stButton>button {
        background-color: #004466;
        color: #00ccff !important;
        border: 2px solid #00ccff;
        box-shadow: 0 0 10px #00ccff;
        font-family: 'Courier New', monospace;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #00ccff;
        color: #00001a !important;
        box-shadow: 0 0 20px #00ccff;
    }
    /* Input fields */
    .stNumberInput {
        background-color: #001a33 !important;
        color: #00ccff !important;
        border: 1px solid #00ccff !important;
    }
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #001a33 !important;
        color: #00ccff !important;
        border: 1px solid #00ccff !important;
    }
    /* Success/Error messages */
    .stSuccess {
        background-color: #004466 !important;
        color: #00ccff !important;
        border: 1px solid #00ccff !important;
    }
    .stError {
        background-color: #330000 !important;
        color: #ff3333 !important;
        border: 1px solid #ff3333 !important;
    }
    /* Footer */
    footer {
        color: #00ccff !important;
        border-top: 1px solid #00ccff;
        text-shadow: 0 0 5px #00ccff;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'prediction' not in st.session_state:
    st.session_state.prediction = None

# Load functions
@st.cache_resource
def load_model():
    try:
        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

@st.cache_data
def load_data():
    try:
        return pd.read_csv(DATA_PATH)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Initialize model and data
model = load_model()
df = load_data()

if model is None or df is None:
    st.error("Failed to load model or data. Please check the file paths.")
    st.stop()

# Attack types mapping
attack_types = {
    0: "🟢 LEGITIMATE NETWORK TRAFFIC",
    1: "🔴 DDoS ATTACK DETECTED",
    2: "🔴 PROTOCOL EXPLOITATION DETECTED",
    3: "🔴 RECONNAISSANCE DETECTED",
    4: "🔴 TRAFFIC MANIPULATION DETECTED",
    5: "🔴 BUFFER OVERFLOW DETECTED"
}

# Title and description
st.title("💙 Network Intrusion Detection System")
st.markdown("""
    <div style='background-color: #001a33; padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 1px solid #00ccff; box-shadow: 0 0 15px #00ccff;'>
        <p style='font-size: 1.2em; color: #00ccff; font-family: "Courier New", monospace;'>
            Welcome to the AI-powered Network Intrusion Detection System. This platform analyzes network traffic to detect potential threats in real-time.
        </p>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=100)
    st.markdown("## Navigation")
    page = st.selectbox("Choose a page", ["Attack Detection", "Detection Result"])
    st.markdown("---")
    st.markdown("### System Statistics")
    col1, col2 = st.columns(2)
    col1.metric("Total Records", len(df))
    col2.metric("Attack Types", len(attack_types))

if page == "Attack Detection":
    st.header("🔍 Network Attack Detection")
    with st.expander("ℹ️ How to use the detection form", expanded=False):
        st.markdown("""
            1. Enter your network traffic parameters below.
            2. Click 'Detect Attack' to analyze traffic.
            3. View results in the 'Detection Result' page.
        """)

    col1, col2, col3 = st.columns(3)
    input_data = {}
    for i, feature in enumerate(FEATURES):
        with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3:
            input_data[feature] = st.number_input(
                f"{feature}",
                value=float(df[feature].mean()),
                help=f"Average value: {df[feature].mean():.2f}"
            )

    if st.button("🔍 Detect Attack", use_container_width=True):
        with st.spinner('Analyzing network traffic...'):
            input_df = pd.DataFrame([input_data])[FEATURES]
            try:
                st.session_state.prediction = model.predict(input_df)[0]
                st.success("Detection complete! View result in the 'Detection Result' page.")
            except Exception as e:
                st.error(f"Error in attack detection: {e}")

elif page == "Detection Result":
    st.header("🎯 Detection Result")
    if st.session_state.prediction is not None:
        result = attack_types[st.session_state.prediction]
        is_legitimate = st.session_state.prediction == 0

        st.markdown(
            f"""
            <div style='text-align: center; padding: 50px; 
                        background-color: {'#00264d' if is_legitimate else '#330000'}; 
                        border: 2px solid {'#00ccff' if is_legitimate else '#ff3333'}; 
                        border-radius: 10px; margin: 20px 0; color: {'#00ccff' if is_legitimate else '#ff3333'};
                        box-shadow: 0 0 20px {'#00ccff' if is_legitimate else '#ff3333'};'>
                <h1 style='font-size: 2.5em; font-family: "Courier New", monospace;'>{result}</h1>
                <p style='font-size: 1.2em; margin-top: 20px; font-family: "Courier New", monospace;'>
                    {'Your network traffic appears normal.' if is_legitimate else 'Potential security threat detected!'}
                </p>
            </div>
            """, 
            unsafe_allow_html=True
        )

        if not is_legitimate:
            st.markdown("""
                <div style='background-color: #001a33; padding: 20px; border-radius: 10px; border: 1px solid #ff3333; box-shadow: 0 0 10px #ff3333;'>
                    <h3 style='color: #ff3333; text-shadow: 0 0 5px #ff3333;'>🚨 Recommended Actions:</h3>
                    <ol style='color: #ff6666; font-family: "Courier New", monospace;'>
                        <li>Isolate affected systems.</li>
                        <li>Review security logs.</li>
                        <li>Update firewall rules.</li>
                        <li>Contact the security team.</li>
                    </ol>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No detection results yet. Please go to the 'Attack Detection' page to analyze network traffic.")

# Enhanced footer with blue neon theme
st.markdown("---")
st.markdown("""
    <div style='text-align: center; padding: 20px; background-color: #001a33; border-top: 2px solid #00ccff; box-shadow: 0 -5px 15px #00ccff;'>
        <h4 style='color: #00ccff; text-shadow: 0 0 10px #00ccff; font-family: "Courier New", monospace;'>Network Intrusion Detection System</h4>
        <p style='color: #00ccff; font-family: "Courier New", monospace;'>Powered by AI & Machine Learning • Built with Streamlit</p>
        <p style='color: #00ccff; font-size: 0.8em; margin-top: 10px; font-family: "Courier New", monospace;'>
            © 2024 Security Operations Center
        </p>
    </div>
""", unsafe_allow_html=True)
