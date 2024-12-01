import streamlit as st
from service.blob_service import upload_blob
from service.credit_card_service import analize_credit_card


def configure_interface():
    st.title("Upload de arquivo - desafio anti fraude")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
       fileName = uploaded_file.name

       blob_url = upload_blob(uploaded_file, fileName)
       if blob_url:
           st.write("arquivo {fileName} foi enviado com sucesso")
           credit_card_info = analize_credit_card(blob_url)
           show_image_and_validation(blob_url, credit_card_info)
       else:
           st.write("erro ao enviar o arquivo para {fileName}")

def show_image_and_validation(blob_url, credit_card_info):
  st.image(blob_url, caption="imagem enviada", use_column_width=True)
  st.write("Resultado da validação:")
  if credit_card_info and credit_card_info["card_name"]:
      st.markdown(f"<h1 stryle'color: green;'>Cartão valido</h1>", unsafe_allow_html=True)
      st.write(f"Nome do titular: {credit_card_info["card_name"]}")
  st.write("Informações de cartão de credito encontradas")
  st.write(credit_card_info)

if __name__ == "__main__" :
    configure_interface()