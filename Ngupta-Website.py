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

# --- 2. MOBILE NAVIGATION & CSS ---
st.markdown("""
    <style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* FORCE SIDEBAR ARROW VISIBILITY & COLOR */
    button[kind="headerNoContext"] {
        color: white !important;
        background-color: #FF4B4B !important; /* Bright Red for visibility */
        border-radius: 5px !important;
        width: 50px !important;
        height: 50px !important;
        position: fixed !important;
        top: 10px !important;
        left: 10px !important;
        z-index: 999999 !important;
        display: block !important;
    }

    /* Mobile "Open Menu" Alert Box */
    @media only screen and (max-width: 768px) {
        .mobile-nav-notice {
            background-color: #f0f2f6;
            padding: 15px;
            border-radius: 10px;
            border: 2px dashed #1f77b4;
            text-align: center;
            margin-bottom: 20px;
        }
    }
    @media only screen and (min-width: 769px) {
        .mobile-nav-notice { display: none; }
    }

    /* Main Styles */
    .stApp { background-color: #fcfcfc; }
    .main-header { color: #1f77b4; font-size: 2.5rem; font-weight: bold; margin-bottom: 0; }
    .company-title { font-weight: bold; font-size: 1.2rem; color: #1f77b4; }
    .edu-card { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #eee; margin-bottom: 10px; }
    .project-card-content { background-color: #f0f8ff; padding: 15px; border-radius: 10px; border-left: 5px solid #1f77b4; }
    </style>
    """, unsafe_allow_html=True)

# --- PAGE: HOME ---
def home_page():
    # Mobile Specific Toggle Instructions
    st.markdown("""
        <div class="mobile-nav-notice">
            <strong>📱 Mobile Navigation</strong><br>
            If the menu is hidden, tap the <b>Red Square Arrow</b> in the top-left corner to switch between Experience, Projects, and Contact.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    try:
        st.image(PHOTO_FILENAME, width=200) 
    except:
        st.warning("Photo not found.")

    st.markdown(f"<h1 class='main-header'>Nehil Gupta</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size:1.4rem; color:#444;'>Senior Specialist | G2 (Ex-Gartner)</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True) 
    
    st.write("---")
    st.markdown("### 👤 Professional Summary")
    st.write("""
    I am an analytical and data-driven professional with over 4 years of experience specializing in product review analytics, 
    process automation, and AI-content detection. Currently serving as a **Senior Specialist at G2**.
    """)

    st.markdown("### 🎯 Core Expertise")
    st.write("🔍 **Secondary Research** | 📊 **Data Analysis** | 📈 **Sales Operations** | ⚙️ **Process Automation**")

    st.header("🛠️ Tools & Technologies")
    st.markdown("""
        <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=microsoftpowerbi&logoColor=black" /> 
        <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" /> 
        <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> 
        <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
        """, unsafe_allow_html=True)

# --- PAGE: PROJECTS ---
def projects_page():
    st.title("📂 Key Projects")
    with st.expander("1. 🎯 VIP Account Prioritization and Whitespacing", expanded=True):
        st.markdown("""<div class='project-card-content'>
            <p><strong>Objective:</strong> Rank 963 products and identify revenue 'white spaces'.</p>
            <p><strong>Impact:</strong> Delivered interactive dashboards and identified 102 new category opportunities.</p>
        </div>""", unsafe_allow_html=True)
    with st.expander("2. 🤝 Partnership Business Development Framework"):
        st.write("Managed a $1.25M revenue target with 9% conversion rate.")
    with st.expander("3. 🏆 GDM Hackathon: AI-Driven Automation"):
        st.write("1st Place Winner. Saved 1 hour daily and unlocked $60,000+ in revenue.")
    with st.expander("4. 🤖 AI-Generated Content Detection Framework"):
        st.write("Reduced ambiguity by 95% and improved quality by 10%.")
    with st.expander("5. ⚙️ Disablement Menu Automation"):
        st.write("Increased review-publishing efficiency by 3x (16% → 48%).")

# --- PAGE: EXPERIENCE ---
def experience_page():
    st.title("💼 Professional Experience")
    with st.expander("🚀 G2 | Senior Specialist | Feb 2026 – Present", expanded=True):
        st.write("* **Strategic Enablement:** Consultant for Sales/SLT; revenue-focused analytics.")
    with st.expander("📊 Gartner (Full Tenure: 4 yrs 7 mos)"):
        with st.popover("Product Reviews Specialist"):
            st.write("* Won Hackathon 2025; Led automation for 20+ members.")
        with st.popover("Product Reviews Associate"):
            st.write("* Recognized as 'SQLNinja'; Organized ManifestGDM & KRITI.")

# --- PAGE: EDUCATION ---
def education_page():
    st.title("🎓 Education Journey")
    st.markdown("<div class='edu-card'><strong>MDI, Gurgaon</strong><br>PGDM (OPGDM) | 2023 – 2025</div>", unsafe_allow_html=True)
    st.markdown("<div class='edu-card'><strong>G.D. Goenka University</strong><br>BBA, Marketing | 2018 – 2021 | CGPA: 8.95</div>", unsafe_allow_html=True)
    st.markdown("<div class='edu-card'><strong>MM Public School</strong> | XII (CBSE): 90%</div>", unsafe_allow_html=True)
    st.markdown("<div class='edu-card'><strong>The Heritage School</strong> | X (CBSE): CGPA 9.2</div>", unsafe_allow_html=True)

# --- PAGE: ACHIEVEMENTS ---
def achievements_page():
    st.title("🏆 Achievements & Awards")
    st.success("**GDM Operations Hackathon 2025 Winner**")
    st.success("**Best Associate 2022** - Gartner")
    st.info("**Scholarship Holder:** MDI Gurgaon")
    st.info("**IELTS Band 8.5**")

# --- PAGE: CONTACT ---
def contact_page():
    st.title("📧 Contact Now")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("📞 +91 9821783999")
        st.write("✉️ [nehil30jan@gmail.com](mailto:nehil30jan@gmail.com)")
    with col2:
        try: st.image(PHOTO_FILENAME, width=120)
        except: pass
    
    st.write("---")
    st.header("✉️ Drop a Message")
    name = st.text_input("Name")
    email = st.text_input("Email")
    msg = st.text_area("Message")
    req_meeting = st.radio("Request meeting?", ["No", "Yes"], horizontal=True)
    
    if st.button("Submit Message"):
        if name and email and msg:
            st.success("Message Ready!")
            body = f"Name: {name}\nEmail: {email}\nMessage: {msg}"
            st.markdown(f'<a href="mailto:nehil30jan@gmail.com?subject=Message from {name}&body={body}" style="padding:10px; background:#1f77b4; color:white; border-radius:5px; text-decoration:none;">Send Email</a>', unsafe_allow_html=True)

# --- NAVIGATION ---
pg = st.navigation([
    st.Page(home_page, title="Home", icon="🏠"),
    st.Page(experience_page, title="Experience", icon="💼"),
    st.Page(projects_page, title="Projects", icon="📂"),
    st.Page(education_page, title="Education", icon="🎓"),
    st.Page(achievements_page, title="Achievements", icon="🏆"),
    st.Page(contact_page, title="Contact Now", icon="📧"),
])

# SIDEBAR
st.sidebar.markdown("### Quick Connect")
st.sidebar.write("✉️ [nehil30jan@gmail.com](mailto:nehil30jan@gmail.com)")
st.sidebar.write("📞 +91 9821783999")

pg.run()
