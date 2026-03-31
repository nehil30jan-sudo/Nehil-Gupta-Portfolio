import streamlit as st
from datetime import datetime, date

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="Nehil Gupta | Portfolio", 
    page_icon="📈", 
    layout="wide",
    initial_sidebar_state="expanded" # Keep expanded by default
)

# --- PHOTO FILENAME ---
PHOTO_FILENAME = "Nehil Profile Photo.jpg"

# --- 2. ADVANCED MOBILE CSS & STYLING ---
st.markdown("""
    <style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Highlight the Sidebar Toggle Arrow for Mobile */
    button[kind="headerNoContext"] {
        background-color: #1f77b4 !important;
        color: white !important;
        border-radius: 50% !important;
        width: 40px !important;
        height: 40px !important;
        position: fixed !important;
        top: 10px !important;
        left: 10px !important;
        z-index: 999999 !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3) !important;
    }

    /* Floating Mobile Menu Prompt (Only shows on mobile) */
    @media only screen and (max-width: 768px) {
        .mobile-hint {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #1f77b4;
            color: white;
            padding: 12px 20px;
            border-radius: 30px;
            font-size: 14px;
            font-weight: bold;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
            z-index: 1000;
            animation: bounce 2s infinite;
        }
    }
    @media only screen and (min-width: 769px) {
        .mobile-hint { display: none; }
    }

    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
        40% {transform: translateY(-10px);}
        60% {transform: translateY(-5px);}
    }

    /* Main Content Styles */
    .stApp { background-color: #fcfcfc; }
    .main-header { color: #1f77b4; font-size: 2.8rem; font-weight: bold; margin-bottom: 0; }
    .sub-header { color: #444; font-size: 1.6rem; margin-top: 0; margin-bottom: 20px; }
    .company-title { font-weight: bold; font-size: 1.3rem; color: #1f77b4; margin-top: 5px;}
    .edu-card { background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #eee; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);}
    .project-card-content { background-color: #f0f8ff; padding: 15px; border-radius: 10px; border-left: 5px solid #1f77b4; }
    </style>
    
    <div class="mobile-hint">📍 Tap Top-Left Arrow for Menu</div>
    """, unsafe_allow_html=True)

# --- PAGE: HOME ---
def home_page():
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    try:
        st.image(PHOTO_FILENAME, width=220) 
    except Exception:
        st.warning(f"Note: Ensure '{PHOTO_FILENAME}' is uploaded to your GitHub repository.")

    st.markdown(f"<h1 class='main-header'>Nehil Gupta</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Senior Specialist | G2 (Ex-Gartner)</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True) 
    
    st.write("---")
    st.markdown("### 👤 Professional Summary")
    st.write("""
    I am an analytical and data-driven professional with over 4 years of experience specializing in product review analytics, 
    process automation, and AI-content detection. Currently serving as a **Senior Specialist at G2**, I lead strategic 
    projects that enhance efficiency, data quality, and business outcomes. Skilled in SQL, Power BI, and Power Automate.
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
            <img src="https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white" /> 
            <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /> 
            <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
            <img src="https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white" />
            <img src="https://img.shields.io/badge/Power_Automate-0066FF?style=for-the-badge&logo=powerautomate&logoColor=white" />
        </div>
        """, unsafe_allow_html=True)

# --- PAGE: EXPERIENCE ---
def experience_page():
    st.title("💼 Professional Experience")
    with st.expander("🚀 G2 | Senior Specialist (Operations) | Feb 2026 – Present", expanded=True):
        st.markdown("<div class='company-title'>G2 · Gurugram, India</div>", unsafe_allow_html=True)
        st.write("* **Strategic Enablement:** Consultant for Sales/SLT; deliver high-impact analytics.")
        st.write("* **Project Leadership:** Manage full lifecycle of multi-stakeholder projects.")

    with st.expander("📊 Gartner (Full Tenure: 4 yrs 7 mos)"):
        with st.popover("Product Reviews Specialist | Oct 2023 – Dec 2025"):
            st.write("* Led automation projects; Won **GDM Operations Hackathon 2025**.")
        with st.popover("Product Reviews Associate | Aug 2021 – Sep 2023"):
            st.write("* Recognized as **'SQLNinja'** after winning internal SQL Bootcamp.")

# --- PAGE: PROJECTS ---
def projects_page():
    st.title("📂 Key Projects")
    with st.expander("1. 🎯 VIP Account Prioritization and Whitespacing", expanded=True):
        st.write("Developed a Weighted Scoring Model for 963 products identifying revenue white spaces.")
    with st.expander("2. 🤝 Partnership Business Development Framework"):
        st.write("Managed a $1.25M revenue target with 9% conversion via CRM-based operating models.")
    with st.expander("3. 🏆 Hackathon 2025: AI Automation"):
        st.write("Awarded 1st Place. Saved 1 hour daily and unlocked $60,000+ in revenue.")

# --- PAGE: EDUCATION ---
def education_page():
    st.title("🎓 Education Journey")
    st.markdown("<div class='edu-card'><strong>MDI, Gurgaon</strong><br>PGDM (OPGDM) | 2023 – 2025</div>", unsafe_allow_html=True)
    st.markdown("<div class='edu-card'><strong>G.D. Goenka University</strong><br>BBA, Marketing | 2018 – 2021 | ⭐ CGPA: 8.95</div>", unsafe_allow_html=True)

# --- PAGE: ACHIEVEMENTS ---
def achievements_page():
    st.title("🏆 Achievements & Awards")
    st.success("**Winner: GDM Operations Hackathon 2025** - Gartner Innovation Award")
    st.info("**IELTS Band 8.5:** Overall score")

# --- PAGE: CONTACT NOW ---
def contact_page():
    st.title("📧 Contact Now")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("#### 📱 Connect Directly")
        st.markdown("<p style='font-size:1.2rem;'>📞 +91 9821783999</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:1.2rem;'>✉️ <a href='mailto:nehil30jan@gmail.com'>nehil30jan@gmail.com</a></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:1.2rem;'>🔗 <a href='https://www.linkedin.com/in/nehilgupta/'>LinkedIn Profile</a></p>", unsafe_allow_html=True)
    with col2:
        try: st.image(PHOTO_FILENAME, width=150)
        except: pass

    st.write("---")
    st.header("✉️ Drop a Message")
    with st.container():
        name = st.text_input("Name")
        email = st.text_input("Email")
        msg = st.text_area("Message")
        req_meeting = st.radio("Request a meeting invite?", ["No", "Yes"], horizontal=True)
        
        meeting_details = ""
        if req_meeting == "Yes":
            col_date, col_time = st.columns(2)
            with col_date: m_date = st.date_input("Select Date", min_value=date.today())
            with col_time: m_time = st.time_input("Select Preferred Time")
            meeting_details = f"\n[MEETING REQUESTED: {m_date} at {m_time}]"

        if st.button("Submit Message"):
            if name and email and msg:
                st.success("Message prepared!")
                st.balloons()
                full_body = f"Name: {name}\nEmail: {email}\n\nMessage: {msg}\n{meeting_details}"
                st.markdown(f'<a href="mailto:nehil30jan@gmail.com?subject=Portfolio Message from {name}&body={full_body}" style="padding: 10px 20px; background-color: #1f77b4; color: white; border-radius: 5px; text-decoration: none; font-weight: bold;">Click to Finalize & Send</a>', unsafe_allow_html=True)

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
st.sidebar.write("✉️ [nehil30jan@gmail.com](mailto:nehil30jan@gmail.com)")
st.sidebar.write("📞 +91 9821783999")

pg.run()
