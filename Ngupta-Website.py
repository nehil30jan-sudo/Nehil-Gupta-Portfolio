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

# --- 2. ADVANCED MOBILE CSS & STYLING ---
st.markdown("""
    <style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* CHANGE SIDEBAR ARROW TO BLACK */
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

    /* Floating Mobile Menu Hint (Only shows on mobile) */
    @media only screen and (max-width: 768px) {
        .mobile-hint {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: black;
            color: white;
            padding: 10px 18px;
            border-radius: 25px;
            font-size: 13px;
            font-weight: bold;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
            z-index: 1000;
        }
    }
    @media only screen and (min-width: 769px) {
        .mobile-hint { display: none; }
    }

    /* Original Styles */
    .stApp { background-color: #fcfcfc; }
    .main-header { color: #1f77b4; font-size: 2.8rem; font-weight: bold; margin-bottom: 0; }
    .sub-header { color: #444; font-size: 1.6rem; margin-top: 0; margin-bottom: 20px; }
    .company-title { font-weight: bold; font-size: 1.3rem; color: #1f77b4; margin-top: 5px;}
    .job-date { color: #888; font-size: 0.95rem; font-weight: bold; display: block; margin-bottom: 10px;}
    .edu-card { background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #eee; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);}
    .project-card-content { background-color: #f0f8ff; padding: 15px; border-radius: 10px; border-left: 5px solid #1f77b4; }
    .contact-text { font-size: 1.2rem; margin-bottom: 10px; }
    </style>
    
    <div class="mobile-hint">⬅️ Tap Top-Left Arrow for Menu</div>
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

# --- PAGE: PROJECTS ---
def projects_page():
    st.title("📂 Key Projects")
    st.info("I served as the Project Lead for all initiatives listed below.")

    with st.expander("1. 🎯 VIP Account Prioritization and Whitespacing", expanded=True):
        st.markdown("""
        <div class='project-card-content'>
            <p><strong>Objective:</strong> Build a data-driven vendor prioritization framework to rank 963 products and identify revenue 'white spaces'.</p>
            <p><strong>Key Actions:</strong> Developed a Weighted Scoring Model analyzing 13 factors across 5 categories (Account Activity, Revenue, Alignment, Sales Readiness, and Traffic). Distributed products into prioritization quadrants (High, Med-High, Med-Low, Low).</p>
            <p><strong>Impact:</strong> Delivered interactive dashboards for sales support, provided 665 POCs for High-priority products, and identified 102 new category opportunities via AI and secondary research.</p>
            <p><strong>Role:</strong> Project Lead & Lead Strategist.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("2. 🤝 Partnership Business Development Framework"):
        st.markdown("""
        <div class='project-card-content'>
            <p><strong>Objective:</strong> Enhance the PPL Partnerships program by identifying new associations across priority markets.</p>
            <p><strong>Key Actions:</strong> Restructured the workflow into 'Research & Data Management' and 'Outreach'. Built a CRM-based operating model on Monday.com to improve data visibility and real-time collaboration.</p>
            <p><strong>Impact:</strong> Managed a $1.25M revenue target with a 9% conversion rate. Provided 139 high-intent leads resulting in 13 immediate wins and structured a WIP pipeline for 37% of leads.</p>
            <p><strong>Role:</strong> Project Lead & Lead Strategist.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("3. 🏆 GDM Operations Hackathon: AI-Driven Automation (Winner)"):
        st.markdown("""
        <div class='project-card-content'>
            <p><strong>Objective:</strong> Eliminate operational bottlenecks in contact discovery for prospecting teams and optimize resource allocation.</p>
            <p><strong>Key Actions:</strong> Pitched and designed an automation framework using Power Automate and Python to handle repetitive contact discovery and resource allocation tasks.</p>
            <p><strong>Impact:</strong> Awarded 1st Place (Winner). Saved 1 hour of manual work daily and unlocked an estimated $60,000+ in untapped annual revenue.</p>
            <p><strong>Role:</strong> Project Lead & Automation Architect.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("4. 🤖 AI-Generated Content Detection Framework"):
        st.markdown("""
        <div class='project-card-content'>
            <p><strong>Objective:</strong> Standardize identification of AI-generated reviews to ensure review quality and data integrity.</p>
            <p><strong>Key Actions:</strong> Led development of pattern-based classifiers and detection guidelines. Trained a 20+ member global team on analytical best practices.</p>
            <p><strong>Impact:</strong> Reduced ambiguity by 95% and improved overall review quality by 10% across the ecosystem.</p>
            <p><strong>Role:</strong> Project Lead.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("5. ⚙️ Disablement Menu Automation & Re-engineering"):
        st.markdown("""
        <div class='project-card-content'>
            <p><strong>Objective:</strong> Streamline publishing workflows by re-engineering the manual disablement process.</p>
            <p><strong>Key Actions:</strong> Implemented a new Disablement Menu system with built-in audit tracking for quality control.</p>
            <p><strong>Impact:</strong> Increased review-publishing efficiency by 3x (from 16% to 48%) and introduced audit systems for quality tracking.</p>
            <p><strong>Role:</strong> Project Lead.</p>
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
            st.write("* **Consulting:** Dedicated enabler for Sales and Advisory teams.")
            st.write("* **Analytics:** Streamlined complex workstreams to drive performance and revenue.")
            st.write("* **Tech Integration:** Implemented AI-driven custom automations helping in Lean Management.")
        with st.popover("Product Reviews Specialist | Oct 2023 – Dec 2025"):
            st.write("* **Efficiency Projects:** Led automation projects; Won **GDM Operations Hackathon 2025**.")
            st.write("* **Leadership:** Led brainstorming for 20+ members to solve critical process problems.")
            st.write("* **Analysis:** Conducted secondary research and analysis using **SQL, Power BI, and Excel**.")
        with st.popover("Product Reviews Associate | Aug 2021 – Sep 2023"):
            st.write("* **Validation:** Verified reviews on Gartner platforms (Capterra, Software Advice, GetApp).")
            st.write("* **Tech Recognition:** Recognized as **'SQLNinja'** after winning internal SQL Bootcamp.")
            st.write("* **Events:** Organized 2 GDM Level Events (**ManifestGDM, KRITI**) for 100+ participants.")

    with st.expander("🎨 MRM//McCann, Freelance & Ureka"):
        st.markdown("**MRM//McCann | Account Management Intern (2021)**")
        st.write("* Managed digital marketing for large retail accounts; Analyzed campaign data in Excel.")
        st.markdown("---")
        st.markdown("**Freelance | Research Analyst (2021)**")
        st.write("* Prepared competitive matrices for **Fortune 1000 companies** using secondary research.")
        st.markdown("---")
        st.markdown("**Ureka Education Group | Intern (2020-2021)**")
        st.write("* Conducted competitor analysis for Data Science programs; won **Global Youth Icon (2021)**.")

# --- PAGE: EDUCATION ---
def education_page():
    st.title("🎓 Education Journey")
    st.markdown("### Post-Graduation")
    st.markdown("<div class='edu-card'><strong>Management Development Institute (MDI), Gurgaon</strong><br>PGDM (OPGDM) | 2023 – 2025<br>⭐ <em>Scholarship Holder for Module 2</em></div>", unsafe_allow_html=True)

    st.markdown("### Graduation")
    st.markdown("<div class='edu-card'><strong>G.D. Goenka University</strong><br>BBA, Marketing | 2018 – 2021<br>⭐ <strong>CGPA: 8.95</strong> (Final Sem SGPA: 9.67)<br>🏆 100% Scholarship holder in 3/6 semesters.</div>", unsafe_allow_html=True)

    st.markdown("### Schooling")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='edu-card'><strong>MM Public School, Rohini</strong><br>Class XII (CBSE)<br>📚 <em>PCM + PE & English</em><br>⭐ Result: <strong>90%</strong></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='edu-card'><strong>The Heritage School, Rohini</strong><br>Class I - X (CBSE)<br>⭐ Class X Result: <strong>CGPA 9.2</strong></div>", unsafe_allow_html=True)

# --- PAGE: ACHIEVEMENTS ---
def achievements_page():
    st.title("🏆 Achievements & Awards")
    ach_type = st.radio("Select Category:", ["Corporate Awards", "Academic Honors", "Personal Achievements"], horizontal=True)
    
    if ach_type == "Corporate Awards":
        st.success("**GDM Operations Hackathon 2025 Winner** - Gartner (Innovation Award)")
        st.success("**Best Associate 2022** - Gartner (Internal Team Award)")
        st.success("**Kriti (Project Innovation)** - Gartner")
        st.success("**Manifest GDM** - GDM Values Competition Winner")
        st.success("**SQL Ninja Recognition** - Gartner (Advanced Data Bootcamp Winner)")
        st.success("**YE Spotlight Award (2021):** Recognition for Idea Generation - Gartner")
        st.success("**Going Above and Beyond / Exceptional Idea Generation:** Multiple Internal RnRs")
    elif ach_type == "Academic Honors":
        st.info("**Scholarship Holder:** Module 2 OPGDM (MDI Gurgaon)")
        st.info("**Top 1 Percentile:** BBA Batch 2018-2021")
        st.info("**Gold Medalist:** Ureka Global Youth Icon (2021)")
        st.info("**IELTS Band 8.5:** Overall score (Expert User)")
        st.info("**International Math Olympiad:** 3rd Place (School Level)")
    elif ach_type == "Personal Achievements":
        st.warning("**YouTube Content Creation:** Built a monetized Gaming channel with **3,000+ subscribers** in 6 months.")

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
                st.success(f"Perfect! Your message for Nehil has been prepared.")
                st.balloons()
                
                full_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage: {msg}\n{meeting_details}"
                st.markdown(f'<a href="mailto:nehil30jan@gmail.com?subject=Portfolio Message from {name}&body={full_body}" style="padding: 10px 20px; background-color: #1f77b4; color: white; border-radius: 5px; text-decoration: none; font-weight: bold;">Click here to Finalize & Send</a>', unsafe_allow_html=True)
            else:
                st.error("Please fill in Name, Email, and Message.")

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
st.sidebar.caption("Built with Streamlit 2026")

pg.run()
