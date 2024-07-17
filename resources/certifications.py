import streamlit as st

def display_certifications():

    st.header("Certifications")

    st.markdown(
        """
        <div class="list-container">
            <h2 class="subtitle">Microsoft Certified: Azure Developer Associate</h2>
            <p>This certification proves my skills in creating, building, testing, and managing cloud-based apps and services on Microsoft Azure.</p>
            <p>Key areas I learned and improved during my preparation:</p>
            <ul class="objectives-list">
                <li>Deeper knowledge of Azure's main services, storage, security, message processing etc.</li>
                <li>Learned how to design and build apps that can grow with the business, using Azure tools.</li>
                <li>Got better at making sure cloud apps are secure.</li>
                <li>Practiced with real-world examples and tests to get ready.</li>
            </ul>
            <p><a class="link-externo" href="https://drive.google.com/file/d/1UTwKxZVKNmWrncAPRT--Yg7UP6-kVlnV/view?usp=sharing" target="_blank">View Certificate</a></p>
        </div>

        <div class="list-container">
            <h2 class="subtitle">Scrum Foundation Professional Certificate (SFPC) - CertiProf</h2>
            <p>This certificate shows that I understand how Scrum works—its ideas, the jobs people do, the meetings, and the results it aims for. It proves I can work well in a Scrum team and help projects succeed.</p>
            <p><a class="link-externo" href="https://drive.google.com/file/d/1xSqqDA_6BH80r8qVwNhqEL4epTsmrWZ_/view?usp=sharing" target="_blank">View Certificate</a></p>
        </div>

        <div class="list-container">
            <h2 class="subtitle">Scrum Fundamentals Certified (SFC) - SCRUMstudy</h2>
            <p>This certificate proves my knowledge of the basics of Scrum, like its values, ideas, and how it's done. It shows I can use Scrum for different projects and help Agile teams do well.</p>
            <p><a class="link-externo" href="https://drive.google.com/file/d/195kV3wHsu3v5vlxXITrEm-eQub9tOb6W/view?usp=sharing" target="_blank">View Certificate</a></p>
        </div>

        <div class="list-container">
            <h2 class="subtitle">Bootcamp Santander - Backend Java 2023</h2>
            <p>This intense bootcamp, a partnership with Digital Innovation One (DIO), gave me in-depth training in backend development using Java. I learned the key ideas and tools for making strong, adaptable Java applications.</p>
            <p>Main topics and skills I learned:</p>
            <ul class="objectives-list">
                <li>Basics of Java and how to program with objects.</li>
                <li>Spring Boot framework for building web apps and smaller services.</li>
                <li>JPA (Java Persistence API) for working with databases and data.</li>
                <li>How to design and build RESTful APIs.</li>
                <li>Good practices for testing and making sure software is high quality.</li>
                <li>How to manage projects and use Agile methods.</li>
            </ul>
            <p><a class="link-externo" href="https://drive.google.com/file/d/18QqAxiano_VozkKSt_Ae4Nonns69hFDB/view?usp=sharing" target="_blank">View Certificate</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )