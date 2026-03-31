import streamlit as st
from datetime import datetime, date

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="Nehil Gupta | Portfolio", 
    page_icon="📈", 
    layout="wide",
    initial_sidebar_state="collapsed" # We'll use our own mobile nav
)

# --- PHOTO FILENAME ---
PHOTO_FILENAME = "Nehil Profile Photo.jpg"

# --- 2. CUSTOM CSS & MOBILE NAV ---
st.markdown("""
    <style>
    /* Hide Default Streamlit Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global Styles */
    .stApp { background-color: #fcfcfc; }
    .main-header { color: #1f77b4; font-size: 2.8rem; font-weight: bold; margin-bottom: 0; }
    .company-title { font-weight: bold; font-size: 1.3rem; color: #1f77b4; margin-top: 5px;}
    .edu-card { background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #eee; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);}
    .project-card-content { background-color: #f0f8ff; padding: 15px; border-radius: 10px; border-left: 5px solid #1f77b4; }
    
    /* Desktop Sidebar adjustment */
    [data-testid="stSidebar"] { min-width: 250px; }

    /* Mobile Navigation Bar */
    @media only screen and (max-width: 768px) {
        .mobile-nav {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #ffffff;
            border-bottom: 1px solid #ddd;
            padding: 10px;
            z-index: 9999;
            text-align: center;
        }
        .main-content { padding-top: 50px; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. MOBILE MENU WORKAROUND ---
# Since we can't force the sidebar open with a button, we create a top-bar 
# for mobile users to navigate easily.
if 'page' not in st.session_state:
    st.session_state.page = "Home"

def set_page(page_name):
    st.session_state.page = page_name

# Mobile Top Menu (Visible only on small screens)
st.markdown('<div class="mobile-nav">', unsafe_allow_html=True)
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    if st.button("🏠 Home"): set_page("Home")
with col_m2:
    if st.button("💼 Experience"): set_page("Experience")
with col_m3:
    if st.button("📂 Projects"): set_page("Projects")
st.markdown('</div><div class="main-content"></div>', unsafe_allow_html=True)

# --- PAGE: HOME ---
def home_page():
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    try: st.image(PHOTO_FILENAME, width=220) 
    except: st.warning("Photo not found.")
    st.markdown(f"<h1 class='main-header'>Nehil Gupta</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Senior Specialist | G2 (Ex-Gartner)</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True) 
    st.write("---")
    st.markdown("### 👤 Professional Summary")
    st.write("Analytical and data-driven professional with over 4 years of experience at Gartner/G2 specializing in product review analytics, process automation, and AI-content detection.")
    st.markdown("### 🎯 Core Expertise")
    st.write("🔍 Secondary Research | 📊 Data Analysis | 📈 Sales Operations | ⚙️ Process Automation")
    st.header("🛠️ Tools & Technologies")
    st.markdown('<img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=microsoftpowerbi&logoColor=black" /> <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" />', unsafe_allow_html=True)

# --- PAGE: PROJECTS ---
def projects_page():
    st.title("📂 Key Projects")
    with st.expander("1. 🎯 VIP Account Prioritization and Whitespacing", expanded=True):
        st.markdown("<div class='project-card-content'><p><strong>Objective:</strong> Rank 963 products and identify revenue 'white spaces'. Analyze 13 factors across 5 categories.</p><p><strong>Impact:</strong> Identified 102 new category opportunities via AI and secondary research.</p></div>", unsafe_allow_html=True)
    with st.expander("2. 🤝 Partnership Business Development Framework"):
        st.markdown("<div class='project-card-content'><p><strong>Impact:</strong> Managed a $1.25M revenue target with 9% conversion. Provided 139 high-intent leads.</p></div>", unsafe_allow_html=True)
    with st.expander("3. 🏆 GDM Hackathon: AI-Driven Automation (Winner)"):
        st.markdown("<div class='project-card-content'><p><strong>Impact:</strong> Saved 1 hour of manual work daily and unlocked an estimated $60,000+ in untapped annual revenue.</p></div>", unsafe_allow_html=True)

# --- PAGE: EXPERIENCE ---
def experience_page():
    st.title("💼 Professional Experience")
    with st.expander("🚀 G2 | Senior Specialist | Feb 2026 – Present", expanded=True):
        st.write("* Consultant for Sales/SLT; deliver high-impact analytics to drive revenue.")
    with st.expander("📊 Gartner (Full Tenure: 4 yrs 7 mos)"):
        with st.popover("Product Reviews Specialist"):
            st.write("* Won Hackathon 2025; Led AI-content detection guidelines (95% ambiguity reduction).")
        with st.popover("Product Reviews Associate"):
            st.write("* 'SQLNinja' winner; Developed Disablement Menu (3x efficiency improvement).")

# --- PAGE: EDUCATION ---
def education_page():
    st.title("🎓 Education")
    st.markdown("<div class='edu-card'><strong>MDI, Gurgaon</strong><br>PGDM (OPGDM) | 2023 – 2025</div>", unsafe_allow_html=True)
    st.markdown("<div class='edu-card'><strong>G.D. Goenka University</strong><br>BBA | 8.95 CGPA | 100% Scholarship</div>", unsafe_allow_html=True)

# --- PAGE: ACHIEVEMENTS ---
def achievements_page():
    st.title("🏆 Achievements")
    st.success("**Winner: GDM Operations Hackathon 2025**")
    st.success("**Best Associate 2022** - Gartner")
    st.info("**IELTS Band 8.5**")

# --- PAGE: CONTACT ---
def contact_page():
    st.title("📧 Contact Now")
    st.write("📞 +91 9821783999")
    st.write("✉️ nehil30jan@gmail.com")
    st.write("---")
    st.header("✉️ Drop a Message")
    name = st.text_input("Name")
    msg = st.text_area("Message")
    if st.button("Submit Message"):
        st.success("Ready! Click the email link generated below.")
        st.markdown(f'<a href="mailto:nehil30jan@gmail.com?body={msg}">Finalize Email</a>', unsafe_allow_html=True)

# --- SHARED SIDEBAR (For Desktop) ---
st.sidebar.title("Navigation")
if st.sidebar.button("🏠 Home", key="d1"): set_page("Home")
if st.sidebar.button("💼 Experience", key="d2"): set_page("Experience")
if st.sidebar.button("📂 Projects", key="d3"): set_page("Projects")
if st.sidebar.button("🎓 Education", key="d4"): set_page("Education")
if st.sidebar.button("🏆 Achievements", key="d5"): set_page("Achievements")
if st.sidebar.button("📧 Contact", key="d6"): set_page("Contact")

# --- LOGIC TO DISPLAY PAGES ---
if st.session_state.page == "Home": home_page()
elif st.session_state.page == "Experience": experience_page()
elif st.session_state.page == "Projects": projects_page()
elif st.session_state.page == "Education": education_page()
elif st.session_state.page == "Achievements": achievements_page()
elif st.session_state.page == "Contact": contact_page()
