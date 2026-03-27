import streamlit as st

# 1. Buat Dictionary job_requirements
job_requirements = {
    "Data Scientist": ["Python", "Math", "AI", "SQL"],
    "Web Dev": ["JS", "HTML", "CSS", "React"],
    "Cyber Security": ["Linux", "Networking", "Python", "Encryption"],
    "UI/UX Designer": ["Figma", "User Research", "Prototyping", "Adobe XD"]
}

st.title("LinkedIn Skill Matcher 🚀")

# 2. Input di Streamlit
user_skills_input = st.text_input("Masukkan skill yang kamu miliki (pisahkan dengan koma):", "Python, SQL, HTML")

if user_skills_input:
    # Membersihkan input user (hapus spasi berlebih dan ubah ke list)
    user_skills = [s.strip().lower() for s in user_skills_input.split(",")]
    
    st.subheader("Persentase Kecocokan:")
    
    # 3 & 4. Membandingkan skill dan Output
    for job, reqs in job_requirements.items():
        # Menghitung berapa banyak skill user yang ada di requirement (case-insensitive)
        matched_skills = [skill for skill in reqs if skill.lower() in user_skills]
        
        # Hitung persentase
        score = (len(matched_skills) / len(reqs)) * 100
        
        # Tampilan hasil
        st.write(f"**{job}**: {score:.0f}% cocok")
        st.progress(score / 100)