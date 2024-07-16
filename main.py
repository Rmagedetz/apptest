import streamlit as st

# Заголовок и настройки приложения Streamlit
st.title("Получение Telegram ID")


# Функция для получения Telegram ID из параметров запроса URL
def get_telegram_id():
    telegram_id = st.query_params.get("telegram_id")
    if telegram_id:
        st.success(f"Telegram ID: {telegram_id}")
    else:
        st.error("Telegram ID не найден в параметрах URL")


# Вызов функции
get_telegram_id()
