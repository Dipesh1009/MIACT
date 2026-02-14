import streamlit as st
from bs4 import BeautifulSoup
from scraper import get_oneplus9_specs

st.set_page_config(
    page_title="MIACTool",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- SESSION STATE ----------
if "screen" not in st.session_state:
    st.session_state.screen = "home"

if "query" not in st.session_state:
    st.session_state.query = ""

# ---------- RESULT FUNCTION ----------
def show_result_card():

    specs = get_oneplus9_specs()

    mrp = specs.get("MRP", "Not Found")
    performance = specs.get("Performance", "Not Found")

    st.markdown(f"""
<div class="result-wrapper">
    <div class="result-card">
        <h2 class="phone-title">OnePlus 9</h2>

        <div class="spec-row">
            <div class="spec-label">MRP</div>
            <div class="spec-value">{mrp}</div>
        </div>

        <div class="spec-row">
            <div class="spec-label">Performance</div>
            <div class="spec-value">{performance}</div>
        </div>

        <h3 class="public-heading">Public Opinion</h3>
        <p class="public-text">
        Live scraped data loaded successfully.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)


# Load CSS
def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Sidebar
with st.sidebar:
    st.markdown("## History")
    st.markdown("**Current Chat**")
    st.markdown("Previous Topic")

# ---------- UI LOGIC ----------
if st.session_state.screen == "home":

    st.markdown("""
    <div class="center-container">
        <h1 class="welcome-text">Welcome, Seeker.</h1>
    </div>
    """, unsafe_allow_html=True)

    query = st.text_input(
        "Search",
        placeholder="Please enter a topic",
        label_visibility="collapsed"
    )

    if query:
        st.session_state.query = query
        st.session_state.screen = "result"
        st.rerun()

elif st.session_state.screen == "result":

    show_result_card()

    if st.button("⬅ Back"):
        st.session_state.screen = "home"
        st.rerun()
