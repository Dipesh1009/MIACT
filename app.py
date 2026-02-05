import streamlit as st

# ---------- Page Config ----------
st.set_page_config(
    page_title="MIACT – Prototype",
    layout="wide"
)

# ---------- Sidebar ----------
with st.sidebar:
    st.title("History")
    st.markdown("---")
    
    st.button("Search 1: iPhone 15")
    st.button("Search 2: Samsung S23")
    st.button("Search 3: Pixel 8")

    st.markdown("---")
    st.subheader("Quick Toggles")
    show_facts = st.checkbox("Show Facts", value=True)
    show_opinions = st.checkbox("Show Opinions", value=True)
    show_conflicts = st.checkbox("Show Conflicts", value=True)

    st.markdown("---")
    st.button("⚙ Settings")

# ---------- Main Content ----------
st.markdown("## Multi-source Information Aggregation & Comparison Tool (MIACT)")

# Search Bar
query = st.text_input("Enter product / topic", placeholder="e.g. iPhone 15")

st.markdown("---")

# ---------- Central Info Card ----------
with st.container():
    st.subheader("Info Through Tables")

    st.markdown("""
    ***Brief about the products


    *** 
    """)

# ---------- Modes Section ----------
st.markdown("---")
st.subheader("Modes")

tabs = st.tabs(["Objective Facts", "Conflicts", "Opinions"])

# ---------- Tab 1: Objective Facts ----------
with tabs[0]:
    st.markdown("### Objective Attributes (Mock Data)")
    st.table({
        "Attribute": ["Battery", "Display", "Price"],
        "Source A": ["4500 mAh", "6.1 inch", "₹79,999"],
        "Source B": ["4500 mAh", "6.1 inch", "₹80,499"],
        "Agreed": ["Yes", "Yes", "No"]
    })

# ---------- Tab 2: Conflicts ----------
with tabs[1]:
    st.markdown("### Conflicting Information")
    st.warning("Price information differs across sources")

# ---------- Tab 3: Opinions ----------
with tabs[2]:
    st.markdown("### Opinion Summary")
    st.metric(label="Overall Sentiment", value="Positive", delta="+0.63")

    st.markdown("""
    **Common Opinions**
    - Battery performance is good  
    - Camera quality is excellent  
    - Price is considered high  
    """)

# ---------- Footer ----------
st.markdown("---")
st.caption("Prototype UI – Data shown is illustrative only")
