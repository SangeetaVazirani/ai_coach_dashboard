import streamlit as st
from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
label_map = {
    "LABEL_0": "Negative",
    "LABEL_1": "Neutral",
    "LABEL_2": "Positive"
}

def mental_wellness():
    user_input = st.text_input("How are you feeling today?")
    if st.button("Check Mood"):
        if user_input:
            result = sentiment_model(user_input)[0]
            sentiment = label_map.get(result["label"], "Unknown")
            st.write(f"**Mood detected:** {sentiment} (Confidence: {result['score']:.2f})")
            if sentiment == "Negative":
                st.warning("Consider taking a break, talking to a friend, or going for a walk. 💛")
            elif sentiment == "Neutral":
                st.info("You're feeling neutral. Try something uplifting like music or a hobby. 😊")
            else:
                st.success("Glad to hear you're feeling positive! Keep it up! 🌟")
        else:
            st.error("Please enter your mood to analyze.")