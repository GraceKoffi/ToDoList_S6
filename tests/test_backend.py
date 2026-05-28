from backend import init_tasks, add_task, get_tasks, mark_task_done, delete_task
import sys
import logging


import streamlit as st


# Initialisation

def setup_function():
    """
    Réinitialise le session_state avant chaque test
    """
    st.session_state.clear()
    logging.info("session_state réinitialisé")


# Test init_tasks()

def test_init_tasks():
    logging.info(" test_init_tasks démarré")

    init_tasks()

    assert "tasks" in st.session_state
    assert st.session_state["tasks"] == []

    logging.info("tasks initialisé correctement")
