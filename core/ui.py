import streamlit as st
from core.decrypt import Decrypt
from core.encrypt import Encrypt

class HashUI:
    def __init__(self):
        st.title("Hashman 🔐#️⃣")
        st.markdown("<h5>Hashman - Your secret vault for your message, stored in URL 🔗</h5>", unsafe_allow_html=True)

        self.query_params = st.query_params
        self.secret_data = self.query_params.get("data")
        self.encrypt = Encrypt()
        self.decrypt = Decrypt()

        if self.secret_data:
            self.viewing_mode()
        else:
            pass

    def viewing_mode(self):
        st.info("A Secret Message has been sent to you")
        inputted_pwd = st.text_input("Input password to decrypt", key="decrypt_pwd", type="password")

        if st.button("Unlock"):
            decrypted = self.decrypt.decrypt_message(self.secret_data, inputted_pwd)
            if decrypted:
                st.toast("Message Decrypted!", icon="✅")
                st.code(self.decrypt, language=None)
            else:
                st.toast("Incorrect Password or Corrupted Link. Try Again!", icon="‼️")

    def creation_mode(self):
        st.subheader("Create a Secret")
        msg = st.text_input("Your Message", key="secret_msg")
        pwd = st.text_input("Password", key="secret_pwd", type="password")

        if st.button("Generate Secret Link"):
            if msg and pwd:
                encrypted = self.encrypt.encrypt_message(msg, pwd)
                base_url = "https://hashman-code.streamlit.app"
                shared_link = f"{base_url}/?data={encrypted}"

                st.write("Copy this link and share to a friend")
                st.code(shared_link)
            else:
                st.toast("Please Enter both Message and Password", icon="‼️")