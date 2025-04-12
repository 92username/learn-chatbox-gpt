from unittest.mock import patch, MagicMock

def test_openai_mock_call():
    with patch("openai.OpenAI") as MockClient:
        # Simula o retorno da chamada
        mock_instance = MockClient.return_value
        mock_completion = MagicMock()
        mock_completion.choices = [MagicMock()]
        mock_completion.choices[0].message.content = "Simulação OK"
        mock_instance.chat.completions.create.return_value = mock_completion

        # Executa a "chamada simulada"
        response = mock_instance.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "teste"}]
        )

        assert response.choices[0].message.content == "Simulação OK"
