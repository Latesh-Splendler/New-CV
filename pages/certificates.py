import streamlit as st
from PIL import Image

st.title("My Certificates")

with st.expander("1. Data Structures and Algorithms Course"):
    st.write("""
    Successfully completed a course in Data Structures and Algorithms, focusing on both foundational and advanced concepts 
    that are crucial for problem-solving in tech fields.
    """)
    st.image("./pages/assets/Data.jpg", caption="Data Structures and Algorithms Certificate", width=400)  


with st.expander("2. Java Programming Course"):
    st.write("""
    Acquired in-depth knowledge in Java programming, enhancing skills in object-oriented programming, 
    concurrency, and Java frameworks.
    """)
    st.image("./pages/assets/Java.jpg", caption="Java Programming Certificate", width=400)  


with st.expander("3. Machine Learning Algorithms"):
    st.write("""
    Completed a course focused on Machine Learning and Artificial Intelligence, gaining hands-on experience 
    with algorithms and model building.
    """)
    st.image("./pages/assets/Machine.jpg", caption="Machine Learning and AI Certificate", width=400)  


with st.expander("4. Generative AI"):
    st.write("""
    Completed a course focused on  Artificial Intelligence, gaining hands-on experience 
    with algorithms and model building.
    """)
    st.image("./pages/assets/AI.jpg", caption="Generative AI Certificate", width=400)     


with st.expander("5. BlockChain"):
    st.write("""
    I am thrilled to have successfully completed the Blockchain course. 
             This journey has deepened my understanding of blockchain technology, smart contracts, and decentralized applications. 
             A special thanks to the instructors and my peers for their support and collaboration throughout the course. 
             I'm excited to apply these skills to future projects and contribute to the evolving landscape of blockchain innovation.
    """)
    st.image("./pages/assets/Block.jpg", caption="BlockChain  Certificate", width=400)     



with st.expander("6. C++ Programming"):
    st.write("""
      I am delighted to have completed a comprehensive C++ course. This experience has strengthened my skills in object-oriented programming, 
             memory management, and performance optimization, and has deepened my understanding of efficient coding practices. 
             I'm truly grateful to my instructors and peers for their guidance and support throughout the course. 
             I look forward to applying my C++ knowledge to challenging projects and further developing my programming skills in the future.

    """)
    st.image("./pages/assets/C++.jpg", caption="C++ Programming Certificate", width=400)  


with st.expander("7. C Programming"):
    st.write("""
    I am excited to have completed a rigorous course in C programming. This journey has been instrumental in strengthening my understanding of low-level programming concepts, 
             memory management, and performance optimization. I am grateful to my instructors and peers for their support and guidance throughout the course. Equipped with these skills, 
             I am eager to take on more challenging projects and apply my C programming knowledge to real-world applications.
    """)
    st.image("./pages/assets/CC.jpg", caption="C Programming Certificate", width=400)   


with st.expander("9. Introduction to JavaScript"):
    st.write("""
    I’m thrilled to have completed my JavaScript course! This journey has provided me with a strong foundation in front-end development, 
             enhancing my skills in building interactive and dynamic web applications. I am grateful to my instructors and classmates for their support 
             throughout the course. With this knowledge, I’m excited to dive deeper into web development and bring creative ideas to life through code.
    """)
    st.image("./pages/assets/Script.jpg", caption="Introduction to Javascript Certificate", width=400)   


with st.expander("10. Prompt Engineering"):
    st.write("""
   I am grateful to have completed the Prompt Engineering course, which has given me valuable insights into crafting effective prompts and optimizing AI interactions. 
             This journey has strengthened my ability to work creatively with language models, improving both the quality and accuracy of responses.
              Thank you to my mentors, peers, and everyone who made this learning experience enriching and inspiring. I'm excited to apply these skills to unlock the full potential of AI in real-world applications!
    """)
    st.image("./pages/assets/PP.jpg", caption="Prompt Engineering Certificate", width=400)     

st.write("These certifications represent my commitment to continuous learning and technical proficiency.")
