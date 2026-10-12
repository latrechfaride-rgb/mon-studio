
import streamlit as st
import requests

st.set_page_config(page_title="Mon Studio Vidéo", layout="wide")

st.title("🎬 Mon Studio Vidéo IA")
st.caption("L'usine à gaz qui fait tout !")

# --- CONNEXION AUX APIS ---
api_key_openrouter = st.secrets.get("OPENROUTER_API_KEY", None)
api_key_fal = st.secrets.get("FAL_KEY", None)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "1. 📜 Scénario", "2. 🎨 Branding", "3. 👤 Personnages", 
    "4. 🎥 Vidéo", "5. 🎙️ Audio", "6. 🚀 Montage"
])

# --- FONCTION POUR GÉNÉRER UNE IMAGE AVEC FAL.AI ---
def generer_image_fal(prompt):
    url = "https://fal.run/fal-ai/flux/schnell"
    headers = {
        "Authorization": f"Key {api_key_fal}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "image_size": "landscape_16_9",
        "num_images": 1
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["images"][0]["url"]
    else:
        return None

# --- ONGLET 1 : SCÉNARIO ---
with tab1:
    st.header("L'Histoire")
    prompt = st.text_area("Écris ton idée de film ici :", "Un homme pauvre achète une épave...")
    style = st.selectbox("Style", ["Cinéma", "Dessin animé", "Documentaire"])
    
    if st.button("🪄 Générer le Scénario avec l'IA"):
        if not api_key_openrouter:
            st.error("⚠️ Il manque ta clé OpenRouter.")
        else:
            with st.spinner("L'IA réfléchit..."):
                response = requests.post(
                    url="https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {api_key_openrouter}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "model": "openai/gpt-3.5-turbo",
                        "messages": [
                            {"role": "system", "content": "Tu es un scénariste. Découpe l'histoire en 3 scènes courtes avec descriptions."},
                            {"role": "user", "content": f"Style: {style}. Histoire: {prompt}"}
                        ]
                    }
                )
                if response.status_code == 200:
                    resultat = response.json()['choices'][0]['message']['content']
                    st.session_state.scenario = resultat
                    st.success("✅ Scénario généré !")
                    st.write(resultat)
                else:
                    st.error(f"Erreur : {response.text}")

# --- ONGLET 4 : GÉNÉRATION VIDÉO (IMAGES) ---
with tab4:
    st.header("Génération des Images")
    st.info("Chaque scène de ton scénario va devenir une image de cinéma.")
    
    if "scenario" not in st.session_state:
        st.warning("Va d'abord dans l'onglet 1 et génère un scénario.")
    else:
        if st.button("🎨 Générer les Images des Scènes"):
            if not api_key_fal:
                st.error("⚠️ Il manque ta clé Fal.ai.")
            else:
                texte = st.session_state.scenario
                scenes = []
                if "Scène 1" in texte:
                    parts = texte.split("Scène")
                    for p in parts[1:]:
                        if ":" in p:
                            scenes.append(p.split(":", 1)[1].strip())
                
                if len(scenes) == 0:
                    scenes = [texte[:300]]
                
                for i, scene in enumerate(scenes[:3]):
                    with st.spinner(f"Création de l'image de la Scène {i+1}..."):
                        prompt_image = f"Cinematic scene, movie still, high quality: {scene[:400]}"
                        image_url = generer_image_fal(prompt_image)
                        
                        st.subheader(f"🎬 Scène {i+1}")
                        if image_url:
                            st.image(image_url, use_container_width=True)
                        else:
                            st.error(f"Impossible de créer l'image de la Scène {i+1}.")

# --- ONGLET 2 : BRANDING ---
with tab2:
    st.header("Les Génériques")
    st.text_input("Titre du film", "Mon Super Film")
    st.text_input("Sous-titre", "Une aventure incroyable")

# --- ONGLET 3 : PERSONNAGES ---
with tab3:
    st.header("Les Personnages")
    st.file_uploader("Photo du héros", type=["jpg", "png"])

# --- ONGLET 5 : AUDIO ---
with tab5:
    st.header("Le Son")
    st.selectbox("Voix", ["Homme", "Femme", "Enfant"])
    st.file_uploader("Musique (MP3)", type=["mp3"])

# --- ONGLET 6 : MONTAGE ---
with tab6:
    st.header("Le Montage Final")
    st.success("Tout est prêt pour l'assemblage !")
    if st.button("🎬 Lancer le rendu final"):
        st.warning("C'est parti pour le montage...")
