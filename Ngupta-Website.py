import streamlit as st
from datetime import datetime, date

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="Nehil Gupta | Portfolio", 
    page_icon="📈", 
    layout="wide",
    initial_sidebar_state="collapsed" # Better for mobile Safari
)

# --- PHOTO FILENAME ---
PHOTO_FILENAME = "Nehil Profile Photo.jpg"

# --- 2. ADVANCED CSS: MOBILE TOGGLE & NAVIGATION ---
st.markdown("""
    <style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Make the default arrow black and more visible just in case */
    button[kind="headerNoContext"] {
        color: black !important;
        background-color: #f0f2f6 !important;
        border: 1px solid #ddd !important;
        left: 10px !important;
        top: 10px !important;
    }

    /* CUSTOM MOBILE NAVIGATION BUTTON */
    @media only screen and (max-width: 768px) {
        .mobile-nav-trigger {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background-color: black;
            color: white;
            padding: 12px 24px;
            border-radius: 50px;
            font-size: 14px;
            font-weight: bold;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
            z-index: 9999;
            text-align: center;
            border: 2px solid #1f77b4;
        }
    }
    @media only screen and (min-width: 769px) {
        .mobile-nav-trigger { display: none; }
    }

    /* Original Detailed Styles */
    .stApp { background-color: #fcfcfc; }
    .main-header { color: #1f77b4; font-size: 2.8rem; font-weight: bold; margin-bottom: 0; }
    .sub-header { color: #444; font-size: 1.6rem; margin-top: 0; margin-bottom: 20px; }
    .company-title { font-weight: bold; font-size: 1.3rem; color: #1f77b4; margin-top: 5px;}
    .edu-card { background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #eee; margin-bottom: 15px;}
    .project-card-content { background-color: #f0f8ff; padding: 15px; border-radius: 10px; border-left: 5px solid #1f77b4; }
    </style>
    
    <div class="mobile-nav-trigger">📱 Use Menu in Sidebar</div>
    """, unsafe_allow_html=True)

# --- HELPER: MOBILE MENU OVERLAY ---
def mobile_menu_helper():
    # This creates an easy-access menu at the top of every page for mobile users
    if st.container():
        with st.expander("🚀 QUICK NAVIGATION MENU", expanded=False):
            st.write("Click a button below to jump to that section:")
            col1, col2 = st.columns(2)
            # Note: These are manual anchors since st.navigation handles the main routing
            st.caption("Please use the sidebar (top-left arrow) for full navigation.")

# --- PAGE: HOME ---
def home_page():
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    try:
        st.image(PHOTO_FILENAME, width=220) 
    except Exception:
        st.warning(f"Note: Ensure '{PHOTO_FILENAME}' is uploaded to your GitHub.")

    st.markdown(f"<h1 class='main-header'>Nehil Gupta</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Senior Specialist | G2 (Ex-Gartner)</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True) 
    
    st.write("---")
    st.markdown("### 👤 Professional Summary")
    st.write("""
    I am an analytical and data-driven professional with over 4 years of experience specializing in product review analytics, 
    process automation, and AI-content detection. Currently serving as a **Senior Specialist at G2**, I lead strategic 
    projects that enhance efficiency, data quality, and business outcomes.
    """)

    st.write("---")
    st.markdown("### 🎯 Core Expertise")
    st.write("🔍 **Secondary Research & Market Positioning**")
    st.write("📊 **Data Analysis & Insight Generation**")
    st.write("📈 **Sales Operations & Enablement**")
    st.write("⚙️ **Process Automation (AI/Lean Management)**")

    st.write("---")
    st.header("🛠️ Tools & Technologies")
    st.markdown("""
        <div style="text-align: left; line-height: 2.5;">
            <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=microsoftpowerbi&logoColor=black" /> 
            <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" /> 
            <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> 
            <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
            <img src="https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white" />
        </div>
        """, unsafe_allow_html=True)

# --- PAGE: PROJECTS ---
def projects_page():
    st.title("📂 Key Projects")
    with st.expander("1. 🎯 VIP Account Prioritization and Whitespacing", expanded=True):
        st.markdown("""<div class='project-card-content'>
            <p><strong>Objective:</strong> Build a data-driven vendor prioritization framework to rank 963 products and identify revenue 'white spaces'.</p>
            <p><strong>Impact:</strong> Delivered interactive dashboards for sales support, provided 665 POCs for High-priority products.</p>
        </div>""", unsafe_allow_html=True)

    with st.expander("2. 🤝 Partnership Business Development Framework"):
        st.markdown("""<div class='project-card-content'>
            <p><strong>Impact:</strong> Managed a $1.25M revenue target with a 9% conversion rate. Provided 139 high-intent leads.</p>
        </div>""", unsafe_allow_html=True)

# --- PAGE: EXPERIENCE ---
def experience_page():
    st.title("💼 Professional Experience")
    with st.expander("🚀 G2 | Senior Specialist (Operations) | Feb 2026 – Present", expanded=True):
        st.markdown("<div class='company-title'>G2 · Gurugram, India</div>", unsafe_allow_html=True)
        st.write("* **Strategic Enablement:** Consultant for Sales, Partnerships, and Advisory teams.")

    with st.expander("📊 Gartner (Full Tenure: 4 yrs 7 mos)"):
        with st.popover("Product Reviews Specialist | Oct 2023 – Dec 2025"):
            st.write("* Led automation projects; Won **GDM Operations Hackathon 2025**.")
        with st.popover("Product Reviews Associate | Aug 2021 – Sep 2023"):
            st.write("* Recognized as **'SQLNinja'** after winning internal SQL Bootcamp.")

# --- PAGE: EDUCATION ---
def education_page():
    st.title("🎓 Education Journey")
    st.markdown("<div class='edu-card'><strong>MDI, Gurgaon</strong><br>PGDM (OPGDM) | 2023 – 2025</div>", unsafe_allow_html=True)
    st.markdown("<div class='edu-card'><strong>G.D. Goenka University</strong><br>BBA, Marketing | 2018 – 2021 | ⭐ CGPA: 8.95</div>", unsafe_allow_html=True)

# --- PAGE: ACHIEVEMENTS ---
def achievements_page():
    st.title("🏆 Achievements & Awards")
    st.success("**GDM Operations Hackathon 2025 Winner** - Gartner")
    st.success("**Best Associate 2022** - Gartner (Internal Team Award)")

# --- PAGE: CONTACT NOW ---
def contact_page():
    st.title("📧 Contact Now")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<p style='font-size:1.2rem;'>📞 +91 9821783999</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:1.2rem;'>✉️ <a href='mailto:nehil30jan@gmail.com'>nehil30jan@gmail.com</a></p>", unsafe_allow_html=True)
    with col2:
        try: st.image(PHOTO_FILENAME, width=150)
        except: pass
    
    st.write("---")
    st.header("✉️ Drop a Message")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        msg = st.text_area("Message")
        submitted = st.form_submit_button("Submit Message")
        if submitted:
            if name and email and msg:
                st.success("Redirecting to email...")
                full_body = f"Name: {name}\nEmail: {email}\n\nMessage: {msg}"
                st.markdown(f'<a href="mailto:nehil30jan@gmail.com?subject=Portfolio Message&body={full_body}" target="_blank" style="padding: 10px; background: black; color: white; border-radius: 5px; text-decoration: none;">Click to Send Email</a>', unsafe_allow_html=True)

# --- NAVIGATION ---
pg = st.navigation([
    st.Page(home_page, title="Home", icon="🏠"),
    st.Page(experience_page, title="Experience", icon="💼"),
    st.Page(projects_page, title="Projects", icon="📂"),
    st.Page(education_page, title="Education", icon="🎓"),
    st.Page(achievements_page, title="Achievements", icon="🏆"),
    st.Page(contact_page, title="Contact Now", icon="📧"),
])

# --- SIDEBAR ---
st.sidebar.markdown("### Quick Connect")
st.sidebar.write("✉️ nehil30jan@gmail.com")
st.sidebar.write("📞 +91 9821783999")

pg.run()
