# tests/test_streamlit_load.py
# check if strealit loads without errors
import sys
import os

# Adiciona o diretório raiz do projeto ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_streamlit_script_runs():
    try:
        __import__("form")
    except Exception as e:
        assert False, f"Erro ao carregar Streamlit: {e}"

