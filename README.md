# README.md 

## GPT Exercise Generator

This app generates programming exercises based on difficulty levels, using ChatGPT to provide personalized content. Users can select the number of exercises for each difficulty level, making it easy to practice and learn.

## Requirements

- Python 3.10+
- Dependencies listed in requirements.txt

## Installation and Usage

Follow the steps below to install and run the app:

1. Clone the Repository

    ```bash
    git clone https://github.com/92username/learn-chatbox-gpt.git
    cd learn-chatbox-gpt
    ```

2. Create and Activate a Virtual Environment

    Linux or macOS:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the Dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Run the App

    To run the app, use the command:

    ```bash
    streamlit run form.py
    ```

    This will open the app in your browser (localhost).

    ![Main Screen](/screenshot_localhost.png)

5. Generating Exercises

    Select the programming language, specific topic (e.g., lists, functions), and set the number of exercises for each difficulty level. The app will then generate exercises based on your selections.

## Access the App

The app is 100% functional and can be accessed by clicking the link below:

[Streamlit App Link](https://exercicios-programacao-gpt.streamlit.app/)

## Run Locally

To run the app locally, you need to provide an OpenAI API key.

1. Set up your OpenAI API key as an environment variable:

    ```bash
    export OPENAI_API_KEY='your_openai_api_key'
    ```

2. Follow the installation and usage instructions above.

## Hosting

I am working on hosting this webapp on a VPS at Hostinger.

- [x] Provided APIKEY for free use
- [x] Provide link for direct access

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

## Useful Links

- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Documentation](https://beta.openai.com/docs/)
- [Python Official Documentation](https://docs.python.org/3/)
