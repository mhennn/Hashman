import streamlit as st
from core.decrypt import Decrypt
from core.encrypt import Encrypt

st.title("Hashman 🔐⚠️")
st.markdown("<h6>Hashman - Your secret vault for your message, stored in URL 🔗</h6>", unsafe_allow_html=True)

query_params = st.query_params
secret_data = query_params.get("data")
encrypt = Encrypt()
decrypt = Decrypt()

def viewing_mode():
    st.info("A Secret Message has been sent to you")
    inputted_pwd = st.text_input("Input password to decrypt", key="decrypt_pwd", type="password")

    if st.button("Unlock"):
        decrypted = decrypt.decrypt_message(secret_data, inputted_pwd)
        if decrypted:
            st.toast("Message Decrypted!", icon="✅")
            st.code(decrypted, language=None)
        else:
            st.toast("Incorrect Password or Corrupted Link. Try Again!", icon="‼️")

def creation_mode():
    st.subheader("Create a Secret 🕵🏻")
    cols = st.columns(2)
    with cols[0]:
        msg = st.text_input("Your Message", key="secret_msg")
    with cols[1]:
        pwd = st.text_input("Password", key="secret_pwd", type="password")

    if st.button("Generate Secret Link 🔗"):
        if msg and pwd:
            encrypted = encrypt.encrypt_message(msg, pwd)
            base_url = "https://hashman-code.streamlit.app"
            shared_link = f"{base_url}/?data={encrypted}"

            st.write("Copy this link and share to a friend 👥")
            st.code(shared_link)
        else:
            st.toast("Please Enter both Message and Password", icon="‼️")

if secret_data:
    viewing_mode()
else:
    creation_mode()