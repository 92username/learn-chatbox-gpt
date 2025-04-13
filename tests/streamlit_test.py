"""
Test module to verify if the Streamlit script loads without errors.

This script adds the project root directory to the sys.path and 
tests if the 'form' module can be imported without raising any exceptions.
"""

import sys
import os

# Add the project root directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_streamlit_script_runs():
    """
    Test if the Streamlit script ('form' module) can be imported without errors.
    """
    try:
        __import__("form")
    except ImportError as import_error:
        assert False, f"ImportError while loading Streamlit: {import_error}"
    except Exception as general_error:
        assert False, f"Unexpected error while loading Streamlit: {general_error}"
