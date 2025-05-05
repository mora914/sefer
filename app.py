
import streamlit as st

sefirot = {
    "Keter": "Will / Root Impulse",
    "Chokhmah": "Creative Wisdom",
    "Binah": "Analytical Understanding",
    "Chesed": "Expansion",
    "Gevurah": "Contraction",
    "Tiferet": "Harmony",
    "Netzach": "Endurance",
    "Hod": "Formulation",
    "Yesod": "Foundation / Bridge",
    "Malkuth": "Physical Manifestation",
}

hebrew_letters = {
    "א": "Initiate / Air",
    "ב": "Construct / House",
    "ג": "Transfer / Movement",
    "ד": "Open / Gate",
    "ה": "Reveal / Window",
    "ו": "Connect / Hook",
    "ז": "Cut / Weapon",
    "ח": "Contain / Wall",
    "ט": "Goodness / Spiral",
    "י": "Form / Point of Seed",
    "כ": "Palm / Crown",
    "ל": "Learn / Ascend",
    "מ": "Flow / Water",
    "נ": "Fall / Eternity",
    "ס": "Support / Circle",
    "ע": "Eye / Insight",
    "פ": "Mouth / Speak",
    "צ": "Righteousness / Hook",
    "ק": "Holiness / Condense",
    "ר": "Head / Lead",
    "ש": "Tooth / Fire",
    "ת": "Truth / Seal"
}

def manifest_formula(letters, target_sefira):
    return f"Manifestation path: {' → '.join(letters)} → {target_sefira}"

st.title("Sefer Yetzirah Interactive Console")

letters = st.multiselect("Select Letters (Operators):", list(hebrew_letters.keys()))
target = st.selectbox("Target Sefira:", list(sefirot.keys()))

if st.button("Execute Formula"):
    formula = manifest_formula(letters, target)
    st.success(formula)
