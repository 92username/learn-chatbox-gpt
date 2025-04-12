# tests/test_streamlit_load.py
# check if strealit loads without errors
def test_streamlit_script_runs():
    try:
        __import__("form")
    except Exception as e:
        assert False, f"Erro ao carregar Streamlit: {e}"
