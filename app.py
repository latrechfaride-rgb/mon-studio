import streamlit as st

st.set_page_config(page_title="Mon Studio Vidéo", layout="wide")

st.title("🎬 Mon Studio Vidéo IA")
st.caption("L'usine à gaz qui fait tout !")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "1. 📜 Scénario", 
    "2. 🎨 Branding", 
    "3. 👤 Personnages", 
    "4. 🎥 Vidéo", 
    "5. 🎙️ Audio", 
    "6. 🚀 Montage"
])

with tab1:
    st.header("L'Histoire")
    st.text_area("Écris ton idée de film ici :", "Un homme pauvre achète une épave...")
    st.selectbox("Style", ["Cinéma", "Dessin animé", "Documentaire"])

with tab2:
    st.header("Les Génériques")
    st.text_input("Titre du film", "Mon Super Film")
    st.text_input("Sous-titre", "Une aventure incroyable")

with tab3:
    st.header("Les Personnages")
    st.file_uploader("Photo du héros", type=["jpg", "png"])

with tab4:
    st.header("La Caméra")
    st.selectbox("Moteur IA", ["Wan 2.1", "Kling", "Luma"])
    st.button("Générer les vidéos !")

with tab5:
    st.header("Le Son")
    st.selectbox("Voix", ["Homme", "Femme", "Enfant"])
    st.file_uploader("Musique (MP3)", type=["mp3"])

with tab6:
    st.header("Le Montage Final")
    st.success("Tout est prêt pour l'assemblage !")
    if st.button("🎬 Lancer le rendu final"):
        st.warning("C'est parti pour le montage...")