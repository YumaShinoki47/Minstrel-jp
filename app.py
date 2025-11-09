from showcases.generate import generate
from showcases.test import test
from models.openai import Generator
import streamlit as st
import os

if __name__ == "__main__":
    state = st.session_state

    if "generator" not in state:
        state.generator = Generator(
            api_key = os.environ.get("OPENAI_API_KEY"),
            base_url = "https://api.openai.com/v1"
        )
        state.generator.set_model("gpt-4o")
        pass
    if "page" not in state:
        state.page = "generate"
        pass
    
    if state.page == "generate":
        generate()
        pass
    elif state.page == "test":
        test()
        pass


