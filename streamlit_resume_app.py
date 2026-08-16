"""
Vaibhav Dang — Interactive Resume Website
Run with:  streamlit run streamlit_resume_app.py
"""

import streamlit as st

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Vaibhav Dang | Resume",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# STYLING
# ----------------------------------------------------------------------------
st.markdown("""
<style>
    .main { background-color: #ffffff; }
    h1, h2, h3 { color: #1F3864; }
    .accent-line {
        border: none;
        height: 3px;
        background-color: #1F3864;
        margin: 0.2rem 0 1.2rem 0;
    }
    .pill {
        display: inline-block;
        background-color: #EAF0FA;
        color: #1F3864;
        border-radius: 14px;
        padding: 5px 14px;
        margin: 4px 6px 4px 0;
        font-size: 0.85rem;
        font-weight: 500;
    }
    .job-title { font-size: 1.15rem; font-weight: 700; color: #333333; margin-bottom: 0; }
    .job-meta { font-style: italic; color: #666666; margin-top: 0; }
    .achievement-box {
        background-color: #F7F9FC;
        border-left: 4px solid #1F3864;
        padding: 14px 18px;
        border-radius: 6px;
        margin-bottom: 10px;
    }
    .stat-card {
        background-color: #F7F9FC;
        border: 1px solid #E3E3E3;
        border-radius: 10px;
        padding: 16px 10px;
        text-align: center;
        height: 100%;
        margin-bottom: 12px;
    }
    .stat-number {
        font-size: 1.8rem;
        font-weight: 800;
        color: #1F3864;
        line-height: 1.1;
        word-wrap: break-word;
    }
    .stat-label {
        font-size: 0.85rem;
        color: #555555;
        margin-top: 4px;
        font-weight: 600;
    }
    .project-card {
        background-color: #FAFAFA;
        border: 1px solid #E3E3E3;
        border-radius: 10px;
        padding: 18px 20px;
        margin-bottom: 18px;
    }
    .project-title { color: #1F3864; font-size: 1.1rem; font-weight: 700; }
    a { color: #1F3864; }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# DATA
# ----------------------------------------------------------------------------
CONTACT = {
    "name": "Vaibhav Dang",
    "title": "Senior Data Analyst | Revenue & Pricing Analyst | Commercial Strategy Analyst | Aviation Industry",
    "location": "New Delhi, India",
    "phone": "+91 8800371993",
    "email": "vaibhav95dang@gmail.com",
    "linkedin": "https://www.linkedin.com/",  # replace with actual profile URL
    "open_to": "Open to relocation | Visa sponsorship / work permit required",
}

SUMMARY = (
    "Commercial Analytics professional with 6+ years of experience in the aviation industry "
    "delivering data-driven insights, revenue optimization strategies, and commercial strategy "
    "analysis across large-scale portfolios. Currently a Senior Data Analyst at United Airlines, "
    "responsible for revenue analytics, pricing strategy, yield optimization, and commercial "
    "decision-making across a $750M+ GNF agency portfolio, with previous experience supporting "
    "British Airways commercial analytics teams. Expertise spans three core disciplines: "
    "Data Analytics (SQL, Python, Power BI, Tableau, Databricks), Revenue & Pricing Analysis "
    "(Yield, RASK, Load Factor, dynamic pricing, demand forecasting), and Commercial Strategy "
    "(go-to-market planning, stakeholder engagement, KPI frameworks, executive reporting)."
)

SKILLS = {
    "Data Analytics": ["SQL (Oracle, Teradata, AWS Redshift)", "Python (Pandas, NumPy, Matplotlib, Scikit-learn)",
                        "Databricks", "EDA & Statistical Analysis", "Large datasets (50M+ records)"],
    "Revenue & Pricing": ["Yield Optimization", "RASK", "Load Factor / PLF", "Dynamic Pricing",
                           "Demand Forecasting", "Route Performance", "Revenue Integrity"],
    "Commercial Strategy": ["Go-to-Market Planning", "Growth Analysis", "Commercial KPI Frameworks",
                             "Agency Performance", "Competitive Intelligence", "Market Share Analysis"],
    "BI & Visualization": ["Power BI", "Tableau", "Executive Reporting", "KPI Tracking", "Data Visualization"],
    "Excel & Office Suite": ["Advanced Excel (Pivot Tables, VLOOKUP, VBA, Power Query)", "PowerPoint", "Google Sheets"],
    "Stakeholder Management": ["Senior Leadership Engagement", "Executive QBRs", "Cross-Functional Collaboration"],
}

EXPERIENCE = [
    {
        "title": "Senior Data Analyst — Commercial Strategy & Revenue Analytics",
        "company": "United Airlines, Gurugram",
        "dates": "Jan 2023 – Present",
        "context": "Aviation industry — data analytics, revenue & pricing analysis, and commercial strategy "
                    "across a $750M+ GNF agency portfolio. SQL, Python, Databricks, Power BI, AWS Redshift.",
        "bullets": [
            "Delivered revenue analytics and pricing strategy insights across a $750M+ GNF agency portfolio, "
            "protecting ~2% market share in key competitive regions worth tens of millions in retained annual revenue.",
            "Built and maintained Power BI dashboards and automated reporting pipelines, reducing manual reporting "
            "workload by 40% and enabling 2x faster commercial decision-making across 10+ stakeholder groups.",
            "Developed and executed go-to-market planning and growth analysis frameworks with Sales, Finance, "
            "Operations, and Marketing, delivering recommendations adopted into quarterly executive planning cycles.",
            "Designed and implemented SQL-based ETL pipelines and a dimension-based data warehouse (50M+ records) "
            "on Databricks, improving forecast accuracy and saving 20+ analyst hours per month.",
            "Built a consolidated DDS dashboard covering both international and domestic markets end-to-end "
            "using SQL, Python, and Power BI, unifying fragmented reporting into a single source of truth.",
            "Worked with MIDT data sources to build a ticket performance dashboard for the international market, "
            "giving commercial teams visibility into booking and ticketing trends by route and segment.",
            "Led A/B statistical testing (Z-test, 95% confidence interval) to validate revenue optimization "
            "opportunities, securing full expansion of a high-value tactical sales program.",
            "Delivered agency QBR presentations and executive performance updates, translating complex analytical "
            "output into clear, data-driven narratives for non-technical senior audiences.",
        ],
    },
    {
        "title": "Data Analyst — Revenue Performance & Commercial Analytics",
        "company": "WNS Global Services (British Airways account), Gurugram",
        "dates": "Dec 2021 – Sep 2022",
        "context": "Revenue analytics, pricing analysis, and commercial strategy for British Airways. SQL, Power BI, Python.",
        "bullets": [
            "Delivered revenue analytics and commercial strategy insights, increasing analytical visibility "
            "for commercial leadership by 50%.",
            "Supported commercial forecasting cycles and variance analysis, contributing to an 8% improvement "
            "in client retention.",
            "Built and maintained revenue performance dashboards, improving financial reporting cycle "
            "efficiency by 20%.",
            "Collaborated with Sales, Marketing, and commercial teams on go-to-market planning and pricing strategy.",
        ],
    },
    {
        "title": "Sales Operations & Analytics Analyst",
        "company": "AdPushup, New Delhi",
        "dates": "Mar 2021 – Dec 2021",
        "context": "",
        "bullets": [
            "Built 12+ advanced Excel and SQL analytical models for commercial strategy and pricing analysis, "
            "improving reporting accuracy by 98% and delivering insights 50% faster.",
        ],
    },
    {
        "title": "Business Intelligence & Commercial Analyst",
        "company": "Macro Analytics Technologies, New Delhi",
        "dates": "Oct 2017 – Jul 2019",
        "context": "",
        "bullets": [
            "Designed 15 Power BI dashboards and SQL data models delivering revenue and pricing performance "
            "insight to senior stakeholders, improving revenue by 12% and saving 10+ analyst hours weekly.",
        ],
    },
    {
        "title": "Data & Commercial Analyst",
        "company": "Evalueserve, Gurugram",
        "dates": "Mar 2017 – Oct 2017",
        "context": "",
        "bullets": [
            "Developed 20+ SQL-based KPI trackers and Excel models for senior leadership performance monitoring, "
            "improving reporting efficiency by 30%.",
        ],
    },
]

PROJECTS = [
    {
        "title": "Agency Segmentation Using K-Means Clustering",
        "tools": "Python (Pandas, NumPy, Scikit-learn)",
        "description": (
            "Applied K-Means clustering to segment a $750M+ agency portfolio by booking behavior, yield "
            "contribution, and demand volatility — identifying distinct customer/agency tiers for differentiated "
            "pricing and account treatment. Validated cluster quality via silhouette analysis and iterative "
            "feature selection, then translated cluster profiles into targeted commercial recommendations "
            "presented to senior stakeholders."
        ),
    },
    {
        "title": "End-to-End Commercial Analytics Pipeline",
        "tools": "SQL, Power BI, Databricks",
        "description": (
            "Designed a SQL-based ETL pipeline and dimension-based data warehouse on Databricks (50M+ records), "
            "consolidating booking, pricing, and market data into a single analytics-ready source. Built Power BI "
            "dashboards on top of the pipeline for daily/weekly/monthly performance views, cutting manual "
            "reporting workload by 40% and enabling 2x faster decision-making."
        ),
    },
    {
        "title": "Consolidated DDS Dashboard — International & Domestic Markets",
        "tools": "SQL, Python, Power BI",
        "description": (
            "Built a consolidated DDS dashboard end-to-end covering both international and domestic markets, "
            "unifying previously fragmented reporting into a single view for commercial and sales teams."
        ),
    },
    {
        "title": "MIDT-Based Ticket Performance Dashboard — International Market",
        "tools": "MIDT data source, SQL, Power BI",
        "description": (
            "Worked with MIDT data to build a ticket performance dashboard for the international market, "
            "surfacing booking and ticketing trends by route and segment for commercial decision-making."
        ),
    },
]

EDUCATION = [
    {
        "degree": "PGDM — Business Analytics & Marketing",
        "school": "2019 – 2021",
        "details": "Specialization: Revenue Analytics, Commercial Strategy, Data Science | Modules: Pricing "
                    "Strategy, Demand Forecasting, Statistical Methods, Data Visualization, Go-to-Market Strategy",
    },
    {
        "degree": "B.A. (Hons.) Economics",
        "school": "Sri Guru Gobind Singh College of Commerce, Delhi University | 2013 – 2016",
        "details": "Coursework: Econometrics, Quantitative Methods, Probability & Statistics, Market Demand "
                    "Analysis, Mathematical Economics, International Trade",
    },
]

CERTIFICATIONS = [
    "Databricks SQL & Data Engineering — large-scale data analytics, ETL pipelines, reporting infrastructure",
    "Actuarial CT-3: Probability & Statistics | CT-6: Statistical Methods",
    "Power BI & Tableau (Advanced) — dashboard design, data visualization, automated insight solutions",
    "Advanced Excel — Pivot Tables, VLOOKUP, VBA, Power Query, simulations, commercial models",
]

ACHIEVEMENTS = [
    {"stat": "$750M+", "label": "Portfolio Managed",
     "desc": "Annual GNF agency revenue portfolio managed through data analytics, revenue & pricing analysis, "
             "and commercial strategy"},
    {"stat": "~2%", "label": "Market Share Protected",
     "desc": "Protected through pricing strategy, competitive intelligence, and go-to-market analysis — "
             "worth tens of millions annually"},
    {"stat": "40%", "label": "Efficiency Gain",
     "desc": "Automated Power BI dashboards and SQL pipelines reduced reporting workload"},
    {"stat": "30%", "label": "Retention Lift",
     "desc": "Python and Power BI early-warning system driving proactive commercial adjustments"},
    {"stat": "6+ yrs", "label": "Aviation Experience",
     "desc": "Aviation industry experience across United Airlines and British Airways"},
]

# ----------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# ----------------------------------------------------------------------------
with st.sidebar:
    st.markdown(f"## {CONTACT['name']}")
    st.caption(CONTACT["title"])
    st.write(f"📍 {CONTACT['location']}")
    st.write(f"📞 {CONTACT['phone']}")
    st.write(f"✉️ {CONTACT['email']}")
    st.write(f"🔗 [LinkedIn]({CONTACT['linkedin']})")
    st.info(CONTACT["open_to"])
    st.markdown("---")
    page = st.radio(
        "Navigate",
        ["About", "Experience", "Projects", "Skills", "Education & Certifications", "Achievements", "Contact"],
        label_visibility="collapsed",
    )

    # Optional: resume download button if a PDF/DOCX is placed alongside this script
    st.markdown("---")
    st.caption("Tip: add your resume file to this folder and enable the download button in the code.")

# ----------------------------------------------------------------------------
# HEADER (always visible)
# ----------------------------------------------------------------------------
st.markdown(f"# {CONTACT['name']}")
st.markdown(f"#### {CONTACT['title']}")
st.markdown("<hr class='accent-line'>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# PAGE: ABOUT
# ----------------------------------------------------------------------------
if page == "About":
    st.header("Professional Summary")
    st.write(SUMMARY)

    st.markdown("### Snapshot")
    # Render in rows of 3 so long labels never get clipped
    for i in range(0, len(ACHIEVEMENTS), 3):
        row = ACHIEVEMENTS[i:i + 3]
        cols = st.columns(len(row))
        for col, item in zip(cols, row):
            with col:
                st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-number">{item['stat']}</div>
                    <div class="stat-label">{item['label']}</div>
                </div>
                """, unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# PAGE: EXPERIENCE
# ----------------------------------------------------------------------------
elif page == "Experience":
    st.header("Professional Experience")
    for job in EXPERIENCE:
        st.markdown(f"<p class='job-title'>{job['title']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='job-meta'>{job['company']} &nbsp;|&nbsp; {job['dates']}</p>", unsafe_allow_html=True)
        if job["context"]:
            st.caption(job["context"])
        for b in job["bullets"]:
            st.markdown(f"- {b}")
        st.markdown("---")

# ----------------------------------------------------------------------------
# PAGE: PROJECTS
# ----------------------------------------------------------------------------
elif page == "Projects":
    st.header("Key Projects")
    for proj in PROJECTS:
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title">{proj['title']}</div>
            <div style="color:#666; font-style: italic; margin-bottom: 8px;">{proj['tools']}</div>
            <div>{proj['description']}</div>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# PAGE: SKILLS
# ----------------------------------------------------------------------------
elif page == "Skills":
    st.header("Core Skills")
    for category, items in SKILLS.items():
        st.subheader(category)
        pills_html = "".join([f"<span class='pill'>{item}</span>" for item in items])
        st.markdown(pills_html, unsafe_allow_html=True)
        st.write("")

# ----------------------------------------------------------------------------
# PAGE: EDUCATION & CERTIFICATIONS
# ----------------------------------------------------------------------------
elif page == "Education & Certifications":
    st.header("Education")
    for edu in EDUCATION:
        st.markdown(f"**{edu['degree']}**")
        st.caption(edu["school"])
        st.write(edu["details"])
        st.write("")

    st.header("Certifications & Professional Development")
    for cert in CERTIFICATIONS:
        st.markdown(f"- {cert}")

# ----------------------------------------------------------------------------
# PAGE: ACHIEVEMENTS
# ----------------------------------------------------------------------------
elif page == "Achievements":
    st.header("Key Achievements at a Glance")
    for item in ACHIEVEMENTS:
        st.markdown(f"""
        <div class="achievement-box">
            <strong>{item['stat']} — {item['label']}</strong><br>{item['desc']}
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# PAGE: CONTACT
# ----------------------------------------------------------------------------
elif page == "Contact":
    st.header("Get in Touch")
    st.write(f"📍 **Location:** {CONTACT['location']}")
    st.write(f"📞 **Phone:** {CONTACT['phone']}")
    st.write(f"✉️ **Email:** {CONTACT['email']}")
    st.write(f"🔗 **LinkedIn:** [{CONTACT['linkedin']}]({CONTACT['linkedin']})")
    st.info(CONTACT["open_to"])

    with st.form("contact_form"):
        st.write("Send a quick message (this form is for display purposes — connect it to an email "
                  "service like SendGrid or Formspree to make it functional):")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("Thanks for reaching out! (Wire this form up to an email/API backend to make it live.)")

# ----------------------------------------------------------------------------
# FOOTER
# ----------------------------------------------------------------------------
st.markdown("<hr class='accent-line'>", unsafe_allow_html=True)
st.caption(f"© {CONTACT['name']} — Built with Streamlit")
