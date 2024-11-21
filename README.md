# README.md 
GPT Exercise Generator

This app generates programming exercises based on difficulty levels, using ChatGPT to provide personalized content. Users can select the number of exercises for each difficulty level.
Requirements

- Python 3.10+
- Dependencies listed in requirements.txt

Installation and Usage

Follow the steps below to install and run the app:
1. Clone the Repository

```
git clone https://github.com/92username/learn-chatbox-gpt.git
cd learn-chatbox-gpt
```
2. Create and Activate a Virtual Environment
Linux or macOS:
```
python3 -m venv venv
source venv/bin/activate
```

```
python -m venv venv
venv\Scripts\activate
```
3. Install the Dependencies
```
pip install -r requirements.txt
```
4. Setting Up the OpenAI API Key

To use **learn-chatbox-gpt**, you need to configure an environment variable with your OpenAI API key. Follow the steps below:

  a. **Open a terminal** on your system.
  
  b. Navigate to the project directory. For example:
     ```bash
     cd /home/nbx/Desktop/my-folder/testing/learn-chatbox-gpt
     ```
     
  c. **Create the `.env` file** in the project directory and open it with a text editor. For example:
     ```bash
     nano .env
     ```
     
  d. **Add the following line to the `.env` file**, replacing `your_api_key_here` with your actual OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
     
  e. **Save the file and exit the editor**:
   - In **nano**, press `Ctrl + X`, then `Y`, and then `Enter`.
   - 
  f. After creating the `.env` file, your project will be ready to run.


  > **Note:** Keep your API key secure and do not share it publicly.

  You are now ready to run the script and use **learn-chatbox-gpt**!

5. Run the App

To run the app, use the command:

```
streamlit run form.py
```
This will open the app in your browser(localhost).
![Main Screen](/mainscreen.png)
![Output Screen](/outputscreen.png)

6. Generating Exercises

Select the programming language, specific topic (e.g., lists, functions), and set the number of exercises for each difficulty level. The app will then generate exercises based on your selections.


## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.
