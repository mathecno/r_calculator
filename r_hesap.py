import streamlit as st
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.title('Rakı Hesap Makinesi')

day=st.number_input("Damıtılmış Alkol Yüzdesi", step=1,value=96)
kam=st.number_input("Kullanılacak alkol miktarı (ml)", step=1,value=1000)
am=round(day*kam/32000,2)
sm=int(day*kam/45-kam)
gm=round(day*kam/48000,2)
if(st.button("Hesapla")):
    st.text(f"Anason Miktarı:{am} ml")
    st.text(f"Su Miktarı:{sm} ml")
    st.text(f"Gliserin Miktarı:{gm} ml")




