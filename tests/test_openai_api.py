# tests/test_openai_api.py
# tests calls to openai api
import os
from openai import OpenAI


def test_openai_call():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    api_key = os.environ.get("OPENAI_API_KEY")
    assert api_key is not None, "API Key não está definida!"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Olá, tudo bem?"}]
    )
    assert response.choices[0].message.content is not None
