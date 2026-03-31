import streamlit as st
from datetime import datetime, date

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="Nehil Gupta | Portfolio", 
    page_icon="📈", 
    layout="wide",
    initial_sidebar_state="expanded" 
)

# --- PHOTO FILENAME ---
PHOTO_FILENAME = "Nehil Profile Photo.jpg"

# --- 2. CSS (Hiding Branding & Fixing Sidebar Arrow Color) ---
st.markdown("""
    <style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* SIDEBAR ARROW FIX: Solid Black for visibility on Safari/Chrome Mobile */
    button[kind="headerNoContext"] {
        color: black !important;
        background-color: rgba(0,0,0,0.05) !important;
        border-radius: 50% !important;
        width: 45px !important;
        height: 45px !important;
        position: fixed !important;
        top: 15px !important;
        left: 15px !important;
        z-index: 999999 !important;
    }

    /* Original Detailed Styles */
    .stApp { background-color: #fcfcfc; }
    .main-header { color: #1f77b4; font-size: 2.8rem; font-weight: bold; margin-bottom: 0; }
    .sub-header { color: #444; font-size: 1.6rem; margin-top: 0; margin-bottom: 20px; }
    .company-title { font-weight: bold; font-size: 1.3rem; color: #1f77b4; margin-top: 5px;}
    .job-date { color: #888; font-size: 0.95rem; font-weight: bold; display: block; margin-bottom: 10px;}
    .edu-card { background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #eee; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);}
    .project-card-content { background-color: #f0f8ff; padding: 15px; border-radius: 10px; border-left: 5px solid #1f77b4; }
    .contact-text { font-size: 1.2rem; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- PAGE: HOME ---
def home_page():
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    try:
        st.image(PHOTO_FILENAME, width=220) 
    except Exception:
        st.warning(f"Note: Ensure '{PHOTO_FILENAME}' is uploaded to GitHub.")

    st.markdown(f"<h1 class='main-header'>Nehil Gupta</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Senior Specialist | G2 (Ex-Gartner)</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True) 
    
    st.write("---")
    st.markdown("### 👤 Professional Summary")
    st.write("""
    I am an analytical and data-driven professional with over 4 years of experience specializing in product review analytics, 
    process automation, and AI-content detection. Currently serving as a **Senior Specialist at G2**, I lead strategic 
    projects that enhance efficiency, data quality, and business outcomes. Skilled in SQL, Power BI, and Power Automate, 
    I partner with Senior Leadership Teams (SLT) to drive strategic, data-driven narratives.
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
    st.write("Browse my career journey by company and specific tenure.")

    with st.expander("🚀 G2 | Senior Specialist (Operations) | Feb 2026 – Present", expanded=True):
        st.markdown("<div class='company-title'>G2 · Gurugram, India (Hybrid)</div>", unsafe_allow_html=True)
        st.write("""
        * **Strategic Enablement:** Consultant for Sales, Partnerships, and Advisory teams; deliver high-impact analytics to drive performance and unlock new revenue.
        * **Project Leadership:** Manage full lifecycle of multi-stakeholder projects (Whitespacing, Partnership Development) to unlock revenue and prospecting efficiency.
        * **Executive Support:** Partner directly with the Senior Leadership Team (SLT) to develop strategic decks and narratives for corporate decision-making.
        * **Process Transformation:** Identify and eliminate operational bottlenecks by implementing AI-driven solutions and custom automations for Lean Management.
        """)

    with st.expander("📊 Gartner (Full Tenure: 4 yrs 7 mos)"):
        st.info("Select a specific role below to see detailed responsibilities:")
        with st.popover("Senior Specialist (Operations) | Dec 2025 – Feb 2026"):
            st.write("* Consultant for Sales and Advisory teams; streamlining workstreams via AI-driven automations.")
        with st.popover("Product Reviews Specialist | Oct 2023 – Dec 2025"):
            st.write("* Led automation projects; Won **GDM Operations Hackathon 2025**; Trained 20+ members.")
        with st.popover("Product Reviews Associate | Aug 2021 – Sep 2023"):
            st.write("* Recognized as **'SQLNinja'**; Developed Disablement Menu improving efficiency 3x.")

    with st.expander("🎨 Early Career: MRM//McCann, Freelance & Ureka"):
        st.write("* **MRM//McCann:** Account Management Intern for large retail accounts.")
        st.write("* **Freelance:** Prepared competitive matrices for **Fortune 1000 companies**.")
        st.write("* **Ureka Group:** Intern (2020-2021); won **Global Youth Icon (2021)**.")

# --- PAGE: PROJECTS ---
def projects_page():
    st.title("📂 Key Projects")
    st.info("I served as the Project Lead for all initiatives listed below.")

    with st.expander("1. 🎯 VIP Account Prioritization and Whitespacing", expanded=True):
        st.markdown("""<div class='project-card-content'>
            <p><strong>Objective:</strong> Rank 963 products and identify revenue 'white spaces' using a Weighted Scoring Model (13 factors across 5 categories).</p>
            <p><strong>Impact:</strong> Identified 102 new category opportunities via AI research and secondary analysis.</p>
        </div>""", unsafe_allow_html=True)

    with st.expander("2. 🤝 Partnership Business Development Framework"):
        st.markdown("""<div class='project-card-content'>
            <p><strong>Impact:</strong> Managed a $1.25M revenue target with 9% conversion. Provided 139 high-intent leads.</p>
        </div>""", unsafe_allow_html=True)

    with st.expander("3. 🏆 GDM Operations Hackathon Winner"):
        st.markdown("""<div class='project-card-content'>
            <p><strong>Impact:</strong> Saved 1 hour of manual work daily and unlocked an estimated $60,000+ in untapped annual revenue.</p>
        </div>""", unsafe_allow_html=True)

    with st.expander("4. 🤖 AI-Generated Content Detection Framework"):
        st.write("* Reduced ambiguity by 95% and improved quality by 10% across the ecosystem.")

# --- PAGE: EDUCATION ---
def education_page():
    st.title("🎓 Education Journey")
    st.markdown("<div class='edu-card'><strong>MDI, Gurgaon</strong><br>PGDM (OPGDM) | 2023 – 2025<br>⭐ Scholarship Holder</div>", unsafe_allow_html=True)
    st.markdown("<div class='edu-card'><strong>G.D. Goenka University</strong><br>BBA, Marketing | 2018 – 2021<br>⭐ CGPA: 8.95 | 100% Scholarship holder</div>", unsafe_allow_html=True)
    st.markdown("<div class='edu-card'><strong>MM Public School</strong> | XII (CBSE): 90%</div>", unsafe_allow_html=True)
    st.markdown("<div class='edu-card'><strong>The Heritage School</strong> | X (CBSE): CGPA 9.2</div>", unsafe_allow_html=True)

# --- PAGE: ACHIEVEMENTS ---
def achievements_page():
    st.title("🏆 Achievements & Awards")
    ach_type = st.radio("Select Category:", ["Corporate Awards", "Academic Honors", "Personal"], horizontal=True)
    if ach_type == "Corporate Awards":
        st.success("**GDM Operations Hackathon 2025 Winner** - Gartner Innovation Award")
        st.success("**Best Associate 2022** - Gartner (Internal Team Award)")
        st.success("**SQL Ninja Recognition** - Gartner Bootcamp Winner")
    elif ach_type == "Academic Honors":
        st.info("**Scholarship Holder:** MDI Gurgaon")
        st.info("**IELTS Band 8.5:** Overall score")
    else:
        st.warning("**YouTube Content Creation:** Built a monetized Gaming channel with **3,000+ subscribers**.")

# --- PAGE: CONTACT NOW ---
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
    with st.container():
        name = st.text_input("Name")
        email = st.text_input("Email")
        msg = st.text_area("Message")
        if st.button("Submit Message"):
            if name and email and msg:
                st.success("Message prepared!")
                st.balloons()
                body = f"Name: {name}\nEmail: {email}\n\nMessage: {msg}"
                st.markdown(f'<a href="mailto:nehil30jan@gmail.com?subject=Message from {name}&body={body}" style="padding: 10px 20px; background-color: #1f77b4; color: white; border-radius: 5px; text-decoration: none; font-weight: bold;">Click to Finalize & Send Email</a>', unsafe_allow_html=True)

# --- 3. ORIGINAL SIDEBAR NAVIGATION LOGIC ---
pg = st.navigation([
    st.Page(home_page, title="Home", icon="🏠"),
    st.Page(experience_page, title="Experience", icon="💼"),
    st.Page(projects_page, title="Projects", icon="📂"),
    st.Page(education_page, title="Education", icon="🎓"),
    st.Page(achievements_page, title="Achievements", icon="🏆"),
    st.Page(contact_page, title="Contact Now", icon="📧"),
])

# SIDEBAR FOOTER
st.sidebar.markdown("### Quick Connect")
st.sidebar.write("✉️ [nehil30jan@gmail.com](mailto:nehil30jan@gmail.com)")
st.sidebar.write("📞 +91 9821783999")

pg.run()
