[![CI Workflow](https://github.com/92username/learn-chatbox-gpt/actions/workflows/main.yml/badge.svg)](https://github.com/92username/learn-chatbox-gpt/actions/workflows/main.yml) [![Pylint](https://github.com/92username/learn-chatbox-gpt/actions/workflows/pylint.yml/badge.svg)](https://github.com/92username/learn-chatbox-gpt/actions/workflows/pylint.yml) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/b7a1d3a48d4241c08c41ce6f8f1ff907)](https://app.codacy.com/gh/92username/learn-chatbox-gpt/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade) [![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/) [![License](https://img.shields.io/github/license/92username/learn-chatbox-gpt)](LICENSE) 

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/92username/learn-chatbox-gpt) ![Last Commit](https://img.shields.io/github/last-commit/92username/learn-chatbox-gpt) 

![Docker stats](https://img.shields.io/badge/Docker%20/%20stats-blue?logo=docker)
![Docker Image Size (latest)](https://img.shields.io/docker/image-size/user92/learn-chatbox-gpt/latest)
![Docker Pulls](https://img.shields.io/docker/pulls/user92/learn-chatbox-gpt) ![Docker Image Version](https://img.shields.io/docker/v/user92/learn-chatbox-gpt?sort=semver)




![Amazon AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white) ![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) ![ChatGPT](https://img.shields.io/badge/ChatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

# README.md 

## GPT Exercise Generator

This app generates programming exercises based on difficulty levels, using ChatGPT to provide personalized content. Users can select the number of exercises for each difficulty level, making it easy to practice and learn.

## Access the App

The app is 100% functional and can be accessed by clicking the badge below:

[![AWS](https://img.shields.io/badge/AWS-Cloud-%230072C6.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://chatbox.tamanduas.dev/)
> **Note:** Software is online !

![Containerized](https://img.shields.io/badge/Containerized-Docker-blue?logo=docker&logoColor=white&style=for-the-badge)

![Main Screen](/assets/mainscreen.png)

![Expected Output](/assets/outputscreen.png)

## Requirements

- Python 3.10+
- Dependencies listed in requirements.txt

## Installation and Usage

> Note: If the application does not work because the OpenAI API credits have run out, run it locally using your own API key. Instructions on how to run it locally follow.

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

## Run Locally

To run the app locally, you need to provide an OpenAI API key.

1. Set up your OpenAI API key as an environment variable:

    ```bash
    export OPENAI_API_KEY='your_openai_api_key'
    ```

2. Follow the installation and usage instructions above.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

## Useful Links

- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Documentation](https://beta.openai.com/docs/)
- [Python Official Documentation](https://docs.python.org/3/)
