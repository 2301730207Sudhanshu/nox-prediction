import streamlit as st

def show():

    # ================= ADVANCED CSS =================
    st.markdown("""
    <style>

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: 900;
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        text-align: center;
        color: #aaa;
        margin-bottom: 30px;
    }

    .card {
        background: rgba(255,255,255,0.04);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.08);
        transition: 0.4s;
    }

    .card:hover {
        transform: translateY(-8px);
        box-shadow: 0px 12px 30px rgba(0,198,255,0.25);
        border: 1px solid rgba(0,198,255,0.4);
    }

    .name {
        font-size: 22px;
        font-weight: 700;
    }

    .role {
        color: #00c6ff;
        font-size: 14px;
        margin-bottom: 10px;
    }

    .id {
        font-size: 13px;
        color: #aaa;
    }

    .contact-box {
        margin-top: 10px;
        font-size: 13px;
        color: #bbb;
    }

    .divider {
        margin: 30px 0;
        height: 1px;
        background: linear-gradient(to right, transparent, #00c6ff, transparent);
    }

    </style>
    """, unsafe_allow_html=True)

    # ================= HEADER =================
    st.markdown('<div class="title">👨‍💻 Meet Our Team</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Building Intelligent Systems for Smart Environments</div>', unsafe_allow_html=True)

    # ================= TEAM LEADER =================
    st.markdown("## ⭐ Team Leader")

    with st.container(border=True):
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image("Research images/Figure 16.png", width=170)

        with col2:
            st.markdown("### Sudhanshu Ranjan Singh")
            st.markdown(
                '🆔 2301730207 | 🎓 <a href="https://www.krmangalam.edu.in/" target="_blank">KR Mangalam University</a>',
                unsafe_allow_html=True
                )
            st.markdown("🚀 **AI/ML Engineer & Full Stack Developer**")

            st.write("""
            Leading the development of an **AI-powered NOx prediction system**, integrating 
            machine learning, backend systems, and interactive dashboards.
            """)
            st.success("""
### ✔ Key Responsibilities

• Built and fine-tuned ML models using Random Forest  
• Developed scalable backend APIs with FastAPI  
• Led end-to-end system integration (ML + Backend + Frontend)  
• Implemented Explainable AI (SHAP, LIME) for interpretability  
• Handled authentication and database management  
""")

            # ===== SOCIAL BUTTONS =====
            c1, c2, c3 = st.columns(3)
            with c1:
                st.link_button("🐙 GitHub", "https://github.com/2301730207Sudhanshu")
            with c2:
                st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/sudhanshu-ranjan-singh-b2758a34b/")
            with c3:
                with open("Research images/Figure 20.pdf", "rb") as file:
                    st.download_button(
                        label="📄 Resume",
                        data=file,
                        file_name="Figure 20.pdf",
                        mime="application/pdf"
        )
            # ===== CONTACT =====
            st.markdown("""
<div class="contact-box">
📧 Email: your-2301730207@krmu.edu.in <br>
📞 Phone: +91-9560702588
</div>
""", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # ================= TEAM MEMBERS =================
    st.markdown("## 👥 Core Team Members")

    col1, col2 = st.columns(2)

    # -------- Member 2 --------
    with col1:
        with st.container(border=True):
            st.image("Research images/Figure 18.png", width=130)

            st.markdown("### Nikhil")
            st.markdown(
                '🆔 2301730218 | 🎓 <a href="https://www.krmangalam.edu.in/" target="_blank">KR Mangalam University</a>',
                unsafe_allow_html=True
                )
            st.markdown("📊 **Research & Domain Analyst**")
            st.info("""
### 🎯 Key Research Responsibilities

• Performed in-depth problem analysis and domain understanding  
• Reviewed and synthesized relevant research literature  
• Identified limitations and gaps in existing methodologies  
• Defined research objectives and project scope strategically  
""")

            c1, c2, c3 = st.columns(3)
            c1.link_button("🐙 GitHub", "https://github.com/")
            c2.link_button("💼 LinkedIn", "https://www.linkedin.com/in/nikhil-k-b77157308/")
            with c3:
                with open("Research images/Figure 21.pdf", "rb") as file:
                    st.download_button(
                        label="📄 Resume",
                        data=file,
                        file_name="Figure 21.pdf",
                        mime="application/pdf"
                        )

            st.markdown("""
<div class="contact-box">
📧 Email: your-nikhilkoyiri@gmail.com <br>
📞 Phone: +91-7011994592
</div>
""", unsafe_allow_html=True)

    # -------- Member 3 --------
    with col2:
        with st.container(border=True):
            st.image("Research images/Figure 19.png", width=130)

            st.markdown("### Aditya Mishra")
            st.markdown(
                '🆔 2301730258 | 🎓 <a href="https://www.krmangalam.edu.in/" target="_blank">KR Mangalam University</a>',
                unsafe_allow_html=True
                )
            st.markdown("⚙️ **Data Engineer & System Architect**")
            st.info("""
### 🎯 Key Responsibilities

• Collected and aggregated data from sources such as OpenAQ and other datasets  
• Performed data preprocessing, cleaning, and transformation  
• Engineered meaningful features to enhance model performance  
• Designed the overall system architecture for efficient data flow and integration  
""")

            c1, c2, c3 = st.columns(3)
            c1.link_button("🐙 GitHub", "https://github.com/2301730258Aditya")
            c2.link_button("💼 LinkedIn", "https://www.linkedin.com/in/adityaaiengineer/")
            with c3:
                with open("Research images/Figure 22.pdf", "rb") as file:
                    st.download_button(
                        label="📄 Resume",
                        data=file,
                        file_name="Figure 22.pdf",
                        mime="application/pdf"
                        )

            st.markdown("""
<div class="contact-box">
📧 Email: your-adityamishra265@gmail.com <br>
📞 Phone: +91-8708052246
</div>
""", unsafe_allow_html=True)

    # -------- Member 4 --------
    st.markdown("")

    col3, col4 = st.columns(2)

    with col3:
        with st.container(border=True):
            st.image("Research images/Figure 17.png", width=130)

            st.markdown("### Rohit Kumar")
            st.markdown(
                '🆔 2301730220 | 🎓 <a href="https://www.krmangalam.edu.in/" target="_blank">KR Mangalam University</a>',
                unsafe_allow_html=True
                )
            st.markdown("🌐 **Deployment & Full-Stack Engineer**")
            st.info("""
### 🎯 Key Responsibilities

• Developed and maintained backend services using Flask  
• Integrated machine learning models with the user interface  
• Designed interactive dashboards and data visualizations  
• Managed final system deployment and performance optimization  
""")

            c1, c2, c3 = st.columns(3)
            c1.link_button("🐙 GitHub", "#")
            c2.link_button("💼 LinkedIn", "#")
            c3.link_button("📄 Resume", "#")

            st.markdown("""
<div class="contact-box">
📧 Email: your-email@example.com <br>
📞 Phone: +91-XXXXXXXXXX
</div>
""", unsafe_allow_html=True)

    # ================= FOOTER =================
    st.markdown("---")
    st.caption("🚀 Built with AI, Data Science & Innovation | Team Project | 2026")