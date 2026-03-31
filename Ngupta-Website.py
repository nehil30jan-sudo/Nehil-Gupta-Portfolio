import streamlit as st
from datetime import datetime, date

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="Nehil Gupta | Portfolio", 
    page_icon="📈", 
    layout="wide",
    initial_sidebar_state="collapsed" 
)

# --- PHOTO FILENAME ---
PHOTO_FILENAME = "Nehil Profile Photo.jpg"

# --- 2. SESSION STATE FOR NAVIGATION ---
if 'page' not in st.session_state:
    st.session_state.page = "Home"

def set_page(page_name):
    st.session_state.page = page_name

# --- 3. ADVANCED STYLING & MOBILE NAV CSS ---
st.markdown("""
    <style>
    /* Hide Default Streamlit Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global Styles */
    .stApp { background-color: #fcfcfc; }
    .main-header { color: #1f77b4; font-size: 2.8rem; font-weight: bold; margin-bottom: 0; }
    .sub-header { color: #444; font-size: 1.6rem; margin-top: 0; margin-bottom: 20px; }
    .company-title { font-weight: bold; font-size: 1.3rem; color: #1f77b4; margin-top: 5px;}
    .job-date { color: #888; font-size: 0.95rem; font-weight: bold; display: block; margin-bottom: 10px;}
    .edu-card { background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #eee; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);}
    .project-card-content { background-color: #f0f8ff; padding: 15px; border-radius: 10px; border-left: 5px solid #1f77b4; }
    .contact-text { font-size: 1.2rem; margin-bottom: 10px; }

    /* Mobile Navigation Bar Styling */
    @media only screen and (max-width: 768px) {
        .mobile-nav-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #ffffff;
            border-bottom: 1px solid #ddd;
            padding: 10px 0px;
            z-index: 9999;
            display: flex;
            justify-content: space-around;
        }
        .main-content-area { padding-top: 80px; }
    }
    @media only screen and (min-width: 769px) {
        .mobile-nav-container { display: none; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. TOP NAVIGATION (MOBILE ONLY) ---
# This creates a persistent menu at the top for Safari/Chrome mobile users
with st.container():
    st.markdown('<div class="mobile-nav-container">', unsafe_allow_html=True)
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    with m_col1: 
        if st.button("🏠 Home", key="m1"): set_page("Home")
    with m_col2: 
        if st.button("💼 Exp", key="m2"): set_page("Experience")
    with m_col3: 
        if st.button("📂 Proj", key="m3"): set_page("Projects")
    with m_col4: 
        if st.button("📧 Msg", key="m4"): set_page("Contact")
    st.markdown('</div><div class="main-content-area"></div>', unsafe_allow_html=True)

# --- PAGE FUNCTIONS ---

def home_page():
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    try: st.image(PHOTO_FILENAME, width=220) 
    except: st.warning(f"Ensure '{PHOTO_FILENAME}' is uploaded to GitHub.")
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
    st.markdown("### 🎯 Core Expertise")
    st.write("🔍 **Secondary Research** | 📊 **Data Analysis** | 📈 **Sales Operations** | ⚙️ **Process Automation**")
    st.header("🛠️ Tools & Technologies")
    st.markdown("""
        <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=microsoftpowerbi&logoColor=black" /> 
        <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" /> 
        <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> 
        <img src="https://img.shields.io/badge/Power_Automate-0066FF?style=for-the-badge&logo=powerautomate&logoColor=white" />
        """, unsafe_allow_html=True)

def experience_page():
    st.title("💼 Professional Experience")
    with st.expander("🚀 G2 | Senior Specialist (Operations) | Feb 2026 – Present", expanded=True):
        st.markdown("<div class='company-title'>G2 · Gurugram, India</div>", unsafe_allow_html=True)
        st.write("""
        * **Strategic Enablement:** Consultant for Sales, Partnerships, and Advisory teams; deliver high-impact analytics.
        * **Project Leadership:** Manage full lifecycle of multi-stakeholder projects (Whitespacing, Partnership Development).
        * **Executive Support:** Partner with SLT to develop strategic decks and narratives.
        """)
    with st.expander("📊 Gartner (Full Tenure: 4 yrs 7 mos)"):
        with st.popover("Senior Specialist (Operations) | Dec 2025 – Feb 2026"):
            st.write("* Streamlined complex workstreams to drive performance and revenue via AI-driven custom automations.")
        with st.popover("Product Reviews Specialist | Oct 2023 – Dec 2025"):
            st.write("* Led automation projects; Won **GDM Operations Hackathon 2025**; Trained 20+ members.")
        with st.popover("Product Reviews Associate | Aug 2021 – Sep 2023"):
            st.write("* Recognized as **'SQLNinja'**; Developed Disablement Menu improving efficiency 3x.")

    with st.expander("🎨 Early Career: MRM//McCann, Freelance & Ureka"):
        st.write("* **MRM//McCann:** Account Management Intern for large retail accounts.")
        st.write("* **Freelance:** Prepared competitive matrices for **Fortune 1000 companies**.")
        st.write("* **Ureka Group:** Competitor analysis for Data Science programs; won **Global Youth Icon (2021)**.")

def projects_page():
    st.title("📂 Key Projects")
    with st.expander("1. 🎯 VIP Account Prioritization and Whitespacing", expanded=True):
        st.markdown("""<div class='project-card-content'>
            <p><strong>Objective:</strong> Rank 963 products and identify revenue 'white spaces' using a Weighted Scoring Model (13 factors analyzed).</p>
            <p><strong>Impact:</strong> Delivered interactive dashboards for sales support and identified 102 new category opportunities via AI research.</p>
        </div>""", unsafe_allow_html=True)
    with st.expander("2. 🤝 Partnership Business Development Framework"):
        st.markdown("""<div class='project-card-content'>
            <p><strong>Impact:</strong> Managed a $1.25M revenue target with 9% conversion. Provided 139 high-intent leads resulting in 13 immediate wins.</p>
        </div>""", unsafe_allow_html=True)
    with st.expander("3. 🏆 GDM Operations Hackathon: AI-Driven Automation (Winner)"):
        st.markdown("""<div class='project-card-content'>
            <p><strong>Impact:</strong> Awarded 1st Place (Winner). Saved 1 hour of manual work daily and unlocked an estimated $60,000+ in untapped annual revenue.</p>
        </div>""", unsafe_allow_html=True)
    with st.expander("4. 🤖 AI-Generated Content Detection Framework"):
        st.write("* Reduced ambiguity by 95% and improved overall review quality by 10% across the ecosystem.")

def education_page():
    st.title("🎓 Education Journey")
    st.markdown("<div class='edu-card'><strong>MDI, Gurgaon</strong><br>PGDM (OPGDM) | 2023 – 2025<br>⭐ Scholarship Holder</div>", unsafe_allow_html=True)
    st.markdown("<div class='edu-card'><strong>G.D. Goenka University</strong><br>BBA, Marketing | 2018 – 2021<br>⭐ CGPA: 8.95 | 100% Scholarship holder</div>", unsafe_allow_html=True)
    st.markdown("<div class='edu-card'><strong>MM Public School</strong> | XII (CBSE): 90%</div>", unsafe_allow_html=True)
    st.markdown("<div class='edu-card'><strong>The Heritage School</strong> | X (CBSE): CGPA 9.2</div>", unsafe_allow_html=True)

def achievements_page():
    st.title("🏆 Achievements & Awards")
    st.success("**Winner: GDM Operations Hackathon 2025** - Gartner Innovation Award")
    st.success("**Best Associate 2022** - Gartner (Internal Team Award)")
    st.info("**Scholarship Holder:** Module 2 OPGDM (MDI Gurgaon)")
    st.info("**Gold Medalist:** Ureka Global Youth Icon (2021)")
    st.info("**IELTS Band 8.5:** Overall score")

def contact_page():
    st.title("📧 Contact Now")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<p class='contact-text'>📞 +91 9821783999</p>", unsafe_allow_html=True)
        st.markdown("<p class='contact-text'>✉️ <a href='mailto:nehil30jan@gmail.com'>nehil30jan@gmail.com</a></p>", unsafe_allow_html=True)
        st.markdown("<p class='contact-text'>🔗 <a href='https://www.linkedin.com/in/nehilgupta/'>LinkedIn Profile</a></p>", unsafe_allow_html=True)
    with col2:
        try: st.image(PHOTO_FILENAME, width=150)
        except: pass
    st.write("---")
    st.header("✉️ Drop a Message")
    name = st.text_input("Name")
    email = st.text_input("Email")
    msg = st.text_area("Message")
    req_meeting = st.radio("Request a meeting invite?", ["No", "Yes"], horizontal=True)
    if st.button("Submit Message"):
        if name and email and msg:
            st.success("Message prepared for Nehil!")
            st.balloons()
            full_body = f"Name: {name}\nEmail: {email}\n\nMessage: {msg}"
            st.markdown(f'<a href="mailto:nehil30jan@gmail.com?subject=Message from {name}&body={full_body}" style="padding: 10px 20px; background-color: #1f77b4; color: white; border-radius: 5px; text-decoration: none; font-weight: bold;">Click to Finalize & Send Email</a>', unsafe_allow_html=True)

# --- 5. SHARED SIDEBAR NAVIGATION (DESKTOP) ---
st.sidebar.title("Navigation")
if st.sidebar.button("🏠 Home", use_container_width=True): set_page("Home")
if st.sidebar.button("💼 Experience", use_container_width=True): set_page("Experience")
if st.sidebar.button("📂 Projects", use_container_width=True): set_page("Projects")
if st.sidebar.button("🎓 Education", use_container_width=True): set_page("Education")
if st.sidebar.button("🏆 Achievements", use_container_width=True): set_page("Achievements")
if st.sidebar.button("📧 Contact", use_container_width=True): set_page("Contact")

st.sidebar.write("---")
st.sidebar.caption("Senior Specialist | G2 (Ex-Gartner)")

# --- 6. PAGE ROUTING LOGIC ---
if st.session_state.page == "Home": home_page()
elif st.session_state.page == "Experience": experience_page()
elif st.session_state.page == "Projects": projects_page()
elif st.session_state.page == "Education": education_page()
elif st.session_state.page == "Achievements": achievements_page()
elif st.session_state.page == "Contact": contact_page()
