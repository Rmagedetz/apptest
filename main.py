import streamlit as st

st.set_page_config(page_title="Fast Dash", page_icon=":moneybag:", layout="wide")


def is_authenticated():
    return "authenticated" in st.session_state and st.session_state.authenticated


def login():
    with st.form("my_form"):
        st.title("Вход в приложение")
        password_input = st.text_input("Введите пароль", type="password")

        submit = st.form_submit_button("Войти")
        if submit:
            if password_input == st.secrets["database"]["password"]:
                st.success("Успешный вход!")
                st.session_state.authenticated = True
                show_main_page()
            else:
                st.error("Неверный пароль")


def show_main_page():
    st.title(" :moneybag: PowerDash")
    st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)
    st.write("dsf")


if not is_authenticated():
    login()
else:
    show_main_page()
