import streamlit as st

def display_experience():

    st.header("Academic and Professional Experience")

    with st.container():
        st.markdown(
            """
            <div class="experience-category">
                <h2>Higher Education</h2>
                <h3>XP Educação</h3>
                <p>B.S. in Systems Analysis and Development (Expected Graduation: 2025)</p>
                <p>Relevant Coursework: Software Engineering, Data Structures & Algorithms, Database Management, Web Development</p>
                <p>Key Projects:</p>
                <ul class="objectives-list">
                    <li>Developed a web application for hotel management using Spring Boot and React.</li>
                    <li>Designed and implemented a database schema for a customer relationship management (CRM) system.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with st.container():
        st.markdown(
            """
            <div class="experience-category">
                <h2>High School</h2>
                <h3>IFRN (Federal Institute of Education, Science and Technology of Rio Grande do Norte)</h3>
                <p>Technical High School Diploma in Electrotechnics (2014-2018)</p>
                <p>Relevant Coursework: Electrical Circuits, Electronics, Programming Fundamentals (C)</p>
                <p>Achievements:</p>
                <ul class="objectives-list">
                    <li>Developed a simple automation project using Arduino.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with st.container():
        st.markdown(
            """
            <div class="experience-category">
                <h2>Bootcamps & Online Courses</h2>
                <h3>DIO (Digital Innovation One)</h3>
                <p>Backend Java Bootcamp (Completed)</p>
                <p>Complete Java 2023: Object-Oriented Programming + Projects (In Progress)</p>
                <p>Skills Gained:</p>
                <ul class="objectives-list">
                    <li>Java fundamentals and object-oriented programming principles.</li>
                    <li>Spring Boot framework for building web applications and microservices.</li>
                    <li>JPA (Java Persistence API) for database interaction and data modeling.</li>
                    <li>RESTful API design and implementation.</li>
                    <li>Software testing and quality assurance practices.</li>
                    <li>Project management and Agile methodologies.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with st.container(): 
        st.markdown(
            """
            <div class="experience-category">
                <h2>Internship</h2>
                <h3>SMN (State Meteorological Network)</h3>
                <p>Software Development Intern (October 2023 - Current)</p>
                <p>Key Responsibilities & Accomplishments:</p>
                <ul class="objectives-list">
                    <li>Enhanced database skills through hands-on experience with T-SQL, C#, and data modeling.</li>
                    <li>Improving my english through language courses, immersive conversations with my teacher.</li>
                    <li>Actively preparing for the Microsoft Azure Developer Associate (AZ-204) certification.</li>
                    <li>Currently learning front-end development with a focus on AJAX and jQuery.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )