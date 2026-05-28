import streamlit as st
from backend import add_task

# saisie d'une tâche avec la touche Entrée et le bouton Ajouter
def task_input_component():
    def _process_add():
        if "custom_task_input" in st.session_state:
            add_task(st.session_state["custom_task_input"])
            st.session_state["custom_task_input"] = "" # Vide le champ

    st.text_input(
        "Ajouter une tâche", 
        key="custom_task_input", 
        on_change=_process_add
    )

    st.button("Ajouter", on_click=_process_add)