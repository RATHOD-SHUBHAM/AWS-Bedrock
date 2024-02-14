import streamlit as st
from models.llama2 import llama2
from models.jurassic import jurassic

# streamlit code for viewing document
st.set_page_config(layout="wide",
                   page_title="VerseVoyage",
                   page_icon="💗",
                   )

# hide hamburger and customize footer
hide_menu = """
    <style>

    #MainMenu {
        visibility:hidden;
    }

    footer{
        visibility:visible;
    }

    footer:after{
        content: 'With 🫶️ from Shubham Shankar.';
        display:block;
        position:relative;
        color:grey;
        padding;5px;
        top:3px;
    }
    </style>

"""
# Styling ----------------------------------------------------------------------

st.image("icon.jpg", width=85)
st.title("VerseVoyage")
st.subheader("Make them laugh🥰, make them sigh🎷, with poetry on the fly🎶.")
st.write("Powered by Amazon Bedrock.")
st.markdown(hide_menu, unsafe_allow_html=True)

# Intro ----------------------------------------------------------------------

st.write(
    """

    Hi 👋, I'm **:red[Shubham Shankar]**, and welcome to my **:green[VerseVoyage]**! :rocket: , This application leverages **:blue[Amazon Bedrock]**, and its **:orange[LLMs]** to generate *poems*.  ✨

    """
)

st.markdown('---')

st.write(
    """
    ### App Interface!!

    :dog: The web app has an easy-to-use interface. 
    
    1] **:red[Choose Model]**: From the sidebar, Select the model of your choice.

    2] **:green[Generate]**: Shoot a topic, and the model will compose poem.

    """
)

st.markdown('---')

st.error(
    """
    Connect with me on [**Github**](https://github.com/RATHOD-SHUBHAM) and [**LinkedIn**](https://www.linkedin.com/in/shubhamshankar/). ✨
    """,
    icon="🧟‍♂️",
)

st.markdown('---')


st.sidebar.title("Amazon Bedrock Models 🗿")
model_name = st.sidebar.selectbox('Model of choice?', ('Llama-2', 'Jurassic-2'))

user_input = st.text_input('Poem About?', 'My Beautiful Girlfriend')

if user_input:
    if st.button('Generate'):
        st.snow()
        with st.spinner('Wait for it...'):
            if model_name == 'Llama-2':
                obj = llama2()
                response = obj.llama2(user_input=user_input)
                st.text_area(
                    "Here you go",
                    response
                )
            else:
                obj = jurassic()
                response = obj.jurassic(user_input=user_input)
                st.write(response)
        st.balloons()


st.markdown('---')

# Copyright information
st.markdown(
    """
        © Copyright 2024 Shubham Shankar 
    """
)