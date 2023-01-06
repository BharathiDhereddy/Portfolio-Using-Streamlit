import streamlit as st
from PIL import Image

with open("styles.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Bharathi Dhereddy
##### *Resume* 
''')

image = Image.open('Sample.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- I'm Bharathi and I'm pursuing my BTech 3rd year at GVPCEW. I am passionate about Machine learning and interested in Web development.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="www.linkedin.com/in/bharathi-dhereddy-0b4a05222" target="_blank">Bharathi Dhereddy</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**CSE-AI&ML**-*Gayatri Vidya Parishad College Of Engineering For Women*','2020-2024')
st.markdown('''
- GPA: `8.00`
''')
txt('**MPC**-*Sri Chaitanya Junior College*','2018-2020')
st.markdown('''
- GPA: `9.75`
''')

txt('**Schooling**-*Nallas Vidya Niketan*','2018')
st.markdown('''
- GPA: `9.8`
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**GDSC GVPCEW**-Web Dev Core Member',
'2022-2023')
txt('**Sparks Internship**-Data Science & Business Analytics',
'2022')
txt('**Verzeo Internship**-ML with python',
'2022')

txt('**Hackathon**-Sushant University','2022')
st.markdown('''
- The project I am working on is FoodWaste Management.This hackathon is organized by Sushant University.
''')

txt('**AIML Project**','2022')
st.markdown('''
- A key objective of my project is to determine the number of followers a Twitter account has.
''')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `C`, `Java`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Web development', '`HTML`, `CSS`')
txt3('Web Framework','`Django Basics`')


#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'www.linkedin.com/in/bharathi-dhereddy-0b4a05222')
txt2('GitHub', 'https://github.com/BharathiDhereddy')
txt2('Email','bharathidhereddy27@gmail.com')