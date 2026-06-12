# AI mutli-agents assistant
Python application that simulates an interaction between a user and a technical support system composed of three collaborative AI agents.

The user submits a query to the main agent through the web interface. The main agent first forwards the request to a specialized agent connected to a FAISS knowledge base, referred to as the FAISS Agent.

If the FAISS Agent is unable to find an appropriate answer, the main agent then queries a third agent, which performs a request to ChatGPT-4o, referred to as the GPT-4o Agent.

Regardless of which agent provides the answer, either the FAISS Agent or the GPT-4o Agent, the information is sent back to the main agent, which then returns it to the user through the web interface.


## Install

#### Prerequisites
Python 3.10 was used for the development of this project:  https://www.python.org/downloads/

#### Steps
1. Clone the repository:
````commandline
git clone
````

2. Create a `.env` file at the root of the project: `<path>/ai-multi-agents/`. This file must contain your OpenAI API key:
````commandline
# .env content
OPENAI_API_KEY=<your-openai-api-key>
````

3. Create a virtual environment and install the dependencies:
````commandline
cd <path>/ai-multi-agents/
python -m venv venv
venv\Scripts\activate     # for Windows
source venv/bin/activate  # for Linux
python -m pip install --upgrade pip
pip install -r requirements.txt
````

4. Run app
````commandline
python main.py
````
You should see something like the following output in your terminal:
````commandline
←[32mINFO←[0m:     Started server process [←[36m8164←[0m]
←[32mINFO←[0m:     Waiting for application startup.
←[32mINFO←[0m:     Application startup complete.
←[32mINFO←[0m:     Uvicorn running on ←[1mhttp://0.0.0.0:5000←[0m (Press CTRL+C to quit)

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://<ip>:8501

````
A browser window should open automatically. Well done, you can then start asking questions to the assistant \o/
