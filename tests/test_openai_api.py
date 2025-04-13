"""
Unit tests for OpenAI API integration using mock objects.
"""

from unittest.mock import patch, MagicMock

def test_openai_mock_call():
    """
    Test the OpenAI API mock call to simulate a chat completion response.
    """
    with patch("openai.OpenAI") as mock_client:
        # Simulate the return of the call
        mock_instance = mock_client.return_value
        mock_completion = MagicMock()
        mock_completion.choices = [MagicMock()]
        mock_completion.choices[0].message.content = "Simulação OK"
        mock_instance.chat.completions.create.return_value = mock_completion

        # Execute the "simulated call"
        response = mock_instance.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "teste"}]
        )

        assert response.choices[0].message.content == "Simulação OK"
        