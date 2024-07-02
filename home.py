import streamlit as st
from st_pages import Page,show_pages

if 'is_trending' not in st.session_state:
    st.session_state['is_trending'] = False
st.set_page_config(
        page_title="E-Commerce clicks track/Truck real time tracking",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
        }
    )


side_bar = st.sidebar

show_pages(
    [
        Page("home.py", "Home", "🏠"),
        Page("pages/ecommerce.py", "Ecommerce clicks", "🧺"),
        Page("pages/analysis.py", "Analysis", "📊"),
    ]
)