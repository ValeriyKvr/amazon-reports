import streamlit as st

st.set_page_config(
    page_title="Amazon Reports",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Amazon Reports")
st.markdown("---")

st.markdown("""
### Оберіть звіт у меню ліворуч:

- **Returns Analysis** — аналіз причин повернень по ASIN

---
*Для переходу між звітами використовуйте бічну панель навігації.*
""")
