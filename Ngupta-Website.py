import streamlit as st
from datetime import datetime, date

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="Nehil Gupta | Portfolio", 
    page_icon="📈", 
    layout="wide",
    initial_sidebar_state="expanded" # Forces sidebar to stay open on most devices
)

# --- PHOTO FILENAME (Ensure this matches the file on GitHub) ---
PHOTO_FILENAME = "Nehil Profile Photo.jpg"

# --- 2. SHARED STYLING & CLEAN UI ---
st.markdown("""
    <style>
    /* Hide Streamlit Branding & Menus */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main Content Styles */
    .stApp { background-color: #fcfcfc; }
    .main-header { color: #1f77b4; font-size: 2.8rem; font-weight: bold; margin-bottom: 0; }
    .sub-header { color: #444; font-size: 1.6rem; margin-top: 0; margin-bottom: 20px; }
    .company-title { font-weight: bold; font-size: 1.3rem; color: #1f77b4; margin-top: 5px;}
    .job-date { color: #888; font-size: 0.95rem; font-weight: bold; display: block; margin-bottom: 10px;}
    .edu-card { background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #eee; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);}
    .project-card-content { background-color: #f0f8ff; padding: 15px; border-radius: 10px; border-left: 5px solid #1f77b4; }
    .contact-text { font-size: 1.2rem; margin-bottom: 10px; }
    
    /* Mobile Sidebar visibility fix */
    section[data-testid="stSidebar"] {
        background-color: #f8f9fa;
        border-right: 1px solid #eee;
    }
    </style>
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
    
    st.write("---")
    st.info("💡 **Mobile Users:** Use the menu icon in the top-left corner to explore my Experience, Projects, and Achievements!")

# --- PAGE: PROJECTS ---
def projects_page():
    st.title("📂 Key Projects")
    st.info("I served as the Project Lead for all initiatives listed below.")

    with st.expander("1. 🎯 VIP Account Prioritization and Whitespacing", expanded=True):
        st.markdown("""
        <div class='project-card-content'>
            <p><strong>Objective:</strong> Build a data-driven vendor prioritization framework to rank 963 products and identify revenue 'white spaces'.</p>
            <p><strong>Key Actions:</strong> Developed a Weighted Scoring Model analyzing 13 factors across 5 categories. Distributed products into prioritization quadrants (High, Med-High, Med-Low, Low).</p>
            <p><strong>Impact:</strong> Delivered interactive dashboards for sales support, provided 665 POCs for High-priority products, and identified 102 new category opportunities.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("2. 🤝 Partnership Business Development Framework"):
        st.markdown("""
        <div class='project-card-content'>
            <p><strong>Impact:</strong> Managed a $1.25M revenue target with 9% conversion. Provided 139 high-intent leads resulting in 13 immediate wins and structured a WIP pipeline for 37% of leads.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("3. 🏆 GDM Operations Hackathon: AI-Driven Automation (Winner)"):
        st.markdown("""
        <div class='project-card-content'>
            <p><strong>Impact:</strong> Awarded 1st Place (Winner). Saved 1 hour of manual work daily and unlocked an estimated $60,000+ in untapped annual revenue.</p>
            <p><strong>Role:</strong> Automation Architect.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("4. 🤖 AI-Generated Content Detection Framework"):
        st.markdown("""<div class='project-card-content'><p>Reduced ambiguity by 95% and improved overall review quality by 10% across the ecosystem.</p></div>""", unsafe_allow_html=True)

    with st.expander("5. ⚙️ Disablement Menu Automation & Re-engineering"):
        st.markdown("""<div class='project-card-content'><p>Increased review-publishing efficiency by 3x (from 16% to 48%).</p></div>""", unsafe_allow_html=True)

# --- PAGE: EXPERIENCE ---
def experience_page():
    st.title("💼 Professional Experience")
    
    with st.expander("🚀 G2 | Senior Specialist (Operations) | Feb 2026 – Present", expanded=True):
        st.markdown("<div class='company-title'>G2 · Gurugram, India</div>", unsafe_allow_html=True)
        st.write("""
        * **Strategic Enablement:** Consultant for Sales, Partnerships, and Advisory teams; deliver high-impact analytics to drive performance.
        * **Project Leadership:** Manage full lifecycle of multi-stakeholder projects (Whitespacing, Partnership Development).
        * **Executive Support:** Partner directly with the Senior Leadership Team (SLT) on strategic decks and narratives.
        """)

    with st.expander("📊 Gartner (Full Tenure: 4 yrs 7 mos)"):
        st.info("Select a specific role below to see detailed responsibilities:")
        with st.popover("Senior Specialist (Operations) | Dec 2025 – Feb 2026"):
            st.write("* **Consulting:** Dedicated enabler for Sales and Advisory teams.")
            st.write("* **Analytics:** Streamlined workstreams to drive performance.")
        with st.popover("Product Reviews Specialist | Oct 2023 – Dec 2025"):
            st.write("* **Efficiency Projects:** Led automation projects; Won **GDM Operations Hackathon 2025**.")
            st.write("* **AI Content:** Developed detection guidelines reducing ambiguity by 95%.")
        with st.popover("Product Reviews Associate | Aug 2021 – Sep 2023"):
            st.write("* **Tech Recognition:** Recognized as **'SQLNinja'** after winning internal SQL Bootcamp.")
            st.write("* **Events:** Organized ManifestGDM & KRITI events for 100+ participants.")

    with st.expander("🎨 MRM//McCann, Freelance & Ureka"):
        st.write("* **MRM//McCann:** Account Management Intern (2021); Retail digital marketing.")
        st.write("* **Freelance:** Prepared competitive matrices for **Fortune 1000 companies**.")
        st.write("* **Ureka Group:** Intern (2020-2021); won **Global Youth Icon (2021)**.")

# --- PAGE: EDUCATION ---
def education_page():
    st.title("🎓 Education Journey")
    st.markdown("<div class='edu-card'><strong>MDI, Gurgaon</strong><br>PGDM (OPGDM) | 2023 – 2025<br>⭐ <em>Scholarship Holder</em></div>", unsafe_allow_html=True)
    st.markdown("<div class='edu-card'><strong>G.D. Goenka University</strong><br>BBA, Marketing | 2018 – 2021<br>⭐ <strong>CGPA: 8.95</strong></div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='edu-card'><strong>MM Public School, Rohini</strong><br>Class XII (CBSE) | Result: <strong>90%</strong></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='edu-card'><strong>The Heritage School, Rohini</strong><br>Class X (CBSE) | Result: <strong>CGPA 9.2</strong></div>", unsafe_allow_html=True)

# --- PAGE: ACHIEVEMENTS ---
def achievements_page():
    st.title("🏆 Achievements & Awards")
    ach_type = st.radio("Select Category:", ["Corporate Awards", "Academic Honors", "Personal"], horizontal=True)
    
    if ach_type == "Corporate Awards":
        st.success("**GDM Operations Hackathon 2025 Winner** - Gartner")
        st.success("**Best Associate 2022** - Gartner (Team Award)")
        st.success("**SQL Ninja Recognition** - Gartner Bootcamp Winner")
        st.success("**Multiple RnR Awards:** Exceptional Idea Generation & Spotlight Awards.")
    elif ach_type == "Academic Honors":
        st.info("**Scholarship Holder:** Module 2 OPGDM (MDI Gurgaon)")
        st.info("**Gold Medalist:** Ureka Global Youth Icon (2021)")
        st.info("**IELTS Band 8.5:** Overall score")
    else:
        st.warning("**YouTube Content Creation:** Built a monetized Gaming channel with 3,000+ subscribers.")

# --- PAGE: CONTACT & MESSAGE ---
def contact_page():
    st.title("📧 Contact Now")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("#### 📱 Connect Directly")
        st.markdown("<p class='contact-text'>📞 +91 9821783999</p>", unsafe_allow_html=True)
        st.markdown("<p class='contact-text'>✉️ <a href='mailto:nehil30jan@gmail.com'>nehil30jan@gmail.com</a></p>", unsafe_allow_html=True)
        st.markdown("<p class='contact-text'>🔗 <a href='https://www.linkedin.com/in/nehilgupta/'>LinkedIn Profile</a></p>", unsafe_allow_html=True)
    
    with col2:
        try:
            st.image(PHOTO_FILENAME, width=150)
        except:
            pass

    st.write("---")
    st.header("✉️ Drop a Message")
    
    with st.container():
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number (Optional)")
        msg = st.text_area("Message")
        
        req_meeting = st.radio("Request a meeting invite?", ["No", "Yes"], horizontal=True)
        
        meeting_details = ""
        if req_meeting == "Yes":
            col_date, col_time = st.columns(2)
            with col_date:
                m_date = st.date_input("Select Date", min_value=date.today())
            with col_time:
                m_time = st.time_input("Select Preferred Time Slot")
            meeting_details = f"\n[MEETING REQUESTED: {m_date} at {m_time}]"

        if st.button("Submit Message"):
            if name and email and msg:
                st.success(f"Message prepared for Nehil!")
                st.balloons()
                full_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage: {msg}\n{meeting_details}"
                st.markdown(f'<a href="mailto:nehil30jan@gmail.com?subject=Portfolio Message from {name}&body={full_body}" style="padding: 10px 20px; background-color: #1f77b4; color: white; border-radius: 5px; text-decoration: none; font-weight: bold;">Click to Finalize & Send</a>', unsafe_allow_html=True)
            else:
                st.error("Please fill in Name, Email, and Message.")

# --- NAVIGATION LOGIC ---
pg = st.navigation([
    st.Page(home_page, title="Home", icon="🏠"),
    st.Page(experience_page, title="Experience", icon="💼"),
    st.Page(projects_page, title="Projects", icon="📂"),
    st.Page(education_page, title="Education", icon="🎓"),
    st.Page(achievements_page, title="Achievements", icon="🏆"),
    st.Page(contact_page, title="Contact Now", icon="📧"),
])

# --- SIDEBAR QUICK CONNECT ---
st.sidebar.markdown("### Quick Connect")
st.sidebar.write("✉️ [nehil30jan@gmail.com](mailto:nehil30jan@gmail.com)")
st.sidebar.write("📞 +91 9821783999")
st.sidebar.caption("Built with Streamlit 2026")

pg.run()
