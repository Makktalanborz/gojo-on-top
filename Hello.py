import streamlit as st
st.title("Első weboldalunk")

st.write("Clash of Clans egy rohadt jó játék")

gomb = st.button("Nyomj meg")
if gomb:
    st.write("Nah I'd Win")
like = st.checkbox("You are the honored one?")

gomb2 = st.button("Submit")
if gomb2:
    if like:
        st.write("Hazudsz")
    else:
        st.write("Igazad van")




st.header("Ki erősebb gojo vagy sukuna vagy toji")
kaisen = st.radio("Na ki az erősebb?", ("Sukuna", "Gojo", "Toji"))
gomb3 = st.button("Nah I'd Win")
if gomb3:
    st.write(kaisen)
    if kaisen == "Gojo":
        st.write("Trought Heaven And Earth I Alone Am The Honored One")
st.header("Grand Kasien")
valaszok = st.multiselect("Mikor Jön Ki A Grand Kaisen Update?",["Soha", "Ezen A Héten", "Jövő Héten"])
gomb4 = st.button("Khm")
if gomb4:
    st.write(valaszok)


st.header("Csúszka xD")
valami = st.slider("IDK", 1,100, 10)
if st.button("gombocska"):
    st.write(valami)

st.header("Gojo")
valaszod = st.text_input("Melyik JJK Karakter A Legjobb?", "Toji")
if st.button("Nem birom már"):
    st.write("szerintem is")

számok = st.number_input("random számok")
if st.button("számok"):
    st.write(számok)